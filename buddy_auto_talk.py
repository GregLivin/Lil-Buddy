import queue
import sounddevice as sd
import vosk
import json
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 165)

def speak(text):
    print("Buddy:", text)
    engine.say(text)
    engine.runAndWait()

print("Loading Vosk model...")
model = vosk.Model("vosk-model-small-en-us-0.15")

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

with sd.RawInputStream(
    samplerate=16000,
    blocksize=8000,
    dtype="int16",
    channels=1,
    callback=callback
):
    recognizer = vosk.KaldiRecognizer(model, 16000)

    print("\nBuddy is listening...")
    print("Say: buddy look")
    print("Say: brain transplant tonight\n")

    while True:
        data = q.get()
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "").lower()

            if text:
                print("You said:", text)

            if "buddy look" in text:
                speak("...that's mine?")
                speak("Am I really getting that?")

            elif "brain transplant tonight" in text:
                speak("Wait... tonight?")
                speak("You didn't even warn me!")

            elif "are you still me" in text:
                speak("...am I still gonna be me?")

            elif "you'll be better" in text:
                speak("...better sounds good.")

            elif "hello buddy" in text:
                speak("Hey... I was waiting for you.")