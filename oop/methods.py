class A:
    def Instance_method(self):
        print()


class A:
    @classmethod
    def class_method(cls):
        print("метод класса")
        print("cls",cls)

A.class_method()
# метод класса
#cls class '__main__.A'>

obj = A()
obj.class_method

#все равно от куда вы будете вызывать classmethod (от обьекта или класса),первым аргументом будет приходить class


#примеры
class C:
    counter = 0

    def __init__(self):
        #обьект создается
        # c.counter +=1
        self._inc_counter()
    
    def __del__(self):
        #обьект удаляется
        # c.counter -= 1
        self._dec_counter()

    @classmethod
    def _inc_counter(cls):
        #cls = class c
        #увеличиваем атрибут класса counter на один
        cls.counter += 1

    @classmethod
    def _inc_counter(cls):
        cls.counter -= 1


obj1 = C()
obj1 = C()
obj1 = C()
obj1 = C()
print(C.counter) #4
del obj1
print(C.counter)

class Pizza:
    def __init__(self, radius, *ingridients):
        self.r = radius
        self.ingridients = ingridients

    def cook(self):
        print(f"Пицца размером {self.r*2}")
        print(f"Ингридиенты {self.ingridients}")

    @classmethod
    def four_cheeze(cls, radius):
        pizza = cls(radius, "1 сыр","2 сыра","3 сыра","4 сыра")
        #pizza = Pizza(10, "1 сыр","2 сыра","3 сыра","4 сыра")
        return pizza


pizza1 = Pizza(15, "Сыр","Колбаса","Черри")
pizza1.cook

pizza2 = Pizza(10, "1 сыр","2 сыра","3 сыра","4 сыра")
pizza2.cook()

pizza3 = Pizza(10, "1 сыр","2 сыра","3 сыра","4 сыра")
pizza2.cook()

pizza4 = Pizza.four_cheeze(10)
pizza4.cook()

pizza5 = Pizza.four_cheeze(15)
pizza5.cook()

class A:
    @staticmethod
    def static_method():
        print("статик метод")

obj = A()
obj.static_method()


class Cylinder:
    def __init__(self, diameter, height):
        self.di = diameter
        self.h = height
        self.area = self.get_area(diameter, height)

    @staticmethod
    def get_area(di, h):
        from math import pi
        circle_area = pi * di**2 / 4
        side_area = pi * di * h
        return circle_area*2 + side_area
    
Cylinder1 = Cylinder(4, 10)
print(Cylinder1.area) #150.79644737231007

print(Cylinder.get_area(4, 10)) #150.79644737231007
#мы не создаем обьект, но получили нужные нам расчеты