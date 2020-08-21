def hiding_message(data):
    message = data
    print(message)
    convert = ''
    part_1 = ''
    part_2 = ''
    part_3 = ''
    part_4 = ''
    count = 0
    var = ''
    list = []

    for i in range(count, len(message)):
        if (message[i] == " " or i == len(message) - 1):
            if (i != len(message) - 1):
                list.append(message[count:i])
            elif (i == len(message) - 1):
                list.append(message[count:i + 1])
            count = count + len(message[count:i]) + 1

    count = 0
    for i in range(0, len(list)):
        count = count + 1
        if (count == 1):
            part_1 += list[i]
            if (i == len(list)-1):
                part_1 += "#"
            else:
                part_1 += "$"
        if (count == 2):
            part_2 += list[i]
            if (i == len(list)-1):
                part_2 += "#"
            else:
                part_2 += "$"
        if (count == 3):
            part_3 += list[i]
            if (i == len(list)-1):
                part_3 += "#"
            else:
                part_3 += "$"
        if (count == 4):
            part_4 += list[i]
            if (i == len(list)-1):
                print(i)
                part_4 += "#"
            else:
                part_4 += "$"
            count = 0

    part_1 = part_1 + "="
    part_2 = part_2 + "="
    part_3 = part_3 + "="
    part_4 = part_4 + "="

    data = []
    data.append(part_1)
    data.append(part_2)
    data.append(part_3)
    data.append(part_4)
    print(part_1)
    print(part_2)
    print(part_3)
    print(part_4)

    return data
#hiding_message('g a y a t r i')