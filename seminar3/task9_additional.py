'''Доп. задания'''

# 9) Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = list(
    map(float, input('Введите вещественные числа через пробел: ').split()))
result = []
for i in lst:
    result.append(round(i - int(i), 2))
print(max(result) - min(result))
