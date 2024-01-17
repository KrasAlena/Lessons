class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f'Student ID: {self.student_id}')
        print(f'Name: {self.name}')
        print(f'Grade: {self.grade}')
        if hasattr(self, 'major'):
            print(f'Major: {self.major}')
        else:
            print('Major: Computer Science')

    def promote(self):
        if self.grade < 12:
            self.grade += 1
            print(f'{self.name} has been promoted to grade {self.grade}')
        else:
            print(f'{self.name} has already completed their studies!')

# Example usage:
student1 = Student(student_id=1, name='John Doe', grade=10)
student1.major = 'Law'
student1.display_info()
student1.promote()

student2 = Student(student_id=2, name='Jane Smith', grade=12)
student2.display_info()
student2.promote()

#__________________________________________________________________________-
class Account:

    def __init__(self, amount=0):
        self.amount = amount

    def receive_money(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        if self.amount >= amount:
            self.amount -= amount
            print(f"withdrawn {amount}, {self.amount} remaining")
        else:
            print("not enough money")


account1 = Account()

account2 = Account(2000)

account1.withdraw(10)

account1.receive_money(5000)

account1.withdraw(10)

account2.withdraw(50)

#**************************************************************************************
# EXERCISE 1
# Create a Calculator class with main functionality: add, divide, multiply, subtract,
# etc.. Initiate class and show up some calculations.
#**************************************************************************************
class Calculator:
    def __init__(self, result = 0):
        self.result = result

    def add(self, num1):
        self.result += num1
        print(self.result)

    def sub(self, num1):
        self.result -= num1
        print(self.result)

    def div(self, num1):
        self.result /= num1
        print(self.result)

    def mult(self, num1):
        self.result *= num1
        print(self.result)

calc = Calculator()

calc.add(15)
calc.sub(2)
calc.mult(1)

#**************************************************************************************
# EXERCISE 2
# Create the instance attributes fullname and email in the Employee class.
# Given a person's first and last names:
#
# Form the fullname by simply joining the first and last name together, separated by a space.
# Form the email by joining the first and last name together with a . in between,
# and follow it with @company.com at the end. Make sure the entire email is in lowercase.
#**************************************************************************************

class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def fullname(self):
        self.fullname = f'{self.first_name} {self.last_name}'
        return self.fullname

    def email(self):
        self.email = f'{self.first_name}.{self.last_name}@company.com'.lower()
        return self.email


employee_info = Employee(first_name='John', last_name='Doe')
print(employee_info.fullname())
print(employee_info.email())

#**************************************************************************************
# EXERCISE 3
# Create a Book class that has two attributes:
#
# title
# author
# and two methods:
#
# A method named .get_title() that returns: "Title: " + the instance title.
# A method named .get_author() that returns: "Author: " + the instance author.
# and instantiate this class by creating 3 new books:
#
# Pride and Prejudice - Jane Austen (PP)
# Hamlet - William Shakespeare (H)
# War and Peace - Leo Tolstoy (WP)
# The name of the new instances should be PP, H, and WP, respectively.
# For instance, if I instantiated the following book using this Book class:
#
# Harry Potter - J.K. Rowling (HP)
#**************************************************************************************
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return f'Title: {self.title}'

    def get_author(self):
        return f'Author: {self.author}'


PP = Book(title='Pride and Prejudice', author='Jane Austen')
print(PP.get_title())
print(PP.get_author())

#**************************************************************************************
# EXERCISE 4
# A country can be said as being big if it is:
#
# Big in terms of population.
# Big in terms of area.
# Add to the Country class so that it contains the attribute is_big.
# Set it to True if either criteria are met:
#
# Population is greater than 20 million.
# Area is larger than 3 million square km.
# Also, create a method which compares a country's population density to another country object.
# Return a string in the following format:
#
# {country} has a {smaller / larger} population density than {other_country}
#**************************************************************************************
class Country:
    def __init__(self, country_name, population, area):
        self.population = population
        self.area = area
        self.country_name = country_name
        if self.population > 2e7 and self.area > 3e7:
            self.is_big = True
        else:
            self.is_big = False

    def density(self):
        self.density = self.population / self.area
        return self.density

    def compare(self, other_country):
        if self.density() > other_country.density():
            return f'{self.country_name} has a larger population density than {other_country.country_name}'
        return f'{self.country_name} has a smaller population density than {other_country.country_name}'

Lithuania = Country("Lithuania", 2800000, 65300)
Latvia = Country("Latvia", 1884000, 64589)

print(Lithuania.is_big)
print(Lithuania.compare(Latvia))

