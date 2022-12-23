'''
3) Создайте собственный класс-исключение, обрабатывающий ситуацию деления на
нуль. Проверьте его работу на данных, вводимых пользователем. При вводе
пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
'''


class MyException(Exception):
    def __init__(self, *args):
        self.data = args


while True:
    lst = list(map(int, input('Введите 2 целых числа через пробел: ').split()))
    if not lst:
        break
    try:
        if lst[1] == 0:
            raise MyException("Деление на ноль недопустимо")
        else:
            print(lst[0] / lst[1])
    except MyException as err:
        print(err)
    print('"Enter" для выхода.')
