import time


# Задача1

# class TrafficLight:
#     __color = 'red'
#     def running(self):
#         while True:
#             print(TrafficLight.__color)
#             time.sleep(7)
#             TrafficLight.__color = "yellow"
#             print(TrafficLight.__color)
#             time.sleep(2)
#             TrafficLight.__color = "green"
#             print(TrafficLight.__color)
#             time.sleep(10)
#             TrafficLight.__color = "red"
#
# trafficLight1 = TrafficLight()
# print(trafficLight1.running())

# Задача2

# class Road:
#
#     def __init__(self, length, width, mass, tckns):
#         self._l = length
#         self._w = width
#         self._m = mass
#         self._t = tckns
#
#     def asphalt(self):
#         result = self._l * self._w * self._m * self._t
#         return result
#
# road61 = Road(1500, 20, 25, 2)
#
# print(road61.asphalt())

# Задача3

# class Worker:
#     def __init__(self, name, surname, position):
#         _income = {"wage_ceo": 100000, "bonus_ceo": 25000, "wage_employee": 60000, "bonus_employee": 15000,
#                   "wage_courier": 25000, "bonus_courier": 10000}
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = _income
#
#
#
# class Position(Worker):
#     def get_full_name(self):
#         print(self.name + " " + self.surname)
#
#     def get_full_income(self):
#         if self.position == "CEO":
#             print(self._income["wage_ceo"] + self._income["bonus_ceo"])
#         elif self.position == "employee":
#             print(self._income["wage_employee"] + self._income["bonus_employee"])
#         elif self.position == "courier":
#             print(self._income["wage_courier"] + self._income["bonus_courier"])
#
#
# worker1 = Position("Ivan", "Ivanov", "CEO")
# worker2 = Position("Petr", "Ivanov", "courier")
#
# print(worker1.get_full_name())
# print(worker1.get_full_income())
# print(worker2.get_full_income())

#Задача4

# class Car:
#     def __init__(self, speed, color, name, is_Police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_Police = is_Police
#
#     def go(self):
#         print("Машина едет")
#
#     def stop(self):
#         print("Машина остановилась")
#
#     def turn_left(self):
#         print("Машина повернула налево")
#
#     def turn_right(self):
#         print("Машина повернула направо")
#     def show_speed(self):
#         print(self.speed)
#
#
# class Towncar(Car):
#     def __init__(self, speed, color, name, is_Police):
#         super().__init__(name, color, speed, is_Police)
#
#     def show_speed(self):
#         print(self.speed )
#         if self.speed > 60:
#             print("Ваша машина слишком быстро едет")
#         else:
#             print("Ваша машина едет с разрешенной скоростью")
#
# class Workcar(Car):
#     def __init__(self, speed, color, name, is_Police):
#         super().__init__(name, color, speed, is_Police)
#
#     def show_speed(self):
#         print(self.speed )
#         if self.speed > 40:
#             print("Ваша машина слишком быстро едет")
#         else:
#             print("Ваша машина едет с разрешенной скоростью")
#
# class Sportcar(Car):
#     def __init__(self, speed, color, name, is_Police):
#         super().__init__(name, color, speed, is_Police)
#
#
# class Policecar(Car):
#     def __init__(self, speed, color, name, is_Police):
#         super().__init__(name, color, speed, is_Police)
#
#         if self.is_Police == True:
#            print("Это полицейская машина")
#
# red = Sportcar(100, "red", "Ferrari", False)
# blue = Policecar(60,"blue", "Cop", True)
# print(blue.stop())
# print(red.go())

#Задача5

class Stationary:
    def __init__(self, title):
        self.t = title
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Вы рисуете ручкой")

class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Вы рисуете карандашом")

class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Вы рисуете маркером")

blue_handle = Handle(Stationary)
print(blue_handle.draw())