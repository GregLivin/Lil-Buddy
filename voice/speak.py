import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 160)
engine.setProperty("volume", 1.0)

def speak(text, ui=None):
    if ui is not None:
        ui.update_status("Speaking")
        ui.update_chat(text)

    engine.say(text)
    engine.runAndWait()

    if ui is not None:
        ui.update_status("Idle")
