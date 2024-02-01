class MyString:
    def __init__(self, value: str):
        self.value = value

    def add_exclamation(self) -> 'MyString':
        self.value += "!"
        return self

    def make_upper(self) -> 'MyString':
        self.value = self.value.upper()
        return self


my_string = MyString('hello')
my_string.add_exclamation().make_upper()

print(my_string.value) # output: "HELLO!"

#-------------------------------------------------------------
class Car:
    def __init__(self):
        self.position_x = 0
        self.position_y = 0
        self.direction = "north"

    def turn_left(self):
        if self.direction == "north":
            self.direction = "west"
        elif self.direction == "west":
            self.direction = "south"
        elif self.direction == "south":
            self.direction = "east"
        elif self.direction == "east":
            self.direction = "north"
        return self

    def turn_right(self):
        if self.direction == "north":
            self.direction = "east"
        elif self.direction == "west":
            self.direction = "north"
        elif self.direction == "south":
            self.direction = "west"
        elif self.direction == "east":
            self.direction = "south"
        return self

    def go(self, distance):
        if self.direction == "north":
            self.position_y += distance
        if self.direction == "south":
            self.position_y -= distance
        if self.direction == "west":
            self.position_x -= distance
        if self.direction == "east":
            self.position_x += distance
        return self

    def show_position(self):
        print(f"I am at {self.position_x} : {self.position_y}")
        return self


car = Car().turn_left().go(50).turn_left().go(20).show_position().go(40).turn_right().go(80).show_position().go(50).turn_right()

#---------------------------------------------------------------

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.address = None

    def set_name(self, name: str) -> 'Person':
        self.name = name
        return self

    def set_age(self, age: int) -> 'Person':
        self.age = age
        return self

    def set_address(self, address: str) -> 'Person':
        self.address = address
        return self

    def __str__(self) -> str:
        return f'{self.name}, {self.age}, {self.address}'


p = Person("John", 25)
p.set_address("123 Main St").set_age(26)

print(p)  # output: "John, 26, 123 Main St"
#--------------------------------------------------------

# super() function

class A:
    def __init__(self, value: int) -> None:
        self.value = value

    def increment(self) -> None:
        self.value += 1


class B(A):
    def __init__(self, value: int, step: int) -> None:
        super().__init__(value)
        self.step = step

    def increment(self) -> None:
        super().increment()
        self.value += self.step


b = B(5, 3)
b.increment()
print(b.value)  # output: 8
#-----------------------------------------------------

class Shape:
    def __init__(self, colour):
        self.colour = colour

    def __str__(self):
        return f"colour: {self.colour}"

class NicerShape(Shape):
    def __init__(self, colour, pattern):
        super().__init__(colour)
        self.pattern = pattern

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}, pattern: {self.pattern}"


class NicestShape(NicerShape):
    def __init__(self, colour, pattern, glitter):
        super().__init__(colour, pattern)
        self.glitter = glitter

    def __str__(self):
        nicer_str = super().__str__()
        return f"{nicer_str}, glitter: {self.glitter}"

shape = Shape("red")

print(shape)

nicer_shape = NicerShape("green", "dotted")
nicer_shape2 = NicerShape("blue", "striped")

print(nicer_shape)
print(nicer_shape2)

nicest = NicestShape('yellow', 'waves', True)
print(nicest)

