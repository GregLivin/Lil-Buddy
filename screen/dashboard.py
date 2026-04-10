import streamlit as st
from pathlib import Path
from datetime import datetime
import shutil
import cv2

# Optional system stats
try:
    import psutil
except ImportError:
    psutil = None

# Optional robot controls
try:
    from brain.robot_controls import (
        look_left,
        look_right,
        look_up,
        look_down,
        speak,
        dance_mode,
        wake_buddy,
        stop_buddy,
        center_head,
        mute_speaker,
    )
except ImportError:
    def look_left():
        print("Buddy looks left")

    def look_right():
        print("Buddy looks right")

    def look_up():
        print("Buddy looks up")

    def look_down():
        print("Buddy looks down")

    def speak():
        print("Buddy speaks")

    def dance_mode():
        print("Buddy starts dancing")

    def wake_buddy():
        print("Buddy waking up")

    def stop_buddy():
        print("Buddy stopping")

    def center_head():
        print("Buddy centers head")

    def mute_speaker():
        print("Buddy speaker muted")

# Optional live status
try:
    from memory.live_status import read_status
except ImportError:
    def read_status():
        return {
            "heard": "Nothing yet",
            "response": "No response yet",
            "mode": "Idle"
        }

st.set_page_config(page_title="Lil Buddy Dashboard", layout="wide")

# ---------- SETTINGS ----------
MUSIC_FOLDER = Path("music")
CAMERA_INDEX = 0

# ---------- HELPERS ----------
def get_music_files(folder: Path):
    if not folder.exists():
        return []

    exts = {".mp3", ".wav", ".ogg", ".m4a"}
    return sorted(
        [f for f in folder.iterdir() if f.is_file() and f.suffix.lower() in exts]
    )

def get_system_stats():
    cpu = "N/A"
    mem_used = "N/A"
    mem_avail = "N/A"
    temp = "N/A"
    disk_free = "N/A"

    if psutil:
        cpu = f"{psutil.cpu_percent()}%"

        vm = psutil.virtual_memory()
        mem_used = f"{vm.used / (1024**3):.2f} GB"
        mem_avail = f"{vm.available / (1024**3):.2f} GB"

        disk = shutil.disk_usage("/")
        disk_free = f"{disk.free / (1024**3):.2f} GB"

        try:
            temps = psutil.sensors_temperatures()
            if temps:
                for _, entries in temps.items():
                    if entries:
                        temp = f"{entries[0].current:.1f} °C"
                        break
        except Exception:
            pass

    return cpu, mem_used, mem_avail, temp, disk_free

def get_camera_frame(camera_index=0):
    cap = cv2.VideoCapture(camera_index)
    success, frame = cap.read()
    cap.release()

    if success:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame

    return None

def get_alerts(temp, cpu):
    alerts = []

    if temp != "N/A":
        try:
            temp_value = float(temp.replace(" °C", ""))
            if temp_value >= 70:
                alerts.append(f"High temperature detected: {temp}")
        except ValueError:
            pass

    if cpu != "N/A":
        try:
            cpu_value = float(cpu.replace("%", ""))
            if cpu_value >= 85:
                alerts.append(f"High CPU usage detected: {cpu}")
        except ValueError:
            pass

    return alerts

# ---------- SIDEBAR ----------
with st.sidebar:
    st.title("Lil Buddy")

    now = datetime.now()
    st.markdown("### Time & Date")
    st.write(now.strftime("%I:%M %p"))
    st.write(now.strftime("%A, %B %d, %Y"))

    st.markdown("---")
    st.markdown("### Quick Controls")

    if st.button("Wake Buddy"):
        wake_buddy()
        st.success("Wake command sent")

    if st.button("Stop Buddy"):
        stop_buddy()
        st.success("Stop command sent")

    if st.button("Center Head"):
        center_head()
        st.success("Center head command sent")

    if st.button("Mute Speaker"):
        mute_speaker()
        st.success("Mute speaker command sent")

    st.markdown("---")
    st.markdown("### Status")
    st.success("System Online")
    st.write("Camera: Connected")
    st.write("Audio: Ready")
    st.write("Battery: 87%")

    st.markdown("---")
    st.markdown("### Volume")
    volume = st.slider("Speaker Volume", 0, 100, 50)
    st.write(f"Volume set to {volume}%")

