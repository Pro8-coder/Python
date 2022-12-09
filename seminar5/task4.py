# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на
# русские. Новый блок строк должен записываться в новый текстовый файл.


def open_r_utf():
    try:
        with open('task4.txt', encoding='utf=8') as f_obj:
            lst = [line.strip() for line in f_obj]
    except IOError:
        print('Произошла ошибка ввода/вывода')
    return lst


def f_num_ru(func, num_ru=dict()):
    lst_ru = [num_ru.get(x) + func()[i][-4:] for i, x in
              enumerate(num_ru.keys()) if x in func()[i]]
    return lst_ru


def open_w_utf(f):
    try:
        with open('task4_ru.txt', 'w', encoding='utf=8') as f_obj_ru:
            for j in f:
                print(j, file=f_obj_ru)
    except IOError:
        print('Произошла ошибка ввода/вывода')


n = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}
open_w_utf(f_num_ru(open_r_utf, num_ru=n))
