from Ex_3_pytest import roman_to_int
import pytest


def test_roman_to_int_minimum_roman():
    assert roman_to_int('I') == 1


def test_roman_to_int_maximum_roman():
    assert roman_to_int('MMMCMXCIX') == 3999