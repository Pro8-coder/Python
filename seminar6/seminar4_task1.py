lst = [1, 7, 4, 9, 2, 3]


def payroll_preparation(mp):
    hour, bid, premium = mp[:3]
    wage = hour * bid + premium
    return wage


def new_payroll_preparation(mp):
    return mp[0] * mp[1] + mp[2]
