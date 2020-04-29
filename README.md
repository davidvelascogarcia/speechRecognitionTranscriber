[![speechRecognitionTranscriber Homepage](https://img.shields.io/badge/speechRecognitionTranscriber-develop-orange.svg)](https://github.com/davidvelascogarcia/speechRecognitionTranscriber/tree/develop/programs) [![Latest Release](https://img.shields.io/github/tag/davidvelascogarcia/speechRecognitionTranscriber.svg?label=Latest%20Release)](https://github.com/davidvelascogarcia/speechRecognitionTranscriber/tags) [![Build Status](https://travis-ci.org/davidvelascogarcia/speechRecognitionTranscriber.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/speechRecognitionTranscriber)

# Speech Recognition Transcriber: speechRecognitionTranscriber (Python API)

- [Introduction](#introduction)
- [Use](#use)
- [Requirements](#requirements)
- [Status](#status)
- [Related projects](#related-projects)


## Introduction

`speechRecognitionTranscriber` module use `Google Speech API` in `python`. This module performs speech recognition and converts to text. Admits video and audio files to be transcribed. Use `ffmpeg` to convert video and audio files to `.wav` to be recognized in `Google Speech API`. Also use fragments division based on silence.


## Running software

`speechRecognitionTranscriber` requires video/audio like input.
The process to running the program:

1. Execute [programs/speechRecognitionTranscriber.py](./programs), to start de program.
```python
python speechRecognitionTranscriber.py
```
2. Introduce your file path.
```bash
yourfile.extension
```

NOTE:

- Transcribed text is saved in `transcribedText.txt`.
- Audio fragments are saved in `/fragments`.
- Converted source is saved as `convertedFile.wav`.

## Requirements

`speechRecognitionTranscriber` requires:

* [Install pip](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-pip.md)
* Install SpeechRecognition:

```bash
pip install SpeechRecognition
```
* Install pydub

```bash
pip install pydub
```
* Install ffmpeg

**Linux** **

```bash
sudo apt-get install ffmpeg
```
**Microsoft Windows**
[Download](https://www.ffmpeg.org/download.html#build-windows) binaries and set path in system variables.



Tested on: `windows 10`,`ubuntu 14.04`, `ubuntu 16.04`, `ubuntu 18.04`, `lubuntu 18.04` and `raspbian`.


## Status

[![Build Status](https://travis-ci.org/davidvelascogarcia/speechRecognitionTranscriber.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/speechRecognition)

[![Issues](https://img.shields.io/github/issues/davidvelascogarcia/speechRecognitionTranscriber.svg?label=Issues)](https://github.com/davidvelascogarcia/speechRecognitionTranscriber/issues)

## Related projects

* [realpython: python speech recognition](https://realpython.com/python-speech-recognition/)
* [python basics: transcribe audio](https://pythonbasics.org/transcribe-audio/)

