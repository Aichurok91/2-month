# Задача 1
# Вам нужно создать программу для рисования различных геометрических фигур. У вас должен быть базовый класс Shape (Фигура), а также несколько подклассов, представляющих различные фигуры, такие как Circle (Круг) и Rectangle (Прямоугольник).
# Класс Shape должен иметь метод draw(), который будет выводить на экран "Рисуем фигуру". Классы Circle и Rectangle должны наследовать этот метод и дополнительно реализовать свою функциональность. 
# Подсказка: Делайте точно так же как и на уроке

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def draw(self):
#         print(f"Рисуем круг с радиусом {self.radius}")

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def draw(self):
#         print(f"Рисуем прямоугольник с шириной {self.width} и высотой {self.height}")

# shape = Shape()
# circle = Circle(10)
# rectangle = Rectangle(4, 6)

# shape.draw()      
# circle.draw()    
# rectangle.draw()


# Задача 2

# Создайте класс Counter (Счетчик), который будет представлять счетчик, способный увеличиваться на заданное значение и возвращать текущее значение.
# Класс Counter должен иметь следующие методы:
# __init__(self): Конструктор для инициализации счетчика, начальное значение - 0.
# increment(self, value): Увеличивает счетчик на указанное значение.
# get_value(self): Возвращает текущее значение счетчика.

# class Counter:
#     def __init__(self):
#         self.value = 0
    
#     def increment(self, value):
#         self.value += value
        
#     def get_value(self):
#         return self.value
    
# counter = Counter()
# print("Текущее значение счетчика: ", counter.get_value( ))

# counter.increment(18)
# print("Текущее значение счетчика после увеличения: ", counter.get_value())

# counter.increment(20)
# print("Текущее значение счетчика после еще онного увеличения: ", counter.get_value())

