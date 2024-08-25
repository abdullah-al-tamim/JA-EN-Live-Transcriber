import pyaudio
import wave
import threading

class AudioCapture:
    def __init__(self, output_filename="output.wav", chunk_size=1024, channels=2, rate=44100, input_device_index=None):
        self.output_filename = output_filename
        self.chunk_size = chunk_size
        self.channels = channels
        self.rate = rate
        self.format = pyaudio.paInt16

        self.p = pyaudio.PyAudio()
        self.stream = None
        self.frames = []
        self.is_recording = False

        # List all available input devices
        if input_device_index is None:
            self.input_device_index = self.get_device_index()
        else:
            self.input_device_index = input_device_index

    def get_device_index(self):
        device_index = None
        print("Available audio input devices:")
        for i in range(self.p.get_device_count()):
            info = self.p.get_device_info_by_index(i)
            print(f"{i}: {info['name']}")

            # Automatically select "Stereo Mix" if available
            if "Stereo Mix" in info['name']:
                device_index = i
        if device_index is None:
            raise ValueError("Stereo Mix not found. Please enable it in the sound settings.")
        return device_index

    def start_recording(self):
        if self.is_recording:
            print("Already recording...")
            return

        self.stream = self.p.open(format=self.format,
                                  channels=self.channels,
                                  rate=self.rate,
                                  input=True,
                                  input_device_index=self.input_device_index,
                                  frames_per_buffer=self.chunk_size)

        self.frames = []
        self.is_recording = True

        threading.Thread(target=self._record).start()
        print("Recording started...")

    def _record(self):
        while self.is_recording:
            data = self.stream.read(self.chunk_size)
            self.frames.append(data)

    def stop_recording(self):
        if not self.is_recording:
            print("Not recording...")
            return

        self.is_recording 
