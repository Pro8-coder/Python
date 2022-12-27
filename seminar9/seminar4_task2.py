lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_lst = [x for i, x in enumerate(lst) if i > 0 and x > lst[i - 1]]
