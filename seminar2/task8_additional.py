'''Дополнительные задания'''


# Напишите программу, которая принимает на вход число N и выдает набор
# произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def from_n_to_n(n):
    global count, result
    result = []
    count = 1
    if n > 0:
        from_n_to_n(n - 1)
        count *= n
        result.append(count)
    return result


print(from_n_to_n(int(input('Введите число: '))))
