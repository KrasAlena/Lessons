from Ex_1_unittest import sum_of_three_ints
import unittest


class TestSumOfThreeInts(unittest.TestCase):
    def test_all_negative_inputs(self):
        self.assertEqual(sum_of_three_ints(-1, -2, -3), -6)

    def test_a_negative_b_c_positive(self):
        self.assertEqual(sum_of_three_ints(-1, 2, 3), 4)

    def test_a_negative_b_positive_c_negative(self):
        self.assertEqual(sum_of_three_ints(-1, 2, -3), -2)

    def test_a_b_negative_c_positive(self):
        self.assertEqual(sum_of_three_ints(-1, -2, 3), 0)

    def test_a_positive_b_negative_c_positive(self):
        self.assertEqual(sum_of_three_ints(1, -2, 3), 2)

    def test_a_b_positive_c_negative(self):
        self.assertEqual(sum_of_three_ints(1, 2, -3), 0)

    def test_all_positive_inputs(self):
        self.assertEqual(sum_of_three_ints(1, 2, 3), 6)


if __name__ == '__main__':
    unittest.main()