class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation(self, weight_per_cm=25, thick=5):
        print(f'You need {self._width * self._length * weight_per_cm * thick / 1000} t of asphalt.')


my_road = Road(5000, 20)
my_road.calculation()
your_road = Road(5000, 20)
your_road.calculation(20, 2)
