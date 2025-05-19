import streamlit as st
from transcriber import start_recording, stop_recording, transcribe_audio
from analyzer import analyze_transcript

if "recording" not in st.session_state:
    st.session_state.recording = False

st.title("🎤 Real-Time AI Interview Assistant")

if not st.session_state.recording:
    if st.button("🎙️ Start Recording"):
        start_recording()
        st.session_state.recording = True
        st.rerun()
else:
    if st.button("⏹ Stop Recording"):
        audio, fs = stop_recording()
        question = transcribe_audio(audio, fs)
        st.session_state.recording = False

        st.markdown("### ❓ Transcribed Question")
        st.text_area("Transcription:", question, height=100)

        answer = analyze_transcript(question)
        st.markdown("### 🤖 Suggested Answer")
        st.write(answer)
