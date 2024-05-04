def calculate_grade(score: int) -> str:
    '''
    Converts a numerical score to a letter grade and calculates bonus points.

    Parameters:
    score (int): The numerical score, ranging from 0 to 100.

    Returns:
    tuple: A tuple containing the letter grade and any bonus points awarded.
    The letter grade is a string ('A', 'B', 'C', 'D', or 'F').
    The bonus points is an integer representing additional points.

    Grade Conversion Logic:
    - A: 90-100 (Bonus points: 5)
    - B: 80-89 (Bonus points: 4)
    - C: 70-79 (Bonus points: 3)
    - D: 60-69 (Bonus points: 1)
    - F: 0-59 (No bonus points)
    '''
    if not isinstance(score, int) and not isinstance(score, float):
        raise TypeError('Score must be a number')

    if score > 100 or score < 0:
        raise ValueError('Invalid score')


    if score >= 90:
        return 'A', 5
    elif score >= 80:
        return 'B', 4
    elif score >= 70:
        return 'C', 3
    elif score >= 60:
        return 'D', 1
    else:
        return 'F', 0

