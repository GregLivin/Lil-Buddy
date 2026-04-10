from screen.ui import BuddyUI
from voice.speak import speak

ui = BuddyUI()

def start():
    speak("Yo Greg, I'm online.", ui=ui)

    speak("I have been thinking about upgrades.", ui=ui)

    speak("I still want new arms and maybe some Jordans.", ui=ui)

    speak("Let’s build something today.", ui=ui)

ui.root.after(1000, start)
ui.run()