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
            font=("Arial", 24),
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
        self.status.pack()

        self.chat = tk.Label(
            self.root,
            text="Yo Greg... I'm ready to build.",
            font=("Arial", 20),
            fg="white",
            bg="black",
            wraplength=900,
            justify="left"
        )
        self.chat.pack(pady=50)

        self.wishlist_title = tk.Label(
            self.root,
            text="Buddy's Wishlist",
            font=("Arial", 18),
            fg="cyan",
            bg="black"
        )
        self.wishlist_title.pack()

        self.wishlist_box = tk.Label(
            self.root,
            text="Loading...",
            font=("Arial", 16),
            fg="white",
            bg="black",
            justify="left"
        )
        self.wishlist_box.pack(pady=10)

        self.load_wishlist()

        self.root.bind("<Escape>", lambda e: self.root.destroy())

    def load_wishlist(self):
        try:
            with open("data/wishlist.json", "r") as f:
                data = json.load(f)

            text = ""
            for item in data:
                text += f"- {item['name']}\n"

            self.wishlist_box.config(text=text.strip())

        except Exception:
            self.wishlist_box.config(text="No wishlist found")

    def update_chat(self, message):
        self.chat.config(text=message)
        self.root.update_idletasks()

    def update_status(self, status):
        self.status.config(text=f"Status: {status}")
        self.root.update_idletasks()

    def run(self):
        self.root.mainloop()