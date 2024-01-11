#*******************************************
# Catching and handling Exceptions
#*******************************************
def divide_two_numbers(dividend: int, divisor: int):
    try:
        quotient = dividend / divisor
        print(f'Result = {quotient}')
    except ZeroDivisionError:
        print('Divisor is zero; Division is impossible')

print(divide_two_numbers(50, 0))

#*******************************************
# Multiply Exceptions
#*******************************************
from typing import Union


def my_dummy_int_func(a: Union[str, float]):
    try:
        return int('a')
    except ValueError:
        print('Value of "a" cannot be deduced to integer')
    except TypeError:
        print('Type of "a" is incompatible; should either be a number or a string')

print(my_dummy_int_func(2.0))



#*******************************************
# Aliasing
#*******************************************
try:
    raise NameError('Undefined name')
    # raise ValueError('Invalid name')
except (NameError, ValueError) as err:
    print(f'Got exception with msg {err.args}')



#**************************************************************************************
# EXERCISE 1
# Create at least 5 different functions and try to handle at least 5 built-in Python
# Exceptions.
#**************************************************************************************
# Function 1: ZeroDivisionError
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

print(divide_numbers(10, 0))

# Function 2: AttributeError
def get_uppercase(obj):
    try:
        result = obj.upper()
        return result
    except AttributeError:
        return "Error: Object has no upper attribute."

print(get_uppercase(42))

# Function 3: IndexError
def get_list_element(my_list, index):
    try:
        result = my_list[index]
        return result
    except IndexError:
        return "Error: Index out of range."

print(get_list_element([1, 2, 3], 5))

# Function 4: ValueError
def convert_to_int(value):
    try:
        result = int(value)
        return result
    except ValueError:
        return "Error: Unable to convert to an integer."

print(convert_to_int("abc"))

# Function 5: KeyError
def access_dict_key(my_dict, key):
    try:
        result = my_dict[key]
        return result
    except KeyError:
        return "Error: Key not found in the dictionary."

print(access_dict_key({"a": 1, "b": 2}, "c"))

#**************************************************************************************
# EXERCISE 2
# In Python, dividing by zero raises a ZeroDivisionError.
#
# Your task is to create a function that:
# Takes two numbers as arguments. Tries to divide the first number by the second number.
# If the second number is 0, it should catch the ZeroDivisionError
# and return a custom error message.
# If the division is successful, it should return the result.
# Regardless of whether the division is successful or not, it should print a message
# saying Attempted division. If the inputs are not numbers, it raises a TypeError.
# It catches this TypeError and returns a custom error message.
#**************************************************************************************
def divide_numbers(num1, num2):
    try:
        if not isinstance(num1, int) or not isinstance(num2, int):
            raise TypeError('At least one of the parameters is\'t a number')
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return 'Error: Division by zero is not allowed.'
    except TypeError as err:
        return err.args
    finally:
        print('Attempted division')

print(divide_numbers(10, '0'))

#**************************************************************************************
# EXERCISE 3
# Create a mini python program which would take two numbers as an input
# and would return their sum, subtraction, division, multiplication.
# Handle all possible errors that may occur.
#**************************************************************************************
class SomeError(Exception):
    pass
def math_operations(*args):
    try:
        if len(args) != 2:
            raise SomeError('Error: Incorrect number of arguments.')
        num1, num2 = args
        num_sum = num1 + num2
        num_substraction = num1 - num2
        num_division = num1 / num2
        num_mult = num1 * num2
        return num_sum, num_substraction, num_division, num_mult
    except (ZeroDivisionError, TypeError) as err:
        return err.args
    except SomeError as e:
        return str(e)

print(math_operations(5, 0, 3))