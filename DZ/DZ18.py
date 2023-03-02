"""Задание 1 Написать программу «справочник».
Создать два списка целых. Один список хранит идентификационные коды,
второй — телефонные номера. Реализовать меню для пользователя:
■■ Отсортировать по идентификационным кодам;
■■ Отсортировать по номерам телефона;
■■ Вывести список пользователей с кодами и телефонами;
■■ Выход.
"""


def sort_lists(list_1: list[int], list_2: list[int], chose_list: int) -> tuple[list[int], list[int]]:
    if chose_list == 1:
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
    if chose_list == 1:
        result = (master_list, slave_list)
        print(master_list)
        print(slave_list)
    else:
        result = (slave_list, master_list)
        print(slave_list)
        print(master_list)
    return result


inn_list = [1111111111, 2222222222, 3333333333]
phone_list = [380979797777, 380636336333, 380663322555]
chose_list = 2
a, b = sort_lists(inn_list, phone_list, chose_list)
print(a)
print(b)


"""Задание 2 Написать программу «книги». 
Создать два списка с данными. Один список хранит названия книг, 
второй — годы выпуска. Реализовать меню для пользователя:
■■ Отсортировать по названию книг;
■■ Отсортировать по годам выпуска;
■■ Вывести список книг с названиями и годами выпуска;
■■ Выход;
"""
