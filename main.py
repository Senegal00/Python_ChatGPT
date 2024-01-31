""""
MODELS	DESCRIPTION
GPT-4 Limited beta	A set of models that improve on GPT-3.5 and can understand as well as generate
natural language or code GPT-3.5 A set of models that improve on GPT-3 and can understand
as well as generate natural language or code

DALL·E Beta	A model that can generate and edit images given a natural language prompt
Whisper Beta	A model that can convert audio into text
Embeddings	A set of models that can convert text into a numerical form
Moderation	A fine-tuned model that can detect whether text may be sensitive or unsafe
GPT-3	A set of models that can understand and generate natural language
CodexDeprecated	A set of models that can understand and generate code, including translating
natural language to code We have also published open source models
including Point-E, Whisper, Jukebox, and CLIP.

Visit our model index for researchers to learn more about which models have been featured in 
our research papers and the differences between model series like InstructGPT and GPT-3.5.
"""
# pip install --upgrade openai
from docx import Document
from openai import OpenAI
# pip install --upgrade "typer[all]", para mejorar el aspecto de la consola
import os
# archivo de configuracion para la api-key que se genero en la pagina oficial de openai.
import config

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
    # api_key=config.API_KEY,
)


def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        transcription = client.audio.transcriptions.create(
            "whisper-1", audio_file)
    return transcription['text']


# audio_file_path = "C:\Users\seneg\Downloads\EarningsCall.wav"
transcribe_audio("EarningsCall.wav")
