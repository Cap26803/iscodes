from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), DES.block_size))
    return ciphertext


def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return plaintext.decode()


# Example Usage
key = b"8bytekey"  # DES requires an 8-byte key
plaintext = "Data to Encrypt"
ciphertext = des_encrypt(plaintext, key)
print("Encrypted:", ciphertext)
print("Decrypted:", des_decrypt(ciphertext, key))
