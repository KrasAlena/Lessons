def is_not_number (number)-> bool:
 return not isinstance (number, int) and not isinstance (number, float)

def calculate(num1: float, num2: float, operator: str) -> float:
    """Performs basic arithmetic operations on two numbers using operators (+, -, *, /).
    """
    if is_not_number(num1) or is_not_number(num2):
        raise TypeError

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Division by zero")
        return num1 / num2
    else:
        raise ValueError("Invalid operator")