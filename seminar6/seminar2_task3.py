month = 10


def season_rus(m):
    year_l = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
    year_rus = ['зима', 'весна', 'лето', 'осень']
    for i, x in enumerate(year_l):
        if m in x:
            return year_rus[i]


def new_season_rus(m):
    return ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето',
            'осень', 'осень', 'осень', 'зима'][m - 1]
    # почему я сразу так не сделал!!!
