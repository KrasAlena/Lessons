from is_prime import is_prime
import pytest


@pytest.mark.parametrize('prime_numbers', [
    2, 3, 5, 7, 11, 13, 17, 997, 991, 983, 977

], ids=['small_prime_2', 'small_prime_3', 'small_prime_5', 'small_prime_7',
        'small_prime_11', 'small_prime_13', 'small_prime_17', 'large_prime_997', 'large_prime_991',
        'large_prime_983', 'large_prime_977'])
def test_prime_numbers(prime_numbers):
    assert is_prime(prime_numbers)


@pytest.mark.parametrize('non_prime_numbers', [
    0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20

], ids=['non_prime_0', 'non_prime_1', 'non_prime_2', 'non_prime_6', 'non_prime_8', 'non_prime_9', 'non_prime_10',
        'non_prime_12',
        'non_prime_14', 'non_prime_15', 'non_prime_16', 'non_prime_18', 'non_prime_20'])
def test_non_prime_numbers(non_prime_numbers):
    assert not is_prime(non_prime_numbers)


@pytest.mark.parametrize('negative_numbers', [
    -1, -2, -7, -977

], ids=['non_prime_-1', 'non_prime_-2', 'non_prime_-7', 'non_prime_-977'])
def test_negative_numbers(negative_numbers):
    assert not is_prime(negative_numbers)


# def test_negative_numbers(negative_input):
#     with pytest.raises(ValueError):
#         is_prime(negative_input)