#**************************************************************************************
# EXERCISE 2
# Create a class Currency that has the following properties:
#
# code: A 3-letter currency code (e.g. "USD", "EUR", "GBP"), amount, exchange_rate
# Create the following methods:
#
# 1) set_code: A method that accepts a 3-letter currency code and sets the code attribute
# of the object
# 2) set_amount: A method that accepts a float number and sets the amount attribute
# of the object
# 3) set_exchange_rate: A method that accepts a float number and sets the exchange_rate
# attribute of the object
# 4) convert: A method that accepts a 3-letter currency code and a float number
# representing the new exchange rate, and calculates the new amount of currency based
# on the exchange rate.
# 5) str: A method that returns a string representation of the Currency object in the
# following format "code: amount"
# Each method should return the instance of the class to allow method chaining.
#**************************************************************************************
class Currency:
    def __init__(self, code: str, amount: float, exchange_rate: float):
        self.code = code
        self.amount = amount
        self.exchange_rate = exchange_rate

    def set_code(self, code):
        self.code = code
        return self


    def set_amount(self, amount):
        self.amount = amount
        return self

    def set_exchange_rate(self, exchange_rate):
        self.exchange_rate = exchange_rate
        return self

    def convert(self, new_code: str, new_exchange_rate: float):
        self.amount = self.amount * (new_exchange_rate / self.exchange_rate)
        self.code = new_code
        self.exchange_rate = new_exchange_rate
        return self

    def __str__(self) -> str:
        return f'{self.code}: {self.amount:.2f}'


currency_exchange = Currency('USD', 100.0, 1.0)
result = currency_exchange.set_code('EUR').set_exchange_rate(0.85).convert('GBP', 0.75)
print(result)

#**************************************************************************************
# EXERCISE 3
# Create a class Animal with a method speak that prints "Animal can't speak"
#
# Create a class Dogs that inherits from Animals and overrides the speak method to print
# "Woof woof"
#
# Create a class Cats that inherits from Animals and overrides the speak method.
# But in this new method call the speak method from the Animals class using the super()
# function, after that print "Meow meow"
#**************************************************************************************
class Animals:
    def speak(self):
        print('Animals can\'t speak')


class Dogs(Animals):
    def speak(self):
        print('Woof woof')


class Cats(Animals):
    def speak(self):
        super().speak()
        print('Meow meow')


dog = Dogs()
dog.speak()

cat = Cats()
cat.speak()

#**************************************************************************************
# EXERCISE 4
# Create a class Person that has the following properties:
# name: A string representing the person's name
# age: An integer representing the person's age
# Create the following methods:
# get_name: A method that returns the person's name
# get_age: A method that returns the person's age
# str: A method that returns a string representation of the Person object
# in the following format: "name is age years old."

#Create a class Student that inherits from Person and adds the following properties:
# student_id: An integer representing the student's id
# major: A string representing the student's major
# Create the following methods:
# get_student_id: A method that returns the student's id
# get_major: A method that returns the student's major
# str: A method that returns a string representation of the Student object in the
# following format: "name is a age years old student of major major. Student id: student_id"

# Create a class GraduateStudent that inherits from Student and adds
# the following properties:
# program: A string representing the graduate student's program
# advisor: A string representing the graduate student's advisor
# Create the following methods:
# get_program: A method that returns the graduate student's program
# get_advisor: A method that returns the graduate student's advisor
# str: A method that returns a string representation of the GraduateStudent object
# in the following format: "name is a age years old graduate student of major major.
# Student id: student_id. program: program and advisor: advisor."
# init: This method should take in the same parameters as Person's init,
# but also take in additional parameters student_id, major, program, advisor
# and call the super's class init method with Person's parameters and set
# the additional parameters.Show examples with working code.

#**************************************************************************************
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def __str__(self):
        return f'{self.name} is {self.age} years old.'

class Student(Person):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major

    def get_student_id(self):
        return self.student_id

    def get_major(self):
        return self.major

    def __str__(self):
        bio = super().__str__()
        return f'{bio} Student of {self.major} major. Student id: {self.student_id}'


class GraduateStudent(Student):
    def __init__(self, name: str, age: int, student_id: int, major: str, program: str, advisor: str):
        super().__init__(name, age, student_id, major)
        self.program = program
        self.advisor = advisor

    def get_program(self):
        return self.program

    def get_advisor(self):
        return self.advisor

    def __str__(self):
        student_info = super().__str__()
        return f'{student_info}. Program: {self.program} and advisor: {self.advisor}.'

graduate_student = GraduateStudent('John', 21, 113267, 'Computer Science', 'PhD', 'Dr. Smith')
print(graduate_student)
