def subprogramFirst (array_1, array_2, array_res = []):
    temp = array_1 + array_2
    for number in temp:
        if number not in array_res:
            array_res.append(number)
    print(array_res)
def subprogramSecond (array_1, array_2, array_res = []):
    array_b_res = []
    while len(array_2) > 0:
        print('array B_1= ', array_2)
        elements_b = array_2[0]
        array_2.remove(array_2[0])
        if (elements_b in array_2) and (elements_b not in array_b_res):
            array_b_res.append(elements_b)
            print('array B= ', array_b_res)