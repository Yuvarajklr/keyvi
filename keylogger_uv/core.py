import os
import time
from pynput import keyboard
from cryptography.fernet import Fernet
from datetime import datetime
import re

KEY_FILE = "behavior_key.key"
LOG_FILE = "behavior_log.txt"
ENCRYPTED_LOG_FILE = "behavior_encrypted_log.bin"

def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as f:
            return f.read()
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)
    return key

fernet = Fernet(load_key())

def predict_behavior(typed, delays):
    avg_delay = sum(delays) / len(delays) if delays else 0
    text = typed.strip()

    if avg_delay < 0.2 and len(text) >= 8:
        return "Password"
    elif text.startswith("https://") or text.startswith("http://"):
        return "URL"
    elif re.match(r'^(cd|ls|sudo|ping|nmap)', text):
        return "Command"
    else:
        return "General"

def start_logging():
    keys = []
    timestamps = []

    def on_press(key):
        try:
            keys.append(key.char)
        except:
            keys.append(str(key))

        now = time.time()
        if timestamps:
            timestamps.append(now - timestamps[-1])
        else:
            timestamps.append(now)

        if key == keyboard.Key.esc:
            return False

    print("[🔴] Logging... Press ESC to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    if len(timestamps) > 1:
        delays = timestamps[1:]
    else:
        delays = [0.0]

    typed = ''.join(keys).replace('Key.space', ' ').replace('Key.enter', '\n')
    behavior = predict_behavior(typed, delays)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = f"[{timestamp}]\nTyped: {typed}\nDetected: {behavior}\nDelays: {delays}\n---\n"

    with open(LOG_FILE, 'a') as f:
        f.write(entry)

    encrypted = fernet.encrypt(entry.encode())
    with open(ENCRYPTED_LOG_FILE, 'ab') as f:
        f.write(encrypted + b"\n")

    print(f"[✅] Logged and encrypted. Classified as: {behavior}")

def analyze_logs():
    if not os.path.exists(LOG_FILE):
        print("[❌] No log file found.")
        return
    with open(LOG_FILE, 'r') as f:
        print("[🧠] Behavior Analysis:\n")
        print(f.read())

def decrypt_logs():
    if not os.path.exists(ENCRYPTED_LOG_FILE):
        print("[❌] No encrypted logs found.")
        return
    with open(ENCRYPTED_LOG_FILE, 'rb') as f:
        lines = f.readlines()
        print("[🔓] Decrypted Log:\n")
        for line in lines:
            try:
                print(fernet.decrypt(line).decode())
            except:
                print("[!] Failed to decrypt one line.")
