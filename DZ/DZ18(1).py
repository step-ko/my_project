
from os import system, name

"""Задание 1 Написать программу «справочник».
Создать два списка целых. Один список хранит идентификационные коды,
второй — телефонные номера. Реализовать меню для пользователя:
■■ Отсортировать по идентификационным кодам;
■■ Отсортировать по номерам телефона;
■■ Вывести список пользователей с кодами и телефонами;
■■ Выход.
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
    print("+", "-" * 12, "+", "-" * 14, "+", sep="")
    print("|", "INN".center(12), "|", "PHONE NUMBER".center(14), "|", sep="")
    print("+", "-" * 12, "+", "-" * 14, "+", sep="")
    for item in range(len(list_1)):
        print(f""
              f"|",
              f"{list_1[item]}".center(12), "|",
              f"{list_2[item]}".center(14), "|", sep="")
    print("+", "-" * 12, "+", "-" * 14, "+", sep="")


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


inn_list = [1111111111, 2222222222, 3333333333, 1234567890, 2345678901, 1256789091]
phone_list = [380979797777, 380636336333, 380663322555, 380631252255, 380731253577, 380993357722]

while True:
    print(f"Menu:".center(55), "\n",
          f"@" * 55, "\n",
          f"<1> - to sort by INN.".center(55), "\n",
          f"<2> - to sort by phone number.".center(55), "\n",
          f"<3> - displaying of lists.".center(55), "\n",
          f"...".center(55), "\n",
          f"<5> - to exit.".center(55), sep="")
    act = chose_menu_item()
    if act == "1":
        print(inn_list, "- original INN list.")
        sort_lists(inn_list, phone_list, act)
        print(inn_list, "- sorted list.")
        stop = input("To Continue, press enter -> ")
        clear()
    elif act == "2":
        print(phone_list, "- original phone list.")
        sort_lists(inn_list, phone_list, act)
        print(phone_list, "- sorted phone list.")
        stop = input("To Continue, press enter -> ")
        clear()
    elif act == "3":
        show_lists(inn_list, phone_list)
        stop = input("To Continue, press enter -> ")
        clear()
    elif act == "5":
        print("Goodbye :) ")
        break
