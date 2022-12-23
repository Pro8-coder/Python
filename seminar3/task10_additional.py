from my_functions import input_int

'''Доп. задания'''


# 10) Напишите программу, которая будет преобразовывать десятичное число в
# двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def decimal_to_binary(num, r=[]):
    if num != 0:
        j = num % 2
        decimal_to_binary(num // 2)
        r.append(j)
    return r


print(decimal_to_binary(input_int()))
