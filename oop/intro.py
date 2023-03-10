# class Person:
#     arms = 2
#     legs = 2
#     name = 'Nastya'

    # def __init__(self, name):
        # __init__ - dunder метод, который добавляет в обьект self атрибуты которые отличаются у разных обьектов
        # self.name = name

    # def walk(obj):
    #     print(obj)
    #     print("я хожу")
    # def walk(self):
        #self - ссылка на обьект, у которого мы вызываем данный метод
        # print(self)
        # print("я хожу")

# person1 = Person()
# Person.walk(person1)
#print(type(person1))       #print(person1)<__main__.Person object at 0x7fcdb8b47f70>
# print(person1.arms) #2
# person1.walk()

# p1 = Person()
# p2 = Person()
# p3 = Person()
# print(p1.name, p2.name, p3.name)

# person1 = Person('Nastya')
# person2 = Person('Nurkamila')
# print(person1.name, person2.name)

# Атрибуты класса и атрибуты обьектов класса



obj = A()
print(dir(obj))

print(obj.var1) # 'переменная класса'
print(obj.var2) # 'переменная обьекта'

