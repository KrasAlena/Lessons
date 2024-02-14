# **************************************************************************************
# EXERCISE  1
# Fix these coding examples according to the standards we learnt during this lecture:
# **************************************************************************************
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def say_hello(self):
        print(f"hello, {self.name}")


person = Person("first", "person")
person.say_hello()


def greeting(full_name: str):
    """Function greets a person given full name as a string"""

    print(f"Hello, {full_name}. How are you today?")


def greet_user(age):
    eligible_to_enter = age > 21

    if eligible_to_enter:
        print("Welcome")
    else:
        print("Access denied")


# **************************************************************************************
# EXERCISE  2
# Magic Number problem. A number is said to be a magic number, if the sum of its digits
# are calculated till a single digit recursively by adding the sum of the digits after
# every addition. If the single digit comes out to be 1,then the number is a magic number.
# For example Number = 50113 => 5+0+1+1+3=10 => 1+0=1 This is a Magic Number

# For example Number = 1234 => 1+2+3+4=10 => 1+0=1 This is a Magic Number

# Write a python function that takes in one parameter - integer and then returns
# True if number is magic number or False if it is not a magic number
# **************************************************************************************

def is_magic_number(number: int):
    while number >= 10:
        number = sum(int(digit) for digit in str(number))
    return number == 1


print(is_magic_number(12345))


