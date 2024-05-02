'''
Think of ways how you could break this code - call the function in a way that adheres to the function
description but the answer is incorrect.
Write 10 tests for it checking all possibilities for each argument.
The function description lacks details about when and what errors the function throws.
Add the correct description.
Implement tests reflecting the errors if you haven't already.
'''
from Ex_4 import calculate


def test_calculate_numbers_plus():
    assert calculate(4, 2, '+') == 6


def test_calculate_numbers_minus():
    assert calculate(4, 2.0, '-') == 2.0


def test_calculate_numbers_multiply():
    assert calculate(4.0, 0, '*') == 0


def test_calculate_numbers_division():
    assert calculate(4.0, 2.0, '/') == 2.0


def test_calculate_division_by_zero():
    try:
        calculate(4, 0, '/')
        assert False, 'Should raise ZeroDivisionError'
    except ZeroDivisionError:
        pass


def test_calculate_invalid_operator():
    try:
        calculate(4, 0, '()')
        assert False, 'Should raise ValueError'
    except ValueError:
        pass


def test_calculate_strings_plus():
    try:
        calculate('abbc', '1', '+')
        assert False, 'Should raise TypeError'
    except TypeError:
        pass


def test_calculate_string_number_plus():
    try:
        calculate('4', 0, '+')
        assert False, 'Should raise TypeError'
    except TypeError:
        pass


def test_calculate_string_number_multiply():
    try:
        calculate('a', 3, '*')
        assert False, 'Should raise TypeError'
    except TypeError:
        pass