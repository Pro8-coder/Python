from my_functions import rand_lst

'''Доп. задания'''


# 8) Напишите программу, которая найдёт произведение пар чисел списка. Парой
# считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def product_pairs(lst):
    print(lst)
    result = []
    for i in range(round(len(lst) / 2)):
        result.append(lst[i] * lst[-(i + 1)])
    return result


print(product_pairs(rand_lst()))
