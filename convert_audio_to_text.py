import whisper

model = whisper.load_model("base")
result = model.transcribe("audio_input.wav")
print(result["text"])