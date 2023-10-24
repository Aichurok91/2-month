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


# class Animal: 
#     def __init__(self, name, age): 
#         self.name = name 
#         self.age = age 
         
#     def get_info(self): 
#         return f"{self.name} {self.age}" 

# class Dog(Animal): 
#     def __init__(self, name, age, breed): 
#         super().__init__(name, age) 
#         self.breed = breed 
             
#     def get_breed(self): 
#         return self.breed 
         
# dog = Dog("REX", 3, "Питбуль") 
# print("Имя : ", dog.get_info()) 
# print("Возраст: ", dog.age) 
# print("Порода: ", dog.get_breed()) 

# class Cat(Animal): 
#     def __init__(self, name, age, color): 
#         super().__init__(name, age) 
#         self.color = color 
             
#     def get_color(self): 
#         return self.color 
         
# cat = Cat("Пума", 3, "полосатый") 
# print("Имя: ", cat.get_info()) 
# print("Возраст: ", cat.age) 
# print("Окрас кота:", cat.get_color())

# ДОП задание:
# 	Загрузить Д/З в GitHub



