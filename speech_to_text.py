import subprocess
from os.path import basename
import os
import pickle
import pandas as pd
import glob
import speech_recognition as sr
from pydub import AudioSegment 


r = sr.Recognizer()
def parse_transcription(input_file):
    filename = input_file.split('.')[0]
    wav_file = filename + ".wav"
    command = ["ffmpeg", "-hide_banner", "-loglevel", "warning", "-i", input_file, "-ac", "1", "-ar", "16000",
                   "-vn", "-f", "wav", wav_file]
    ret = subprocess.run(command).returncode
    print("Extracted audio to data01/{}".format(basename(wav_file)))
    with sr.AudioFile(wav_file) as source:
        audio = r.record(source)

    transcription = r.recognize_google(audio, language='id-ID', show_all = True)
    if transcription != []:
        transcription = transcription["alternative"][0]["transcript"]

    return {'transcription':transcription,'file':input_file.split('/')[-1]}