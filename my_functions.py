from random import randint


def input_int(text='Введите число: '):
    '''Ввод целого числа и проверка верности ввода'''
    while True:
        try:
            num = int(input(f'{text}'))
        except ValueError:
            print('Введено не верное значение попробуйте снова.')
            continue
        break
    return num


def rand_lst_int():
    lst = []
    while len(lst) < 7:
        lst.append(randint(0, 10))
    return lst


def rand_lst_float():
    lst = []
    while len(lst) < 7:
        lst.append(randint(100, 1000) / 100)
    return lst


def open_r_utf(file_name):
    try:
        with open(file_name, encoding='utf=8') as f_obj:
            lst = [{line.split()[0]: float(line.split()[1])} for line in f_obj]
    except IOError:
        print('Произошла ошибка ввода/вывода')
    return lst
