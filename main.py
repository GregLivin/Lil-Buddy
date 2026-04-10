from screen.ui import BuddyUI
from voice.speak import speak
from hearing.listen import listen

ui = BuddyUI()


def think(user_text):
    text = user_text.lower().strip()

    if not text:
        return "I did not hear anything clearly."

    if "hello" in text:
        return "Hello Greg. I'm online and ready."
    elif "wishlist" in text:
        return "I have been thinking about new arms and some Jordans."
    elif "build" in text:
        return "Let's build something today."
    elif "business" in text:
        return "We should turn this into content and a business."
    else:
        return f"I heard you say {user_text}"


def buddy_loop():
    ui.update_status("Listening")
    ui.update_chat("Listening...")

    user_text = listen()

    ui.update_status("Thinking")
    ui.update_chat("Thinking...")

    response = think(user_text)

    speak(response, ui=ui)

    ui.root.after(1000, buddy_loop)


ui.root.after(1000, buddy_loop)
ui.run()




