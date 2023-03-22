from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    @abstractmethod  # это абстрактный метод который
    def speak(self):
        pass

class Dog(AbstractAnimal):
    pass

#obj = Dog()
#TypeError: Can't instantiate abstract class Dog with abstract method speak

class Dog(AbstractAnimal):
    def speak(self):
        print("гав-гав")

obj = Dog()
obj.speak()
# теперь ничего не ругается #гав-гав

#Abstractproperty

> "Полиморфизм" - можем унаследовать от самолета(чертежа) основные характеристики и это уже будет реальный обьект
> "Инкапсуляция" - сокрытие данных : например мы можем сокрыть двигатель самолета от всех чтоб его никто не видел (пассажиру не важно видеть двигатель, ему нужно долететь от точки А до точки Б)
> "Класс" это у нас просто чертеж "Обьект" это уже реальный самолет
> "Super" Используется,Хранит в себе функцию , обращается к определенному методу , берет
> __init__ - то что мы прописываем в ините это экземпляр класса
то что мы прописываем в классе это аттрибут класса

class Samolet(ABC)
    def vzlet(self)

sam = Samolet()
sam:vzlet

random - библиотека от туда можно использовать нужные функции , последовательности рандомных чисел (можно использовать для случайной последовательности чисел, например для генерации случайного пароля)

getter setter

class Contact
__phone = None   # это уже не функция, а аттрибут

    @property
        def phone(self)
        return self.__phone
    @phone.setter(self)
        def phone(self)
    
obj = contact()
obj.phone = 1234