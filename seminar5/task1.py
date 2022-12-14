# 1) Создать программно файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных свидетельствует
# пустая строка.

try:
    with open('task1.txt', 'w', encoding='utf=8') as task1:
        print('Введите текст для записи в файл.'
              ' Для выхода введите пустую строку.')
        while True:
            line = input()
            if line == '':
                break
            print(line, file=task1)
except IOError:
    print('Произошла ошибка ввода/вывода')
