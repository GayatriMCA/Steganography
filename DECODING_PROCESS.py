import numpy as np
import cv2

def to_bin(data):
    """Convert `data` to binary format as string"""
    if isinstance(data, str):
        return ''.join([ format(ord(i), "08b") for i in data ])
    elif isinstance(data, bytes) or isinstance(data, np.ndarray):
        return [ format(i, "08b") for i in data ]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported.")

colors=["b","r","g","b"]
def decode_1(image_name):
    'FIRST BLOCK OF THE IMAGE'''
    print("[+] Decoding...FIRST BLOCK OF THE IMAGE")
    # read the image
    image = cv2.imread(image_name)
    height = image.shape[0]
    width = image.shape[1]
    binary_data = ""
    for row in image[0:height-height//2,0:(width-width//2)-1]:
        secret_data = ''
        for pixel in row:
            i = 0
            j = 4
            k = 0
            binary_data = ""
            while (True):
                k = 0
                for pixels in row[i:j]:
                    r, g, b = to_bin(pixels)
                    if (colors[k] == "b" and k == 0):
                        # bit=b[value_1]
                        zeros = b.count('0')
                        ones = b.count('1')
                        if (zeros > ones):
                            bit = '0'
                        else:
                            bit = '1'
                        data_1 = r[-2]
                        data_2 = g[-2]
                        operation_1 = int(bit) ^ int(data_1)
                        operation_2 = int(bit) ^ int(data_2)
                        binary_data += str(operation_1)
                        binary_data += str(operation_2)
                    elif (colors[k] == "r" and k == 1):
                        # bit=r[value_2]
                        zeros = r.count('0')
                        ones = r.count('1')
                        if (zeros > ones):
                            bit = '0'
                        else:
                            bit = '1'
                        data_1 = g[-2]
                        data_2 = b[-2]
                        operation_1 = int(bit) ^ int(data_1)
                        operation_2 = int(bit) ^ int(data_2)
                        binary_data += str(operation_1)
                        binary_data += str(operation_2)
                    elif (colors[k] == "g" and k == 2):
                        # bit = g[value_3]
                        zeros = g.count('0')
                        ones = g.count('1')
                        if (zeros > ones):
                            bit = '0'
                        else:
                            bit = '1'
                        data_1 = b[-2]
                        data_2 = r[-2]
                        operation_1 = int(bit) ^ int(data_1)
                        operation_2 = int(bit) ^ int(data_2)
                        binary_data += str(operation_1)
                        binary_data += str(operation_2)
                    elif (colors[k] == "b" and k == 3):
                        # bit = b[value_4]
                        zeros = b.count('0')
                        ones = b.count('1')
                        if (zeros > ones):
                            bit = '0'
                        else:
                            bit = '1'
                        data_1 = r[-2]
                        data_2 = g[-2]
                        operation_1 = int(bit) ^ int(data_1)
                        operation_2 = int(bit) ^ int(data_2)
                        binary_data += str(operation_1)
                        binary_data += str(operation_2)
                    k = k + 1
                i = i + 4
                j = j + 4
                if (chr(int(binary_data, 2)) == "="):
                    break

                secret_data += chr(int(binary_data, 2))
                #print(secret_data)
                binary_data = ""
            break
        #print(secret_data)
        return secret_data

def decode_2(image_name):
    '''SECOND BLOCK OF THE IMAGE'''
    print("[+] Decoding...SECOND BLOCK OF THE IMAGE")
    # read the image
    image = cv2.imread(image_name)
    height = image.shape[0]
    width = image.shape[1]
    binary_data =""
    for row in image[0:height-height//2,(width-width//2)-1:width]:
        secret_data = ''
        for pixel in row:
            i = 0
            j = 4
            k = 0
            binary_data = ""
            while (True):
                k = 0
                for pixels in row[i:j]:
                    r, g, b = to_bin(pixels)
                    if (colors[k] == "b" and k == 0):
                        # bit=b[value_1]
                        zeros = b.count('0')
                        ones = b.count('1')
                        if (zeros > ones):
                            bit = '0'
                        else:
                            bit = '1'
                        data_1 = r[-2]
                        data_2 = g[-2]
                        operation_1 = int(bit) ^ int(data_1)
                        operation_2 = int(bit) ^ int(data_2)
                        binary_data += str(operation_1)
                        binary_data += str(operation_2)
                    elif (colors[k] == "r" and k == 1):
                        # bit=r[value_2]
                        zeros = r.count('0')
                        ones = r.count('1')
                        if (zeros > ones):
                            bit = '0'
                        else:
                            bit = '1'
                        data_1 = g[-2]
                        data_2 = b[-2]
                        operation_1 = int(bit) ^ int(data_1)
                        operation_2 = int(bit) ^ int(data_2)
                        binary_data += str(operation_1)
                        binary_data += str(operation_2)
                    elif (colors[k] == "g" and k == 2):
                        # bit = g[value_3]
                        zeros = g.count('0')
                        ones = g.count('1')
                        if (zeros > ones):
                            bit = '0'
                        else:
                            bit = '1'
                        data_1 = b[-2]
                        data_2 = r[-2]
                        operation_1 = int(bit) ^ int(data_1)
                        operation_2 = int(bit) ^ int(data_2)
                        binary_data += str(operation_1)
                        binary_data += str(operation_2)
                    elif (colors[k] == "b" and k == 3):
                        # bit = b[value_4]
                        zeros = b.count('0')
                        ones = b.count('1')
                        if (zeros > ones):
                            bit = '0'
                        else:
                            bit = '1'
                        data_1 = r[-2]
                        data_2 = g[-2]
                        operation_1 = int(bit) ^ int(data_1)
                        operation_2 = int(bit) ^ int(data_2)
                        binary_data += str(operation_1)
                        binary_data += str(operation_2)
                        #print(binary_data)
                    k = k + 1
                i = i + 4
                j = j + 4
                #print(chr(int(binary_data)))
                if (chr(int(binary_data, 2)) == "="):
                    break

                secret_data += chr(int(binary_data, 2))
                binary_data = ""
            break
        #print(secret_data)
        return secret_data

def decode_3(image_name):
    '''THIRD BLOCK OF THE IMAGE'''
    print("[+] Decoding...THIRD BLOCK OF THE IMAGE")
    # read the image
    image = cv2.imread(image_name)
    height = image.shape[0]
    width = image.shape[1]
    binary_data = ""
    for row in image[(height-height//2)-1:height,0:(width-width//2)-1]:
        secret_data = ''
        for pixel in row:
            i = 0
            j = 4
            k = 0
            binary_data = ""
            while (True):
                k = 0
                for pixels in row[i:j]:
                    r, g, b = to_bin(pixels)
                    if (colors[k] == "b" and k == 0):
                        # bit=b[value_1]
                        zeros = b.count('0')
                        ones = b.count('1')
                        if (zeros > ones):
                            bit = '0'
                        else:
                            bit = '1'
                        data_1 = r[-2]
                        data_2 = g[-2]
                        operation_1 = int(bit) ^ int(data_1)
                        operation_2 = int(bit) ^ int(data_2)
                        binary_data += str(operation_1)
                        binary_data += str(operation_2)
                    elif (colors[k] == "r" and k == 1):
                        # bit=r[value_2]
                        zeros = r.count('0')
                        ones = r.count('1')
                        if (zeros > ones):
                            bit = '0'
                        else:
                            bit = '1'
                        data_1 = g[-2]
                        data_2 = b[-2]
                        operation_1 = int(bit) ^ int(data_1)
                        operation_2 = int(bit) ^ int(data_2)
                        binary_data += str(operation_1)
                        binary_data += str(operation_2)
                    elif (colors[k] == "g" and k == 2):
                        # bit = g[value_3]
                        zeros = g.count('0')
                        ones = g.count('1')
                        if (zeros > ones):
                            bit = '0'
                        else:
                            bit = '1'
                        data_1 = b[-2]
                        data_2 = r[-2]
                        operation_1 = int(bit) ^ int(data_1)
                        operation_2 = int(bit) ^ int(data_2)
                        binary_data += str(operation_1)
                        binary_data += str(operation_2)
                    elif (colors[k] == "b" and k == 3):
                        # bit = b[value_4]
                        zeros = b.count('0')
                        ones = b.count('1')
                        if (zeros > ones):
                            bit = '0'
                        else:
                            bit = '1'
                        data_1 = r[-2]
                        data_2 = g[-2]
                        operation_1 = int(bit) ^ int(data_1)
                        operation_2 = int(bit) ^ int(data_2)
                        binary_data += str(operation_1)
                        binary_data += str(operation_2)
                    k = k + 1
                i = i + 4
                j = j + 4
                if (chr(int(binary_data, 2)) == "="):
                    break

                secret_data += chr(int(binary_data, 2))
                binary_data = ""
            break
        #print(secret_data)
        return secret_data

def decode_4(image_name):
    '''FOURTH BLOCK OF THE IMAGE'''
    print("[+] Decoding...FOURTH BLOCK OF THE IMAGE")
    # read the image
    image = cv2.imread(image_name)
    height = image.shape[0]
    width = image.shape[1]
    binary_data = ""
    for row in image[(height-height//2)-1:height,(width-width//2)-1:width]:
        secret_data = ''
        for pixel in row:
            i = 0
            j = 4
            k = 0
            binary_data = ""
            while (True):
                k = 0
                for pixels in row[i:j]:
                    r, g, b = to_bin(pixels)
                    if (colors[k] == "b" and k == 0):
                        # bit=b[value_1]
                        zeros = b.count('0')
                        ones = b.count('1')
                        if (zeros > ones):
                            bit = '0'
                        else:
                            bit = '1'
                        data_1 = r[-2]
                        data_2 = g[-2]
                        operation_1 = int(bit) ^ int(data_1)
                        operation_2 = int(bit) ^ int(data_2)
                        binary_data += str(operation_1)
                        binary_data += str(operation_2)
                    elif (colors[k] == "r" and k == 1):
                        # bit=r[value_2]
                        zeros = r.count('0')
                        ones = r.count('1')
                        if (zeros > ones):
                            bit = '0'
                        else:
                            bit = '1'
                        data_1 = g[-2]
                        data_2 = b[-2]
                        operation_1 = int(bit) ^ int(data_1)
                        operation_2 = int(bit) ^ int(data_2)
                        binary_data += str(operation_1)
                        binary_data += str(operation_2)
                    elif (colors[k] == "g" and k == 2):
                        # bit = g[value_3]
                        zeros = g.count('0')
                        ones = g.count('1')
                        if (zeros > ones):
                            bit = '0'
                        else:
                            bit = '1'
                        data_1 = b[-2]
                        data_2 = r[-2]
                        operation_1 = int(bit) ^ int(data_1)
                        operation_2 = int(bit) ^ int(data_2)
                        binary_data += str(operation_1)
                        binary_data += str(operation_2)
                    elif (colors[k] == "b" and k == 3):
                        # bit = b[value_4]
                        zeros = b.count('0')
                        ones = b.count('1')
                        if (zeros > ones):
                            bit = '0'
                        else:
                            bit = '1'
                        data_1 = r[-2]
                        data_2 = g[-2]
                        operation_1 = int(bit) ^ int(data_1)
                        operation_2 = int(bit) ^ int(data_2)
                        binary_data += str(operation_1)
                        binary_data += str(operation_2)
                    k = k + 1
                i = i + 4
                j = j + 4
                if (chr(int(binary_data, 2)) == "="):
                    break

                secret_data += chr(int(binary_data, 2))
                binary_data = ""
            break
        return secret_data

output_image = "Encrypted_image.PNG"
# decode the secret data from the image
decoded_data_1 = decode_1(output_image)
decoded_data_2 = decode_2(output_image)
decoded_data_3 = decode_3(output_image)
decoded_data_4 = decode_4(output_image)
print()
print("[+] Decoded data:1", decoded_data_1)
print("[+] Decoded data:2", decoded_data_2)
print("[+] Decoded data:3", decoded_data_3)
print("[+] Decoded data:4", decoded_data_4)
