"""
1. Миксины - классы, которые будут использоваться для наследования от миксинов не создаются обьекты
2. Миксины - классы примеси, которые служат для расширения функционала класса
"""
#От Миксинов нельзя создавать обьекты, поскольку миксины - не самостоятельные классы
#При наследовании миксины должны идти в первую очередь

class WalkMixin:
    def walk(self):
        print('я могу ходить')

class SwimMixin:
    def swim(self):
        print('я могу плыть')

class FlyMixin:
    def fly(self):
        print('я могу летать')

class Human(WalkMixin, SwimMixin):
    name = 'Человек'

    def talk(self):
        print('я могу говорить')

class Fish(SwimMixin):
    name = 'рыба'

class Exocoetidae(SwimMixin, FlyMixin):
    name = 'летучая рыба'

class Duck(WalkMixin, SwimMixin, FlyMixin):
    name = 'утка'

obj = Human()
setattr(obj, 'new_attribute', 'Hello world')
print(dir(obj))

# object = [Human(), Fish(), Exocoetidae(), Duck()]

# for obj in object:
#     #print(obj.name)

#     attrs = ['fly', 'swim', 'walk', 'talk']
#     for attr in attrs:
#         if hasattr(obj, attr):
#             method = getattr(obj, attr)
#             method()

#obj = Human()
#print(hasattr(obj), 'fly') -> True
#print(getattr(obj, 'walk')) 
#<bound method WalkMixin.walk of <__main__.Human object at 0x7fd498c35c40>>
# method()
# obj = Human()
# print(hasattr(obj, 'fly')) #False
# obj = Fish()
# print(hasattr(obj, 'fly')) #True
# obj = Duck()
# obj.fly()
# obj.walk()
# obj.swim()
# obj = Exocoetidae()
# obj.fly()
# obj.swim()
# obj = Human()
# obj.talk()
# obj.walk()

# hasattr - функция, которая принимает обьект и название аттрибута. Возвращает  True, если у обьекта есть такой аттрибут (метод)
#getattr -  функция, которая принимает обьект и название аттрибута. Возвращает значение аттрибута
#setattr - функция, которая принимает обьект, название аттрибута и значение аттрибута. Добавляет в обьект новый аттрибут или перезапишет одноименный аттрибут