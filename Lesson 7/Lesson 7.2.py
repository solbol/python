from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        super().__init__('Пальто')
        self.size = size

    @property
    def tissue_consumption(self):
        return self.size/6.5 + 0.5


class Costume(Clothes):
    def __init__(self, growth):
        super().__init__('Костюм')
        self.growth = growth

    @property
    def tissue_consumption(self):
        return 2 * self.growth + 0.3


coat = Coat(52)
costume = Costume(1.8)

print(coat.tissue_consumption)
print(costume.tissue_consumption)

print(coat.tissue_consumption + costume.tissue_consumption)