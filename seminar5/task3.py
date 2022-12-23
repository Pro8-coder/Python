# 3) Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк). Определить, кто из
# сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32


def open_r_utf():
    try:
        with open('task3.txt', encoding='utf=8') as f_obj:
            lst = [{line.split()[0]: float(line.split()[1])} for line in f_obj]
    except IOError:
        print('Произошла ошибка ввода/вывода')
    return lst


def task3():
    average_salary = 0
    for i in open_r_utf():
        average_salary += i.get(*i.keys())
        if i.get(*i.keys()) < 20000:
            print(*i.keys())
    return average_salary / len(open_r_utf())


print(f'Средняя величина дохода сотрудников: {round((task3()), 2)}')
