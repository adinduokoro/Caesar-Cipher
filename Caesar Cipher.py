alphabet = "abcdefghijklmnopqrstuvwxyz"

user_message = input("Enter your secret message: ")  # Get the message from the user
key = int(input("What is the key: "))  # Get the key from the user

secret_message = ""  # Holds the secret message
for character in user_message:  # Updates the character in the user message
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position + key) % 26
        new_character = alphabet[new_position]
        secret_message += new_character
print(secret_message)
