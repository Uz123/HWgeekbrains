""" Класс 1 """
from random import choice
from time import sleep
print("\n" + "1" + 24 * "-")


# class TrafficLight:
#     __color = ['Красный', 'Желтый', 'Зеленый']
#
#     def running(self):
#         while True:
#             flag = 0
#             if flag == 0:
#                 for i in TrafficLight.__color:
#                     print(i)
#                     if i == 'Красный':
#                         sleep(4)
#                     elif i == 'Желтый':
#                         sleep(1)
#                     elif i == 'Зеленый':
#                         sleep(5)
#             flag += 1
#             if flag == 1:
#                 for i in reversed(TrafficLight.__color[1:2]):
#                     print(i)
#                     if i == 'Красный':
#                         sleep(4)
#                     elif i == 'Желтый':
#                         sleep(1)
#             flag -= 1
#
#
# t = TrafficLight()
# t.running()
#
print("\n" + "2" + 24 * "-")


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * 25 * 5 / 1000
        print(f'Для покрытия всего дорожного полотна неободимо {round(asphalt_mass)} тонн массы асфальта')


r = Road(5000, 20)
r.asphalt_mass()

print("\n" + "3" + 24 * "-")


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


p = Position('Серафима', 'Андреева', 'Инженер мостов', '100000', '20000')
print(p.get_full_name(), p.get_total_income())

print("\n" + "4" + 24 * "-")


class Car:
    direction = ["вперед", "назад", "налево", "направо"]

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} тронулась.'

    def stop(self):
        return f'\nМашина {self.name} остановилась.'

    def turn(self):
        return f'\nМашина {self.name} едет {choice(self.direction)}'

    def show_speed(self):
        return f'\nСкорость машины {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nПревышена скорость! Скорость {self.speed}'
        else:
            return f"\nСкорость машины {self.speed}"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nПревышена скорость! Скорость {self.speed}'
        else:
            return f"\nСкорость машины {self.speed}"


class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police=True):
        super().__init__(name, speed, color, is_police)


town = TownCar('Ауди', 70, 'blue')
print(f"\n{town.go()} {town.show_speed()} {town.turn()} {town.stop()}")

sport = SportCar('Порше', 120, 'red')
print(f"\n{sport.go()} {sport.show_speed()} {sport.turn()} {sport.stop()}")

work = WorkCar('Газель', 30, 'red')
print(f"\n{work.go()} {work.show_speed()} {work.turn()} {work.stop()}")

police = PoliceCar('Тайота', 100, 'yellow')
print(f"\n{police.go()} {police.show_speed()} {police.turn()} {police.stop()}")

print("\n" + "5" + 24 * "-")


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


pen = Pen('ручкой')
print(pen.draw())
pencil = Pencil('карандашем')
print(pencil.draw())
handle = Handle('маркером')
print(handle.draw())
