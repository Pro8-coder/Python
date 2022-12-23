from Python_my_functions import rand_lst_int, new_rand_lst_int, \
    rand_lst_float, new_rand_lst_float

num = 10000000

'''
Python_my_functions.py
new_rand_lst_int и new_rand_lst_float используют генератор и как следствие
экономят место.
'''
print(rand_lst_int(num))
print(new_rand_lst_int(num))
print(rand_lst_float(num))
print(new_rand_lst_float(num))
