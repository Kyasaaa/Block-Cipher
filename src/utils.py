from constant import *

def string_2_bit_string(str, n_bits=8):
    return ''.join(format(ord(c), 'b').zfill(n_bits) for c in str)

def bit_string_2_string(bit_str, n_bits=8):
    return ''.join(chr(int(bit_str[i:i+n_bits], 2)) for i in range(0, len(bit_str), n_bits))

def subkey_generator(external_key):
    # pad with "." if length is not a multiple of 16
    if (len(external_key) % 16 != 0):
        num_padding = (16 - len(external_key) % 16)
        external_key += ("." * num_padding)
        
    subkey_len = len(external_key) // 16
    subkeys = []
    x = 0
    for i in range(0, len(external_key)//subkey_len):
        sum_temp = 0
        for j in range(0, subkey_len):
            sum_temp = (sum_temp + ord(external_key[i*subkey_len+j])) % 256
        x = (x + sum_temp) % 256
        subkey = ''.join(format(x, 'b').zfill(8))
        subkeys.append(subkey)
    return subkeys

def block_feistel(block):
    leng = len(block)//2
    result = block[leng:] + block[:leng]
    return result

def xor_block_with_subkey(block, subkey):
    subkey *= 16
    result = ""
    for i in range(len(block)):
        result += str(int(block[i]) ^ int(subkey[i]))
    return result

def substract_each_4bits_of_block_by_half(block, addition=False):
    x = 8
    result = ""
    for i in range(0, len(block)//4):
        four_bit = block[i*4:i*4+4]
        four_bit_int = int(four_bit, 2)
        if addition:
            x *= -1
        four_bit_int = (four_bit_int - x) % 16
        four_bit = ''.join(format(four_bit_int, 'b').zfill(4))
        result += four_bit
    return result

def block_substitution_by_sBox(block):
    result = ""
    for i in range(0, len(block)//8):
        eight_bit = block[i*8:i*8+8]
        the_row = eight_bit[:4]
        the_col = eight_bit[4:]
        row_idx = int(the_row, 2)
        col_idx = int(the_col, 2)
        res_int = S_BOX[row_idx*BOX_DIM[1] + col_idx]
        res_bit = ''.join(format(res_int, 'b').zfill(8))
        result += res_bit
    return result

def reverse_block_substitution(block):
    result = ""
    for i in range(0, len(block)//8):
        eight_bit = block[i*8:i*8+8]
        el = int(eight_bit, 2)
        el_idx = S_BOX.index(el)
        row_idx = el_idx // BOX_DIM[1]
        col_idx = el_idx % BOX_DIM[1]
        the_row = format(row_idx, 'b').zfill(4)
        the_col = format(col_idx, 'b').zfill(4)
        res_bit = the_row + the_col
        result += res_bit
    return result

def shift_arr_by_x(arr, x=0):
    result_arr = arr
    if x > 0:
        arr_before = arr[:x]
        arr_after = arr[x:]
        result_arr = arr_after + arr_before
    elif x < 0:
        arr_before = arr[:len(arr)+x]
        arr_after = arr[len(arr)+x:]
        result_arr = arr_after + arr_before
    return result_arr

def arr_2_matrix_of_string(arr, n_cols=16):
    matrix = []
    matrix_temp = []
    for i in range(0, len(arr)):
        matrix_temp.append(arr[i])
        if ((i+1)%n_cols == 0):
            matrix.append(matrix_temp)
            matrix_temp = []
    return matrix

def block_shifting(block, right=False):
    shifted_block = ""
    temp = ""
    for i in range(0, len(block)):
        temp += block[i]
        if (((i+1)%16) == 0):
            dist = (i+1)//16-1
            if (right):
                dist *= -1
            temp = shift_arr_by_x(temp, dist)
            shifted_block += temp
            temp = ""
    return shifted_block