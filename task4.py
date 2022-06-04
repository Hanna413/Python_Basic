class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} car is going.')

    def stop(self):
        print(f'{self.name} car stopped.')

    def turn(self, direction):
        print(f'{self.name} car turned {direction}')

    def show_speed(self):
        print(f'{self.name} car is going {self.speed} m/h!')


class TownCar(Car):
    def __init__(self, speed, color, name='town', is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.speed} m/h is too fast for town!')
        else:
            print(f'Car is going {self.speed} m/h!')


class PoliceCar(Car):
    def __init__(self, speed, color, name='police', is_police=True):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.speed} m/h is too fast for police car!')
        else:
            print(f'{self.name} car is going {self.speed} m/h!')


car = Car(70, 'pink', 'Just a car', False)
town_car = TownCar(80, 'black')
police_car = PoliceCar(35, 'blue')

print(vars(car))
print(vars(town_car))
print(vars(police_car))

town_car.go()
town_car.show_speed()
town_car.turn('right')
town_car.stop()
police_car.go()
police_car.show_speed()
