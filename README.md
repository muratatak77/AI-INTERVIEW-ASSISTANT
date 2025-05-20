Here's the updated **README** in English with your requested change:

---

# 🤖 AI-INTERVIEW-ASSISTANT

**AI-INTERVIEW-ASSISTANT** is an AI-powered interview assistant that helps users prepare for behavioral and technical questions using OpenAI's language models. During an interview, **it records the interviewer's voice and instantly provides suggestions and responses** based on your answers — all in real time.

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

Or follow the instructions from the [pyenv GitHub page](https://github.com/pyenv/pyenv).

### 3. Run the setup script

```bash
chmod +x setup.sh
./setup.sh
```

This will:

* Set Python to version 3.10.13 via `pyenv`
* Create and activate a virtual environment in `.venv/`
* Install dependencies from `requirements.txt`
* Copy `.env.example` to `.env`
* Downgrade `numpy` to ensure compatibility

---

## 🧪 Usage

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Then run the app (example):

```bash
streamlit run app.py
```

Make sure to replace `app.py` with the actual entry point if different.

---

## 🔐 Environment Variables

Create a `.env` file at the root of the project (automatically done by the setup script). It should include your OpenAI API key:

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

## 🎤 Real-Time Interview Mode

During an interview session, the assistant:

* **Records the interviewer’s voice**
* **Transcribes the conversation**
* **Analyzes your responses**
* **Instantly provides suggestions, feedback, and follow-ups**

This enables you to improve your answers on the fly and get better prepared with each session.



https://github.com/user-attachments/assets/bd1a3662-9166-44f8-b5d1-f519edbf6e2e



---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

MIT License

---

Let me know if you'd like to include a GIF or screenshot section for better visual clarity!
