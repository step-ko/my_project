
from os import system, name

"""Задание 2 Написать программу «книги». 
Создать два спискас данными. Один список хранит названия книг, 
второй — годы выпуска. 
Реализовать меню для пользователя:
■■ Отсортировать по названию книг;
■■ Отсортировать по годам выпуска;
■■ Вывести список книг с названиями и годами выпуска;
■■ Выход;
"""


def sort_lists(list_1: list[int], list_2: list[int], chose_list: int) -> tuple[list[int], list[int]]:
    if chose_list == "1":
        master_list, slave_list = list_1, list_2
    else:
        master_list, slave_list = list_2, list_1
    for i in range(len(master_list)):
        swapped = False
        for j in range(0, len(master_list) - i - 1):
            if master_list[j] > master_list[j + 1]:
                master_list[j], master_list[j + 1] = master_list[j + 1], master_list[j]
                slave_list[j], slave_list[j + 1] = slave_list[j + 1], slave_list[j]
                swapped = True
        if not swapped:
            break
    if chose_list == "1":

        result = (master_list, slave_list)
    else:
        result = (slave_list, master_list)
    return result


def show_lists(list_1: list[int], list_2: list[int]):
    print("+", "-" * 12, "+", "-" * 40, sep="")
    print("|", "Graduation".center(12), "|", "Book".center(14), sep="")
    print("|", "year".center(12), "|", "title".center(14), sep="")
    print("+", "-" * 12, "+", "-" * 55, sep="")
    for item in range(len(list_1)):
        print(f""
              f"|",
              f"{list_1[item]}".center(12), "|",
              f"{list_2[item]}".ljust(55), sep="")
    print("+", "-" * 12, "+", "-" * 55, sep="")


def chose_menu_item() -> str:
    while True:
        menu_list = ["1", "2", "3", "5"]
        menu_item = input("Please, choose the item from menu - > ".center(55))
        if menu_item in menu_list:
            return menu_item
            break
        else:
            print("You made a mistake. Be more careful..".center(55))


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def menu():
    while True:
        print(f"Menu:".center(55), "\n",
              f"-" * 55, "\n",
              f"<1> - to sort by graduation_year.".center(55), "\n",
              f"<2> - to sort by book title.".center(55), "\n",
              f"<3> - displaying of lists.".center(55), "\n",
              f"...".center(55), "\n",
              f"<5> - to exit.".center(55), "\n",
              f"-" * 55, "\n", sep="")

        act = chose_menu_item()
        if act == "1":
            print(graduation_year, "- original graduation year list.")
            sort_lists(graduation_year, book_title, act)
            print(graduation_year, "- sorted list.")
            stop = input("To Continue, press enter -> ")
            clear()
        elif act == "2":
            print("\nBefore sorting.")
            for book in book_title:
                print(book)
            sort_lists(graduation_year, book_title, act)
            print("\nAfter sorting.")
            for book in book_title:
                print(book)
            stop = input("To Continue, press enter -> ")
            clear()
        elif act == "3":
            show_lists(graduation_year, book_title)
            stop = input("To Continue, press enter -> ")
            clear()
        elif act == "5":
            print("Goodbye :) ")
            break


graduation_year = ["2021", "2021", "2022", "2022", "2020", "2023"]
book_title = ["Початківці. Чому вчитися нового ніколи не пізно",
              "A Handbook for New Stoics: How to Thrive in a World Out of Your Control—52 Week-by-Week Lessons "
              "by Massimo Pigliucci, Gregory Lopez",
              "Stolen Focus. Why You Can't Pay Attention by Johann Hari",
              "Feeling & Knowing: Making Minds Conscious by António Damásio",
              "Churchill and Orwell: The Fight for Freedom by Thomas E. Ricks",
              "За лаштунками війни. Сталін, нацисти і Захід, Лоренс Ріс."]

menu()
