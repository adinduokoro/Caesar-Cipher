def converter(alphabet):
    position = alphabet.find(character)
    new_position = (position + key) % 26
    new_character = alphabet[new_position]
    return new_character


alphabet = "abcdefghijklmnopqrstuvwxyz"

user_message = input("Enter your secret message: ")  # Get the message from the user
key = int(input("What is the key: "))  # Get the key from the user

secret_message = ""
for character in user_message:
    if character.isupper():
        character = character.lower()
        if character in alphabet:
            converter(alphabet)
            secret_message += converter(alphabet).upper()
    elif character.islower():
        if character in alphabet:
            converter(alphabet)
            secret_message += converter(alphabet)
    else:
        secret_message += character
print(secret_message)
