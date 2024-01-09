#*******************************************
# List comprehensions
#*******************************************
squares = []
for number in range(10):
    squares.append(number * number)
print(squares)

squares = [number * number for number in range(10)]
print(squares)

#*******************************************
# Enumerate
#*******************************************
# Add to a new list names that appear on even indices
# List comprehension + enumerate

names = ['John', 'Mary', 'Lina', 'Mark', 'Steve', 'Lin', 'Max']

even_names = [name for idx, name in enumerate(names) if idx % 2 == 0]

print(even_names)
#-------------------------------------------

#**************************************************************************************
# EXERCISE 1
# Find all of the numbers from 1-1000 that are divisible by 6.
#**************************************************************************************
num_list = [num for num in range(1, 1001) if num % 6 == 0]
print(num_list)

#**************************************************************************************
# EXERCISE 2
# Find all number from 1-1000 that have 9 in them.
#**************************************************************************************
num_list = [num for num in range(1, 1001) if '9' in str(num)]
print(num_list)

#**************************************************************************************
# EXERCISE 3
# Given string: text = 'In this lecture we will review some additional functionalities
# of python built-in data structures.' calculate how many words have letter e in it.
#**************************************************************************************
text = ('In this lecture we will review some additional functionalities '
        'of python built-in data structures.')

words = [word for word in text.split() if 'e' in word]
print(len(words))

#**************************************************************************************
# EXERCISE 4
# Given the same string as in previous exercise: calculate count of words
# that have more than 5 characters.
#**************************************************************************************
text = ('In this lecture we will review some additional functionalities '
        'of python built-in data structures.')

words = [word for word in text.split() if len(word) > 5]
print(len(words))

#**************************************************************************************
# EXERCISE 5
# Given the same string calculate the occurrence of each letter in the string.
# (HINT: store everything in dictionary)
#**************************************************************************************
text = ('In this lecture we will review some additional functionalities '
        'of python built-in data structures.')
uniq = set(text)

letters_dict = {letter:text.count(letter) for letter in uniq}

print(letters_dict)

# **************************************************************************************
# EXERCISE 6
# Write a program that checks if given number is a perfect square.
# **************************************************************************************
import math
user_number = int(input('Enter a number: '))

if math.sqrt(user_number).is_integer():
    print(f'Number {user_number} is a perfect square!')
else:
    print(f'Number {user_number} isn\'t a perfect square!')