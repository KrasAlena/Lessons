# def love6(a: int, b: int) -> bool:
#     return a == 6 or b == 6 or a + b == 6 or a - b == 5
#
# assert love6(1, 2) == False, "Must be False: neither arg is 6, nor is the sum or subtraction equal to 6"
# assert love6(5, 6) == True, "Must be True: second arg is 6"
# assert love6(1, 5) == True, "Must be True: 1 + 5 = 6"
# assert love6(12, 12) == False, "Must be False: neither arg is 6, nor is the sum or subtraction equal to 6"
# assert love6(13, 7) == True, "Must be True, because 13 - 7 = 6"


# test_reverse_string.py
def reverse_string(text: str) -> str:
    """Reverses the order of any given string.

    Throws a TypeError on inputs that are not strings.
    """
    return text[::-1]

def test_reverse_string_letters():
    assert reverse_string("abc") == "cba", "abc reversed is cba"


def test_reverse_string_numbers():
    assert reverse_string("12345") == "54321", "12345 reversed is 54321"


def test_reverse_string_mixed():
    assert reverse_string("12abc45") == "54cba21", "12abc45 reversed is 54cba21"


if __name__ == "__main__":
    test_reverse_string_letters()
    test_reverse_string_numbers()
    test_reverse_string_mixed()
    print("Tests passed")