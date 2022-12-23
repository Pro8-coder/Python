lst = [1, 2, 5, 6, 7]


def exchange_neighbor_elements(l):
    for i in range(1, len(l), 2):
        count = l[i]
        l[i] = l[i - 1]
        l[i - 1] = count
    return l


def new_exchange_neighbor_elements(l):
    for i in range(1, len(l), 2):
        l[i], l[i - 1] = l[i - 1], l[i]
    return l
