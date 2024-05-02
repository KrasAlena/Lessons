from Ex_3 import sum_numbers


def test_all_positive_int():
    assert sum_numbers([1, 2, 3]) == 6.0


def test_all_positive_floats():
    assert sum_numbers([1.2, 2.3, 3.1]) == 6.6


def test_all_negative_int():
    assert sum_numbers([-1, -2, -3]) == -6


def test_all_negative_floats():
    assert sum_numbers([-1.2, -2.3, -3.1]) == -6.6


def test_empty_list():
    assert sum_numbers([]) == 0


def test_all_strings():
    try:
        sum_numbers(['acc', 'bcc', 'ccc'])
        assert False,'All elements in the list must be numbers'
    except TypeError as e:
        pass