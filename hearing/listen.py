import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=5)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except:
        return ""

