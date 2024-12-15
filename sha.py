import hashlib


def sha1_hash(input_string):
    # Create a new sha1 hash object
    sha1 = hashlib.sha1()
    # Update the hash object with the bytes of the input string
    sha1.update(input_string.encode())
    # Return the hexadecimal digest of the hash
    return sha1.hexdigest()

def sha256_hash(input_string):
    # Create a new sha256 hash object
    sha256 = hashlib.sha256()
    # Update the hash object with the bytes of the input string
    sha256.update(input_string.encode())
    # Return the hexadecimal digest of the hash
    return sha256.hexdigest()

# Example Usage
input_string = "Hello, World!"
sha1_result = sha1_hash(input_string)
sha256_result = sha256_hash(input_string)

print("SHA-1 Hash:", sha1_result)
print("SHA-256 Hash:", sha256_result)