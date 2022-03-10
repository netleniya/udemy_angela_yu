import string
from art import logo

alphabet = [i for i in string.ascii_lowercase]


def caesar(message, shift_value, cipher_direction):

    result = ""
    if cipher_direction.startswith('dec'):
        shift_value *= -1

    alphabet.extend(alphabet)

    for char in message:
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = pos + shift_value
            result += alphabet[new_pos]
        else:
            result += char

    print(f"The {cipher_direction}d text is: {result}")


if __name__ == "__main__":

    print(logo)

    play_on = True

    while play_on:
        answer = input("Any text to encrypt/decrypt? (Y/N): ").lower()
        if answer.startswith('y'):
            direction = input(
                "Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))

            shift %= 26

            caesar(message=text, shift_value=shift, cipher_direction=direction)
        else:
            print("Arrivederci...")
            play_on = False
