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
