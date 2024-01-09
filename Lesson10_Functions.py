def is_even(number):
    return number % 2 == 0

print(is_even(12))
#**************************************************************************************
# EXERCISE 1
# Create at least 5 different functions by your own and test it.
# 1) should return the sum of three numbers
# 2) returns a new list with the first and the last element of the given list
#**************************************************************************************
def numbers_sum(a, b, c):
    return a + b + c

print(numbers_sum(1, 5, 9))

def first_and_last(user_list):
    return [user_list[0], user_list[-1]]

user_list = ['John', 'Mary', 'Lina', 'Mark', 'Steve', 'Lin', 'Max']
print(first_and_last(user_list))
#**************************************************************************************
# EXERCISE 2
# Create a function that adds a string ending to each member in a list.
#**************************************************************************************
def member_ending(member_list):
    return [member + '\'s' for member in member_list]

member_list = ['John', 'Mary', 'Lina', 'Mark', 'Steve', 'Lin', 'Max']
print(member_ending(member_list))
#**************************************************************************************
# EXERCISE 3
# Create a mini python program which would take two numbers as an input
# and would return their sum, subtraction, division, multiplication.
#**************************************************************************************
def math_operations():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    return (f'The sum of your numbers is {num1 + num2}.\nThe subtraction of your numbers is {num1 - num2}.\n'
            f'The division of your numbers is {num1 / num2}.\nThe multiplication of your numbers is {num1 * num2}.')

print(math_operations())
#**************************************************************************************
# EXERCISE 4
# Create a function that returns only strings with unique characters.
#**************************************************************************************
def unique_char(text):
    return ''.join(set(text))

text = 'Create a function that returns only strings with unique characters.'
print(unique_char(text))

#**************************************************************************************
# EXERCISE 5
# Write a program that defines a function called extract_email_addresses()
# that takes a text as input and extracts all email addresses from the text.
#**************************************************************************************
def cut_emails(text):
    words_list = [word for word in text.split() if '@' not in word]
    return ' '.join(words_list)

text = 'We have the list of company\'s emails: example@gmail.com, support@example.com. But these emails are only for internal use.'
print(cut_emails(text))

