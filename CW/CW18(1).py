import random


def binary_search(nums, item):
    start, end = 0, len(nums) - 1

    while start <= end:
        middle = (start + end) // 2
        if nums[middle] == item:
            return middle
        elif item < nums[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1


def binary_search_recursive(nums, item, start, end):
    if start <= end:
        middle = (start + end) // 2

        if nums[middle] == item:
            return middle
        elif item < nums[middle]:
            return binary_search_recursive(nums, item, start, middle - 1)
        else:
            return binary_search_recursive(nums, item, middle + 1, end)
    return -1


numbers = [random.randint(1, 10) for i in range(10)]
print(numbers)
numbers.sort()
print(numbers)

search_value = 3
print(binary_search(numbers, search_value))
print(binary_search_recursive(numbers, search_value, 0, len(numbers) - 1))