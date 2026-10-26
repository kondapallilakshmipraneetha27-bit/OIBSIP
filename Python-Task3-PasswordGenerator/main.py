import secrets
import string

while True:
    print("\nPASSWORD GENERATOR")

    length = input("Enter password length (minimum 8): ")

    if not length.isdigit() or int(length) < 8:
        print("Please enter a valid length of at least 8.")
        continue

    length = int(length)
    groups = []

    if input("Include uppercase letters? (y/n): ").lower() == "y":
        groups.append(string.ascii_uppercase)

    if input("Include lowercase letters? (y/n): ").lower() == "y":
        groups.append(string.ascii_lowercase)

    if input("Include numbers? (y/n): ").lower() == "y":
        groups.append(string.digits)

    if input("Include symbols? (y/n): ").lower() == "y":
        groups.append(string.punctuation)

    if len(groups) < 2:
        print("Please select at least 2 character types.")
        continue

    # take one character from each chosen type
    password_chars = [secrets.choice(g) for g in groups]
    all_chars = "".join(groups)

    # fill the rest of the length
    while len(password_chars) < length:
        password_chars.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password_chars)
    password = "".join(password_chars)

    print("Your password is:", password)

    again = input("Generate another? (y/n): ").lower()
    if again != "y":
        break
