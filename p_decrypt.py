from utils import *


if __name__ == '__main__':
    import os
    # Clearing the Screen
    # os.system('cls')

    # 1. Get the ciphertext as a bits
    f = open("c.txt", "r")
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

    # # 3. For all block from ciphertext, do XOR with subkey
    # # Make blocks of block that contains 128 bits
    # blocks = []
    # for i in range(0, len(cipher_bits), 128):
    #     blocks.append(cipher_bits[i:i+128])
    
    # # Do XOR with subkey
    # result = []
    # for block in blocks:
    #     result.append(xor_block_with_subkey(block, subkeys_list[0]))
    
        
    # print("after xor\n",result)
    # blok1 = block_substitution_by_sBox(result[0])
    # print("after s-box\n",blok1)
    # after_shift = block_shifting(blok1)
    # print("after shifting\n", after_shift)
    # resulttt = bit_string_2_string(after_shift)
    # print("to string again\n", resulttt)