from Ex_6_unittest import calculate_grade
import unittest
'''
Write tests for valid scores, negative scores, scores above 100, 
scores hitting grade boundaries (e.g., 89.9 vs 90), 
and how bonus points are awarded and reflected in the grade.
'''


class TestCalculateGrade(unittest.TestCase):
    def test_valid_score(self):
        self.assertEqual(calculate_grade(58), ('F', 0))

    def test_negative_score(self):
        with self.assertRaises(ValueError):
            calculate_grade(-13)

    def test_score_above_100(self):
        with self.assertRaises(ValueError):
            calculate_grade(113)

    def test_boundary_scores(self):
        self.assertEqual(calculate_grade(89.9), ('B', 4))
        self.assertEqual(calculate_grade(90.0), ('A', 5))

    def test_bonus_points(self):
        self.assertEqual(calculate_grade(81), ('B', 4))
        self.assertEqual(calculate_grade(75), ('C', 3))
        self.assertEqual(calculate_grade(65), ('D', 1))

    def test_no_bonus_points(self):
        self.assertEqual(calculate_grade(59), ('F', 0))
        self.assertEqual(calculate_grade(100), ('A', 5))


if __name__ == '__main__':
    unittest.main()