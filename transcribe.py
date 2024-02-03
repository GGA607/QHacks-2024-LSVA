"""
QHacks 2024 Project

TODO: This file is meant to interpret user speech and render it back to the console

Authors: Alec Glasford, Logan Jarvis, Shravan Agnihotri, Vedansh Bhatt
Last Modified: 2024/02/02
"""
import speech_recognition as sr 
import pyttsx3

r = sr.Recognizer() # initializes the recognizer

def UserSpeech(command):
    # intialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    
with sr.Microphone as source2:
    print("Calibrating... silence please")
    r.adjust_for_ambient_noise(source2, duration = 2)
    print("Calibrated, feel free to speak :)")
    
UserSpeech("Greetings, Earthlings!")