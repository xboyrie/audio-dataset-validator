# audio-dataset-validator

Automated quality assurance tool for validating speech and voice recordings against technical audio specifications.

## Overview

Audio Dataset Validator analyzes WAV files and verifies compliance with predefined delivery requirements. The tool is intended for speech datasets, voice AI training data, IVR prompts, and other large-scale voice collection projects where technical consistency is critical.

## Features

* Sample rate validation
* Channel count validation
* Peak level analysis
* Clipping detection
* CSV report generation
* Configurable validation rules using YAML

## Example Specification

```yaml
sample_rate: 48000
channels: 1
max_peak_db: -1
```

## Example Output

| File                  | Status | Failure Reason       |
| --------------------- | ------ | -------------------- |
| good.wav              | PASS   |                      |
| clipped.wav           | FAIL   | peak_level, clipping |
| wrong_sample_rate.wav | FAIL   | sample_rate          |
| stereo.wav            | FAIL   | channels             |

## Use Cases

* Speech AI datasets
* Automatic Speech Recognition (ASR) collections
* Text-to-Speech (TTS) datasets
* IVR prompt libraries
* Voice data quality assurance workflows

## Future Enhancements

* LUFS compliance checking
* Silence detection
* Noise floor analysis
* HTML reporting
* Batch dataset summaries

## Technologies

* Python
* NumPy
* Pandas
* PyYAML
* SoundFile
