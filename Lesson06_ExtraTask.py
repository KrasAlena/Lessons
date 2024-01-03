#Exercise 1: String Analyzer
#Write a program that takes a string as input and prints:
#The length of the string. The type of the string. The string in uppercase. The string in lowercase.
#---------------------------------------
# my_string = input('Enter a string: ')
# print(len(my_string), type(my_string), my_string.upper(), my_string.lower(), sep='\n')
#---------------------------------------


#Exercise 2: List Statistics
#Create a list of numbers and write a program that prints:
#The length of the list. The sum of the numbers in the list.
# The average of the numbers in the list (rounded to two decimal places). The list sorted in ascending order.
#----------------------------------------
# my_numbers = [1, 0, 0.3456, 100, 45.0, 19.65757, 9.0986]
# print(len(my_numbers),
#       sum(my_numbers),
#       round((sum(my_numbers)/len(my_numbers)), 2),
#       sorted(my_numbers), sep='\n')
#----------------------------------------

# Exercise 3: Temperature Converter
# Write a program that converts a temperature in Fahrenheit to Celsius.
# Take the temperature as input and use the formula: Celsius = (Fahrenheit - 32) * 5/9.
# Round the result to two decimal places.
#----------------------------------------
# fahr_temp = int(input('Enter a temperature in Fahrenheit: '))
# cels_temp = (fahr_temp - 32) * 5/9
# print(f'{fahr_temp}°F to Celsius equals {round(cels_temp, 2)}°C')
#----------------------------------------

#Exercise 4: Word Sorter
#Write a program that takes a sentence as input and prints the words in the sentence in alphabetical order.
#You can use the sorted function.

#----------------------------------------
# print(sorted(input('Enter any sentence: ').lower().split()))
#----------------------------------------

#Exercise 5: List Reverser
#Create a list of items and write a program that prints the list in reverse order.
#Use the reverse method or slicing.
#----------------------------------------
# my_list = [1, 'Max', True, {'1': 'value', '2': 'value2'}, 2.56, [1, 2, 3]]
# print(my_list[::-1])
#----------------------------------------


#Exercise 7: Area Calculator
#Write a program that calculates the area of a circle.
#Take the radius as input and use the formula: Area = π * r^2.
# You can use the round function to round the result.
#----------------------------------------
print(round(3.14 * (float(input('Enter a circle radius: ')) ** 2), 2))
#----------------------------------------

#Exercise 8: List Concatenation
#Create two lists and write a program that concatenates them into a single list.
#Print the concatenated list.

list1 = [10, 11, 12, 13, 14]
list2 = [20, 30, 42]

res = [a for item in [list1, list2] for a in item]

print(res)

#Exercise 10: List Element Counter
#Write a program that takes a list of elements and a specific element as input,
#and then prints the count of that element in the list. Use the count method.

my_list = [10, 11, 12, 13, 14, 12, 38, 13, 13, 0, 13]

specific_element = input('Enter a specific element: ')