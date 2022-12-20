'''
3) Реализовать базовый класс Worker (работник), в котором определить
атрибуты: name, surname, position (должность), income (доход). Последний
атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс
Position (должность) на базе класса Worker. В классе Position реализовать
методы получения полного имени сотрудника (get_full_name) и дохода с учетом
премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
'''


class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": None, "bonus": None}

    def __init__(self, name, surname, position, wage_bonus):
        self.position = position
        self.name = name
        self.surname = surname
        self._income['wage'], self._income['bonus'] = wage_bonus


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


worker1 = Position("Иван", "Иванов", "Учитель", (50000, 10000))
print(worker1.get_full_name())
print(worker1.get_total_income())
