"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


def enc_dec(lst):
    for i in lst:
        print(f'оригинал: {i}, {type(i)}')
        b = i.encode(encoding='utf8')
        print(f'результат encode: {b}, {type(b)}')
        s = b.decode()
        print(f'результат decode: {s}, {type(s)}\n')


lst1 = ['разработка', 'администрирование', 'protocol', 'standard']
enc_dec(lst1)
