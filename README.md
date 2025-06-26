# 🎬 videoTranscript

A lightweight Python tool to transcribe audio/video files using [AssemblyAI](https://www.assemblyai.com/)’s powerful speech-to-text API. Easily extract clean, accurate transcripts from video or audio sources with minimal code.

---

## 🔧 Features

* Transcribe audio from video files (e.g., `.mp4`, `.mov`, `.mp3`, etc.)
* Uses [AssemblyAI API](https://docs.assemblyai.com/) for speech recognition
* Automatically uploads local files to AssemblyAI
* Retrieves and saves transcripts in plain text
* Handles end-to-end transcription process (upload → transcribe → fetch result)

---

## 📦 Requirements

* Python 3.8+
* [AssemblyAI API Key](https://app.assemblyai.com/signup)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup

1. Create a free account on [AssemblyAI](https://app.assemblyai.com)
2. Get your API key from the dashboard
3. Set the API key as an environment variable:

```bash
export ASSEMBLYAI_API_KEY=your_api_key_here
```

---

## 🚀 Usage

```bash
python main.py
```

---
