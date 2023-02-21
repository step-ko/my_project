import random

"""
- Создать игру угадай число используя бинарный поиск.
  Игрок загадывает число, пк отгадывает. Вывести кол-во попыток.
- Создать игру угадай число в которой пк будет отгадывать число загаданное игроком.
"""

min_value1, max_value1, count = 0, 100, 0


def input_number() -> int:
    while True:
        try:
            number = int(input("Name any number from 1 to 100 -> "))
            if 0 < number < 101:
                break
        except ValueError:
            print("Error. Try again.")
    return number


print("Welcome to the game - Guess the Number !")
secret_number = input_number()
while True:
    count += 1
    guessed_number = (min_value1 + max_value1) // 2
    if secret_number == guessed_number:
        print(f"Your number is {guessed_number}, i was able to guess it in {count} tries")
        break
    elif secret_number < guessed_number:
        max_value1 = guessed_number - 1
    else:
        min_value1 = guessed_number + 1
