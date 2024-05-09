def roman_to_int(roman_num: str) -> int:
    """Converts a basic Roman numeral string (I, V, X, L, C) to an integer (limited to values up to 3999)."""
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "M": 1000}
    total = 0
    prev_val = 0
    for char in roman_num:
        val = roman_map[char]
        total += val
        # Handle subtractive notation (e.g., IV, IX)
        if prev_val < val and prev_val in (1, 10, 100):
            total -= 2 * prev_val
        prev_val = val
        if total > 3999:
            raise ValueError('Roman numeral exceed maximum value of 3999')
    return total

