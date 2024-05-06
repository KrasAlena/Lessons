from Ex_3_unittest import sum_numbers
import unittest


class TestSumNumbers(unittest.TestCase):

    def test_all_positive_int(self):
        self.assertEqual(sum_numbers([1, 2, 3]), 6.0)

    def test_all_positive_floats(self):
        self.assertEqual(sum_numbers([1.2, 2.3, 3.1]), 6.6)

    def test_all_negative_int(self):
        self.assertEqual(sum_numbers([-1, -2, -3]), -6)

    def test_all_negative_floats(self):
        self.assertEqual(sum_numbers([-1.2, -2.3, -3.1]), -6.6)

    def test_empty_list(self):
        self.assertEqual(sum_numbers([]), 0)

    def test_all_strings(self):
        with self.assertRaises(TypeError):
            sum_numbers(['acc', 'bcc', 'ccc'])


if __name__ == '__main__':
    unittest.main()