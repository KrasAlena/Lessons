def add(x: int, y: int) -> int:
    return x + y

def sub(x: int, y: int) -> int:
    return x - y

def prod(x: int, y: int) -> int:
    return x * y

def div(x: int, y: int) -> int:
    try:
        return x // y
    except ZeroDivisionError as err:
        return err.args