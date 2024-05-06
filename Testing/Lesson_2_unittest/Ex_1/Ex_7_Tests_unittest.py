from Ex_7_unittest import first_last6
import unittest


class TestFirstLast6(unittest.TestCase):
    def test_6_in_single_element_list(self):
        self.assertTrue(first_last6([6]))

    def test_6_in_first_position(self):
        self.assertTrue(first_last6([6, 1, 0]))

    def test_6_in_last_position(self):
        self.assertTrue(first_last6([1, 6]))

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            first_last6([])

    def test_non_integer_element(self):
        with self.assertRaises(TypeError):
            first_last6([6, '6'])

    def test_no_6_in_list(self):
        self.assertFalse(first_last6([1, 5, 3]))

    def test_6_not_in_first_nor_last_position(self):
        self.assertFalse(first_last6([1, 6, 3]))


if __name__ == '__main__':
    unittest.main()