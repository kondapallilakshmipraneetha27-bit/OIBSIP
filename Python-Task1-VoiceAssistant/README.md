# Voice Assistant

## Description
A Python voice assistant that listens to spoken commands through the microphone and replies with speech.

## Features
* Captures voice input using the `speech_recognition` library.
* Replies to "hello" with a greeting.
* Tells the current time and date.
* Searches the web: say "search", then say your topic, and the browser opens Google with it.
* If the voice is not understood, it asks the user to repeat.
* Speaks every reply using `pyttsx3` (text-to-speech).
* Say "exit", "stop" or "bye" to close the assistant.

## Technology
* Python 3.12
* `SpeechRecognition`
* `pyttsx3`
* `PyAudio`
* `datetime` and `webbrowser` modules

## How to Run
1. Install the libraries:
   `pip install SpeechRecognition pyttsx3 pyaudio`
2. Run the program:
   `python main.py`
3. When it says "Listening...", speak a command: hello, time, date, search, or exit.

An internet connection and a working microphone are required.

## Privacy
Your voice is recorded only while the program is listening. The audio is sent to Google's free speech recognition service to convert it to text. No audio or text is saved to any file.

## Project Files
* `main.py` - voice assistant source code.
* Screenshot - example output.
