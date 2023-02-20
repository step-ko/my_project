"""При выполнении дз использовать Git (делать коммиты, работать в dev ветке,
для каждой задачи отдельная ветка из dev ветки и потом делать merge в dev ветку,
после выполнения всех заданий сделать merge develop в master)
1. Пользователь вводит с клавиатуры три числа.
В зависимости от выбора пользователя программа выводит на экран
максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел.
2. Пользователь вводит с клавиатуры количество метров.
В зависимости от выбора пользователя программа переводит
метры в мили, дюймы или ярды.
3. Пользователь вводит с клавиатуры номер дня недели (1-7).
Необходимо вывести на экран названия дня недели.
Например, если 1, то на экране надпись понедельник, 2 — вторник и т.д.
4. Пользователь вводит два числа.
Определить, равны ли эти числа, и, если нет,
вывести их на экран в порядке возрастания
Пример с пары ниже.
Прислать архив с проектом польностью чтоб можно было проверить вашу работу с git.
"""


def input_number() -> float:
    while True:
        try:
            number = float(input("Please enter any number -> "))
            break
        except ValueError:
            print("Error. The number consists of characters from 0 to 9")
    number = round(number, 2)
    return number


def max_number(list_number: list[int]) -> int:
    number = max(list_number)
    return number


def min_number(list_number: list[int]) -> int:
    number = min(list_number)
    return number


def average_number(list_number: list[int]) -> int:
    number = round((sum(list_number) / len(list_number)), 2)
    return number


def action_for_menu() -> str:
    action_list = ["1", "2", "3", ""]
    while True:
        act = input("Please select an item from the menu -> ")
        if act in action_list:
            break
        else:
            print("Please select an item from the menu.\nTo exit, please press enter.")
    return act


def menu():
    while True:
        print(f"Menu:".center(40), "\n",
              f"*" * 40, "\n",
              f"Press <1> to find the maximum number".center(40), "\n",
              f"Press <2> to find minimum number".center(40), "\n",
              f"Press <3> to find the average".center(40), "\n",
              f"Press enter to exit".center(40), "\n",
              f"*" * 40)
        act = action_for_menu()
        if act == "":
            print("Goodbye :)")
            break
        elif int(act) == 1:
            print(f"The maximum number is {max_number(nums_list)}.")
        elif int(act) == 2:
            print(f"The minimum number is {min_number(nums_list)}.")
        elif int(act) == 3:
            print(f"The average value is {average_number(nums_list)}.")


# num1, num2, num3 = input_number(), input_number(), input_number()
# nums_list = [num1, num2, num3]
# menu()

# 2. Пользователь вводит с клавиатуры количество метров.
# В зависимости от выбора пользователя программа переводит
# метры в мили, дюймы или ярды.


def input_metr() -> int:
    while True:
        try:
            number = int(input("Please enter the number of meters -> "))
            break
        except ValueError:
            print("Error. The number consists of characters from 0 to 9")
    return number


def action_for_menu2():
    action_list = ["1", "2", "3", ""]
    while True:
        act = input("Please select an item from the menu -> ")
        if act in action_list:
            break
        else:
            print("Please select an item from the menu.\nTo exit, please press enter.")
    return act


print("Press <1> to convert meters to miles.")
print("Press <2> to convert meters to inches.")
print("Press <3> to convert meters to yards.")

meters = input_metr()
print(meters)
