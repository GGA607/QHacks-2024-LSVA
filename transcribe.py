import speech_recognition as sr 
r = sr.Recognizer()

response = sr.AudioFile("output.wav")
with response as source:
    audio = r.record(source)

print(r.recognize_google(audio))