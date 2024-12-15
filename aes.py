from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return cipher.iv + ciphertext


def aes_decrypt(ciphertext, key):
    iv = ciphertext[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[16:]), AES.block_size)
    return plaintext.decode()


# Example Usage
key = get_random_bytes(16)  # 128-bit key
plaintext = "This is Elon Musk,Saviour of humanity."
ciphertext = aes_encrypt(plaintext, key)
print("Encrypted:", ciphertext)
print("Decrypted:", aes_decrypt(ciphertext, key))
