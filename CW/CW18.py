import random

# Написать игру "угадай число" используя рекурсивный бинарный поиск
# Дописать игру со словами: добавить считывание слов с файла, возможность добавить слова в файл с клавиатуры


def binary_search(guess, low, high, answer):
    if low <= high:
        mid = (low + high) // 2
        if guess[mid] == answer:
            return mid
        elif guess[mid] < answer:
            return binary_search(guess, mid+1, high, answer)
        else:
            return binary_search(guess, low, mid-1, answer)
    else:
        return -1


def game(low, high):
    answer = random.randint(low, high)
    guess = [i for i in range(low, high+1)]
    tries = 0
    while True:
        user_guess = int(input("Угадайте число между {} и {}: ".format(low, high)))
        tries += 1
        result = binary_search(guess, low-1, high-1, user_guess)
        if result == -1:
            print("Неправильный ответ")
        elif guess[result] == answer:
            print("Вы угадали число {} за {} попыток".format(answer, tries))
            break
        elif guess[result] < answer:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")


n1, n2 = 1, 100
game(n1, n2)

