'''
1) Создать класс TrafficLight (светофор) и определить у него один атрибут
color (цвет) и метод running (запуск). Атрибут реализовать как приватный. В
рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и
вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его
нарушении выводить соответствующее сообщение и завершать скрипт.
'''
from time import sleep

iter = 3
'''
Измените на 0 для бесконечного цикла.
'''


class TrafficLight:
    __color = {"Красный": 7, "Желтый": 2, "Зеленый": 7}

    def running(self):
        for key, value in self.__color.items():
            print(key)
            sleep(value)


def iterations(num):
    if num == 0:
        while True:
            TrafficLight().running()
    for i in range(num):
        TrafficLight().running()


iterations(iter)
