import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = ['h', '<', ' ', 'O', 'H', '0', 'R', 'B', 'J', 'X', 'T', 'C', '9', ':', '[', '6', '2', 'b', '~', 'r', 'e', 'c', 'y', 'L', 'N', '|', '+', '7', 'k', '3', 'm', '{', 'j', ')', 'o', '^', '_', 'E', 'v', 'S', '.', 'K', '(', '/', 'D', 'i', '@', '$', 'p', 'g', ',', '}', '*', "'", 'n', '1', '%', 'Y', 'f', 'U', 'P', 'V', '?', 'Q', 'M', 'l', 'u', '4', 'q', '-', 'Z', 'd', '\\', 'G', 'W', '>', ';', 'w', 's', '5', '"', 'z', 't', '#', 'x', 'a', 'F', '`', ']', '=', '!', '&', 'A', 'I', '8']

while True:
    mode = input('Select mode(d for decrypt/e to encrypt): ').strip().lower()
    if mode == 'e':
        plain_text = input('Enter a message to encrypt: ')
        cipher_text = ""
        for letter in plain_text:
            index = chars.index(letter)
            cipher_text += key[index]

        print(f'Here is the encryption: {cipher_text}')
        continue

    if mode == 'd':
        plain_text = ""
        cipher_text = input("Enter a message to decrypt: ")
        for letter in cipher_text:
            index = key.index(letter)
            plain_text += chars[index]

        print(f'Here is the decryption: {plain_text}')
        continue