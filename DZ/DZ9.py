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
    count = 1
    with open(name_of_file, "r", newline="") as file:
        reader = csv.DictReader(file)
        print('+', '-' * 3, '+', '-' * 15, '+', '-' * 25, '+', '-' * 3, '+', '-' * 11, '+', sep="")
        print(
            f'|', "Num".center(3),
            f'|', "Name".center(15),
            f'|', "Surname".center(25),
            f'|', "Age".center(3),
            f'|', "Job title".center(11), "|", sep=""
              )
        print('+', '-' * 3, '+', '-' * 15, '+', '-' * 25, '+', '-' * 3, '+', '-' * 11, '+', sep="")
        for row in reader:
            print(
                f'|', str(count).center(3),
                f'|', row["name"].center(15),
                f'|', row["surname"].center(25),
                f'|', row["age"].center(3),
                f'|', row["job title"].center(11), "|", sep=""
            )
            count += 1
        print('+', '-' * 3, '+', '-' * 15, '+', '-' * 25, '+', '-' * 3, '+', '-' * 11, '+', sep="")


def add_employee(name_of_file):
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
    with open(name_of_file, "a", newline="") as file:
        columns = ["name", "surname", "age", "job title"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerow(new_user)


def edit_employee(name_of_file):
    print_open_file(name_of_file)
    edit_list = []
    with open(name_of_file, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            edit_list.append(row)
    while True:
        need_num = input("To edit, please, enter the num of employee.\nTo exit, press Enter.")
        if need_num == "":
            break
        if int(need_num) in range(1, len(edit_list) + 1):
            for key in edit_list[int(need_num) - 1]:
                print(f"Editing - {key}, current value - {edit_list[int(need_num) - 1][key]}."
                      f"To cancel editing, press enter.")
                new_value = input("Enter a new value -> ")
                if new_value == "":
                    pass
                else:
                    edit_list[int(need_num) - 1][key] = new_value
            print("The data was changed successfully.")
            break
        else:
            print("The specified number is not available.")
    with open("new_employees.csv", "w", newline="") as file:
        columns = ["name", "surname", "age", "job title"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(edit_list)


def del_employee(name_of_file):
    print_open_file(name_of_file)
    edit_list = []
    with open(name_of_file, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            edit_list.append(row)
    while True:
        del_num = input("Please, choose the num of employee, what need to remove.\nTo exit, press Enter.")
        if del_num == "":
            break
        if int(del_num) in range(1, len(edit_list) + 1):
            edit_list.pop(int(del_num) -1)
            break
        else:
            print("The specified number is not available.")
    with open("new_employees.csv", "w", newline="") as file:
        columns = ["name", "surname", "age", "job title"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(edit_list)


def search_employee():
    pass


def display_employees():
    pass


edit_list = [
        {"name": "Maksim", "surname": "Bychkov", "age": 38, "job title": "Director"},
        {"name": "Yuri", "surname": "Gun", "age": 38, "job title": "Manager"},
        {"name": "Slava", "surname": "Galagan", "age": 39, "job title": "Сourier"},
    ]

FILENAME = "new_employees.csv"
# edit_employee(FILENAME)
# print_open_file(FILENAME)
del_employee(FILENAME)

