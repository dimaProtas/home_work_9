class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        return print('Запуск отрисовки!')

class Pen(Stationery):
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        return print(f'Запуск отрисовки "Ручкой": \n {self.title}!')

class Pencil(Stationery):
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        return print(f'Запуск отрисовки "Карандашем": \n {self.title}')

class Handle(Stationery):
    def __init__(self, title):
        # super.__init__(title)
        self.title = title

    def draw(self):
        return print(f'Запуск отрисовки "Маркером": \n {self.title}')


a = Pencil('my_projekt')
a.draw()
b = Pen('new projet')
b.draw()
c = Handle('first proj')
c.draw()