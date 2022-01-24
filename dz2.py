class Road:
    _len = 0
    _width = 0
    asphalt_mass = 0
    thickness = 0

    def __init__(self, len, width, asphalt_mass, thickness):
        self._len = len
        self._width = width
        self.asphalt_mass = asphalt_mass
        self.thickness = thickness

    def weight(self):
        result = self._len * self._width * self.asphalt_mass * self.thickness / 1000
        return print(f'Масса асфальта {result} для поерытия всей дороги.')


r = Road(20, 5000, 25, 5)
r.weight()