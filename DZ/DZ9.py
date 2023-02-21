import csv


# FILENAME1 = "employees1.csv"
# employees1 = [
#     {"name": "Maks", "age": 38},
#     {"name": "Yuri", "age": 38},
#     {"name": "Petr", "age": 36}
# ]
# with open(FILENAME1, "w", newline="") as file:
#     columns = ["name", "age"]
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()
#     writer.writerows(employees1)


def open_file():
    while True:
        try:
            FILENAME = input("Please specify a file to open -> ")
            with open(FILENAME, "r", newline="") as file:
                break
        except FileNotFoundError:
            print("File not found. Сheck the filename or create a new file.")
    return FILENAME


def print_open_file(name_of_file):
    with open(FILENAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        print("*" * 40)
        for row in reader:
            print(row["name"], " - ", row["age"])
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
    pass


def search_employee():
    pass

FILENAME = open_file()
print_open_file(FILENAME)
add_employee()