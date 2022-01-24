import time


class TrafficLight:
    __color = []

    def __init__(self, color):
        self.__color = color

    def running(self):
        color = self.__color
        for i in color:
            if i == 'red':
                print('Светафор "КРАСНЫЙ"!')
                time.sleep(7)
                for i in color:
                    if i == 'yellow':
                        print('Светафор "ЖЕЛТЫЙ"!')
                        time.sleep(3)
                        for i in color:
                            if i == 'green':
                                print('Светафор "ЗЕЛЕНЫЙ"!')
                                time.sleep(5)
                                break


r = TrafficLight(['yellow', 'red', 'green'])
r.running()
