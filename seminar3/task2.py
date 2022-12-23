from my_functions import input_int

'''Базовые задания'''


# 2) Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать
# вывод данных о пользователе одной строкой.


def user_information(**user):
    print(*user.values())


user_information(name=input('Имя: '), surname=input('Фамилия: '),
                 year=input_int(text='год рождения: '),
                 city=input('город проживания: '), email=input('email: '),
                 phone=input_int(text='телефон(только цифры): '))
