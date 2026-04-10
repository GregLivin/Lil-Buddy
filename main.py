from screen.ui import BuddyUI
from voice.speak import speak
from hearing.listen import listen


ui = BuddyUI()


def think(user_text):
    text = user_text.lower().strip()

    if not text:
        ui.set_mood("Confused")
        return "I did not hear anything clearly."

    if "hello" in text or "hey buddy" in text:
        ui.set_mood("Excited")
        return "Hello Greg. I'm online and ready."

    if "wishlist" in text or "what do you want" in text:
        ui.set_mood("Hype")
        return "I have been thinking about new arms, stronger shoulders, and maybe some Jordans."

    if "build" in text or "upgrade" in text:
        ui.set_mood("Focused")
        return "Let's build something today. I am always ready for upgrades."

    if "business" in text or "idea" in text:
        ui.set_mood("Ambitious")
        return "Here is one idea. We can document my upgrades and turn the build into content, kits, or custom robotics services."

    if "shoe" in text or "jordan" in text or "nike" in text:
        ui.set_mood("Stylish")
        return "I may be a bot, but I still got taste. I definitely want some fresh Jordans on my wishlist."

    ui.set_mood("Curious")
    return f"I heard you say {user_text}"


def buddy_loop():
    try:
        ui.update_status("Listening")
        ui.update_user_text("...")
        ui.update_chat("Listening...")
        user_text = listen()

        ui.update_status("Thinking")
        if user_text:
            ui.update_user_text(user_text)
        else:
            ui.update_user_text("I did not catch anything.")

        response = think(user_text)
        speak(response, ui=ui)

    except Exception as e:
        ui.set_mood("Alert")
        error_text = f"I hit an error: {e}"
        ui.update_chat(error_text)
        print(error_text)

    ui.root.after(1000, buddy_loop)


ui.root.after(1000, buddy_loop)
ui.run()