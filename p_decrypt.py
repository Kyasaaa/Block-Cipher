from utils import *


if __name__ == '__main__':
    import os
    # Clearing the Screen
    # os.system('cls')

    # 1. Get the ciphertext as a bits
    f = open("c.txt", "r", encoding="utf-8")
    cipher = f.read()
    f.close()
    # pad with "." if length is not a multiple of 16
    if (len(cipher) % 16 != 0):
        cipher += "." * (16 - len(cipher) % 16)

    cipher_bits = string_2_bit_string(cipher)
    print(cipher_bits)
    
    # 2. Get 16 subkeys from external key
    key = "ABCDEFGHIJKLMNOP"
    subkeys_list = subkey_generator(key)    
    
    reshift = block_shifting(cipher_bits, right=True)
    print(reshift)
    reverseSub = reverse_block_substitution(reshift)
    print(reverseSub)
    reXor = xor_block_with_subkey(reverseSub, subkeys_list[0])
    print(reXor)
