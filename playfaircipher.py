def generate_key_matrix(key):
    key = key.upper().replace('J', 'I')
    seen = set()
    matrix = []
    for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def encrypt_playfair(key, plaintext):
    matrix = generate_key_matrix(key)
    plaintext = plaintext.upper().replace('J', 'I').replace(' ', '')
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    ciphertext = ''
    for a, b in zip(plaintext[::2], plaintext[1::2]):
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        if row_a == row_b:
            ciphertext += matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            ciphertext += matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
        else:
            ciphertext += matrix[row_a][col_b] + matrix[row_b][col_a]
    return ciphertext

def decrypt_playfair(key, ciphertext):
    matrix = generate_key_matrix(key)
    plaintext = ''
    for a, b in zip(ciphertext[::2], ciphertext[1::2]):
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        if row_a == row_b:
            plaintext += matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            plaintext += matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]
        else:
            plaintext += matrix[row_a][col_b] + matrix[row_b][col_a]
    return plaintext

key = "MONARCHY"
plaintext = "HELLO WORLD"
ciphertext = encrypt_playfair(key, plaintext)
print("Playfair Cipher (Encrypted):", ciphertext)

decrypted_text = decrypt_playfair(key, ciphertext)
print("Playfair Cipher (Decrypted):", decrypted_text)