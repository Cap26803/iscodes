from tinyec import registry


def ecc_example():
    curve = registry.get_curve('brainpoolP256r1')
    alice_private_key = 0xA0DC65FFCA799873
    bob_private_key = 0x9C8A3E8D8A1FB663
    alice_public_key = alice_private_key * curve.g
    bob_public_key = bob_private_key * curve.g
    shared_key_alice = alice_private_key * bob_public_key
    shared_key_bob = bob_private_key * alice_public_key
    assert shared_key_alice == shared_key_bob
    return shared_key_alice

print("ECC Shared Key:", ecc_example())