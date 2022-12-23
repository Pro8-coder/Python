'''
5) Реализовать класс Stationery (канцелярская принадлежность). Определить в нем
атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
“Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение. Создать
экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
'''


class Stationery:
    title = "название"

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    title = "ручка"

    def draw(self):
        super().draw()
        print('\tвыбрана ручка', "\n")


class Pencil(Stationery):
    title = "карандаш"

    def draw(self):
        super().draw()
        print('\tвыбран карандаш', "\n")


class Handle(Stationery):
    title = "маркер"

    def draw(self):
        super().draw()
        print('\tвыбран маркер', "\n")


pen = Pen()
print(f'Инструмент: {pen.title}')
pen.draw()

pencil = Pencil()
print(f'Инструмент: {pencil.title}')
pencil.draw()

handle = Handle()
print(f'Инструмент: {handle.title}')
handle.draw()
