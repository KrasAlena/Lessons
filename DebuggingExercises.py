'''The following is a list of buggy python code snippets. Try debugging them using Pycharm's IDE
 debugger (click to make breakpoints, traverse the code using buttons or keyboard shortcuts
 (F7 for Step Into, F8 for Step Over in Pycharm) and become a detective to solve the mystery
 of the bug). Describe what is wrong and why in a comment and fix the code.'''


# **************************************************************************************
# EXERCISE 1
# This code is supposed to compute an average of a list of numbers
# def calculate_average(numbers):
#     total = 0
#     for i in range(len(numbers)):
#         total += i
#     average = total / len(numbers)
#     return average
#
# numbers = [5, 10, 15, 20]
# result = calculate_average(numbers)
# print(result)
# **************************************************************************************
def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i] # total += i - here the sum of the indices was calculated
    average = total / len(numbers)
    return average


numbers = [5, 10, 15, 20]
result = calculate_average(numbers)
print(result)

# **************************************************************************************
# EXERCISE 2
# The following should return `True` if the input is 1 or 2
# def is_1_or_2(num):
#     if num == 1 or 2:
#         print('the number is 1 or 2')
#         return True
#     else:
#         print('the number is not 1 or 2')
#         return False
#
# result = is_1_or_2(2)
# print(result)
# **************************************************************************************
def is_1_or_2(num):
    if num == 1 or num == 2: # num == 1 or 2 - this condition doesn't work as intended because or 2 is evaluated separately and always returns True like num == 1 or True
        print('the number is 1 or 2')
        return True
    else:
        print('the number is not 1 or 2')
        return False


result = is_1_or_2(3)
print(result)

# **************************************************************************************
# EXERCISE 3
# This code is supposed to compare the means of two lists where the second list is an extended list of the first one.
# def mean(lst):
#     return sum(lst) / len(lst)
#
#
# # Define the original set of values.
# values = [8., 7., 9., 4., 6., 7., 8., 4.]
#
# # Create a new list with the original values and add a few more
# new_values = values
# new_values.append(1.)
# new_values.append(2.)
# new_values.append(3.)
# new_values.append(4.)
# new_values.append(1.)
#
# print(f"Difference in the mean: {mean(new_values) - mean(values)}")
# **************************************************************************************
def mean(lst):
    return sum(lst) / len(lst)


# Define the original set of values.
values = [8., 7., 9., 4., 6., 7., 8., 4.]

# Create a new list with the original values and add a few more
new_values = values[:]
new_values.append(1.)
new_values.append(2.)
new_values.append(3.)
new_values.append(4.)
new_values.append(1.)

print(f'Difference in the mean: {mean(new_values) - mean(values):.2f}')
# before in line 87 new_values = values we are not creating a new list with the same values as values.
# Instead, we are creating a new reference new_values that points to the same list object as values.
# Any modifications made to new_values will also affect values

# **************************************************************************************
# EXERCISE 4
# This code attempts to concatenate a list of words into a sentence
# def create_sentence(words):
#     sentence = ""
#     for word in words:
#         sentence = sentence + word + " "
#     return sentence
#
# word_list = ["The", "quick", "brown", "fox"]
# result = create_sentence(word_list)
# print(result)
# **************************************************************************************
def create_sentence(words):
    sentence = ""
    for word in words:
        if word != words[-1]:
            sentence = sentence + word + " " # we don't need to add a space to the last word in the sentence
        else:
            sentence = sentence + word
    return sentence


word_list = ["The", "quick", "brown", "fox"]
result = create_sentence(word_list)
print(result)

# **************************************************************************************
# EXERCISE 5
# This code should return a list of small elements (less than `threshold`) from the given list
# def filter_low(lst, threshold=5):
#     for element in lst:
#         low = []
#         if element < threshold:
#             low.append(element)
#     return low
#
# my_list = [5, 2, 12, 7, 3, 8]
# result = filter_low(my_list)
# print(result)
# **************************************************************************************
def filter_low(lst, threshold=5):
    low = []
    for element in lst:
        # low = [] # each iteration we define low af an empty list
        if element < threshold:
            low.append(element)
    return low


my_list = [5, 2, 12, 7, 3, 8]
result = filter_low(my_list)
print(result)

# **************************************************************************************
# EXERCISE 6
# The following code should remove even numbers from a list
# def remove_even_numbers(numbers):
#     for num in numbers:
#         if num % 2 == 0:
#             numbers.remove(num)
#     return numbers
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = remove_even_numbers(numbers)
# print(result)
# **************************************************************************************
def remove_even_numbers(numbers):
    # for num in numbers:
    #     if num % 2 == 0:
    #         numbers.remove(num)
    odd_numbers = [num for num in numbers if num % 2 != 0]
    # odd_numbers = list(filter(lambda num: num % 2 != 0, numbers))
    return odd_numbers


numbers = [10, 6, 5, 6, 4, 2, 3, 3, 7]
result = remove_even_numbers(numbers)
print(result)


def remove_even_numbers(numbers):
    i = 0
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            numbers.remove(numbers[i])
        else:
            i += 1
    return numbers


numbers = [10, 6, 5, 6, 4, 2, 3, 3, 7]
result = remove_even_numbers(numbers)
print(result)

# Iterate over the list backwards to avoid index shifting when removing elements
for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] % 2 != 0:
        del my_list[i]

print(my_list)

# **************************************************************************************
# EXERCISE 7
# The following code is supposed to print the original and squared list of numbers
# def square_elements(numbers):
#     for i in range(len(numbers)):
#         numbers[i] = numbers[i] ** 2
#     return numbers
#
# numbers = [1, 2, 3, 4]
# result = square_elements(numbers)
# print(numbers)
# print(result)
# **************************************************************************************
def square_elements(numbers):
    squares = numbers[:]
    for i in range(len(numbers)):
        squares[i] = squares[i] ** 2
        i += 1
    return squares


numbers = [1, 2, 3, 4]
result = square_elements(numbers)
print(numbers)
print(result)

# **************************************************************************************
# EXERCISE 8
# The parameter `weekday` is `True` if it is a weekday, and the parameter `vacation` is
# `True` if we are on vacation. We sleep in if it is not a weekday or we're on vacation.
# Return `True` if we sleep in. Exercise from [here](https://codingbat.com/prob/p173401).
# ```
# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True
# ```
# def sleep_in(weekday, vacation):
#     if vacation is True:
#         return True
#     elif weekday != True or vacation != True:
#         return True
#     else
#         return False
#
# result = sleep_in(False, False)
# print(result)
# **************************************************************************************
def sleep_in(weekday, vacation):
    if vacation is True:
        return True
    elif weekday != True:
        return True
    else:
        return False

result = sleep_in(True, False)
print(result)
