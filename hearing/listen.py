import speech_recognition as sr

def listen(timeout=5, phrase_time_limit=5):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(
            source,
            timeout=timeout,
            phrase_time_limit=phrase_time_limit
        )

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""
