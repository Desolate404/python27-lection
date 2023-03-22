"   ----Ассоциация----   "
#Ассоциация - принцип ООП, в котором два класса друг с другом связаны
#Ассоциация делится на 2 принципа:
#1. агрегация (более слабая связь)
#2. композиция (более сильная связь)

class Battery:
    power = 100

    def charge(self):
        if self.power < 100:
            self.power = 100

class Iphone:
    def __init__(self, color):
        self.color = color
        self.battery = battery()
        #когда мы создаем обьект от другого класса прям внутри другого - композиция

iphone = Iphone('золотой')
del iphone
#обьект батарейки удаляется вместе с обьектом iphone

#print(iphone.battery) #<__main__.battery object at 0x7f9575334ee0>
# print(iphone.battery.power) #100

# del iphone

# print()

class Nokia:
    def __init__(self, color, battery):
        self.color = color
        self.battery = battery
        # когда мы принимаем уже созданный вне класса обьект - агрегация

battery = Battery()

nokia = Nokia('черный', battery)

del nokia
#удаляется только обьект nokia
#обьект батарейки сохраняется

print(nokia.battery)
print(nokia.battery.power)#NameError: name 'nokia' is not defined