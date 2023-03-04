from s_box import *

def get_sBox():
    return S_BOX

def string_2_bit_string(str, n_bits=8):
    return ''.join(format(ord(c), 'b').zfill(n_bits) for c in str)

def bit_string_2_string(bit_str, n_bits=8):
    return ''.join(chr(int(bit_str[i:i+n_bits], 2)) for i in range(0, len(bit_str), n_bits))

def subkey_generator(key):
    # pad with "." if length is not a multiple of 16
    if (len(key) % 16 != 0):
        key = key + "." * (16 - len(key) % 16)
        
    subkey_len = len(key) // 16
    subkeys = []
    x = 0
    for i in range(0, len(key)//subkey_len):
        sum = 0
        for j in range(0, subkey_len):
            sum = (sum + ord(key[i*subkey_len+j])) % 256
        x = (x + sum) % 256
        subkey = ''.join(format(x, 'b').zfill(8))
        subkeys.append(subkey)
    return subkeys

def xor_block_with_subkey(block, subkey):
    subkey *= 16
    result = ""
    for i in range(len(block)):
        result += str(int(block[i]) ^ int(subkey[i]))
    return result

def block_substitution_by_sBox(block):
    result = ""
    for i in range(0, len(block)//8):
        eight_bit = block[i*8:i*8+8]
        the_row = eight_bit[:4]
        the_col = eight_bit[4:]
        row_idx = int(the_row, 2)
        col_idx = int(the_col, 2)
        res_int = S_BOX[row_idx*BOX_DIM[0] + col_idx]
        res_bit = ''.join(format(res_int, 'b').zfill(8))
        result += res_bit
    return result

def shift_arr_by_x(arr, x=0):
    result_arr = arr
    if x > 0:
        arr_before = arr[:x]
        arr_after = arr[x:]
        result_arr = arr_after + arr_before
    return result_arr

def arr_2_matrix_of_string(arr, n_cols=16):
    matrix = []
    temp = []
    for i in range(0, len(arr)):
        temp.append(arr[i])
        if ((i+1)%n_cols == 0):
            matrix.append(temp)
            temp = []
    return matrix

def block_shifting(block):
    shifted_block = ""
    temp = ""
    for i in range(0, len(block)):
        temp += block[i]
        if (((i+1)%16) == 0):
            temp = shift_arr_by_x(temp, (i+1)//16-1)
            shifted_block += temp
            temp = ""
    return shifted_block