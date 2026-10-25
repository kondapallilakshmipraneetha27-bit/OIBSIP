import secrets
import string

while True:
    print("\nPASSWORD GENERATOR")

    length = input("Enter password length (minimum 8): ")

    if not length.isdigit() or int(length) < 8:
        print("Please enter a valid length of at least 8.")
        continue

    characters = ""

    if input("Include uppercase letters? (y/n): ").lower() == "y":
        characters += string.ascii_uppercase

    if input("Include lowercase letters? (y/n): ").lower() == "y":
        characters += string.ascii_lowercase

    if input("Include numbers? (y/n): ").lower() == "y":
        characters += string.digits

    if input("Include symbols? (y/n): ").lower() == "y":
        characters += string.punctuation

    if not characters:
        print("Select at least one character type.")
        continue

    password = "".join(
        secrets.choice(characters) for _ in range(int(length))
    )

    print("Your password is:", password)

    again = input("Generate another? (y/n): ").lower()
    if again != "y":
        break
