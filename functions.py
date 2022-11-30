def input_int(text='Введите число: '):
    '''Ввод целого числа и проверка верности ввода'''
    while True:
        try:
            num = int(input(f'{text}'))
        except ValueError:
            print('Введено не верное значение попробуйте снова.')
            continue
        break
    return num
