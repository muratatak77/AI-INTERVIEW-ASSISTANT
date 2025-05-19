import sounddevice as sd
import numpy as np

recording_data = []


def start_recording(fs=16000):
    global stream, recording_data
    recording_data = []

    def callback(indata, frames, time, status):
        recording_data.append(indata.copy())

    stream = sd.InputStream(
        samplerate=fs, channels=1, dtype="float32", callback=callback
    )
    stream.start()


def stop_recording():
    global stream, recording_data
    stream.stop()
    stream.close()
    audio = np.concatenate(recording_data, axis=0).flatten()
    return audio, 16000


def transcribe_audio(audio, fs):
    import whisper

    model = whisper.load_model("tiny")
    return model.transcribe(audio, fp16=False)["text"]
