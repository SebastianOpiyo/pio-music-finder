import pyaudio
import wave

# Parameters
chunk = 1024  # Number of frames per buffer
fs = 44100  # Sampling rate (Hz)
seconds = 3  # Duration of recording
format = pyaudio.paInt16  # Format for audio
channels = 2  # Number of audio channels
output_file = "output.wav"  # Output file name

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open stream
stream = p.open(format=format,
                channels=channels,
                rate=fs,
                input=True,
                frames_per_buffer=chunk)

print("Recording...")

frames = []

# Record in chunks for the specified duration
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

print("Recording finished.")

# Stop and close the stream
stream.stop_stream()
stream.close()
p.terminate()

# Save the recorded data as a WAV file
wf = wave.open(output_file, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()

print(f"Audio saved to {output_file}")
