class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, asphalt_mass_one, thickness):
        return self._length * self._width * asphalt_mass_one * thickness


print(Road(20, 5000).asphalt_mass(25, 5))