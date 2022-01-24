import random


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = True or False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} go-go!')

    def stop(self):
        print(f'{self.color} {self.name} stop!')

    def turn_direction(self):
        i = ('направо', 'налево', 'прямо')
        direction = random.choice(i)
        # i.choice()
        print(f'{self.color} {self.name} едет {direction}, is polis {self.is_police}')

    def show_speed(self):
        return print(f'Текущая скорость {self.color} {self.name}: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        # super().__init__(speed, color, name, is_police)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        s_car = self.speed
        if s_car > 60:
            print(f'{self.color} {self.name} привышает скорость на {self.speed - 60} км!')
        else:
            print(f'Текущая скорость {self.color} {self.name}: {self.speed}')
        return


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        s_car = self.speed
        if s_car > 40:
            print(f'{self.color} {self.name} привышает скорость на {self.speed - 40} км!')
        else:
            print(f'Текущая скорость {self.color} {self.name}: {self.speed}')
        return


r = Car(80, 'red', 'ferari', is_police=True)
r.turn_direction()
# r.stop()
# r.go()
r.show_speed()
b = TownCar(61, 'black', 'mercedes', is_police=True)
b.go()
b.show_speed()
c = WorkCar(48, 'green', 'porshe', is_police=False)
c.show_speed()

