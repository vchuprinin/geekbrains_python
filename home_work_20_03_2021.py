import time


# 1
class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        for item in self.__color:
            if item == 'red':
                print(item)
                time.sleep(7)
            elif item == 'yellow':
                print(item)
                time.sleep(2)
            elif item == 'green':
                print(item)
                time.sleep(4)


a = TrafficLight()

a.running()
print('*' * 50)


# 2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_calculation(self):
        print(self._length * self._width * 25 * 5)


mass_asphalt = Road(int(input('Введите длинну полотна ')), int(input('Введите ширину полотна ')))
mass_asphalt.get_calculation()
print('*' * 50)


# 3
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': 100, 'bonus': income}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


my_worker = Position('Oleg', 'Kotov', 'manager', 30)
best_worker = my_worker.get_full_name()
salary_best_worker = my_worker.get_total_income()
print('*' * 50)


# 4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if self.is_police == True:
            self.is_police = 'Полиция'
        else:
            self.is_police = 'Гражданский'

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')


class TownCar(Car):
    def new_car(self):
        print(self.name, self.color, self.speed, self.is_police)
        if self.speed > 60:
            print('Привышена скорость')


class SportCar(Car):
    def new_car(self):
        print(self.name, self.color, self.speed, self.is_police)


class WorkCar(Car):
    def new_car(self):
        print(self.name, self.color, self.speed, self.is_police)
        if self.speed > 40:
            print('Привышена скорость')


class PoliceCar(Car):
    def new_car(self):
        print(self.name, self.color, self.speed, self.is_police)


town_car = TownCar(250, 'black', 'BMW', False)
town_car.new_car()
town_car.go()
town_car.stop()
town_car.turn('Налево')
town_car.show_speed()
print('*' * 50)


# 5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Рисует {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисует {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Рисует {self.title}')


pen = Pen('pen')
pen.draw()

pencil = Pencil('pencil')
pencil.draw()

handle = Handle('handle')
handle.draw()
