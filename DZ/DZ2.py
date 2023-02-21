import random

"""
- Создать игру угадай число используя бинарный поиск.
  Игрок загадывает число, пк отгадывает. Вывести кол-во попыток.
- Создать игру угадай число в которой пк будет отгадывать число загаданное игроком.
"""

min_value2, max_value2, count = 0, 100, 0


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
    guessed_number = (min_value2 + max_value2) // 2
    if secret_number == guessed_number:
        print(f"Your number is {guessed_number}, i was able to guess it in {count} tries")
        break
    elif secret_number < guessed_number:
        max_value2 = guessed_number - 1
    else:
        min_value2 = guessed_number + 1


def input_guess() -> int:
    while True:
        try:
            number = int(input("Enter any number from 1 to 100 -> "))
            if 0 <= number <= 100:
                break
        except ValueError:
            print("Error. Try again.")
    return number


print("Welcome to the game - Guess the Number!")
print("I will choose a number from 1 to 100 and you have to guess it.")
secret_number = random.randint(0, 101)

guesses, count = [], 0

while True:
    count += 1
    guess = input_guess()
    if guess in guesses:
        print("You have already entered this number, try another one.")
    else:
        guesses.append(guess)
        if guess == secret_number:
            print(f"<<<Congratulations!!!>>> \nYou guessed the number {secret_number} in {count} tries")
            break
        else:
            if guess > secret_number:
                hint = "less"
            elif guess < secret_number:
                hint = "more"
            print(f"Attempt {count}. Sorry, but you're wrong. My number is {hint}.Try again.\n"
                  f"\t\tThe previously indicated numbers - {guesses}.")
