import random


def diffie_hellman():
    p = 23  # Prime number
    g = 5   # Primitive root mod p
    alice_private = random.randint(1, p-1)
    bob_private = random.randint(1, p-1)
    alice_public = (g ** alice_private) % p
    bob_public = (g ** bob_private) % p
    alice_shared = (bob_public ** alice_private) % p
    bob_shared = (alice_public ** bob_private) % p
    assert alice_shared == bob_shared
    return alice_shared

print("Diffie-Hellman Shared Key:", diffie_hellman())