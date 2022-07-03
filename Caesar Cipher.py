def converter():  # This function will either use a encrypt or decrypt formula
    new_position = ""
    position = alphabet.find(character)
    if response == "E":   # Encrypt formula
        new_position = (position + key) % 26
    elif response == "D":  # Decrypt formula
        new_position = (position - key) % 26
    new_character = alphabet[new_position]
    return new_character


alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Ask the user if they want to encrypt or decrypt
while response := input("Do you want to (E)ncrypt or (D)ecrypt: ").upper():
    if response == "E" or response == "D":
        break

# Ask the user for the message or the key
user_message = input("Enter your secret message: ")
key = int(input("What is the key: "))

secret_message = ""
for character in user_message:  # Handles uppercase, lowercase, and space characters
    if character.isupper():
        character = character.lower()
        if character in alphabet:
            converter()
            secret_message += converter().upper()
    elif character.islower():
        if character in alphabet:
            converter()
            secret_message += converter()
    else:
        secret_message += character
print(">" + secret_message)
