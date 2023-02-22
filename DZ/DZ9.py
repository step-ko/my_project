import csv
from os import system, name


clean_list = [{"name": "", "surname": "", "age": 0, "": ""}]


def clear():
    if name == 'nt':    # for windows
        _ = system('cls')
    else:    # for mac and linux(here, os.name is 'posix')
        _ = system('clear')


def new_file(list_users):
    new_name = input("Enter a name for the new file with the CSV extension.")
    with open(new_name, "w", newline="") as file:
        columns = ["name", "surname", "age", "job title"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(list_users)
    return name


def open_file() -> str:
    while True:
        try:
            filename = input("Please specify a file to open (for example: new_employees.csv) -> ")
            if filename == "":
                new_file(clean_list)
            with open(filename, "r", newline="") as file:
                break

        except FileNotFoundError:
            print("File not found. Сheck the filename or create a new file.")
    return filename


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


def print_list(some_list):
    count = 1
    print('+', '-' * 3, '+', '-' * 15, '+', '-' * 25, '+', '-' * 3, '+', '-' * 11, '+', sep="")
    print(
        f'|', "Num".center(3),
        f'|', "Name".center(15),
        f'|', "Surname".center(25),
        f'|', "Age".center(3),
        f'|', "Job title".center(11), "|", sep=""
    )
    print('+', '-' * 3, '+', '-' * 15, '+', '-' * 25, '+', '-' * 3, '+', '-' * 11, '+', sep="")
    for employee in some_list:
        print(
            f'|', str(count).center(3),
            f'|', employee["name"].center(15),
            f'|', employee["surname"].center(25),
            f'|', str(employee["age"]).center(3),
            f'|', employee["job title"].center(11), "|", sep=""
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


def display_employees(name_of_file):
    action = int(input(f"Please choose one of the options below:\n"
                       f"Press <1> to display information about all employees.\n"
                       f"Press <2> to display information about employees of the specified age.\n"
                       f"Press <3> to display information about employees whose last name begins "
                       f"with the specified letter\n"
                       f" - > \n"))
    if action in range(1, 4) and action == 1:
        print_open_file(name_of_file)
        for_continue = input("For continue press enter -> ")

    elif action in range(1, 4) and action == 2:
        need_age = input("Please, enter the age for the search ->")
        result_list = []
        with open(name_of_file, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["age"] == need_age:
                    result_list.append(row)
        if len(result_list) == 0:
            print(f"No employees under the age of {need_age} years were found.")
            for_continue = input("For continue press enter -> ")
        elif len(result_list) > 0:
            print(f"{len(result_list)} employees in age {need_age} years were found.")
            print_list(result_list)
            act = input("Would you like to save your search results? \n"
                        "Press <Y>  to save - any value to cancel ->")
            if act.upper() == "Y":
                new_file(result_list)

    elif action in range(1, 4) and action == 3:
        need_letters = input("Please, enter first letters for the search ->")
        result_list = []
        with open(name_of_file, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if (row["surname"][0:len(need_letters)]).upper() == need_letters.upper():
                    result_list.append(row)
        if len(result_list) == 0:
            print("Nothing found.")
            for_continue = input("For continue press enter -> ")
        elif len(result_list) > 0:
            print(f"Found {len(result_list)} employees with entered letters ({need_letters}) in the surname.")
            print_list(result_list)
            act = input("Would you like to save your search results? \n"
                        "Press <Y>  to save - any value to cancel ->")
            if act.upper() == "Y":
                new_file(result_list)


def show_menu():
    print(
        f"Menu:".center(55), "\n",
        f"*" * 55, "\n",
        f"Press <1> to enter the data of the new employee.", "\n",
        f"Press <2> to change the data of the employee.", "\n",
        f"Press <3> to to remove the employee.", "\n",
        f"Press <4> to display information the new employees.", "\n"
        f"Press <9> to exit the program.", "\n",
        f"*" * 55, sep=""
    )


menu_item = ""
need_file = open_file()

while menu_item != "9":
    show_menu()
    menu_item = input("Please select a menu item -> ")
    if menu_item == "1":
        add_employee(need_file)
    elif menu_item == "2":
        edit_employee(need_file)
    elif menu_item == "3":
        del_employee(need_file)
    elif menu_item == "4":
        display_employees(need_file)
    elif menu_item == "9":
        print("GOODBYE.")
        break
    clear()

