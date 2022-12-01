from random import randint


def input_int(text='Введите число: '):
    '''Ввод целого числа и проверка верности ввода'''
    while True:
        try:
            num = int(input(f'{text}'))
        except ValueError:
            print('Введено не верное значение попробуйте снова.')
            continue
        break
    return num


def rand_lst():
    lst = []
    while len(lst) < 7:
        lst.append(randint(0, 10))
    return lst