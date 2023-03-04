
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