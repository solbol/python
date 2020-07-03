class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} поехала')

    def stop(self):
        print(f'{self.color} {self.name} остановилась')

    def turn(self, direction):
        print(f'{self.color} {self.name} повернула {"налево" if direction == "left" else "направо"}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')
        if self.speed > 60:
            print('Текущая скорость превышена. Разрешённая скорость 60 км/ч')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')
        if self.speed > 40:
            print('Текущая скорость превышена. Разрешённая скорость 40 км/ч')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(70, 'красная', 'Тоёта', False)
town_car.go()
town_car.stop()
town_car.turn('left')
town_car.show_speed()

print('')

police_car = PoliceCar(90, 'чёрная', 'Лада', True)
police_car.turn('right')
police_car.show_speed()