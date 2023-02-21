import csv


def new_file(list_users):
    with open("new_employees.csv", "w", newline="") as file:
        columns = ["name", "surname", "age", "job title"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(list_users)


def open_file() -> str:
    while True:
        try:
            FILENAME = input("Please specify a file to open -> ")
            with open(FILENAME, "r", newline="") as file:
                break
        except FileNotFoundError:
            print("File not found. Сheck the filename or create a new file.")
    return FILENAME


def print_open_file(name_of_file):
    with open(name_of_file, "r", newline="") as file:
        reader = csv.DictReader(file)
        print("*" * 40)
        for row in reader:
            print(row["name"], "-", row["surname"], "-", row["age"], "-", row["job title"])
        print("*" * 40)


def add_employee():
    name = input("Please, enter name of new employee. -> ")
    surname = input(f"Please, enter surname for {name}. -> ")
    age = input(f"Please, enter age of {name}. -> ")
    job_title = input(f"Please, enter job title for {name}. -> ")
    new_user = {
        "name": name,
        "surname": surname,
        "age": age,
        "job title": job_title,
    }
    with open(open_file(), "a", newline="") as file:
        columns = ["name", "surname", "age", "job title"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerow(new_user)


def edit_employee():
    pass


def del_employee():
    list_of_employee = []
    with open(open_file(), "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            user = {row}
            list_of_employee = list_of_employee.append(user)
    print(list_of_employee)


def search_employee():
    pass


def display_employees():
    pass

employees = [
        {"name": "Maksim", "surname": "Bychkov", "age": 38, "job title": "Director"},
        {"name": "Yuri", "surname": "Gun", "age": 38, "job title": "Manager"},
        {"name": "Slava", "surname": "Galagan", "age": 39, "job title": "Сourier"},
    ]

new_file(employees)
# FILENAME = open_file()
# print_open_file("employees.csv")
# add_employee()

