'''
4) Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40
(WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите
результат.
'''


class Car:
    speed = 0
    color = None
    name = "car"
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, side):
        return ("повернула налево", "повернула направо")[side == 'right']

    def show_speed(self):
        return f'Текущая скорость {self.name}: {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Текущая скорость {self.name}: {self.speed}')
            return f'{self.name} превышена скорость для "town car"'
        else:
            return f'Текущая скорость {self.name}: {self.speed}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость {self.name}: {self.speed}')
            return f'{self.name} превышена скорость для "work car"'
        else:
            return f'Текущая скорость {self.name}: {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car1 = TownCar(14, 'серый', 'car1', False)
car2 = SportCar(88, 'красный', 'car2', False)
car3 = WorkCar(63, 'черный', 'car3', False)
car4 = PoliceCar(100, 'белый', 'car4', True)
print(car1.show_speed())
print(f'{car1.turn("right")}, {car1.stop()}.')
print(car2.show_speed())
print(f'{car3.go()}, {car3.turn("left")}')
print(car3.show_speed())
print(f'{car3.name}'
      f' {("не полицейская машина", "полицейская машина")[car3.is_police]}')
print(f'Цвет {car3.name} {car3.color}')
print(car4.show_speed())
print(f'{car4.name}'
      f' {("не полицейская машина", "полицейская машина")[car4.is_police]}')
