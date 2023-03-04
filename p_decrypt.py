from utils import *


if __name__ == '__main__':
    import os
    # Clearing the Screen
    os.system('cls')

    # 1. Read ciphertext from text file
    f = open("text file//c.txt", "r", encoding="utf-8")
    cipher = f.read()
    f.close()
    
    # 1.5. pad with "." if length is not a multiple of 16
    # ?????????????????????????
    num_padding = (16 - len(cipher) % 16)
    if (num_padding > 0):
        cipher += " " * num_padding

    # 2. Get the ciphertext as a bits
    cipher_bits = string_2_bit_string(cipher)
    
    # 3. Get 16 subkeys from external key
    
    subkeys_list = subkey_generator(KEY)
    
    # 4. Make blocks of block that contains 128 bits
    blocks = []
    for i in range(0, len(cipher_bits), 128):
        blocks.append(cipher_bits[i:i+128])
    
    # 5. For each block from ciphertext do Reverse-Encoding by block cipher algorithm
    plaintext = ""
    for block in blocks:
        result_block = block
        ### It be done for 16 iterations (16 subkeys)
        for i in range(16):
            reverse_shift = block_shifting(result_block, right=True)
            reverse_subs = reverse_block_substitution(reverse_shift)
            reXor_str = xor_block_with_subkey(reverse_subs, subkeys_list[15-i])
            result_block = reXor_str
        plaintext += bit_string_2_string(result_block)
    
    # 6. Remove padding from the plaintext result
    if plaintext[len(plaintext)-num_padding-1] == " ":
        num_padding += 1
    plaintext = plaintext[:len(plaintext)-num_padding]
    
    # 7. Write plaintext to text file
    f = open("text file//p_back.txt", "w", encoding="utf-8")
    f.write(plaintext)
    f.close()
