'''
Think of ways how you could break this code - call the function in a way that adheres to the function
description but the answer is incorrect.
Write 10 tests for it checking all possibilities for each argument.
The function description lacks details about when and what errors the function throws.
Add the correct description.
Implement tests reflecting the errors if you haven't already.
'''
from Ex_4_unittest import calculate
import unittest


class TestCalculate(unittest.TestCase):

    def test_calculate_numbers_plus(self):
        self.assertEqual(calculate(4, 2, '+'), 6)

    def test_calculate_numbers_minus(self):
        self.assertEqual(calculate(4, 2.0, '-'), 2.0)

    def test_calculate_numbers_multiply(self):
        self.assertEqual(calculate(4.0, 0, '*'), 0)

    def test_calculate_numbers_division(self):
        self.assertEqual(calculate(4.0, 2.0, '/'), 2.0)

    def test_calculate_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(4, 0, '/')

    def test_calculate_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate(4, 0, '()')

    def test_calculate_strings_plus(self):
        with self.assertRaises(TypeError):
            calculate('abbc', '1', '+')

    def test_calculate_string_number_plus(self):
        with self.assertRaises(TypeError):
            calculate('4', 0, '+')

    def test_calculate_string_number_multiply(self):
        with self.assertRaises(TypeError):
            calculate('a', 3, '*')


if __name__ == '__main__':
    unittest.main()