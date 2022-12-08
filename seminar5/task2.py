# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('task2.txt', encoding='utf=8') as task2:
    lines = 0
    try:
        for i in task2:
            words = len(i.split())
            print(f'В строке "{i}": {words} слов')
            lines += 1
        print(f'Всего {lines} строк')
    except IOError:
        print('Произошла ошибка ввода/вывода')
