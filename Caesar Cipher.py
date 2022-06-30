def converter():
    position = alphabet.find(character)
    new_position = (position + key) % 26
    new_character = alphabet[new_position]
    return new_character


alphabet = 'abcdefghijklmnopqrstuvwxyz'

while True:
    response = input("Do you want to Encrypt or Decrypt: ").upper()
    if response == "E" or response == "D":
        break

user_message = input("Enter your secret message: ")  # Get the message from the user
key = int(input("What is the key: "))  # Get the key from the user

secret_message = ""
for character in user_message:
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
print(secret_message)
