# Задача: Управление животными
# Вы разрабатываете программу для управления информацией о различных животных. Вам нужно реализовать базовый класс Animal, представляющий общий функционал для всех типов животных, а также два дочерних класса Dog (собака) и Cat (кот).
# Вам нужно обеспечить инкапсуляцию данных о животных и методов для доступа к этим данным. Каждое животное должно иметь свои особенности, например, звуки, которые они издают.
# Требования:
# Базовый класс Animal должен иметь следующие атрибуты:
# name (имя животного)
# age (возраст животного)
# У классов Dog и Cat должны быть свои дополнительные атрибуты и методы, например:
# Dog:
# breed (порода собаки)
# Метод bark(), который выводит на экран звук лая собаки.
# Cat:
# color (окрас кота)
# Метод meow(), который выводит на экран звук мяуканья кота.
# Оба дочерних класса должны наследовать методы get_name() и get_age() от базового класса.
# Обеспечьте инкапсуляцию, чтобы атрибуты были защищены от неправильных модификаций извне.

class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self._breed = breed

    def sound(self):
        print("Woof!")

    def get_breed(self):
        return self._breed


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self._color = color

    def sound(self):
        print("Meow!")

    def get_color(self):
        return self._color

dog = Dog("Бобик", 3, "Джек Рассел терьер")
cat = Cat("Мурзик", 5, "серый")

print(dog.get_name())  
print(dog.get_age())  
print(dog.get_breed())  
dog.sound() 

print(cat.get_name())  
print(cat.get_age())  
print(cat.get_color())  
cat.sound() 


# ДОП задание:
# 	Загрузить Д/З в GitHub



