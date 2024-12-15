from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


def rsa_encrypt(plaintext, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    return cipher.encrypt(plaintext.encode())


def rsa_decrypt(ciphertext, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    return cipher.decrypt(ciphertext).decode()


# Example Usage
key_pair = RSA.generate(2048)
public_key = key_pair.publickey()
plaintext = "Secure Message"
ciphertext = rsa_encrypt(plaintext, public_key)
print("Encrypted:", ciphertext)
print("Decrypted:", rsa_decrypt(ciphertext, key_pair))
