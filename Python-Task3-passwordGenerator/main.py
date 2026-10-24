import secrets
import string

print("PASSWORD GENERATOR")

length = int(input("Enter password length: "))

if length <= 0:
    print("Please enter a positive length.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    print("Your password is:", password)
