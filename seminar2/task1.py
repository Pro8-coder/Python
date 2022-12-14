'''Базовые задания'''
# 1) Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию
# type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
#  а указать явно, в программе.

lst = []


def list_append(lt=[],
                l=['str', 1, 3.14, [1, 2, 3], {1: 'кол'}, (1,), {1, 2, 3}]):
    enter = input('Для ручного ввода введите "да": ')
    if enter == 'да':
        l.clear()
        l.append(input('Введите строку: '))
        l.append(int(input('Введите целое число: ')))
        l.append(float(input('Введите число с точкой: ')))
        l.append(input('Введите список(через пробел): ').split())
        l.append(dict.fromkeys(*[[x] if i % 2 == 0 else x for i, x in enumerate
        (input('Введите словарь(1 ключ/1 значение через пробел): ').split())]))
        l.append(tuple(input('Введите кортеж(через пробел): ').split()))
        l.append({*input('Введите множества(через пробел): ').split()})
    [lt.append(y) for j, y in enumerate(l)]
    return [(type(x), x) for i, x in enumerate(lt)]


print(*list_append(lst))
