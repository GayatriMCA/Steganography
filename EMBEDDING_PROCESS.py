import cv2
import numpy as np

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

def encode(image_name, secret_data_1, secret_data_2, secret_data_3, secret_data_4):
    # read the image
    image = cv2.imread(image_name)
    height, width, channels = image.shape
    print(image.shape)

    # convert data to binary
    #binary_secret_data_1 = to_bin(secret_data_1)
    #binary_secret_data_2 = to_bin(secret_data_2)
    #binary_secret_data_3 = to_bin(secret_data_3)
    #binary_secret_data_4 = to_bin(secret_data_4)

    print(secret_data_1)
    binary_secret_data_1 = to_bin(secret_data_1)
    data_len = len(binary_secret_data_1)
    print("s-d:", binary_secret_data_1, data_len)

    colors = ['b', 'r', 'g', 'b']
    i = 0
    j = 8
    secret_blocks_1 = []
    while (True):
        if (binary_secret_data_1[i:j] != ''):
            secret_blocks_1.append(binary_secret_data_1[i:j])
        else:
            break
        i = i + 8
        j = j + 8
    print(secret_blocks_1)

    print(secret_data_2)
    binary_secret_data_2 = to_bin(secret_data_2)
    data_len = len(binary_secret_data_2)
    print("s-d:", binary_secret_data_2, data_len)

    i = 0
    j = 8
    secret_blocks_2 = []
    while (True):
        if (binary_secret_data_2[i:j] != ''):
            secret_blocks_2.append(binary_secret_data_2[i:j])
        else:
            break
        i = i + 8
        j = j + 8
    print(secret_blocks_2)

    print(secret_data_3)
    binary_secret_data_3 = to_bin(secret_data_3)
    data_len = len(binary_secret_data_3)
    print("s-d:", binary_secret_data_3, data_len)

    i = 0
    j = 8
    secret_blocks_3 = []
    while (True):
        if (binary_secret_data_3[i:j] != ''):
            secret_blocks_3.append(binary_secret_data_3[i:j])
        else:
            break
        i = i + 8
        j = j + 8
    print(secret_blocks_3)

    print(secret_data_4)
    binary_secret_data_4 = to_bin(secret_data_4)
    data_len = len(binary_secret_data_4)
    print("s-d:", binary_secret_data_4, data_len)

    i = 0
    j = 8
    secret_blocks_4 = []
    while (True):
        if (binary_secret_data_4[i:j] != ''):
            secret_blocks_4.append(binary_secret_data_4[i:j])
        else:
            break
        i = i + 8
        j = j + 8
    print(secret_blocks_4)

    '''FIRST BLOCK OF THE IMAGE'''
    print("[*] Encoding data... IN FIRST BLOCK OF THE IMAGE")
    for row in image[0:height-height//2,0:(width-width//2)-1]:
        i = 0
        j = 4
        for each_block in secret_blocks_1:
            # print("each_block", each_block)
            k = 0
            for pixels in row[i:j]:
                r, g, b = to_bin(pixels)
                #print('p', pixels)
                if (colors[k] == "b" and k == 0):
                    #print('-------blue------------')
                    # bit = b[value_1]
                    zeros = b.count('0')
                    ones = b.count('1')
                    if (zeros > ones):
                        bit = '0'
                    else:
                        bit = '1'
                    #print(bit, b)
                    # bit=b[7]
                    #print("RED PIXEL", r)
                    #print("GREEN PIXEL", g)
                    first = each_block[0:2]
                    #print("first", first)
                    result_1 = int(bit) ^ int(first[0])
                    pixels[0] = int(r[:-2] + str(result_1) + r[-1], 2)
                    result_2 = int(bit) ^ int(first[1])
                    pixels[1] = int(g[:-2] + str(result_2) + g[-1], 2)
                    #print(r[:-2] + str(result_1) + r[-1], "<---red")
                    #print(g[:-2] + str(result_2) + g[-1], "<---green")
                    #print(pixels)

                elif (colors[k] == "r" and k == 1):
                    #print('-----RED---------------')
                    # bit = r[value_2]
                    zeros = r.count('0')
                    ones = r.count('1')
                    if (zeros > ones):
                        bit = '0'
                    else:
                        bit = '1'
                    #print(bit, r)
                    # bit=r[6]
                    #print("GREEN PIXEL", g)
                    #print("BLUE PIXEL", b)
                    second = each_block[2:4]
                    #print("second", second)
                    result_1 = int(bit) ^ int(second[0])
                    pixels[1] = int(g[:-2] + str(result_1) + g[-1], 2)
                    result_2 = int(bit) ^ int(second[1])
                    pixels[2] = int(b[:-2] + str(result_2) + b[-1], 2)
                    #print(g[:-2] + str(result_1) + g[-1], "<---green")
                    #print(b[:-2] + str(result_2) + b[-1], "<---blue")
                    #print(pixels)

                elif (colors[k] == "g" and k == 2):
                    #print('------green---------------')
                    # bit = g[value_3]
                    zeros = g.count('0')
                    ones = g.count('1')
                    if (zeros > ones):
                        bit = '0'
                    else:
                        bit = '1'
                    #print(bit, g)
                    # bit=g[5]
                    #print("BLUE PIXEL", b)
                    #print("RED PIXEL", r)
                    third = each_block[4:6]
                    #print("third", third)
                    result_1 = int(bit) ^ int(third[0])
                    pixels[2] = int(b[:-2] + str(result_1) + b[-1], 2)
                    result_2 = int(bit) ^ int(third[1])
                    pixels[0] = int(r[:-2] + str(result_2) + r[-1], 2)
                    #print(b[:-2] + str(result_1) + b[-1], "<---blue")
                    #print(r[:-2] + str(result_2) + r[-1], "<---red")
                    #print(pixels)

                elif (colors[k] == "b" and k == 3):
                    #print('-------blue------------')
                    # bit = b[value_4]
                    zeros = b.count('0')
                    ones = b.count('1')
                    if (zeros > ones):
                        bit = '0'
                    else:
                        bit = '1'
                   # print(bit, b)
                    # bit=b[4]
                    #print("RED PIXEL", r)
                    #print("GREEN PIXEL", g)
                    fourth = each_block[6:8]
                    #print("fourth", fourth)
                    result_1 = int(bit) ^ int(fourth[0])
                    pixels[0] = int(r[:-2] + str(result_1) + r[-1], 2)
                    result_2 = int(bit) ^ int(fourth[1])
                    pixels[1] = int(g[:-2] + str(result_2) + g[-1], 2)
                    #print(r[:-2] + str(result_1) + r[-1], "<---red")
                    #print(g[:-2] + str(result_2) + g[-1], "<---green")
                    #print(pixels)
                k = k + 1
            i = i + 4
            j = j + 4
            #print()
        break

    '''SECOND BLOCK OF THE IMAGE'''
    print("[*] Encoding data... IN SECOND BLOCK OF THE IMAGE")
    for row in image[0:height-height//2,(width-width//2)-1:width]:
        i = 0
        j = 4
        for each_block in secret_blocks_2:
            # print("each_block", each_block)
            k = 0
            for pixels in row[i:j]:
                r, g, b = to_bin(pixels)
                #print('p', pixels)
                if (colors[k] == "b" and k == 0):
                    #print('-------blue------------')
                    # bit = b[value_1]
                    zeros = b.count('0')
                    ones = b.count('1')
                    if (zeros > ones):
                        bit = '0'
                    else:
                        bit = '1'
                    #print(bit, b)
                    # bit=b[7]
                    #print("RED PIXEL", r)
                    #print("GREEN PIXEL", g)
                    first = each_block[0:2]
                    #print("first", first)
                    result_1 = int(bit) ^ int(first[0])
                    pixels[0] = int(r[:-2] + str(result_1) + r[-1], 2)
                    result_2 = int(bit) ^ int(first[1])
                    pixels[1] = int(g[:-2] + str(result_2) + g[-1], 2)
                    #print(r[:-2] + str(result_1) + r[-1], "<---red")
                    #print(g[:-2] + str(result_2) + g[-1], "<---green")
                    #print(pixels)

                elif (colors[k] == "r" and k == 1):
                    #print('-----RED---------------')
                    # bit = r[value_2]
                    zeros = r.count('0')
                    ones = r.count('1')
                    if (zeros > ones):
                        bit = '0'
                    else:
                        bit = '1'
                    #print(bit, r)
                    # bit=r[6]
                    #print("GREEN PIXEL", g)
                    #print("BLUE PIXEL", b)
                    second = each_block[2:4]
                    #print("second", second)
                    result_1 = int(bit) ^ int(second[0])
                    pixels[1] = int(g[:-2] + str(result_1) + g[-1], 2)
                    result_2 = int(bit) ^ int(second[1])
                    pixels[2] = int(b[:-2] + str(result_2) + b[-1], 2)
                    #print(g[:-2] + str(result_1) + g[-1], "<---green")
                    #print(b[:-2] + str(result_2) + b[-1], "<---blue")
                    #print(pixels)

                elif (colors[k] == "g" and k == 2):
                    #print('------green---------------')
                    # bit = g[value_3]
                    zeros = g.count('0')
                    ones = g.count('1')
                    if (zeros > ones):
                        bit = '0'
                    else:
                        bit = '1'
                    #print(bit, g)
                    # bit=g[5]
                    #print("BLUE PIXEL", b)
                    #print("RED PIXEL", r)
                    third = each_block[4:6]
                    #print("third", third)
                    result_1 = int(bit) ^ int(third[0])
                    pixels[2] = int(b[:-2] + str(result_1) + b[-1], 2)
                    result_2 = int(bit) ^ int(third[1])
                    pixels[0] = int(r[:-2] + str(result_2) + r[-1], 2)
                    #print(b[:-2] + str(result_1) + b[-1], "<---blue")
                    #print(r[:-2] + str(result_2) + r[-1], "<---red")
                    #print(pixels)

                elif (colors[k] == "b" and k == 3):
                    #print('-------blue------------')
                    # bit = b[value_4]
                    zeros = b.count('0')
                    ones = b.count('1')
                    if (zeros > ones):
                        bit = '0'
                    else:
                        bit = '1'
                    #print(bit, b)
                    # bit=b[4]
                    #print("RED PIXEL", r)
                    #print("GREEN PIXEL", g)
                    fourth = each_block[6:8]
                    #print("fourth", fourth)
                    result_1 = int(bit) ^ int(fourth[0])
                    pixels[0] = int(r[:-2] + str(result_1) + r[-1], 2)
                    result_2 = int(bit) ^ int(fourth[1])
                    pixels[1] = int(g[:-2] + str(result_2) + g[-1], 2)
                    #print(r[:-2] + str(result_1) + r[-1], "<---red")
                    #print(g[:-2] + str(result_2) + g[-1], "<---green")
                    #print(pixels)
                k = k + 1
            i = i + 4
            j = j + 4
            #print()
        break

    '''THIRD BLOCK OF THE IMAGE'''
    print("[*] Encoding data... IN THIRD BLOCK OF THE IMAGE")
    for row in image[(height-height//2)-1:height,0:(width-width//2)-1]:
        i = 0
        j = 4
        for each_block in secret_blocks_3:
            # print("each_block", each_block)
            k = 0
            for pixels in row[i:j]:
                r, g, b = to_bin(pixels)
                #print('p', pixels)
                if (colors[k] == "b" and k == 0):
                    #print('-------blue------------')
                    # bit = b[value_1]
                    zeros = b.count('0')
                    ones = b.count('1')
                    if (zeros > ones):
                        bit = '0'
                    else:
                        bit = '1'
                    #print(bit, b)
                    # bit=b[7]
                    #print("RED PIXEL", r)
                    #print("GREEN PIXEL", g)
                    first = each_block[0:2]
                    #print("first", first)
                    result_1 = int(bit) ^ int(first[0])
                    pixels[0] = int(r[:-2] + str(result_1) + r[-1], 2)
                    result_2 = int(bit) ^ int(first[1])
                    pixels[1] = int(g[:-2] + str(result_2) + g[-1], 2)
                    #print(r[:-2] + str(result_1) + r[-1], "<---red")
                    #print(g[:-2] + str(result_2) + g[-1], "<---green")
                    #print(pixels)

                elif (colors[k] == "r" and k == 1):
                    #print('-----RED---------------')
                    # bit = r[value_2]
                    zeros = r.count('0')
                    ones = r.count('1')
                    if (zeros > ones):
                        bit = '0'
                    else:
                        bit = '1'
                    #print(bit, r)
                    # bit=r[6]
                    #print("GREEN PIXEL", g)
                    #print("BLUE PIXEL", b)
                    second = each_block[2:4]
                    #print("second", second)
                    result_1 = int(bit) ^ int(second[0])
                    pixels[1] = int(g[:-2] + str(result_1) + g[-1], 2)
                    result_2 = int(bit) ^ int(second[1])
                    pixels[2] = int(b[:-2] + str(result_2) + b[-1], 2)
                    #print(g[:-2] + str(result_1) + g[-1], "<---green")
                    #print(b[:-2] + str(result_2) + b[-1], "<---blue")
                    #print(pixels)

                elif (colors[k] == "g" and k == 2):
                    #print('------green---------------')
                    # bit = g[value_3]
                    zeros = g.count('0')
                    ones = g.count('1')
                    if (zeros > ones):
                        bit = '0'
                    else:
                        bit = '1'
                    #print(bit, g)
                    # bit=g[5]
                    #print("BLUE PIXEL", b)
                    #print("RED PIXEL", r)
                    third = each_block[4:6]
                    #print("third", third)
                    result_1 = int(bit) ^ int(third[0])
                    pixels[2] = int(b[:-2] + str(result_1) + b[-1], 2)
                    result_2 = int(bit) ^ int(third[1])
                    pixels[0] = int(r[:-2] + str(result_2) + r[-1], 2)
                    #print(b[:-2] + str(result_1) + b[-1], "<---blue")
                    #print(r[:-2] + str(result_2) + r[-1], "<---red")
                    #print(pixels)

                elif (colors[k] == "b" and k == 3):
                    #print('-------blue------------')
                    # bit = b[value_4]
                    zeros = b.count('0')
                    ones = b.count('1')
                    if (zeros > ones):
                        bit = '0'
                    else:
                        bit = '1'
                    #print(bit, b)
                    # bit=b[4]
                    #print("RED PIXEL", r)
                    #print("GREEN PIXEL", g)
                    fourth = each_block[6:8]
                    #print("fourth", fourth)
                    result_1 = int(bit) ^ int(fourth[0])
                    pixels[0] = int(r[:-2] + str(result_1) + r[-1], 2)
                    result_2 = int(bit) ^ int(fourth[1])
                    pixels[1] = int(g[:-2] + str(result_2) + g[-1], 2)
                    #print(r[:-2] + str(result_1) + r[-1], "<---red")
                    #print(g[:-2] + str(result_2) + g[-1], "<---green")
                    #print(pixels)
                k = k + 1
            i = i + 4
            j = j + 4
            #print()
        break

    '''FOURTH BLOCK OF THE IMAGE'''
    print("[*] Encoding data... IN FOURTH BLOCK OF THE IMAGE")
    for row in image[(height-height//2)-1:height,(width-width//2)-1:width]:
        i = 0
        j = 4
        for each_block in secret_blocks_4:
            # print("each_block", each_block)
            k = 0
            for pixels in row[i:j]:
                r, g, b = to_bin(pixels)
                #print('p', pixels)
                if (colors[k] == "b" and k == 0):
                    #print('-------blue------------')
                    # bit = b[value_1]
                    zeros = b.count('0')
                    ones = b.count('1')
                    if (zeros > ones):
                        bit = '0'
                    else:
                        bit = '1'
                    #print(bit, b)
                    # bit=b[7]
                    #print("RED PIXEL", r)
                    #print("GREEN PIXEL", g)
                    first = each_block[0:2]
                    #print("first", first)
                    result_1 = int(bit) ^ int(first[0])
                    pixels[0] = int(r[:-2] + str(result_1) + r[-1], 2)
                    result_2 = int(bit) ^ int(first[1])
                    pixels[1] = int(g[:-2] + str(result_2) + g[-1], 2)
                    #print(r[:-2] + str(result_1) + r[-1], "<---red")
                    #print(g[:-2] + str(result_2) + g[-1], "<---green")
                    #print(pixels)

                elif (colors[k] == "r" and k == 1):
                    #print('-----RED---------------')
                    # bit = r[value_2]
                    zeros = r.count('0')
                    ones = r.count('1')
                    if (zeros > ones):
                        bit = '0'
                    else:
                        bit = '1'
                    #print(bit, r)
                    # bit=r[6]
                    #print("GREEN PIXEL", g)
                    #print("BLUE PIXEL", b)
                    second = each_block[2:4]
                    #print("second", second)
                    result_1 = int(bit) ^ int(second[0])
                    pixels[1] = int(g[:-2] + str(result_1) + g[-1], 2)
                    result_2 = int(bit) ^ int(second[1])
                    pixels[2] = int(b[:-2] + str(result_2) + b[-1], 2)
                    #print(g[:-2] + str(result_1) + g[-1], "<---green")
                    #print(b[:-2] + str(result_2) + b[-1], "<---blue")
                    #print(pixels)

                elif (colors[k] == "g" and k == 2):
                    #print('------green---------------')
                    # bit = g[value_3]
                    zeros = g.count('0')
                    ones = g.count('1')
                    if (zeros > ones):
                        bit = '0'
                    else:
                        bit = '1'
                    #print(bit, g)
                    # bit=g[5]
                    #print("BLUE PIXEL", b)
                    #print("RED PIXEL", r)
                    third = each_block[4:6]
                    #print("third", third)
                    result_1 = int(bit) ^ int(third[0])
                    pixels[2] = int(b[:-2] + str(result_1) + b[-1], 2)
                    result_2 = int(bit) ^ int(third[1])
                    pixels[0] = int(r[:-2] + str(result_2) + r[-1], 2)
                    #print(b[:-2] + str(result_1) + b[-1], "<---blue")
                    #print(r[:-2] + str(result_2) + r[-1], "<---red")
                    #print(pixels)

                elif (colors[k] == "b" and k == 3):
                    #print('-------blue------------')
                    # bit = b[value_4]
                    zeros = b.count('0')
                    ones = b.count('1')
                    if (zeros > ones):
                        bit = '0'
                    else:
                        bit = '1'
                    #print(bit, b)
                    # bit=b[4]
                    #print("RED PIXEL", r)
                    #print("GREEN PIXEL", g)
                    fourth = each_block[6:8]
                    #print("fourth", fourth)
                    result_1 = int(bit) ^ int(fourth[0])
                    pixels[0] = int(r[:-2] + str(result_1) + r[-1], 2)
                    result_2 = int(bit) ^ int(fourth[1])
                    pixels[1] = int(g[:-2] + str(result_2) + g[-1], 2)
                    #print(r[:-2] + str(result_1) + r[-1], "<---red")
                    #print(g[:-2] + str(result_2) + g[-1], "<---green")
                    #print(pixels)
                k = k + 1
            i = i + 4
            j = j + 4
            #print()
        break
    return image

def main_data(Image_name, secret_data):
    print(Image_name, secret_data)
    encoded_image = encode(Image_name, secret_data[0], secret_data[1], secret_data[2], secret_data[3])
    output_image = "Encrypted_image.PNG"
    cv2.imwrite(output_image, encoded_image)