# ---------- MAIN HEADER ----------
st.title("Lil Buddy Control Dashboard")
st.caption("AI robot vision, music, health, control, and live status center")

header_left, header_right = st.columns([2, 1])

with header_left:
    st.subheader("Buddy Home Screen")

with header_right:
    now_main = datetime.now()
    st.metric("Time", now_main.strftime("%I:%M %p"))
    st.write(now_main.strftime("%A, %B %d, %Y"))

# ---------- SYSTEM HEALTH ----------
cpu, mem_used, mem_avail, temp, disk_free = get_system_stats()

health_col1, health_col2, health_col3, health_col4, health_col5 = st.columns(5)
health_col1.metric("Temp", temp)
health_col2.metric("CPU", cpu)
health_col3.metric("Mem Used", mem_used)
health_col4.metric("Mem Free", mem_avail)
health_col5.metric("Disk Free", disk_free)

# ---------- MODE + ALERTS ----------
st.markdown("---")
mode_col, alert_col = st.columns([1, 2])

with mode_col:
    st.subheader("Buddy Mode")
    mode = st.selectbox(
        "Select Mode",
        ["Idle", "Listening", "Talking", "Dancing", "Patrol"]
    )
    st.success(f"Current Mode: {mode}")

with alert_col:
    st.subheader("Alerts / Notifications")
    alerts = get_alerts(temp, cpu)

    if alerts:
        for alert in alerts:
            st.error(alert)
    else:
        st.warning("No alerts")

# ---------- BUDDY BRAIN ----------
st.markdown("---")
st.subheader("Buddy Brain")

status = read_status()

brain_col1, brain_col2, brain_col3 = st.columns(3)
brain_col1.info(f"Last Heard: {status['heard']}")
brain_col2.success(f"Response: {status['response']}")
brain_col3.warning(f"Mode: {status['mode']}")

# ---------- TOP LAYOUT ----------
left_col, right_col = st.columns([1, 2])

with left_col:
    st.subheader("Buddy Actions")

    if st.button("Look Left"):
        look_left()
        st.success("Look left command sent")

    if st.button("Look Right"):
        look_right()
        st.success("Look right command sent")

    if st.button("Look Up"):
        look_up()
        st.success("Look up command sent")

    if st.button("Look Down"):
        look_down()
        st.success("Look down command sent")

    if st.button("Speak"):
        speak()
        st.success("Speak command sent")

    if st.button("Dance Mode"):
        dance_mode()
        st.success("Dance mode command sent")

with right_col:
    st.subheader("Buddy Eyes Live View")

    frame = get_camera_frame(CAMERA_INDEX)

    if frame is not None:
        st.image(frame, channels="RGB", use_container_width=True)
    else:
        st.error("Camera not detected")

# ---------- WISH LIST ----------
st.markdown("---")
st.subheader("Buddy Wish List")

wish_items = [
    "New songs to play",
    "Dance upgrade",
    "Better vision tracking",
    "New voice lines",
    "More interactions"
]

for item in wish_items:
    st.write(f"- {item}")

# ---------- MUSIC PLAYER ----------
st.markdown("---")
st.subheader("Music Library")

music_files = get_music_files(MUSIC_FOLDER)

if not music_files:
    st.warning("No music files found. Add songs to the 'music' folder.")
else:
    song_names = [f.name for f in music_files]
    selected_song_name = st.selectbox("Choose a song", song_names)
    selected_song = next(
        (f for f in music_files if f.name == selected_song_name),
        None
    )

    playlist_col, player_col = st.columns([1, 2])

    with playlist_col:
        st.markdown("### Playlist")
        for name in song_names:
            st.write(f"• {name}")

    with player_col:
        st.markdown("### Now Playing")
        if selected_song:
            audio_bytes = selected_song.read_bytes()
            st.audio(audio_bytes, format=f"audio/{selected_song.suffix[1:]}")
            st.success(f"Playing: {selected_song.name}")

# ---------- FOOTER ----------
st.markdown("---")
st.caption("Next: connect Pi camera, servo hardware, wake word, and real voice output.")