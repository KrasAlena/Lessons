def first_two_chars(word: str) -> str:
    if not isinstance(word, str):
        raise TypeError
    return word[:2]