def encrypt_transposition(key, plaintext):
    plaintext = plaintext.replace(' ', '')
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def decrypt_transposition(key, ciphertext):
    num_full_columns = len(ciphertext) // key
    num_short_columns = len(ciphertext) % key

    column_lengths = [num_full_columns + 1] * num_short_columns + [num_full_columns] * (key - num_short_columns)

    columns = []
    index = 0
    for length in column_lengths:
        columns.append(ciphertext[index:index + length])
        index += length

    plaintext = ''
    for i in range(num_full_columns + 1):
        for column in columns:
            if i < len(column):
                plaintext += column[i]
    return plaintext

key = 5
plaintext = "HELLO WORLD"
ciphertext = encrypt_transposition(key, plaintext)
print("Transposition Cipher:", ciphertext)
print("Decrypted Text:", decrypt_transposition(key, ciphertext))