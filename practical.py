def subprogramFirst (array_1, array_2, array_res = []):
    temp = array_1 + array_2
    for number in temp:
        if number not in array_res:
            array_res.append(number)
    print(array_res)