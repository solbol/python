class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self):
        super().__init__('ручка')

    def draw(self):
        print(f'Запуск отрисовки - {self.title}.')


class Pencil(Stationery):
    def __init__(self):
        super().__init__('карандаш')

    def draw(self):
        print(f'Запуск отрисовки - {self.title}.')


class Handle(Stationery):
    def __init__(self):
        super().__init__('маркер')

    def draw(self):
        print(f'Запуск отрисовки - {self.title}.')


Pen().draw()
Pencil().draw()