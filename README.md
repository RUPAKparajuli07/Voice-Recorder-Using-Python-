# Voice Recorder App Documentation

## Overview
This documentation provides an explanation of the "Voice Recorder" application, which allows users to record audio and save it as a WAV file. The app is built using Python and the tkinter library for the graphical user interface (GUI). It utilizes the pyaudio library to handle audio input and output, and the PIL library to display a background image on the GUI.

## Requirements
- Python 3.x
- tkinter library
- pyaudio library
- PIL library (Pillow)

## Class: VoiceRecorderApp
This class represents the main application for the Voice Recorder.

### Constructor
```
def __init__(self, root)
```
- `root`: The root window of the application.

### Attributes
- `self.sample_rate`: An integer representing the audio sample rate (44100 samples per second).
- `self.chunk_size`: An integer representing the number of audio frames per buffer (8192 frames).
- `self.audio_format`: An integer representing the audio format (pyaudio.paInt16).
- `self.channels`: An integer representing the number of audio channels (2 channels for stereo).
- `self.is_recording`: A boolean flag to indicate if the app is currently recording audio.
- `self.frames`: A list to store the audio data frames during recording.

### Methods

#### `toggle_recording(self)`
This method is called when the "Record" button is pressed. It toggles between starting and stopping the audio recording.

#### `start_recording_thread(self)`
This method starts a new thread to handle the audio recording.

#### `record_audio(self)`
This method is executed in a separate thread to record audio. It opens an audio stream, continuously reads audio data, and appends the frames to the `self.frames` list while `self.is_recording` is `True`. It also updates the recording time on the GUI.

#### `save_recording(self)`
This method is called when the "Save Recording" button is pressed. It prompts the user to choose a file name and location to save the recorded audio as a WAV file. If no frames are recorded, it displays an appropriate message.

## How to Use
1. Import the required libraries and classes.
2. Create a `tkinter` root window.
3. Initialize the `VoiceRecorderApp` class, passing the `root` window as an argument.
4. Call the `mainloop()` method on the `root` window to run the application.

## Sample Output
The application provides a graphical user interface (GUI) with the following components:
- A "Record" button: Click this button to start recording audio. While recording, the button text changes to "Stop Recording." Click it again to stop the recording.
- A "Save Recording" button: Click this button to save the recorded audio as a WAV file. If there is no recording, a message will be displayed.
- A status label: This label displays the recording status, either "Recording..." along with the elapsed time or "Recording stopped" when the recording is stopped.


Please note that the background image displayed in the demos may vary depending on the image you choose to use.

## Important Notes
- The audio format used in the application is `pyaudio.paInt16`, which corresponds to 16-bit signed integer PCM audio format.
- The audio is recorded with a sample rate of 44100 Hz, which is commonly used for high-quality audio recording.
- The application saves the recorded audio as a WAV file, but you can modify it to support other audio formats if needed.
- Ensure that you have the necessary permissions to access the microphone when running the application to record audio successfully.

This concludes the documentation for the "Voice Recorder" application. Enjoy recording audio effortlessly with this app!
