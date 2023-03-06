# Задание 1:
# Создайте класс «Город».Необходимо хранить в полях  класса: название города, название региона, название страны,
# количество жителей в городе, почтовый индекс города, телефонный код города.Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

class City:
    def __init__(self, city_name, region, country, people, zip_code, city_code):
        self.__city_name = city_name
        self.__region = region
        self.__country = country
        self.__people = people
        self.__zip_code = zip_code
        self.__phone_code = city_code

    def input_data(self):
        self.city_name = input("Введите название города -> ")
        self.region = input("Введите название региона -> ")
        self.country = input("Введите название страны -> ")
        self.people = int(input("Укажите количество жителей в городе -> "))
        self.zip_code = input("Введите почтовый индекс города -> ")
        self.phone_code = input("Телефонный код города -> ")

    def output_data(self):
        print("Название города:", self.city_name)
        print("Регион:", self.region)
        print("Страна:", self.country)
        print("Количество жителей:", self.people)
        print("Почтовый индекс:", self.zip_code)
        print("Телефонный код города:", self.phone_code)

    @property
    def city_name(self):
        return self.__city_name

    @city_name.setter
    def city_name(self, city_name):
        if 2 < len(city_name) < 56:
            self.__city_name = city_name
        else:
            print("Недопустимое название города.")

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if 2 < len(region) < 56:
            self.__region = region
        else:
            print("Недопустимое название региона.")

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        if 2 < len(country) < 56:
            self.__country = country
        else:
            print("Недопустимое название страны.")

    @property
    def people(self):
        return self.__people

    @people.setter
    def people(self, people):
        if 1000000 < people < 10000000:
            self.__people = people
        else:
            print("Не корректно введено количество жителей в городе.")

    @property
    def zip_code(self):
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        if len(zip_code) == 5:
            self.__zip_code = zip_code
        else:
            print("Не корректно введен почтовый индекс города.")

    @property
    def phone_code(self):
        return self.__phone_code

    @phone_code.setter
    def phone_code(self, phone_code):
        if 2 < len(phone_code) < 4:
            self.__phone_code = phone_code
        else:
            print("Не корректно введен телефонный код города.")


data = ["Kyiv", "Kyiv", "Ukraine", "3.65 млн.", "01001", "044"]
city1 = City("Kyiv", "Kyiv", "Ukraine", "3.65 млн.", "01001", "044")
print(city1.__dict__)
city1.city_name = "1"
print(city1.city_name)
city1.city_name = "Brovaru"
print(city1.city_name)



# Задание 2:
# Создайте класс «Страна».Необходимо хранить в полях класса: название страны, название континента, количество
# жителей в стране, телефонный код страны, название столицы, название городов страны.Реализуйте методы класса для
# ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

