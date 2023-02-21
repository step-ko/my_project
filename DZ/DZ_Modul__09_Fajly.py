import csv
import shelve

# employees1.csv
"""Задание 1 Напишите информационную систему «Сотрудники».
Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск
сотрудника по фамилии, вывод информации обо всех сотрудниках, указанного возраста, или фамилия которых
начинается на указанную букву.
Организуйте возможность сохранения найденной информации в файл.
Также весь список сотрудников сохраняется в файл (при выходе из программы — автоматически, в процессе исполнения
программы — по команде пользователя).
При старте программы происходит загрузка списка сотрудников из указанного пользователем файла.
"""

FILENAME = "employees.csv"

employees = [
    ["Maks", 38],
    ["Yuri", 38],
    ["Petr", 36]
]

with open(FILENAME, 'w', newline="",) as file:
    writer = csv.writer(file)
    writer.writerows(employees)

with open(FILENAME, 'a', newline="") as file:
    user = ("Slava", 37)
    writer = csv.writer(file)
    writer.writerow(user)

with open(FILENAME, 'r', newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], " - ", row[1])

# FILENAME1 = "employees2.csv"
#
# employees1 = [
#     {"name": "Maks", "age": 38},
#     {"name": "Yuri", "age": 38},
#     {"name": "Petr", "age": 36}
# ]
#
# with open(FILENAME1, "w", newline="") as file:
#     columns = ["name", "age"]
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()
#     writer.writerows(employees1)
#
# with open(FILENAME1, "r", newline="") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["name"], " - ", row["age"])
