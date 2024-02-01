#**************************************************************************************
# EXERCISE 1
#
# Create an abstract class Animal with which takes name of animal as an input and
# initialize it. The create speak abstract method, to be overridden by subclasses.
# And get_name method which returns name of the animal.
#
# Now create two subclasses of Animals: Dog and Cat which overrides the speak method,
# and provide the implementation which returns a string "Dog says Woof!" and
# "Cat says Meow!" respectively.
#**************************************************************************************
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        raise NotImplemented('Subclasses must implement the speak method')

    def get_name(self):
        return self.name

class Dog(Animal):
    def speak(self):
        return 'Dog says Woof!'

class Cat(Animal):
    def speak(self):
        return 'Cat says Meow!'

cat = Cat('Fluffy')
print(cat.speak())
dog = Dog('Ficha')
print(dog.speak())

#**************************************************************************************
# EXERCISE 2
#
# Create an abstract class Money which takes currency and value as input and
# initializes it. A class must have these methods:
#
# get_value method which returns the value of the money.
# get_currency method which returns the currency of the money.
# convert_to_currency abstract method, which takes target currency and conversion rate
# as input and converts the value of the money to the target currency.

# Now create two subclasses of Money: Cash and Card. The Cash class should take the
# denomination of the cash as input in the constructor, and should implement
# the convert_to_currency method. The Card class should take the credit limit of
# the card as input in the constructor, and should implement the convert_to_currency
# method using the conversion rate to convert the value of the card to the target currency.
#**************************************************************************************
from abc import ABC, abstractmethod

class Money(ABC):
    def __init__(self, currency, value):
        self.currency = currency
        self.value = value

    def get_value(self):
        return self.value

    def get_currency(self):
        return self.currency

    @abstractmethod
    def convert_to_currency(self, target_currency, rate):
        raise NotImplemented('Subclasses must implement the convert_to_currency method')


class Cash(Money):
    def __init__(self, currency, value):
        super().__init__(currency, value)

    def convert_to_currency(self, target_currency, rate):
        if self.currency != target_currency:
            self.value *= rate[target_currency] / rate[self.currency]
            self.currency = target_currency

class Card(Money):
    def __init__(self, currency, value, credit_limit):
        super().__init__(currency, value)
        self.credit_limit = credit_limit

    def convert_to_currency(self, target_currency, rate):
        self.value = round(min(self.value, self.credit_limit) * rate[self.currency] * rate[target_currency], 2)
        self.currency = target_currency

rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
}

# Example usage with Cash
cash = Cash(currency='USD', value=100.0)
print('Original Cash:')
print(f'Value: ${cash.get_value()}, Currency: {cash.get_currency()}')

# Convert Cash to EUR
cash.convert_to_currency(target_currency='EUR', rate=rates)
print('\nConverted Cash:')
print(f'Value: ${cash.get_value()}, Currency: {cash.get_currency()}')

# Example usage with Card
card = Card(currency='EUR', value=500.0, credit_limit=1000.0)
print('\nOriginal Card:')
print(f'Value: ${card.get_value()}, Currency: {card.get_currency()}')

# Convert Card to GBP
card.convert_to_currency(target_currency='GBP', rate=rates)
print('\nConverted Card:')
print(f'Value: ${card.get_value()}, Currency: {card.get_currency()}')

#**************************************************************************************
# EXERCISE 4
#
# Create a Calculator program : it should contain abstract class with methods (abstract
# and not), base class, geometry, arithmetic calculator classes. Every subclass should
# have at least 5 methods to make some meaningful calculus operations.
#**************************************************************************************
from abc import ABC, abstractmethod
import math

class Calc(ABC):

    def get_values(self):
        pass
    @abstractmethod
    def get_result(self):
        raise NotImplemented('Subclasses must implement the get_result method')

class Geometry(Calc):
    pass

class Arithmetic(Calc):

    def addition(self, a, b):
        return a + b

    def substruction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError('Division by zero is not allowed')

    def get_result(self):
        pass

    print("Choose a calculator:")
    print("1. Arithmetic Calculator")
    print("2. Geometry Calculator")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        calculator = Arithmetic()
    elif choice == '2':
        calculator = Geometry()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        exit()

    result = calculator.get_result()
    print("Result:", result)