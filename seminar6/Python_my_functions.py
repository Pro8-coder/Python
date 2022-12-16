from random import randint
from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff

    return wrapper


@decor
def rand_lst_int(n):
    '''Создание и заполнение рандомайзером списка целых чисел'''
    lst = []
    while len(lst) < n:
        lst.append(randint(0, 10))
    return "old_int"


@decor
def new_rand_lst_int(n):
    '''Создание и заполнение рандомайзером списка целых чисел'''
    lst = []
    while len(lst) < n:
        lst.append(randint(0, 10))
    yield "new_int"


@decor
def rand_lst_float(n):
    '''Создание и заполнение рандомайзером списка чисел с плавающей точкой'''
    lst = []
    while len(lst) < n:
        lst.append(randint(100, 1000) / 100)
    return "old_float"


@decor
def new_rand_lst_float(n):
    '''Создание и заполнение рандомайзером списка чисел с плавающей точкой'''
    lst = []
    while len(lst) < n:
        lst.append(randint(100, 1000) / 100)
    yield "new_float"
