from itertools import cycle, islice

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(plain_text, shift_amt):
    cipher_text = ""
    alphabet.extend(list(islice(cycle(alphabet), shift_amt)))

    for letter in plain_text:
        pos = alphabet.index(letter)
        new_pos = pos + shift_amt
        new_letter = alphabet[new_pos]
        cipher_text += new_letter

    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    decrypted = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        decrypted += alphabet[new_position]

    print(f"The decoded text is {decrypted}")


if __name__ == "__main__":

    if direction.startswith('enc'):
        encrypt(plain_text=text, shift_amt=shift)
    else:
        decrypt(cipher_text=text, shift_amount=shift)
