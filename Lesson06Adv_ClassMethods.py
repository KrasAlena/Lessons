class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    @classmethod
    def from_square(cls, side_length: float) -> 'Rectangle':
        return cls(side_length, side_length)


rectangle1: Rectangle = Rectangle(3.0, 4.0)
rectangle2: Rectangle = Rectangle.from_square(2.0)

print(rectangle1.area())  # 12.0
print(rectangle2.area())  # 4.0

#**************************************************************************************
# EXERCISE 1
# Create a class method to return the factorial of a given number.
#**************************************************************************************
class MathOperations:
    @classmethod
    def factorial(cls, n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * cls.factorial(n-1)

print(MathOperations.factorial(5))

#**************************************************************************************
# EXERCISE 4
# Create a simple bank account class, BankAccount, with the following specifications:
#
# The BankAccount class should have an attribute balance which starts at 0.
# It should have an instance method deposit that allows an amount to be added to the balance.
# It should have an instance method withdraw that allows an amount to be taken from the balance.
# If the balance is less than the withdrawal amount, print a message that says "Insufficient funds".
# Add a class method from_balance that takes a starting balance as an argument and returns
# a new BankAccount instance with that starting balance.
# Add a static method transfer that takes two BankAccount instances and an amount as arguments.
# It should withdraw the amount from the first account and deposit it into the second account.
#**************************************************************************************
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print('Insufficient funds')
        self.balance -= amount

    @classmethod
    def from_balance(cls, balance):
        new_account = cls()
        new_account.balance = balance
        return new_account

    @staticmethod
    def transfer(acc1, acc2, amount):
        if acc1.balance < amount:
            print('Insufficient funds for transfer')
        acc1.balance -= amount
        acc2.balance += amount


account1 = BankAccount.from_balance(100)
account1.deposit(50)
print(account1.balance)

account2 = BankAccount.from_balance(200)
account2.withdraw(30)
print(account2.balance)

BankAccount.transfer(account1, account2, 50)
print(account1.balance)
print(account2.balance)

#**************************************************************************************
# EXERCISE 5
# Create a SpaceStation class with the following specifications:
#
# The SpaceStation class should have an attribute astronauts which is a list of dictionaries.
# Each dictionary represents an astronaut and has keys: name, nationality, and mission_duration.
# It should have an instance method add_astronaut that takes a name, nationality, and mission
# duration, creates a new astronaut dictionary, and adds it to the astronauts list.
# It should have an instance method find_astronaut that takes a name and returns the astronaut
# dictionary with that name, or None if no such astronaut is found.
# Add a class method from_astronaut_list that takes a list of astronauts (each represented
# as a dictionary) and returns a new SpaceStation instance with those astronauts.
# Add a static method is_long_term_mission that takes an astronaut dictionary and returns True
# if the astronaut's mission duration is more than 6 months, and False otherwise.
# Add an instance method remove_astronaut that takes a name and removes the astronaut
# with that name from the astronauts list.
#**************************************************************************************
class SpaceStation:
    def __init__(self, astronauts: list):
        self.astronauts = astronauts #[{'name': 'John', 'nationality': 'USA', 'mission_duration': 9}]

    def add_astronaut(self, name: str, nationality: str, mission_duration: int):
        new_astronaut = {'name': name, 'nationality': nationality, 'mission_duration': mission_duration}
        self.astronauts.append(new_astronaut)

    def find_astronaut(self, name):
        for astronaut in self.astronauts:
            if astronaut['name'] == name:
                return astronaut
        return None

    @classmethod
    def from_astronaut_list(cls, astronauts: list):
        return cls(astronauts)

    @staticmethod
    def is_long_term_mission(astronaut: dict):
        if astronaut['mission_duration'] > 6:
            return True
        else:
            return False

    def remove_astronaut(self, name):
        self.astronauts = [astronaut for astronaut in self.astronauts if astronaut['name'] != name]


station = SpaceStation([{'name': 'John', 'nationality': 'USA', 'mission_duration': 9},
                        {'name': 'Marco', 'nationality': 'Italy', 'mission_duration': 5},
                        {'name': 'Alice', 'nationality': 'Norway', 'mission_duration': 11}])

station.add_astronaut('Ian', 'Spain', 4)
print(station.astronauts)
print(station.find_astronaut('Marco'))
print(station.find_astronaut('Ivan'))

station.remove_astronaut('John')
print('New Astronauts:', station.astronauts)

new_astronauts = [{'name': 'Jessica', 'nationality': 'Canada', 'mission_duration': 8},
                  {'name': 'David', 'nationality': 'Germany', 'mission_duration': 3}]
new_space_station = SpaceStation.from_astronaut_list(new_astronauts)

astronaut = {'name': 'Jessica', 'nationality': 'Canada', 'mission_duration': 8}
is_long_term = SpaceStation.is_long_term_mission(astronaut)
print('Is Long Term Mission:', is_long_term)
astronaut = {'name': 'David', 'nationality': 'Germany', 'mission_duration': 3}
is_long_term = SpaceStation.is_long_term_mission(astronaut)
print('Is Long Term Mission:', is_long_term)

new_space_station.remove_astronaut('David')
print('New Astronauts:', new_space_station.astronauts)

