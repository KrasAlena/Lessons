# **************************************************************************************
# EXERCISE 1
# Write a Python program to find if a given string starts with a given character using
# Lambda. Output:True or False
# **************************************************************************************
start_with_char = (lambda string, char: string[0] == char)('hello', 'k')
print(start_with_char)


# **************************************************************************************
# EXERCISE 2
# Write a Python program to create a lambda function that adds 15 to a given number
# passed in as an argument, also create a lambda function that multiplies argument x
# with argument y and print the result.
# **************************************************************************************

add_fifteen = (lambda num: num + 15)(15)
print(add_fifteen)

adding_numbers = (lambda x, y: x + y)(13, (lambda num: num + 15)(15))
print(adding_numbers)

# **************************************************************************************
# EXERCISE 3
# Write a Python program to square and cube every number in a given list of integers
# using Lambda.
# **************************************************************************************
square_cube = list(map(lambda x: (x ** 2, x ** 3), [1, 2, 3]))
print(square_cube)

# **************************************************************************************
# EXERCISE 4
# Write a Python program to extract year, month, date and time using Lambda. Sample Output:
#
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178
# **************************************************************************************

from datetime import datetime, date

d = str(date.today()).split('-')
t = str(datetime.now().time())

_ = [print(pair[0]) for pair in zip(d, t)] + [print(t)]

_ = [print(pair[0]) for pair in zip(str(date.today()).split('-'), str(datetime.now().time()))] + [print(str(datetime.now().time()))]

# **************************************************************************************
# EXERCISE 5
# Write a Python program to sort a list of tuples using Lambda.
#
# # Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
#
# # Sorted the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
# **************************************************************************************
scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_score = sorted(scores, key=lambda item: item[1])
print(sorted_score)

# **************************************************************************************
# EXERCISE 6
# Write a Python program to sort a list of dictionaries buy color value using Lambda.
#
# # Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2',
# 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
#
# # Sorted the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7,
# 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
# **************************************************************************************
phones = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

sorted_by_color = sorted(phones, key=lambda phone: phone['color'])
print(sorted_by_color)

# **************************************************************************************
# EXERCISE 7
# Write a Python program to sort a given matrix in ascending order according to the sum
# of its rows using lambda.
#
# # Original Matrix:
# `[[1, 2, 3], [2, 4, 5], [1, 1, 1]]`
#
# # Sort the said matrix in ascending order according to the sum of its rows
# `[[1, 1, 1], [1, 2, 3], [2, 4, 5]]`
#
# # Original Matrix:
# `[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]`
#
# # Sort the said matrix in ascending order according to the sum of its rows
# `[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]`
# **************************************************************************************
origin_matrix = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

sorted_matrix = sorted(origin_matrix, key=lambda item: sum(item))
print(sorted_matrix)