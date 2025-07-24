#!/bin/bash

# === [📦 Create requirements.txt if missing] ===
if [ ! -f requirements.txt ]; then
    echo "🔍 requirements.txt not found. Creating a basic one..."
    echo -e "pynput\ncryptography" > requirements.txt
    echo "✅ Created requirements.txt with basic dependencies."
fi

# === [🐍 Virtual Environment Setup] ===
echo "🔧 Creating virtual environment..."
python3 -m venv venv || { echo "❌ Failed to create virtualenv"; exit 1; }

echo "🚀 Activating virtual environment..."
source venv/bin/activate || { echo "❌ Failed to activate venv"; exit 1; }

# === [📥 Install Dependencies] ===
echo "📦 Upgrading pip..."
pip install --upgrade pip

echo "📦 Installing from requirements.txt..."
pip install pynput
pip install cryptography

# === [🧠 Install CLI Tool in Editable Mode] ===
echo "🧠 Installing project in editable mode..."
pip install -e . || { echo "❌ pip install -e . failed"; exit 1; }

# === [🎯 Final Info] ===
echo "✅ Setup complete!"
echo "📂 To activate venv later: source venv/bin/activate"
echo "📌 To run CLI: keyvi --help"

# === [🛠 Make setup.sh executable] ===
chmod +x setup.sh
