import os
from constant import ENCODING
from decrypt import decrypt
from encrypt import encrypt

### FUNCTIONS ###
def cls():
    os.system("cls")
    
def read_file(filename):
    dir_path = "Text_files//Test//" + filename + ".txt"
    f = open(dir_path, "r", encoding=ENCODING)
    text = f.read()
    f.close()
    return text

def write_file(text, filename):
    dir_path = "Text_files//After_Crypt//" + filename + ".txt"
    f = open(dir_path, "w", encoding=ENCODING)
    text = f.write(text)
    f.close()
    return text
# def another_func:
#     put code here

###

### VARIABLES ###
cript_op = 0
input_op = 0
text = ""    
key  = ""
result = ""
text_filename = ""
key_filename  = ""
###

### ALGORITHM ###
cls()
# 1. Choose the cryptographic mode
print("-------------------------------------------------------------")
print("~~~  Welcome to SwazzyCipher..!!!  ~~~")
print("What will you like to do?")
print("1. Encrypt your plaintext.")
print("2. Decrypt your ciphertext.")
print()
cript_op = int(input("Kript Mode: "))
print()
print("-------------------------------------------------------------")
match cript_op:
    case 1:
        print("~~~ You Choose Encryption Mode  ~~~")
    case 2:
        print("~~~ You Choose Decryption Mode ~~~")
    case default:
        print("Please type correct number")
        cript_op = int(input("Choose Kript: "))
        
# 2. Choose the input mode
print("How will you like to input your text and key?")
print("1. Input by user typing.")
print("2. Input by filename.")
print()
input_op = int(input("Choose Input: "))
print()
match input_op:
    case 1:
        print("~~~ Input by user typing  ~~~")
        text = input("Enter your text: ")
        key  = input("Enter your key: ")
    case 2:
        print("~~~ Input by filename (in 'Text_Files/Test' folder)  ~~~")
        text_filename = input("Enter your text filename: ")
        key_filename  = input("Enter your  key filename: ")
        text = read_file(text_filename)
        key = read_file(key_filename)
    case default:
        print("Please type correct number")
        input_op = int(input("Input Mode: "))

# 3. Start Criptography
print()
match cript_op:
    case 1:
        print("-------------------------------------------------------------")
        print("~~~ Start Encryption  ~~~")
        result = encrypt(text, key)
        print("Your plaintext is: ", f"'{text}'")
        print("Your       key is: ", f"'{key}'")
        print("Your encrypted is: ", f"'{result}'")
    case 2:
        print("-------------------------------------------------------------")
        print("~~~ Start Decryption ~~~")
        result = decrypt(text, key)
        print("Your ciphertext is: ", f"'{text}'")
        print("Your        key is: ", f"'{key}'")
        print("Your  decrypted is: ", f"'{result}'")
print()

# 4. Save all the text
match cript_op:
    case 1:
        write_file(text, "01_origin plaintext")
        write_file(result, "01_result ciphertext")
    case 2:
        write_file(text, "02_origin ciphertext")
        write_file(result, "02_result plaintext")
write_file(key, "03_external key")