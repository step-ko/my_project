import random
# from random import randint

# Создать генератором список их 10 чисел от -10 до 10
# вторым генератором получить все четные положительные значения из первого списка

random_list = [random.randint(-10, 10) for i in range(10)]
print(random_list, "- список их 10 чисел от -10 до 10")
result_list = [i for i in random_list if i > 0 and i % 2 == 0]
print(result_list, " - все четные положительные значения из первого списка")



