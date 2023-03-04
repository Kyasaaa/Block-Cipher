from utils import *


if __name__ == '__main__':
    import os
    # Clearing the Screen
    os.system('cls')

    # 1. Read plaintext from text file
    f = open("text file//p.txt", "r", encoding="utf-8")
    plain = f.read()
    f.close()
    
    # 1.5. pad with "." if length is not a multiple of 16, because 128 bits contains of 16 letters
    num_padding = (16 - len(plain) % 16)
    if (num_padding > 0):
        plain += "." * num_padding

    # 2. Get the plaintext as a bits
    plain_bits = string_2_bit_string(plain)
    
    # 3. Get 16 subkeys from external key
    subkeys_list = subkey_generator(KEY)

    # 4. Make blocks of block that contains 128 bits
    blocks = []
    for i in range(0, len(plain_bits), 128):
        blocks.append(plain_bits[i:i+128])
    
    # 5. For each block from plaintext do Encoding by block cipher algorithm
    ciphertext = ""
    for block in blocks:
        result_block = block
        ### It be done for 16 iterations (16 subkeys)
        for i in range(16):
            # a) Do XOR with subkey
            xor_str = xor_block_with_subkey(result_block, subkeys_list[i])
            # b) Do Substitution by S_BOX
            subs_str = block_substitution_by_sBox(xor_str)
            # c) Do Block Shifting (permutation alt)
            shifted_str = block_shifting(subs_str, right=False)
            result_block = shifted_str
        ciphertext += bit_string_2_string(result_block)
        
    # 6. Remove padding from the ciphertext result
    ciphertext = ciphertext[:len(ciphertext)-num_padding]
    
    # 7. Write ciphertext to text file
    f = open("text file//c.txt", "w", encoding="utf-8")
    f.write(ciphertext)
    f.close()