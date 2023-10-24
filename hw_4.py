# Задача 1
class Shape:
    def draw(self):
        print("Рисуем фигуру")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Рисуем круг с радиусом {self.radius}")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print(f"Рисуем прямоугольник с шириной {self.width} и высотой {self.height}")

shape = Shape()
circle = Circle(10)
rectangle = Rectangle(4, 6)

shape.draw()      
circle.draw()    
rectangle.draw()


class Counter:
    def __init__(self):
        self.value = 0
    
    def increment(self, value):
        self.value += value
        
    def get_value(self):
        return self.value
    
counter = Counter()
print("Текущее значение счетчика: ", counter.get_value( ))

counter.increment(18)
print("Текущее значение счетчика после увеличения: ", counter.get_value())

counter.increment(20)
print("Текущее значение счетчика после еще онного увеличения: ", counter.get_value())