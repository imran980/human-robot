
import requests
import pyaudio
import numpy as np

# Define the URL of your Flask API
api_server_address = "http://10.205.5.5:5555"  # Replace with the actual server address
print("sarting ...")
# Function to capture audio locally
def capture_audio(sample_rate=16000, record_duration=2):
    print("Line 1 ...")
    p = pyaudio.PyAudio()
    print("Line 2 ...")
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True,
                    frames_per_buffer=1024)
    print("Line 3 ...")
    audio_frames = []
    for _ in range(0, int(sample_rate / 1024 * record_duration)):
        data = stream.read(1024)
        audio_frames.append(data)
    print("Line 4 ...")
    stream.stop_stream()
    print("Line 44 ...")
    stream.close()
    p.terminate()
    print("Line 5 ...")
    # Concatenate the audio frames into a single bytes object
    audio_data = b''.join(audio_frames)
    return audio_data

# Start recording on the API server
start_recording_url = "http://10.205.5.5:5555/start_recording"
print("start_recording ...")
response = requests.post(start_recording_url)
print("Line 7 ...", response)
if response.status_code == 200:
    print("Recording started on the server.")
else:
    print("Error starting recording:", response.status_code)

# Continuously record audio and send it to the server
while True:
    audio_data = capture_audio()
    transcription_url = "http://10.205.5.5:5555/get_transcription"
    response = requests.get(transcription_url)
    if response.status_code == 200:
        transcription = response.json().get("transcription")
        print("Transcription:", transcription)
    else:
        print("Error getting transcription:", response.status_code)
