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


def input_number() -> int:
    while True:
        try:
            number = float(input("Please enter any number ->"))
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
    number = sum(list_number) / len(list_number)
    return number

num1, num2, num3, action = input_number(), input_number(), input_number(), 0


while action == "":


