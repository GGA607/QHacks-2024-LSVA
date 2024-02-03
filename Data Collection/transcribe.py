import speech_recognition as sr 
r = sr.Recognizer()

response = sr.AudioFile("output.wav")
with response as source:
    audio = r.record(source)

words = r.recognize_google(audio)
file_path = "answer.txt"

with open(file_path, mode = "w") as f:
    f.write(words)