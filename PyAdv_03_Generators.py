from typing import Generator


def simple_generator(n: int) -> Generator[int, None, None]:
    for i in range(n):
        yield i


# Usage
for value in simple_generator(5):
    print(value)


def infinite_range(start: int = 0) -> Generator[int, None, None]:
    current = start
    while True:
        yield current
        current += 1


# Usage
counter = 0
for value in infinite_range(10):
    print(value)
    counter += 1
    if counter == 5:
        break


def count_up_to(x: int) -> Generator[int, None, None]:
    count = 1
    while count <= x:
        yield count
        count += 1


for number in count_up_to(5):
    print(number)

# **************************************************************************************
# EXERCISE  1
# Write a Python program to create a generator that generates the squares of numbers up
# to a given number.
# **************************************************************************************
from typing import Generator


def generate_squares(n: int) -> Generator[int, None, None]:
    for i in range(1, n + 1):
        yield i ** 2


n = 5
print('Squares of numbers up to', n, ':')
for square in generate_squares(n):
    print(square)

# **************************************************************************************
# EXERCISE  2
# Write a Python program to create a generator that yields "n" random numbers between a
# low and high number that are inputs.
# **************************************************************************************
from typing import Generator
import random


def generate_random_numbers(n: int, low: int, high: int) -> Generator[int, None, None]:
    for _ in range(n):
        yield random.randint(low, high)


n = int(input('Enter n:'))
low = int(input('Enter low:'))
high = int(input('Enter high:'))
random_numbers_generator = generate_random_numbers(n, low, high)

print(f'{n} random numbers between {low} and {high}:')
for num in random_numbers_generator:
    print(num)

# **************************************************************************************
# EXERCISE  3
# Write a Python program to create a generator that iterates over a string.
# **************************************************************************************
from typing import Generator


def iterate_string(string: str) -> Generator[int, None, None]:
    for i in string:
        yield i


string = input('Enter a string: ')
for word in iterate_string(string):
    print(word)

# **************************************************************************************
# EXERCISE  4
# Write a Python program to create a Fibonacci series generator.
# **************************************************************************************


# **************************************************************************************
# EXERCISE  5
# Write a Python program to create a generator from a list that yields item from the
# list if it is a number.
# **************************************************************************************
from typing import Generator


def list_generator(lst: list) -> Generator[int, None, None]:
    for i in lst:
        if isinstance(i, int):
            yield i


lst = [1, 2, 3, 'John', 7, None]
for i in list_generator(lst):
    print(i)

# **************************************************************************************
# EXERCISE  6
# Create a list of tuples, each representing a person's information. Each tuple contains
# the following information: (name: str, age: int, city: str, salary: float). Your task
# is to create Python generators to perform the following tasks:
#
# Filtering Generator: Create a generator function that filters the people who are below
# a certain age threshold.
# Mapping Generator: Create a generator function that maps the names of people to uppercase.
# Aggregation Generator: Create a generator function that calculates the average salary
# of the selected group.
# **************************************************************************************
from typing import Generator


def filtering_generator(people: list, threshold: int) -> Generator[int, None, None]:
    for person in people:
        if person[1] < threshold:
            yield person


def mapping_generator(people: list) -> Generator[int, None, None]:
    names = [person[0] for person in people]
    for name in names:
        yield name.upper()


def aggregation_generator(people: list) -> Generator[float, None, None]:
    salaries = [person[3] for person in people]
    av_salary = sum(salaries) / len(salaries)
    yield av_salary


people = [('John', 30, 'New York', 4500.5), ('Alice', 25, 'Los Angeles', 2700.0), ('Mark', 35, 'Boston', 3700.8),
         ('Emily', 41, 'San Francisco', 6500.0)]


for person in mapping_generator(people):
    print(person)

for person in filtering_generator(people, 30):
    print(person)

for avg_salary in aggregation_generator(people):
    print('Average salary:', avg_salary)