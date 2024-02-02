
import openai
import config

# Configura la API Key
openai.api_key = config.API_KEY


def transcribe_audio(audio_file_path):
    try:
        with open(audio_file_path, 'rb') as audio_file:
            transcription = openai.Audio.transcribe("whisper-1", audio_file)
            return transcription['text']
    except Exception as e:
        print(f"Error al transcribir el audio: {e}")


# Ruta al archivo de audio
audio_file_path = "./EarningsCall.wav"
transcription_text = transcribe_audio(audio_file_path)
print(transcription_text)
