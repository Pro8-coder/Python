from random import randint
from time import time


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


def rand_lst_int():
    lst = []
    while len(lst) < 7:
        lst.append(randint(0, 10))
    return lst


def rand_lst_float():
    lst = []
    while len(lst) < 7:
        lst.append(randint(100, 1000) / 100)
    return lst


def test_time(func):
    def wrapper(*args, **kwargs):
        start_t = time()
        func(*args, **kwargs)
        end_t = time()
        return start_t - end_t

    return wrapper
