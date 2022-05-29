import numpy as np

# TO BE KEPT CONSTANT THROUGHOUT THE PROJECT
block_size_unpadded = 5
block_padding = 11
block_size = 16
chrlist = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z', '.', ',', '!', '?',
    ':', ' '
]
binlist = [
    '00000', '00001', '00010', '00011', '00100', 
    '00101', '00110', '00111', '01000', '01001',
    '01010', '01011', '01100', '01101', '01110', 
    '01111', '10000', '10001', '10010', '10011',
    '10100', '10101', '10110', '10111', '11000',
    '11001', '11010', '11011', '11100', '11101', 
    '11110', '11111'
]

# To generate random bits for padding 
def randombits(n):
    if n == 0:
        return ''
    decvalue = np.random.randint(0, 2**n)
    formatstring = '0' + str(n) + 'b'
    return format(decvalue, formatstring)

# To convert a character string into binary string
def encstr(message, block_padding=0):
    cipher = ''
    bintext = ' '.join('{0:016b}'.format(ord(x), 'b') for x in message)
    cipher  = bintext.replace(" ", "")

    return [cipher, len(message)]

# To convert binary cipher text into deiphered text
def decstr(cipher, n, block_padding=0):
    seperated = ''
    for i in range(len(cipher)):
        if i%16 == 0:
            seperated += " "
        seperated += cipher[i]

    # print(seperated)
    bin_list = seperated.split()
    text = ''

    for bin in bin_list:
        an_integer = int(bin, 2)
        ascii_character = chr(an_integer)
        text += ascii_character

    return text

# Convert a string of binary characters into a corresponding numpy array 
def strToArr(bin_string,block_size):
    bin_list = []
    keys = []
    letter_count = 0
    innerList = []
    
    for letter in bin_string:
        innerList.append(int(letter))
        letter_count += 1
        if (letter_count % block_size) == 0:
            bin_list.append(innerList)
            innerList = []
            key_bit = np.random.randint(0, 2, 16)
            keys.append(key_bit)
    
    input_list = np.array(bin_list)
    key_list = np.array(keys)
    return [input_list, key_list]

# To convert a binary numpy array to a string of binary characters
def arrToStr(bin_arr):
    bin_string = ''
    
    for inner in bin_arr:
        for bit in inner:
            bin_string += str(bit)
    return bin_string

# Combines above functions into one to encrypt a text message
def processRawMessage(raw_message):
    encrypt = encstr(raw_message,block_padding)
    bin_cipher = strToArr(encrypt[0], block_size)
    bin_message = bin_cipher[0]
    bin_key = bin_cipher[1]

    return [bin_message,bin_key]

# Combines above functions into one to decrypt a text message
def processBinaryMessage(binary_message):
    message_str = arrToStr(binary_message)
    decipher = decstr(message_str,len(binary_message),block_padding) 
    return decipher

# Combines above functions into one to encrypt a file
def processRawFile(file):
    converted_string = base64.b64encode(file.read())
    return converted_string

# Combines above functions into one to decrypt a file 
def processBinaryFile(img_text):
    image_file = base64.b64decode(img_text)
    return image_file
