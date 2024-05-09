import pytest
from Ex_2_pytest import is_balanced


def test_is_balanced_balanced_expression():
    assert is_balanced('Hello (customer: {name: Alex})')


def test_is_balanced_only_spaces():
    assert is_balanced('   ')


def test_is_balanced_not_balanced_expression():
    assert not is_balanced('Hello (customer: {name: Alex}})')


def test_is_balanced_only_opening_parentheses():
    assert not is_balanced('Hello (customer: {name: Alex')


def test_is_balanced_only_closing_parentheses():
    assert not is_balanced('Hello customer: name: Alex}})')


def test_is_balanced_non_bracket_characters():
    assert not is_balanced('Hello (customer: [name: Alex!)')


def test_is_balanced_mixed_brackets():
    assert not is_balanced('Hello (customer: {name: [Alex})')


def test_is_balanced_empty_expression():
    with pytest.raises(ValueError):
        is_balanced('')


def test_is_balanced_empty_list():
    with pytest.raises(TypeError):
        is_balanced([])


def test_is_balanced_list_of_dictionaries():
    with pytest.raises(TypeError):
        is_balanced([{'1': 1}, {'2': 2}])