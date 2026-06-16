import os
import yaml
import numpy as np
import pandas as pd
import soundfile as sf


def load_spec():
    with open("spec.yaml", "r") as file:
        return yaml.safe_load(file)


def peak_db(audio):
    peak = np.max(np.abs(audio))

    if peak == 0:
        return -np.inf

    return 20 * np.log10(peak)


def has_clipping(audio):
    return np.any(np.abs(audio) >= 0.999)


def analyze_file(filepath, spec):
    audio, sample_rate = sf.read(filepath)

    channels = 1 if audio.ndim == 1 else audio.shape[1]

    peak = peak_db(audio)
    clipping = has_clipping(audio)

    passes = True
    failures = []

    if sample_rate != spec["sample_rate"]:
        passes = False
        failures.append("sample_rate")

    if channels != spec["channels"]:
        passes = False
        failures.append("channels")

    if peak > spec["max_peak_db"]:
        passes = False
        failures.append("peak_level")

    if clipping:
        passes = False
        failures.append("clipping")

    return {
        "filename": os.path.basename(filepath),
        "sample_rate": sample_rate,
        "channels": channels,
        "peak_db": round(peak, 2),
        "clipping": clipping,
        "status": "PASS" if passes else "FAIL",
        "failures": ", ".join(failures)
    }


def main():
    spec = load_spec()

    audio_folder = "test_audio"

    results = []

    for filename in os.listdir(audio_folder):
        if filename.lower().endswith(".wav"):
            filepath = os.path.join(audio_folder, filename)
            results.append(analyze_file(filepath, spec))

    df = pd.DataFrame(results)

    os.makedirs("sample_output", exist_ok=True)

    output_file = "sample_output/report.csv"
    df.to_csv(output_file, index=False)

    print(f"\nFiles analyzed: {len(df)}")

    if len(df) > 0:
        passed = len(df[df["status"] == "PASS"])
        failed = len(df[df["status"] == "FAIL"])

        print(f"Passed: {passed}")
        print(f"Failed: {failed}")

    print(f"\nReport saved to: {output_file}")


if __name__ == "__main__":
    main()