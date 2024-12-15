def encrypt_transposition(key, plaintext):
    plaintext = plaintext.replace(' ', '')
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

key = 5
plaintext = "HELLO WORLD"
print("Transposition Cipher:", encrypt_transposition(key, plaintext))
