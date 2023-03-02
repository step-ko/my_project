###########
import math
import random
# from random import *
# from random import randint, choice

# print(random.randint(1, 100))  # от 1 до 100
# print(random.random())
# print(random.choice("qwerty"))
# print(random.randrange(10))  # от нуля до 9
# print(random.randrange(2, 10))  # от 2 до 9
# print(random.randrange(2, 10, 2))  # от 2 до 9 через один (каждый второй)
# nums = [1, 2, 3, 4, 5]
# random.shuffle(nums)  # перемешиваем значения списка
# print(nums)

###
# print(-math.inf)
# print(math.inf)
# print(math.ceil(10.2))
# print(math.floor(10.2))
# print(math.factorial(5))
# print(math.pow(2, 3))
# print(math.sqrt(9))

####
# decimal
# from decimal import *
#
# number = 0.1 + 0.1 + 0.1
# print(number)
# number = Decimal("0.1")
# number = number + number + number
# print(number)
#
# number = Decimal("0.333")
# number = number.quantize(Decimal("1.00"))
# print(number)
#
# number = Decimal("0.333")
# number = number.quantize(Decimal("1.0000"))
# print(number)
#
# number = Decimal("12.123456789")
# number = number.quantize(Decimal("1.000"))
# print(number)
#
# number = Decimal("12.5555")
# number = number.quantize(Decimal("1.000"))
# print(number)
#
# number = Decimal("12.9999")
# number = number.quantize(Decimal("1.000"))
# print(number)
#
# number = Decimal("12.025")
# number = number.quantize(Decimal("1.00"), ROUND_HALF_EVEN)
# print(number)
#
# number = Decimal("12.035")
# number = number.quantize(Decimal("1.00"), ROUND_HALF_EVEN)
# print(number)

###
# datetime
import datetime
import time

# print(datetime.date.today())
# print(datetime.date(2022, 11, 10))
# print(datetime.time())
# print(datetime.time(10, 13, 15))
# print(datetime.time(10, 13))
#
# print(datetime.datetime.now())
# dt_now = datetime.datetime.now()
# print(f"{dt_now.day}/{dt_now.month}/{dt_now.year} {dt_now.hour}:{dt_now.minute}:{dt_now.second}:{dt_now.microsecond}")
#
# print(datetime.datetime)
#
# my_date = datetime.datetime.strptime("12/03/2020", "%d/%m/%Y")
# print(my_date)

# while True:
#     print(datetime.datetime.now())
#     time.sleep(1)

# https://www.programiz.com/python-programming/datetime/strftime

# from datetime import datetime, timezone, timedelta
#
# # naive
# naive = datetime.now()
# print("Naive DateTime:", naive)
#
# # UTC aware
# UTC = datetime.now(timezone.utc)
# print("UTC DateTime", UTC)
#
# # Creating a datetime with JST (Japan) TimeZone
# jst_dateTime = datetime.now(timezone(timedelta(hours=+9), 'JST'))
# print("In JST::", jst_dateTime)

####
from random import *

# nums = [input("Enter number: ") for i in range(3)]
# print(nums)

# генератор списка
# nums = [randint(1, 10) for i in range(10)]
# print(nums)
#
# nums = [i for i in nums if i % 2 == 0]
# print(nums)
#
# numbers = [-3, -2, -1, 0, 1, 2, 3]
# positive_numbers = [n for n in numbers if n > 0]
#
# numbers = [-3, -2, -1, 0, 1, 2, 3]
# new_numbers = [n * 2 for n in numbers]
#
# numbers = [-3, -2, -1, 0, 1, 2, 3]
# new_numbers = [n * 2 if n > 0 else n for n in numbers]
#
# # генератор словаря
# my_dict = {i: i**2 for i in range(10)}
# print(my_dict)
#
# dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
# words = [f"{key}: {dictionary[key]}" for key in dictionary if len(key) > 3]
#
# # генератор множества
# my_set = {i for i in range(10)}
# print(my_set)

# Генераторы. Генератор - это объект, который сразу при создании не вычисляет значения всех своих элементов
generator = (i for i in range(3))
# print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))  # error: StopIteration
# дополнительные методы:
# close() - остановить выполнение генератора
# throw() - генератор бросит исключение
# send() - отправить значение генератору

