from Ex_7 import first_last6


def test_first_last6_grade_1_6element_length():
    assert first_last6([6]) == True


def test_first_last6_first_6element():
    assert first_last6([6, 1, 0]) == True


def test_first_last6_last_6element():
    assert first_last6([1, 6]) == True


def test_first_last6_empty_list():
    try:
        first_last6([])
        assert False, 'The length of the list must be at least 1'
    except ValueError:
        pass


def test_first_last6_not_integers():
    try:
        first_last6([6, '6'])
        assert False, 'The list must contain only integers'
    except TypeError:
        pass


def test_first_last6_not_last_not_first_6element():
    assert first_last6([1, 6, 3]) == False


def test_first_last6_not_last_no_6element():
    assert first_last6([1, 5, 3]) == False