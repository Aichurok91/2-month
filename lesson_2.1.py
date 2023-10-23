# class Geeks:
#     # print("Hello World")
#     name = "Natasha"                                             #экземплеяр атрибут
#     def my_method(self):
#         print("Привет, это мой метод!!!")
    
#     def hello_method(self):
#         print(f"Я {self.name}, я поняла что это твой метод")
# # # Geeks()
# geeks = Geeks()
# geeks.my_method()

# geeks.hello_method()

# class User:
#     def __init__(self, name, surname, age, phone):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.phone = phone

#     def info_user(self):
#         print(f"Имя: {self.name}, Фамилия: {self.surname}, Возраст:{self.age}, Моб.телефон:{self.phone}")

# user = User("Aichurok", "Abdukadyr kyzy", "32", "0778493732")
# user.info_user()

class Car:
    def __init__(self,brand, model, year, type_fuel):
        self.brand = brand
        self.model = model
        self.year = year
        self.type_fuel =year

    def info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год: {self.year}, Топлива: {self.type_fuel}")
    def cars(self):
        print("МАшина завелась")
        n = 0
        while True:
            n=+0.5
            if n == 20:
                print("Мы проехали 20 км.")
            elif n==50:
                print("Вы проехали 50км.")
            elif n ==80:
                print("У вас мало топлива")
            elif n==100:
                print("Вы проехали 100км.")
                print("Машина остановлена, не осталось топлива")
                break
car = Car("Daewoo", "Matiz 3", "2008", "benzin-gaz")
car.info()
car.cars()