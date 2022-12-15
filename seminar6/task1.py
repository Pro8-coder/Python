from timeit import timeit

'''
seminar2_task3.py
Новый код работает быстрее за счёт отказа от цикла.
'''
print('seminar2_task3')
print(f'Старый: ', timeit("season_rus(month)",
                          setup="from seminar2_task3 import season_rus, month",
                          number=10000000))
print(f'Новый: ', timeit("new_season_rus(month)",
                          setup="from seminar2_task3 import new_season_rus, month",
                          number=10000000))

'''
seminar2_task2.py
Новый код работает быстрее за счёт множественного присвоения.
'''
print('seminar2_task2')
print(f'Старый: ', timeit("exchange_neighbor_elements(lst)",
                          setup="from seminar2_task2 import exchange_neighbor_elements, lst",
                          number=10000000))
print(f'Новый: ', timeit("new_exchange_neighbor_elements(lst)",
                          setup="from seminar2_task2 import new_exchange_neighbor_elements, lst",
                          number=10000000))

'''
seminar4_task1.py
Новый код работает быстрее за счёт отказа от создания переменных.
'''
print('seminar4_task1')
print(f'Старый: ', timeit("payroll_preparation(lst)",
                          setup="from seminar4_task1 import payroll_preparation, lst",
                          number=10000000))
print(f'Новый: ', timeit("new_payroll_preparation(lst)",
                          setup="from seminar4_task1 import new_payroll_preparation, lst",
                          number=10000000))
