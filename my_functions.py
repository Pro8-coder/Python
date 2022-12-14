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
    '''Создание и заполнение рандомайзером списка целых чисел'''
    lst = []
    while len(lst) < 7:
        lst.append(randint(0, 10))
    return lst


def rand_lst_float():
    '''Создание и заполнение рандомайзером списка чисел с плавающей точкой'''
    lst = []
    while len(lst) < 7:
        lst.append(randint(100, 1000) / 100)
    return lst


def decorator_time(func):
    '''Декоратор для замера времени работы функции'''

    def wrapper(*args, **kwargs):
        start_t = time()
        func(*args, **kwargs)
        end_t = time()
        return end_t - start_t

    return wrapper
