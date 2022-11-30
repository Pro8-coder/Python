from functions import input_int

'''Базовые задания'''


# 3) Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(*args):
    return sum(sorted(args)[1:])


print(my_func(input_int(), input_int(), input_int()))
