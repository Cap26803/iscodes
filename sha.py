import hashlib


def sha1_hash(input_string):
    sha1 = hashlib.sha1()
    sha1.update(input_string.encode())
    return sha1.hexdigest()

def sha256_hash(input_string):
    sha256 = hashlib.sha256()
    sha256.update(input_string.encode())
    return sha256.hexdigest()

# Example Usage
input_string = "Hello, World!"
sha1_result = sha1_hash(input_string)
sha256_result = sha256_hash(input_string)

print("SHA-1 Hash:", sha1_result)
print("SHA-256 Hash:", sha256_result)