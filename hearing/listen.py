import speech_recognition as sr

WAKE_WORD = "hey buddy"


def listen_for_wake_word():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Waiting for wake word...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(source, phrase_time_limit=3)
            text = recognizer.recognize_google(audio).lower()
            print("Heard:", text)

            return WAKE_WORD in text

        except:
            return False


def listen_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(source, phrase_time_limit=5)
            text = recognizer.recognize_google(audio)
            print("Command:", text)
            return text

        except:
            return ""