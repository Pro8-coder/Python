"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""


def cycle_print(lst):
    for i in lst:
        print(f'содержимое: {i}, тип: {type(i)}, длина: {len(i)}')


cls_func_mtd = [b'class', b'function', b'method']
cycle_print(cls_func_mtd)