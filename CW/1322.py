# class Line:
#     name = "test_1"
#
#     # def __init__(self, color, type, length):
#     #     self.__color = "black"
#     #     self.__type = "solid"
#     #
#     #     self.__length = 5
#     def say_hello(self):
#         print("Hello", self.name)
#
#
# line1 = Line()
# line1.say_hello()
# line2 = Line()
# line2.name = "Test_2"
# line2.say_hello()
# print(line1.__dict__)
# print(line2.__dict__)
# print(Line.__dict__)

# class Person:
#     def say(self, message):
#         print(message)
#
#     def say_hello(self):
#         self.say("Hello work")
#
#
# petya = Person()
# petya.say("And What")
# petya.say_hello()


class Person:
    def __init__(self, name):
        self.name = name
        self.age = 1

    def display_info(self):
        print(f"Name: {self.name}  \nAge: {self.age}")


petya = Person("Petya")
print(petya.name)
print(petya.age)
petya.display_info()
petya.age = 36
print(petya.name)
print(petya.age)
petya.display_info()


