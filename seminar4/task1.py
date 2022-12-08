from my_functions import rand_lst_float

'''Базовые задания'''


# 1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.

def payroll_preparation(mp):
    hour, bid, premium = mp[:3]
    wage = hour * bid + premium
    return wage


print(f'Заработная плата: {payroll_preparation(rand_lst_float())}')