# for i in generator:
#     print(i)


#############
# def create_generator():
#     num = 1
#     while True:
#         yield num ** 2
#         num += 1
#
#
# gen1 = create_generator()
#
# try:
#     for i in gen1:
#         print(i)
#         if i > 10:
#             # gen1.close()
#             gen1.throw(Exception("Finish!"))
# except Exception as ex:
#     print(ex)

####
# \d — соответствует любой одной цифре и заменяет собой выражение [0-9];
# \D — исключает все цифры и заменяет [^0-9];
# \w — заменяет любую цифру, букву, а также знак нижнего подчёркивания;
# \W — любой символ кроме латиницы, цифр или нижнего подчёркивания;
# \s — соответствует любому пробельному символу;
# \S — описывает любой непробельный символ.
#
#
# .	Один любой символ, кроме новой строки \n.
# ?	0 или 1 вхождение шаблона слева
# +	1 и более вхождений шаблона слева
# *	0 и более вхождений шаблона слева
# \w	Любая цифра или буква (\W — все, кроме буквы или цифры)
# \d	Любая цифра [0-9] (\D — все, кроме цифры)
# \s	Любой пробельный символ (\S — любой непробельный символ)
# \b	Граница слова
# [..]	Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
# \	Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)
# ^ и $	Начало и конец строки соответственно
# {n,m}	От n до m вхождений ({,m} — от 0 до m)
# a|b	Соответствует a или b
# ()	Группирует выражение и возвращает найденный текст
# \t, \n, \r	Символ табуляции, новой строки и возврата каретки соответственно
#
# Для чего используются регулярные выражения
# для определения нужного формата, например телефонного номера или email-адреса;
# для разбивки строк на подстроки;
# для поиска, замены и извлечения символов;
# для быстрого выполнения нетривиальных операций.
#
# А вот наиболее популярные методы, которые предоставляет модуль:
#
# re.match() - Этот метод ищет по заданному шаблону в начале строки
# re.search() - Метод похож на match(), но ищет не только в начале строки
# re.findall() - Возвращает список всех найденных совпадений. У метода findall() нет ограничений на поиск в начале или конце строки.
# re.split() - Этот метод разделяет строку по заданному шаблону
# re.sub() - Ищет шаблон в строке и заменяет его на указанную подстроку. Если шаблон не найден, строка остается неизменной
# re.compile() - Мы можем собрать регулярное выражение в отдельный объект, который может быть использован для поиска. Это также избавляет от переписывания одного и того же выражения.


import re
# result = re.match(r'he', 'hello world hello')
# print(result)
# print(result.group(0))

#
# result = re.search(r'world', 'hello world hello')
# print(result.start())
# print(result.end())

#
# result = re.findall(r'he', 'hello world hello')
# print(result)

#
# result = re.split(r'l', 'hello world hello', maxsplit=1)
# print(result)
#
# result = re.split(r'l', 'hello world hello')
# print(result)

#
# pattern = re.compile('hello')
# result = pattern.findall('hello world hello')
# print(result)

##
result = re.findall(r'.', "It is a long established fact that a reader")
print(result)

result = re.findall(r'\w', "It is a long established fact that a reader")
print(result)

result = re.findall(r'\w*', "It is a long established fact that a reader")
print(result)

result = re.findall(r'\w+', "It is a long established fact that a reader")
print(result)

result = re.findall(r'\w+$', "It is a long established fact that a reader")
print(result)

result = re.findall(r'^\w+', "It is a long established fact that a reader")
print(result)

result = re.findall(r'\w\w', "It is a long established fact that a reader")
print(result)

result = re.findall(r'\b\w', "It is a long established fact that a reader")
print(result)

result = re.findall(r'@\w+.\w+', "test1@gmail.com, test2@qqq.com, test3@www.com")
print(result)

result = re.findall(r'@\w+.(\w+)', "test1@gmail.com, test2@qqq.ua, test3@www.com")
print(result)

result = re.findall(r'\d{2}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2004')
print(result)

li = ['9999999999', '999999-999', '99999x9999']

for val in li:
    if re.match(r'[8-9]{1}[0-9]{9}', val) and len(val) == 10:
        print('yes')
    else:
        print('no')