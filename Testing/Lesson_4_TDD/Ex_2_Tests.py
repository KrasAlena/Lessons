import pytest
from Ex_2 import rotated_left_2


def test_rotated_left_2_more_than_2_chars_string():
    assert rotated_left_2('hello') == 'llohe'


def test_rotated_left_2_2_chars_string():
    assert rotated_left_2('ok') == 'ok'


def test_rotated_left_2_3_chars_string():
    assert rotated_left_2('cat') == 'tca'


def test_rotated_left_2_less_than_2_chars_string():
    with pytest.raises(ValueError):
        rotated_left_2('i')


def test_rotated_left_2_empty_string():
    with pytest.raises(ValueError):
        rotated_left_2('')


def test_rotated_left_2_number():
    with pytest.raises(TypeError):
        rotated_left_2(123)


def test_rotated_left_2_list():
    with pytest.raises(TypeError):
        rotated_left_2(['h', 'i'])