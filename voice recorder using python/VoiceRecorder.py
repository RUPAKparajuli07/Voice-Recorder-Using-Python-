import pyaudio
import wave
import threading
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import time

class VoiceRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Recorder")
        self.root.geometry("1000x800")

        self.sample_rate = 44100
        self.chunk_size = 8192
        self.audio_format = pyaudio.paInt16
        self.channels = 2
        self.is_recording = False
        self.frames = []

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.background_image = Image.open("background.jpg")
        self.background_image = self.background_image.resize((screen_width, screen_height), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.canvas = tk.Canvas(root, width=screen_width, height=screen_height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_photo)

        self.record_button = tk.Button(root, text="Record", command=self.toggle_recording,
                                       font=("Times New Roman", 30), fg="orange", bg="black")
        self.record_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.save_button = tk.Button(root, text="Save Recording", command=self.save_recording,
                                     font=("Times New Roman", 30), fg="orange", bg="black")
        self.save_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        self.status_label = tk.Label(root, text="", font=("Times New Roman", 20), fg="orange", bg="black")
        self.status_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    def toggle_recording(self):
        if not self.is_recording:
            self.is_recording = True
            self.record_button.config(text="Stop Recording")
            self.status_label.config(text="Recording...")
            self.start_recording_thread()
        else:
            self.is_recording = False
            self.record_button.config(text="Record")
            self.status_label.config(text="Recording stopped")

    def start_recording_thread(self):
        recording_thread = threading.Thread(target=self.record_audio)
        recording_thread.start()

    def record_audio(self):
        audio = pyaudio.PyAudio()
        self.frames = []
        start_time = time.time()

        stream = audio.open(format=self.audio_format,
                            channels=self.channels,
                            rate=self.sample_rate,
                            input=True,
                            frames_per_buffer=self.chunk_size)

        while self.is_recording:
            data = stream.read(self.chunk_size)
            self.frames.append(data)
            
            elapsed_time = int(time.time() - start_time)
            minutes, seconds = divmod(elapsed_time, 60)
            recording_time = f"Recording... {minutes:02d}:{seconds:02d}"
            self.status_label.config(text=recording_time)

        stream.stop_stream()
        stream.close()
        audio.terminate()

    def save_recording(self):
        if not self.frames:
            self.status_label.config(text="No recording to save.")
            return

        output_file = filedialog.asksaveasfilename(defaultextension=".wav",
                                                   filetypes=[("WAV files", "*.wav")])

        if output_file:
            wf = wave.open(output_file, 'wb')
            wf.setnchannels(self.channels)
            wf.setsampwidth(pyaudio.get_sample_size(self.audio_format))
            wf.setframerate(self.sample_rate)
            wf.writeframes(b''.join(self.frames))
            wf.close()

            self.status_label.config(text=f"Recording saved as '{output_file}'")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceRecorderApp(root)
    root.mainloop()
