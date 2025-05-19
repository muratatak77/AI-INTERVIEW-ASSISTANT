#!/bin/bash

# Setup script for AI-INTERVIEW-ASSISTANT
# Run with: chmod +x setup.sh && ./setup.sh

echo "🔧 Checking pyenv..."
if ! command -v pyenv &> /dev/null; then
  echo "❌ pyenv not found. Please install pyenv first."
  exit 1
fi

echo "🐍 Setting Python version to 3.10.13..."
pyenv install -s 3.10.13
pyenv local 3.10.13

echo "💥 Removing old virtual environment..."
rm -rf .venv

echo "🧪 Creating new virtual environment..."
python -m venv .venv

echo "⚙️ Activating virtual environment..."
source .venv/bin/activate

echo "🔐 Checking for .env file..."
if [ ! -f .env ]; then
  cp .env.example .env
  echo "✅ .env file created from .env.example."
fi

echo "📦 Cleaning up requirements.txt..."
grep -v '^whisper$' requirements.txt > temp_requirements.txt
mv temp_requirements.txt requirements.txt

echo "📦 Installing dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo "📉 Downgrading numpy to 1.26.4 for compatibility..."
pip install numpy==1.26.4

echo "✅ Setup complete. Environment is ready!"
