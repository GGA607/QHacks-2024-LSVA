"""
QHacks 2024 Project

TODO: This file is meant to collect user speech and store it in a wav file.

Authors: Alec Glasford, Logan Jarvis, Shravan Agnihotri, Vedansh Bhatt
Last Modified: 2024/02/02
"""
import pyaudio, wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True, frames_per_buffer = CHUNK)

print("start recording...")

frames = []
seconds = 10
for i in range(0, int(RATE / CHUNK * seconds)):
    data = stream.read(CHUNK)
    frames.append(data)
    
print("recording has stopped.")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open("output.wav", "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()