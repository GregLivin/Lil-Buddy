import json
import os

try:
    import pygame
    pygame.mixer.init()
except:
    pygame = None

LIBRARY_FILE = "data/music_library.json"


def load_library():
    try:
        with open(LIBRARY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def find_song(name):
    name = name.lower()
    for song in load_library():
        if name in song["name"].lower():
            return song
    return None


def play_song(name):
    if pygame is None:
        return "Music system not available."

    song = find_song(name)

    if not song:
        return f"I could not find {name}."

    path = song["file"]

    if not os.path.exists(path):
        return f"File missing for {song['name']}."

    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

    return f"Playing {song['name']}."


def stop_music():
    if pygame:
        pygame.mixer.music.stop()
        return "Music stopped."
    return "Music system not available."