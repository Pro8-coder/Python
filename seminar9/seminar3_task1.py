def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return 'На ноль нельзя делить'
    return result
