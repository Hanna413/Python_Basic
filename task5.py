class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Рисование ручкой, будьте аккуратны.')


class Pencil(Stationery):
    def draw(self):
        print('Рисование карандашом, ошибку можно исправить ластиком.')


class Handle(Stationery):
    def draw(self):
        print('Вы рисуете маркером. Не лучше ли взять фломастеры?')


draw_stat = Stationery('что-то')
draw_pen = Pen('Pen')
draw_pencil = Pencil('Pencil')
draw_handle = Handle('Handle')

draw_stat.draw()
draw_pen.draw()
draw_pencil.draw()
draw_handle.draw()
