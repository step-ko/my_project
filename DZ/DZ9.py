import csv


FILENAME1 = "employees1.csv"
employees1 = [
    {"name": "Maks", "age": 38},
    {"name": "Yuri", "age": 38},
    {"name": "Petr", "age": 36}
]
with open(FILENAME1, "w", newline="") as file:
    columns = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(employees1)
with open(FILENAME1, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], " - ", row["age"])


def open_file():
    while True:
        try:
            FILENAME = input("Please specify a file to open")
            with open(FILENAME, "r", newline="") as file:
                reader = csv.DictReader(file)
                break
        except FileNotFoundError:
            print("File not found. Сheck the filename or create a new file.")
    return FILENAME


FILENAME = open_file()
