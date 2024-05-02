from Ex_2 import find_largest_number


def test_all_positive_int():
    assert find_largest_number([1, 2, 3]) == 3


def test_all_positive_floats():
    assert find_largest_number([1.2, 2.3, 3.1]) == 3.1


def test_all_negative_int():
    assert find_largest_number([-1, -2, -3]) == -1


def test_all_negative_floats():
    assert find_largest_number([-1.2, -2.3, -3.1]) == -1.2


def test_positive_and_negative_numbers():
    assert find_largest_number([1.2, -2, 3.1]) == 3.1


def test_empty_list():
    assert find_largest_number([]) == None


def test_duplicates():
    assert find_largest_number([1.2, -2, 3.1, -2, 3.1]) == 3.1