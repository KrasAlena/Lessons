from Ex_6 import calculate_grade

'''
Write tests for valid scores, negative scores, scores above 100, 
scores hitting grade boundaries (e.g., 89.9 vs 90), 
and how bonus points are awarded and reflected in the grade.
'''


def test_calculate_grade_valid_score():
    assert calculate_grade(58) == ('F', 0)


def test_calculate_grade_negative_score():
    try:
        calculate_grade(-13)
        assert False, 'Invalid score'
    except ValueError:
        pass


def test_calculate_grade_score_above_100():
    try:
        calculate_grade(113)
        assert False, 'Invalid score'
    except ValueError:
        pass


def test_calculate_grade_on_boundary():
    assert calculate_grade(89.9) == ('B', 4)
    assert calculate_grade(90.0) == ('A', 5)


def test_calculate_grade_with_bonus_points():
    assert calculate_grade(81) == ('B', 4)
    assert calculate_grade(75) == ('C', 3)
    assert calculate_grade(65) == ('D', 1)


def test_calculate_grade_with_no_bonus_points():
    assert calculate_grade(59) == ('F', 0)
    assert calculate_grade(100) == ('A', 5)