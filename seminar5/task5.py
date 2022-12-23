from my_functions import rand_lst_int

# 5) Создать (программно) текстовый файл, записать в него программно набор
# чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в
# файле и выводить ее на экран.

try:
    with open('task5.txt', 'w', encoding='utf=8') as task5:
        for num in rand_lst_int():
            print(num, file=task5, end=' ')
except IOError:
    print('Произошла ошибка ввода/вывода')

try:
    with open('task5.txt', encoding='utf=8') as task5:
        for i in task5:
            print(sum(map(int, i.split())))
except IOError:
    print('Произошла ошибка ввода/вывода')
