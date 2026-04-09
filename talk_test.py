import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 160)
engine.say("Hello Greg. I am Lil Buddy.")
engine.runAndWait()
