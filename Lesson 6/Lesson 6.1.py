from time import sleep


class TrafficLight:

    __color = 'красный'

    def running(self, length_red = 7, length_yellow = 2, length_green = 10):

        self.__color = 'красный'
        print(self.__color)
        sleep(length_red)

        self.__color = 'желтый'
        print(self.__color)
        sleep(length_yellow)

        self.__color = 'зелёный'
        print(self.__color)
        sleep(length_green)

        print('Сфетофор отработал')


TrafficLight().running(3, 1, 5)