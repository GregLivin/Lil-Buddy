from pathlib import Path

STATUS_FILE = Path("data/live_status.txt")

def write_status(heard="", response="", mode="Idle"):
    STATUS_FILE.parent.mkdir(exist_ok=True)
    STATUS_FILE.write_text(
        f"Heard: {heard}\nResponse: {response}\nMode: {mode}",
        encoding="utf-8"
    )

def read_status():
    if not STATUS_FILE.exists():
        return {
            "heard": "Nothing yet",
            "response": "No response yet",
            "mode": "Idle"
        }

    lines = STATUS_FILE.read_text(encoding="utf-8").splitlines()
    result = {
        "heard": "Nothing yet",
        "response": "No response yet",
        "mode": "Idle"
    }

    for line in lines:
        if line.startswith("Heard: "):
            result["heard"] = line.replace("Heard: ", "", 1)
        elif line.startswith("Response: "):
            result["response"] = line.replace("Response: ", "", 1)
        elif line.startswith("Mode: "):
            result["mode"] = line.replace("Mode: ", "", 1)

    return result