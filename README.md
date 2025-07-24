# 🔐 Smart Behavior-Based Keylogger (CLI Tool)

A Python-based intelligent keylogger that:
- Detects user typing behavior (Password, URL, Command, General)
- Encrypts logs securely using Fernet (AES)
- Provides a custom CLI (`keyvi`) to control all actions

> ⚡ Built without TensorFlow — lightweight, simple, and powerful.

---

## 📌 Features

- 🧠 Rule-based behavior detection (no AI model required)
- ⌨️ Keylogging with timing analysis
- 🔐 Secure encryption using Fernet (AES symmetric encryption)
- 📊 Behavior log analysis
- 🔓 Encrypted log decryption
- ⚙️ Installable CLI tool: `keyvi`

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Yuvarajklr/keyvi.git
cd keyvi

2. Run the setup script

bash setup.sh

This will:

    Create a virtual environment

    Install required dependencies

    Install the keyvi CLI globally (editable mode)

    Make the setup.sh script executable

🧪 How to Use
➤ Activate environment (if not already active)

source venv/bin/activate

➤ Run commands

keyvi --start      # Start keylogging (press ESC to stop)
keyvi --analyze    # Analyze recorded behavior logs
keyvi --decrypt    # Decrypt and view encrypted logs

📁 Project Structure

keyvi/
├── keylogger_uv/             # Main Python package
│   ├── __init__.py
│   └── clic.py                # CLI logic
├── setup.py                  # Python packaging config
├── setup.sh                  # Auto-setup script
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

📜 License

This project is licensed under the MIT License.[https://github.com/Yuvarajklr/keyvi/blob/main/LICENSE]
You're free to use, modify, and share it — with proper credit.
