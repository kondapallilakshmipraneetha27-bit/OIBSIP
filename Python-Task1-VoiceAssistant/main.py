import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()
recognizer = sr.Recognizer()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=6)
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.WaitTimeoutError:
        speak("I did not hear anything. Please repeat.")
    except sr.UnknownValueError:
        speak("Sorry, I did not understand. Please repeat.")
    except sr.RequestError:
        speak("Network problem. Please check your internet.")
    return ""


speak("Voice assistant started. Say hello, time, date, search, or exit.")

while True:
    command = listen()
    if command == "":
        continue

    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        speak("The time is " + datetime.datetime.now().strftime("%I:%M %p"))
    elif "date" in command:
        speak("Today's date is " + datetime.datetime.now().strftime("%d %B %Y"))
    elif "search" in command:
        speak("What do you want to search?")
        topic = listen()
        if topic:
            speak("Searching for " + topic)
            webbrowser.open("https://www.google.com/search?q=" + topic.replace(" ", "+"))
    elif "exit" in command or "stop" in command or "bye" in command:
        speak("Goodbye!")
        break
    else:
        speak("Sorry, I can't do that yet.")
