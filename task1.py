import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        print(f'{self.__color.title()} now!')


color_red = TrafficLight('red')
color_yellow = TrafficLight('yellow')
color_green = TrafficLight('green')
for i in range(1, 4):
    color_red.running()
    time.sleep(7)
    color_yellow.running()
    time.sleep(2)
    color_green.running()
    time.sleep(10)
