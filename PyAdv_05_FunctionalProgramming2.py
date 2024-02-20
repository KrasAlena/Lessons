# MAP
animals = ["cat", "dog", "hedgehog", "gecko"]
iterator = map(lambda s: s[::-1], animals)
list(iterator)
# ['tac', 'god', 'gohegdeh', 'okceg']

# FILTER
list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def is_even(x):
    return x % 2 == 0

list(filter(is_even, range(10)))
# [0, 2, 4, 6, 8]

list(filter(lambda x: x % 2 == 0, range(10)))
# [0, 2, 4, 6, 8]

# REDUCE
def multiply(x, y):
    return x * y


def factorial(n):
    from functools import reduce
    return reduce(multiply, range(1, n + 1))


factorial(4)  # 1 * 2 * 3 * 4

factorial(6)  # 1 * 2 * 3 * 4 * 5 * 6

# **************************************************************************************
# EXERCISE 1
# Write a Python program to triple all numbers of a given list of integers.
# Use Python map()
# **************************************************************************************
list(map(lambda item: item * 3, [1, 2, 3, 4]))

# **************************************************************************************
# EXERCISE 2
# Write a Python program to square the elements of a list using map() function.
# **************************************************************************************
list(map(lambda item: item ** 2, [1, 2, 3, 4]))

# **************************************************************************************
# EXERCISE 3
# Write a Python program to add three given lists using Python map and lambda
# **************************************************************************************
list(map(lambda a, b, c: a + b + c, [1, 2, 3], [10, 20, 30], [100, 200, 300]))

# **************************************************************************************
# EXERCISE 4
# Write a Python program to add two given lists and find the difference between lists.
# Use map() function.
# **************************************************************************************
list(map(lambda a, b: (a + b, a - b), [100, 200, 300], [10, 20, 30]))

lst1 = [100, 200, 300]
lst2 = [10, 20, 30]

sum_result = list(map(lambda x, y: x + y, lst1, lst2))
diff_result = list(map(lambda x, y: x - y, lst1, lst2))

# **************************************************************************************
# EXERCISE 5
# Write a Python program to convert a given list of integers and a tuple of integers in
# a list of strings.
# **************************************************************************************
str_list = list(map(str, [1, 2, 3, 4]))
print(str_list)

# **************************************************************************************
# EXERCISE 6
# Write a Python program to filter a list of integers using Lambda
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Even numbers from the said list:
# [2, 4, 6, 8, 10]

# Odd numbers from the said list:
# [1, 3, 5, 7, 9]
# **************************************************************************************
list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

list(filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# **************************************************************************************
# EXERCISE 7
# Write a Python program to find numbers divisible by nineteen or thirteen from a list
# of numbers using Lambda.
# Orginal list:
# [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
#
# Numbers of the above list divisible by nineteen or thirteen:
# [19, 65, 57, 39, 152, 190]
# **************************************************************************************
list(filter(lambda x: x % 19 == 0 or x % 13 == 0, [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]))

# **************************************************************************************
# EXERCISE 8
# Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
#
# Number of even numbers in the above array: 3
# Number of odd numbers in the above array: 5
# **************************************************************************************
len(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 5, 7, 8, 9, 10])))
len(list(filter(lambda x: x % 2 != 0, [1, 2, 3, 5, 7, 8, 9, 10])))

num_even, num_odd = sum(map(lambda x: x % 2 == 0, [1, 2, 3, 5, 7, 8, 9, 10])), sum(map(lambda x: x % 2 != 0, [1, 2, 3, 5, 7, 8, 9, 10]))
print(num_even, num_odd)

# **************************************************************************************
# EXERCISE 9
# Write a python program that multiplies all the values in a given list of integers.
# **************************************************************************************
from functools import reduce
result = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(result)

# **************************************************************************************
# EXERCISE 10
# Write a python program that finds the maximum value within the given list.
# **************************************************************************************
from functools import reduce
result = reduce(lambda x, y: x if x > y else y, [1, 2, 3, 4, 5])
print(result)

# **************************************************************************************
# EXERCISE 11
# Write a python function that given list of strings concatenates all of them together.
# **************************************************************************************
from functools import reduce
result = reduce(lambda x, y: x + y, ['1', '2', '3', '4', '5'])
print(result)