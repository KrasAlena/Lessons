from Ex_1 import sum_of_three_ints


def test_all_negative_inputs():
    assert sum_of_three_ints(-1, -2, -3) == -6


def test_a_negative_b_c_positive():
    assert sum_of_three_ints(-1, 2, 3) == 4


def test_a_negative_b_positive_c_negative():
    assert sum_of_three_ints(-1, 2, -3) == -2


def test_a_b_negative_c_positive():
    assert sum_of_three_ints(-1, -2, 3) == 0


def test_a_positive_b_negative_c_positive():
    assert sum_of_three_ints(1, -2, 3) == 2


def test_a_b_positive_c_negative():
    assert sum_of_three_ints(1, 2, -3) == 0


def test_all_positive_inputs():
    assert sum_of_three_ints(1, 2, 3) == 6