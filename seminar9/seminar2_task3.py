'''
seminar2/task3.py
'''


def season_rus(m):
    for i, x in enumerate(year_l):
        if m in x:
            year_rus = ['зима', 'весна', 'лето', 'осень']
            return year_rus[i]


year_l = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
