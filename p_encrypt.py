from utils import *


if __name__ == '__main__':
    import os
    # Clearing the Screen
    os.system('cls')

    # 1. Get the plaintext as a bits
    f = open("p.txt", "r", encoding="utf-8")
    plain = f.read()
    f.close()
    # pad with "." if length is not a multiple of 16
    if (len(plain) % 16 != 0):
        plain += "." * (16 - len(plain) % 16)

    plain_bits = string_2_bit_string(plain)
    
    # 2. Get 16 subkeys from external key
    key = "ABCDEFGHIJKLMNOP"
    subkeys_list = subkey_generator(key)

    # 3. For all block from plaintext, do XOR with subkey
    # Make blocks of block that contains 128 bits
    blocks = []
    for i in range(0, len(plain_bits), 128):
        blocks.append(plain_bits[i:i+128])
    
    print(blocks)
    
    # Do XOR with subkey
    result = []
    for block in blocks:
        result.append(xor_block_with_subkey(block, subkeys_list[0]))
        
    print("after xor\n",result)
    blok1 = block_substitution_by_sBox(result[0])
    print("after s-box\n",blok1)
    after_shift = block_shifting(blok1)
    print("after shifting\n", after_shift)
    resulttt = bit_string_2_string(after_shift)
    print("to string again\n", resulttt)
    f = open("c.txt", "w", encoding="utf-8")
    f.write(resulttt)
    f.close()