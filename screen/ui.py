import tkinter as tk
import json


class BuddyUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Lil Buddy")
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="black")

        self.header = tk.Label(
            self.root,
            text="LIL BUDDY | Mood: Hype",
            font=("Arial", 24, "bold"),
            fg="lime",
            bg="black"
        )
        self.header.pack(pady=10)

        self.status = tk.Label(
            self.root,
            text="Status: Idle",
            font=("Arial", 16),
            fg="white",
            bg="black"
        )
        self.status.pack(pady=5)

        self.you_label = tk.Label(
            self.root,
            text="You: ...",
            font=("Arial", 18),
            fg="cyan",
            bg="black",
            wraplength=1000,
            justify="left"
        )
        self.you_label.pack(pady=15)

        self.buddy_label = tk.Label(
            self.root,
            text="Buddy: Yo Greg... I'm ready to build.",
            font=("Arial", 22),
            fg="white",
            bg="black",
            wraplength=1000,
            justify="left"
        )
        self.buddy_label.pack(pady=25)

        self.wishlist_title = tk.Label(
            self.root,
            text="Buddy's Wishlist",
            font=("Arial", 18, "bold"),
            fg="orange",
            bg="black"
        )
        self.wishlist_title.pack(pady=10)

        self.wishlist_box = tk.Label(
            self.root,
            text="Loading wishlist...",
            font=("Arial", 16),
            fg="white",
            bg="black",
            justify="left"
        )
        self.wishlist_box.pack(pady=10)

        self.footer = tk.Label(
            self.root,
            text="ESC = Exit",
            font=("Arial", 12),
            fg="gray",
            bg="black"
        )
        self.footer.pack(side="bottom", pady=10)

        self.load_wishlist()
        self.root.bind("<Escape>", lambda e: self.root.destroy())

    def load_wishlist(self):
        try:
            with open("data/wishlist.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            lines = []
            for item in data:
                name = item.get("name", "Unknown item")
                reason = item.get("reason", "")
                lines.append(f"- {name}")
                if reason:
                    lines.append(f"  {reason}")

            self.wishlist_box.config(text="\n".join(lines))
        except Exception as e:
            self.wishlist_box.config(text=f"No wishlist found\n{e}")

    def update_status(self, status):
        self.status.config(text=f"Status: {status}")
        self.root.update_idletasks()

    def update_user_text(self, text):
        self.you_label.config(text=f"You: {text}")
        self.root.update_idletasks()

    def update_chat(self, text):
        self.buddy_label.config(text=f"Buddy: {text}")
        self.root.update_idletasks()

    def set_mood(self, mood):
        self.header.config(text=f"LIL BUDDY | Mood: {mood}")
        self.root.update_idletasks()

    def run(self):
        self.root.mainloop()