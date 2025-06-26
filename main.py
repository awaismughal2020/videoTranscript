import subprocess
import os
import requests
import time
import assemblyai as aai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")

# Check if API key is loaded
if not ASSEMBLYAI_API_KEY:
    raise ValueError("❌ ASSEMBLYAI_API_KEY not found in environment variables. Please check your .env file.")


def extract_audio(video_path, audio_path="temp_audio.wav"):
    print("🎞️ Extracting audio...")
    command = [
        "ffmpeg", "-y", "-i", video_path,
        "-vn",  # no video
        "-acodec", "pcm_s16le",  # WAV format
        "-ar", "16000",  # 16 kHz
        "-ac", "1",  # mono channel
        audio_path
    ]
    subprocess.run(command, check=True)
    return audio_path


def transcribe_with_assemblyai(audio_source, model="best"):
    """
    Transcribes a local or remote audio/video file using AssemblyAI.

    Args:
        audio_source (str): Path to local file or public URL (e.g., .wav, .mp3)
        model (str): Speech model to use: 'best', 'nano', or 'default'

    Returns:
        str: Transcript text or raises error on failure
    """
    aai.settings.api_key = ASSEMBLYAI_API_KEY

    # Choose speech model - using correct enum values
    if model == "best":
        speech_model = aai.SpeechModel.best
    elif model == "nano":
        speech_model = aai.SpeechModel.nano
    else:
        speech_model = None  # Use default (no speech_model specified)

    # Configure transcription with minimal, widely supported parameters
    config_params = {}

    # Add speaker labels if supported
    try:
        config_params['speaker_labels'] = True
    except:
        pass

    # Only add speech_model if it's not None (default)
    if speech_model is not None:
        try:
            config_params['speech_model'] = speech_model
        except:
            pass

    # Create config with available parameters
    if config_params:
        config = aai.TranscriptionConfig(**config_params)
    else:
        config = aai.TranscriptionConfig()

    # Transcribe
    print(f"🎧 Transcribing with model: {model}")
    transcriber = aai.Transcriber(config=config)
    transcript = transcriber.transcribe(audio_source)

    # Handle errors
    if transcript.status == "error":
        raise RuntimeError(f"❌ Transcription failed: {transcript.error}")

    # Success
    print("✅ Transcription complete.")
    return transcript.text


# 🔧 Example usage
if __name__ == "__main__":
    # transcribe_video_file("data/motivational.mp4")
    transcript_text = transcribe_with_assemblyai('temp_audio.wav')
    print(transcript_text)