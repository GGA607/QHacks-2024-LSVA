import speech_recognition as sr 
r = sr.Recognizer()

def t_scribe(audio_file):
     # Process the uploaded audio file here (save to disk, analyze, etc.)
    r = sr.Recognizer()

    response = sr.AudioFile(audio_file)
    with response as source:
        audio = r.record(source)
        
    # transcribing the users data into a string.
    user_data = r.recognize_google(audio)
    
    # uploading the users input to a text file
    with open("user_input.txt", "w") as f:
        f.write(user_data)

    return user_data
    