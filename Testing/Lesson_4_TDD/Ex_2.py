def rotated_left_2(string: str) -> str:
    if len(string) < 2:
        raise ValueError

    if not isinstance(string, str):
        raise TypeError

    return string[2:] + string[:2]