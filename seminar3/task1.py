from functions import input_int

'''Базовые задания'''


# 1) Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

# def input_int(text='Введите число: '):
#     while True:
#         try:
#             num = int(input(f'{text}'))
#         except ValueError:
#             print('Введено не верное значение попробуйте снова.')
#             continue
#         break
#     return num


def division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return 'На ноль нельзя делить'


print(round(division(input_int(text='Введите делимое: '),
                     input_int(text='Введите делитель: ')), 2))
