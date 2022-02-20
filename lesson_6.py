# ДЗ к уроку №6
# Попова Светлана

#1

from time import sleep

class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        for key, value in self._color.items():
            sleep(value)
            print(key)


traffic = TrafficLight(color={
    "Красный": 7,
    "Желтый": 2,
    "Зеленый": 3})
traffic.running()

#2

class Road:
    def __init__(self, length, width, mass, thickness): #переделать вход только длина и ширина
        self._length = length
        self._width = width
        self._mass = mass
        self._thickness = thickness

    def mass(self): #переделать сюда входит масса и толщина
        length = int(input('Введите длину дороги в метрах: '))
        width = int(input('Введите ширину дороги в метрах: '))
        mass = int(input('Введите массу асфальта в килограммах: '))
        thickness = int(input('Введите толщину асфальта в сантиметрах: '))
        print(f'Количество асфальта толщиной {thickness} и массой {mass} т. на 1 кв.м. равен {int(length * width * (mass * 0.001) * thickness)} тонн.')


massa = Road(0, 0, 0, 0)
massa.mass()

#3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.full_name = [name, surname, position]
        self._income = {"wage": int(wage), "bonus": int(bonus)}

class Position(Worker):

    def get_full_name(self):
        print(f'{self.full_name}:')

    def get_total_income(self):
        print(f'Ваш доход с учетом премии составляет: {sum(self._income.values())}рублей.')


total = Position('Poll', 'John', 'developer', 5000, 3000)
total.get_full_name()
total.get_total_income()

#4

class Car:
    def __init__(self, name, color, speed, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        print(f'Машина {self.name}, цвет- {self.color} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self):
        print(f'Машина {self.name} повернула направо!')

    def show_speed(self):
        return f'Машина {self.name} двигается со скоростью {self.speed} км/час.'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость {self.name} составляет {self.speed} - это больше чем 60 км/час! Нарушаете!')

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость {self.name} составляет {self.speed} - это больше чем 40 км/час! Нарушаете!')

class PoliceCar(Car):
    pass

my_car = Car('Москвич', 'красный', 40)
my_car.go()
my_car.stop()
my_car.turn()
my_car.show_speed()

lomborgini = TownCar('Ломборджини', 'зеленый', 220)
lomborgini.show_speed()

gazel = WorkCar('Газель', 'белая', 90)
gazel.show_speed()

#5

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки!')

class Pen(Stationery):

    def draw(self):
        print(f'Вы рисуете ручкой!')

class Pencil(Stationery):

    def draw(self):
        print(f'Вы ресуете карандашом!')

class Handle(Stationery):

    def draw(self):
        print(f'Вы ресуете маркером!')

my_draw = Stationery('')
my_draw.draw()

my_pen = Pen('')
my_pen.draw()

my_pencil = Pencil('')
my_pencil.draw()

my_handle = Handle('')
my_handle.draw()

