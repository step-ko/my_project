import re


# Написать валидации с помощью регулярных выражений:
# - мобильный номер телефона (только цифры, возможное наличие плюса, длина номера)
# - домашний номер телефона (только цифры и длина номера)
# - email (наличие @, домена: gmail.com например, минимальная длина и максимальная на ваш выбор)
# - ФИО клиента (3 слова, минимальная длина 2 символа, максимальная длина 20)
# - Пароль (минимально: одна большая буква, одна маленькая буква, одна цифра, один символ,
# длина пароля - от 8 до 16 символов)

print("mob_number_validator".center(55), "\n", "-" * 55)
mob_number_validator = re.compile(r"^([+]?38)?(38)?(8)?((0)+([0-9]{9}))+$")
variant_list = ["+380731234567", "380731234567", "80731234567", "+38073123456", "+480731234567", "+80731234567", "90731234567", "0731234567", "073123456"]
print(variant_list)
for var in variant_list:
    print(mob_number_validator.match(var))
print("-" * 55, "\n")

print("home_number_validator".center(55), "\n", "-" * 55)
home_number_validator = re.compile(r"^\d{10,15}$")
variant_list = ["06556659910911", "3379339910911", "123456", "02", "Admin0636248560", "3373870"]
for var in variant_list:
    print(home_number_validator.match(var))
print("-" * 55, "\n")

print("mail_validator".center(55), "\n", "-" * 55)
mail_validator = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$")
variant_list = ["admin@i.ua", "sobaka@mail.ru", "125.gmail@com", "125@i.ua", "Jhon@Ivanov", "@12345689.com.ua"]
print(variant_list)
for var in variant_list:
    print(mail_validator.match(var))
print("-" * 55, "\n")

print("full_name_validator".center(55), "\n", "-" * 55)
full_name_validator = re.compile(r"^[a-zA-Zа-яА-Я]{2,20}\s[a-zA-Zа-яА-Я]{2,20}\s[a-zA-Zа-яА-Я]{2,20}$")
variant_list = ["Иванов Иван Иванович", "Иванов Иван", "Иван", "Пётр 1", "Admin Jhon Ivanov", "12345689"]
print(variant_list)
for var in variant_list:
    print(full_name_validator.match(var))
print("-" * 55, "\n")

print("password_validator".center(55), "\n", "-" * 55)
password_validator = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z]).{8,16}$")
variant_list = ["Passw0rd*", "Admin123!", "admin123!", "!Admin123", "Admin123", "Admin"]
print(variant_list)
for var in variant_list:
    print(password_validator.match(var))
print("-" * 55, "\n")
