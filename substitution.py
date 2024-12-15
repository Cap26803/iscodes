def encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

def decrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    return result

text = "ATTACKATONCE"
s = 5

encrypted_text = encrypt(text, s)
print(f"Original Text : {text}")
print(f"Shift Amount  : {s}")
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = decrypt(encrypted_text, s)
print(f"Decrypted Text: {decrypted_text}")