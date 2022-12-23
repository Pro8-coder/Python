from my_functions import input_int

'''Доп. задания'''


# 11) Задайте число. Составьте список чисел Фибоначчи, в том числе для
# отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fib(l, count=1, lst=[1, 0, 1]):
    if l - 1 > 0:
        lst.append(lst[count] + lst[count + 1])
        fib(l - 1, count=count + 1)
        count = 0
        lst.insert(0, lst[count + 1] - lst[count])
    return lst


k = input_int()
print(fib(k))
