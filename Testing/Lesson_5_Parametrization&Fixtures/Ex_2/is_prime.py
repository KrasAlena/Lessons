def is_prime(num: int) -> bool:
    """Checks if a number is prime (greater than 1 and only divisible by 1 and itself)."""
    if not isinstance(num, int):
        raise TypeError('Prime number must be an integer')

    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True