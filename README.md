# 🤖 AI-INTERVIEW-ASSISTANT

AI-INTERVIEW-ASSISTANT is an AI-powered interview assistant that helps users prepare for behavioral and technical questions using OpenAI's language models. It transcribes, analyzes, and responds to answers in real-time.

---

## 🚀 Setup

### 1. Clone the repository

```bash
git clone https://github.com/muratatak77/AI-INTERVIEW-ASSISTANT.git
cd AI-INTERVIEW-ASSISTANT
```

### 2. Make sure `pyenv` is installed

Install via Homebrew (macOS):

```bash
brew install pyenv
```

Or follow instructions from [pyenv GitHub page](https://github.com/pyenv/pyenv).

### 3. Run the setup script

```bash
chmod +x setup.sh
./setup.sh
```

This will:

- Set Python to version 3.10.13 via `pyenv`
- Create and activate a virtual environment in `.venv/`
- Install dependencies from `requirements.txt`
- Copy `.env.example` to `.env`
- Downgrade `numpy` to ensure compatibility

---

## 🧪 Usage

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Then run the app (example):

```bash
python app.py
```

Make sure to replace `app.py` with the actual entry point if different.

---

## 🔐 Environment Variables

Create a `.env` file at the root of the project (automatically done by the setup script). It should include your OpenAI key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 📁 Project Structure

```
AI-INTERVIEW-ASSISTANT/
├── analyzer.py
├── app.py
├── transcriber.py
├── requirements.txt
├── setup.sh
├── .env.example
├── resume.txt
├── behavioral_questions.txt
└── .venv/
```

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

MIT License
