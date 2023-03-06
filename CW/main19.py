# ооп
#
# класс - кастомный тип данных, чертеж будущих экземпляров объектов
#
# Инкапсуляция - сокрытие внутренней реализации и предоставление санкционированного доступа к интерфейсу класса.
# Абстрагируемся от внутренней реализации.

# Наследование - расширение базового класса производными. В Python доступно множественного наследование.
# Абстрагируемся от базовых классов используя дочерние.

# Полиморфизм - один интерфейс и много реализаций. Абстрагируемся от конкретной реализации.

# v1
# class Person:  # определение класса Person
#     name = "Test"  # поле класса (переменная которая является частью класса)
#
#     # self - ссылка на текущий контекст класса, текущий экземпляр класса, дает доступ к любой части этого класса
#     # в пределах класса
#     def say_hello(self):  # метод класса (функция которая является частью класса)
#         print(f"Hello, {self.name}")
#
#
# tom = Person()
# tom.say_hello()  # Hello
#
# vasya = Person()
# vasya.say_hello()

# v2
# class Person:
#
#     def say(self, message):
#         print(message)
#
#     def say_hello(self):
#         self.say("Hello work")  # обращаемся к выше определенному методу say
#
#
# tom = Person()
# tom.say_hello()  # Hello work

# v3
# class Person:
#     # конструктор
#     def __init__(self):
#         print("Создание объекта Person")
#
#     def say_hello(self):
#         print("Hello")
#
#
# tom = Person()  # Создание объекта Person
# tom.say_hello()  # Hello

# v4
# class Person:
#
#     def __init__(self, name):
#         self.name = name  # имя человека
#         self.age = 1  # возраст человека
#
#
# tom = Person("Tom")
#
# # обращение к атрибутам
# # получение значений
# print(tom.name)  # Tom
# print(tom.age)  # 1
# # изменение значения
# tom.age = 37
# print(tom.age)  # 37

# v5
# class Person:
#     # def __new__(cls, *args, **kwargs):
#     #     pass
#
#     def __init__(self, name):
#         self.name = name  # имя человека
#         self.age = 1  # возраст человека
#
#     def display_info(self):
#         print(f"Name: {self.name}  Age: {self.age}")
#
#
# tom = Person("Tom")
# tom.age = 37
# tom.display_info()  # Name: Tom  Age: 37
#
# bob = Person("Bob")
# bob.age = 41
# bob.display_info()  # Name: Bob  Age: 41

################################################################
# инкапсуляция (тема)
# проблема
# class Person:
#     def __init__(self, name):
#         self.name = name  # устанавливаем имя
#         self.age = 1  # устанавливаем возраст
#
#     def display_info(self):
#         print(f"Имя: {self.name}\tВозраст: {self.age}")
#
#
# tom = Person("Tom")
# tom.name = "Человек-паук"  # изменяем атрибут name
# tom.age = -129  # изменяем атрибут age
# tom.name = ""
# tom.display_info()  # Имя: Человек-паук     Возраст: -129


# v1
# class Person:
#     def __init__(self, name):
#         self.__name = name  # устанавливаем имя, два нижних подчеркивания - обозначает что поле или метод private
#         # то есть доступен только внутри этого класса, для того чтобы получить доступ за пределами класса - нужно реализовать
#         # геттеры и сеттеры: методы которые дадут санкционированный доступ
#         self.__age = 1  # устанавливаем возраст
#
#     def set_age(self, age):
#         if 1 < age < 110:
#             self.__age = age
#         else:
#             print("Недопустимый возраст")
#
#     def get_age(self):
#         return self.__age
#
#     def get_name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f"Имя: {self.__name}\tВозраст: {self.__age}")
#
#
# tom = Person("Tom")
# # print(tom.__name)  # нет доступа
# tom.display_info()  # Имя: Tom  Возраст: 1
# tom.set_age(-3486)  # Недопустимый возраст
# tom.set_age(25)
# tom.display_info()  # Имя: Tom  Возраст: 25

# v2 аннотация свойств
# class Person:
#     def __init__(self, name):
#         self.__name = name  # устанавливаем имя
#         self.__age = 1  # устанавливаем возраст
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if 1 < age < 110:
#             self.__age = age
#         else:
#             print("Недопустимый возраст")
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f"Имя: {self.__name}\tВозраст: {self.__age}")
#
#
# tom = Person("Tom")
#
# tom.display_info()  # Имя: Tom  Возраст: 1
# tom.age = -3486  # Недопустимый возраст
# print(tom.age)  # 1
# tom.age = 36
# tom.display_info()  # Имя: Tom  Возраст: 36

#####
# подводные камни
# class Car:
#     def __init__(self, year):
#         self.__year = year
#
#     def show(self):
#         print("Year: ", self.__year)
#
#     def __secret_data(self):
#         print("Secret: ", self.__year)
#
#
# my_car = Car(2020)
# # print(my_car.__year)
# my_car.__year = 123
# print(my_car.__year)
# my_car.show()
# # my_car.__secret_data()
# my_car._Car__secret_data()

###
