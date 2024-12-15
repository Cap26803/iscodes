import random
import string


def generate_key():
    letters = string.ascii_uppercase
    key = ''.join(random.sample(letters, len(letters)))
    return key

def encrypt_message(message, key):
    upper_message = message.upper()
    table = str.maketrans(string.ascii_uppercase, key)
    return upper_message.translate(table)

def decrypt_message(ciphertext, key):
    table = str.maketrans(key, string.ascii_uppercase)
    return ciphertext.translate(table)

# Example usage
message = 'HELLO, WORLD'
key = generate_key()

encrypted_message = encrypt_message(message, key)
print('Key:', key)
print('Encrypted:', encrypted_message)

decrypted_message = decrypt_message(encrypted_message, key)
print('Decrypted:', decrypted_message)
