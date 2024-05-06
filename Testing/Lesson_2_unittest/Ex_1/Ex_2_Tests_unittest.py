from Ex_2_unittest import find_largest_number
import unittest


class TestFindLargestNumber(unittest.TestCase):
    def test_all_positive_int(self):
        self.assertEqual(find_largest_number([1, 2, 3]), 3)

    def test_all_positive_floats(self):
        self.assertEqual(find_largest_number([1.2, 2.3, 3.1]), 3.1)

    def test_all_negative_int(self):
        self.assertEqual(find_largest_number([-1, -2, -3]), -1)

    def test_all_negative_floats(self):
        self.assertEqual(find_largest_number([-1.2, -2.3, -3.1]), -1.2)

    def test_positive_and_negative_numbers(self):
        self.assertEqual(find_largest_number([1.2, -2, 3.1]), 3.1)

    def test_empty_list(self):
        self.assertEqual(find_largest_number([]), None)

    def test_duplicates(self):
        self.assertEqual(find_largest_number([1.2, -2, 3.1, -2, 3.1]), 3.1)


if __name__ == '__main__':
    unittest.main()