from seminar2_task3 import season_rus

'''
Написать тесты для ДЗ уроков 1-8
1) не менее 10 тестов
2) желательно с разными ф-циями (assertEqual, assertRaises и т.д.)
3) тесты не должны быть вместе с исходным кодом (нужно разместить в разных
модулях)
Задание НУЖНО!!!! сдать архивом
'''


def assert_season_rus(n, m):
    assert season_rus(n) == m, f'{n} месяц это не {m}'


# num = int(input('Введите № месяца: '))
# month = input('Введите название месяца: ')
assert_season_rus(1, 'зима')
assert_season_rus(7, 'зима')
