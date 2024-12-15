import numpy as np


def encrypt_hill(key_matrix, plaintext):
    plaintext = plaintext.upper().replace(' ', '')
    while len(plaintext) % len(key_matrix) != 0:
        plaintext += 'X'
    plaintext_vector = [ord(char) - 65 for char in plaintext]
    key_matrix = np.array(key_matrix)
    ciphertext = ""
    for i in range(0, len(plaintext_vector), len(key_matrix)):
        chunk = plaintext_vector[i:i+len(key_matrix)]
        result = np.dot(key_matrix, chunk) % 26
        ciphertext += ''.join(chr(num + 65) for num in result)
    return ciphertext

key_matrix = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
plaintext = "HELLO"
print("Hill Cipher:", encrypt_hill(key_matrix, plaintext))