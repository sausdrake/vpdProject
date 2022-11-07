def subprogramFirst(array_1, array_2, array_res=[]):
    for elements_a in array_1:
        if (array_1.count(elements_a) > 1) and (elements_a not in array_2):
            array_res.append(elements_a)
    for elements_b in array_2:
        if (array_2.count(elements_b) > 1) and (elements_b not in array_1):
            array_res.append(elements_b)
    print(list(set(array_res)))
    stopProgram()


def subprogramSecond(array_1, array_2, array_res=[]):
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
    stopProgram()


def subprogramThird(array_1, array_2, array_res=[]):
    # array_1 = [set(array_1)
    for elements_a in array_1:
        if elements_a not in array_2:
            array_res.append(elements_a)
    print(list(set(array_res)))
    stopProgram()


def menu(array_1, array_2):
    print("______________________Выберите операцию_____________________________\n"
          "____________________________________________________________________\n"
          "(1) Вывод элементов которые присутствуют в нескольких экземплярах\n"
          "      либо только в массиве A, либо только в массиве В\n"
          "____________________________________________________________________\n"
          "(2) Вывод повторяющиеся элементов массива В, которые есть в массиве А\n"
          "                  только в одном экземпляре\n"
          "_____________________________________________________________________\n"
          "(3) Вывод элементов, которые присутствуют в массиве А,\n"
          "                 но отсутствуют в массиве В\n"
          "_____________________________________________________________________\n")
    number_menu = input('number menu= ')
    if number_menu == '1':
        subprogramFirst(array_1, array_2)
    elif number_menu == '2':
        subprogramSecond(array_1, array_2)
    elif number_menu == '3':
        subprogramThird(array_1, array_2)
    else:
        print('Введите число от 1 до 3\n')
        menu(array_1, array_2)


def stopProgram():
    answer = input('Хотите остановить программу? y/n\n')
    if answer == 'y':
        exit()
    elif answer == 'n':
        variable()
    else:
        print('Упс... попробуйте еше раз\n')
        stopProgram()


def variable():
    array_1 = input('Введите массив А= ')
    array_2 = input('Введите массив В= ')
    array_1 = list(map(str, array_1.split()))
    array_2 = list(map(str, array_2.split()))
    menu(array_1, array_2)


variable()
