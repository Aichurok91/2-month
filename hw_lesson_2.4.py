# Задача: Создайте класс "Таймер" (Timer), который будет представлять простой таймер обратного отсчета. 
# Класс должен иметь следующие методы:

# 1. Метод `__init__`: Этот метод должен инициализировать таймер с начальным значением времени 
# (в секундах), которое передается аргументом при создании объекта.

# 2. Метод `get_time`: Этот метод должен возвращать текущее значение времени таймера в секундах.

# 3. Метод `start`: Этот метод должен запустить таймер, уменьшая значение времени на 1 каждую секунду, 
# пока таймер не достигнет значения 0.

# 4. Метод `reset`: Этот метод должен сбрасывать значение таймера в начальное значение, указанное при создании объекта.

class Timer:
    def __init__(self, initial_time):
        self.initial_time = initial_time
        self.current_time = initial_time

    def get_time(self):
        return self.current_time

    def start(self):
        while self.current_time > 0:
            self.current_time -= 1
            print(self.current_time)
            time.sleep(1)

    def reset(self):
        self.current_time = self.initial_time
timer = Timer(10)
print(timer.get_time())
timer.start()  
print(timer.start())
timer.reset()
print(timer.get_time())