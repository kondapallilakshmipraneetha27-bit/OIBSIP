import datetime
import webbrowser

print("Voice Assistant")
print("1. Show time")
print("2. Open Google")
print("3. Say hello")

choice = input("Choose an option (1-3): ")

if choice == "1":
    print("Current time:", datetime.datetime.now().strftime("%I:%M %p"))
elif choice == "2":
    print("Opening Google...")
    webbrowser.open("https://www.google.com")
elif choice == "3":
    print("Hello! How can I help you?")
else:
    print("Invalid choice")
