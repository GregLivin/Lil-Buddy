import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import pyttsx3

fs = 16000
seconds = 5

engine = pyttsx3.init()
engine.setProperty("rate", 160)
engine.setProperty("volume", 1.0)

model = whisper.load_model("base")

print("Speak now...")
audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype="int16")
sd.wait()
write("command.wav", fs, audio)

result = model.transcribe("command.wav")
user_text = result["text"].strip().lower()

print("You said:", user_text)

# 🧠 Simple brain logic
if "hello" in user_text:
    response = "Hello Greg. I'm online and ready."
elif "your name" in user_text:
    response = "I am Lil Buddy, your AI companion."
elif "time" in user_text:
    import datetime
    now = datetime.datetime.now().strftime("%I:%M %p")
    response = f"The time is {now}"
elif "what do you see" in user_text:
    response = "I will need my camera activated to see."
else:
    response = f"I heard you say {user_text}"

print("Lil Buddy:", response)

engine.say(response)
engine.runAndWait()
