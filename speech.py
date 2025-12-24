# speech.py
# -----------------------------------------
# STRICT VOICE-ONLY INPUT
# gTTS for TTS (Telugu)
# SpeechRecognition for STT
# NO text fallback
# -----------------------------------------

from gtts import gTTS
import pygame
import time
import os
import speech_recognition as sr


# ---------------- TTS ----------------
def speak(text):
    print("[TTS]", text)

    tts = gTTS(text=text, lang="te")
    filename = "reply.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.quit()
    os.remove(filename)


# ---------------- STT (VOICE ONLY) ----------------
def listen():
    """
    STRICT voice-only input.
    Blocks until speech is captured.
    Raises error if speech is not recognized.
    """

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("[LISTENING] Speak clearly...")
        r.adjust_for_ambient_noise(source, duration=0.7)
        audio = r.listen(source)  # waits indefinitely

    try:
        text = r.recognize_google(audio, language="te-IN")

        print("[USER - VOICE]", text)
        return text
    except sr.UnknownValueError:
        speak("మీ మాటలు అర్థం కాలేదు. మళ్లీ చెప్పండి.")
        return listen()  # retry voice
    except sr.RequestError:
        speak("ఇంటర్నెట్ సమస్య ఉంది.")
        raise
