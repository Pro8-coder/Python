'''
Создать не менее двух дескрипторов для атрибутов классов, которые вы создали
ранее в ДЗ
'''

print("\nseminar7 task2")


class NumDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        '''Проверка на ввод числа.'''
        if type(value) != int and type(value) != float:
            raise TypeError(
                "Присваивать можно только целые числа.")
        instance.__dict__[self.name] = value


class Road:
    _length = NumDescriptor()
    _width = NumDescriptor()

    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def mass(self):
        return f'{self._width * self._length * 25 * 5 / 1000} т'


road = Road(20, 5000.1)
print(road.__dict__, road.mass)
print("\nseminar7 task3")


class Descriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value != value.title():
            raise ValueError('Укажите имя c большой буквы!')
        instance.__dict__[self.name] = value


class Worker:
    name = Descriptor()
    surname = Descriptor()
    position = ""
    _income = {"wage": None, "bonus": None}

    def __init__(self, name, surname, position, wage_bonus):
        self.position = position
        self.name = name
        self.surname = surname
        self._income['wage'], self._income['bonus'] = wage_bonus


class Position(Worker):
    @property
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    @property
    def get_total_income(self):
        return sum(self._income.values())


worker1 = Position("Иван", "Иванов", "Учитель", (50000, 10000))
print(worker1.get_full_name, worker1.get_total_income)
print(worker1.__dict__)
