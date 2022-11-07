def subprogramFirst (array_1, array_2, array_res = []):
    temp = array_1 + array_2
    for number in temp:
        if number not in array_res:
            array_res.append(number)
    print(array_res)
def subprogramSecond (array_1, array_2, array_res = []):
    array_b_res = []
    array_a_res = []
    while len(array_2) > 0:
        elements_b = array_2[0]
        array_2.remove(array_2[0])
        if (elements_b in array_2) and (elements_b not in array_b_res):
            array_b_res.append(elements_b)
    for elements_a in array_1:
        if array_1.count(elements_a) == 1:
            array_a_res.append(elements_a)
    for number_b in array_b_res:
        if number_b in array_a_res:
            array_res.append(number_b)
    print(array_res)
array_1 = input('Введите массив А= ')
array_2 = input('Введите массив В= ')
array_1 = list(map(int, array_1.split()))
array_2 = list(map(int, array_2.split()))
#subprogramFirst(array_1, array_2)
subprogramSecond(array_1, array_2)