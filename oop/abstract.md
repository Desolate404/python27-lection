# Абстракция
> принцип ООП, в котором создается абстрактный класс пустышка, в котором  указывается названия методов, которые обязательно нужно реализовать при создании дочерного класса

> чтобы реализовать абстракцию, нужно импортировать abc и наследовать от класса ABC, а нужные методы декорируем abcstractmethod

```py
from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    @abstractmethod  # это абстрактный метод который
    def speak(self):
        pass

class Dog(AbstractAnimal):
    pass
```