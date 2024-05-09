import pytest

from Ex_1 import first_two_chars

def test_first_two_chars_more_than_two_chars_word():
    assert first_two_chars('hello') == 'he'


def test_first_two_chars_1_char_word():
    assert first_two_chars('h') == 'h'


def test_first_two_chars_empty_string():
    assert first_two_chars('') == ''


def test_first_two_chars_number():
    with pytest.raises(TypeError):
        first_two_chars(123)


def test_first_two_chars_list():
    with pytest.raises(TypeError):
        first_two_chars(['h', 'e', 'l', 'l', 'o'])