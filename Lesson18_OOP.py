#---------------------------------------------------
# Access modifiers
#---------------------------------------------------
#              PUBLIC

class Employee:
    def __init__(self, name: str, sal: int):
        self.name = name # Public attribute
        self.sal = sal

emp = Employee("Ironman", 999000);
print(emp.sal)

#              PROTECTED

class Employee:
    def __init__(self, name: str, sal: int):
        self._name = name # Protected attribute
        self._sal = sal # Protected attribute

emp = Employee("Captain", 10000);
print(emp._sal)

#              PRIVATE

class Employee:
    def __init__(self, name: str, sal: int):
        self.__name = name # Private attribute
        self.__sal = sal # Private attribute

emp = Employee("Bill", 10000)
print(emp.__sal)

#---------------------------------------------------
# 1 OOP principle: INHERITANCE
#---------------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Subclasses must implement this method')


class Dog(Animal):
    def speak(self):
        return f'{self.name} says Woof!'


class Cat(Animal):
    def speak(self):
        return f'{self.name} says Meow!'


# Example usage:
dog = Dog('Buddy')
cat = Cat('Whiskers')

print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!

#---------------------------------------------------
# 2 OOP principle: ENCAPSULATION
#---------------------------------------------------
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self._account_holder = account_holder  # Private attribute with a single leading underscore
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds")

    def get_balance(self):
        return self._balance


# Example usage:
account = BankAccount("John Doe", 1000)

# Accessing private attributes using public methods
account.deposit(500)
account.withdraw(200)

# Accessing private attribute directly (not recommended)
# Use public methods instead for better encapsulation
print(account._balance)  # Output: 1300

#---------------------------------------------------
# 3 OOP principle: POLYMORPHISM
#---------------------------------------------------
'''Polymorphism in object-oriented programming refers to the ability of a class
to take on multiple forms. In Python, polymorphism is achieved through method overriding. '''
class Shape:
    def area(self):
        raise NotImplementedError('Subclasses must implement this method')


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


# Example usage:
square = Square(5)
circle = Circle(3)

shapes = [square, circle]

for shape in shapes:
    print(f'Area of {shape.__class__.__name__}: {shape.area()}')


#**************************************************************************************
# EXERCISE 2
# Write a class called CoffeeShop, which has three instance variables:
# 1) name : a string (basically, of the shop)
# 2) menu : a list of items (of dict type), with each item containing the item (name of the item),
# type (whether a food or a drink) and price.
# 3) orders : an empty list

# and seven methods:
# 1) add_order: adds the name of the item to the end of the orders list if it exists
# on the menu, otherwise, return "This item is currently unavailable!"
# 2) fulfill_order: if the orders list is not empty, return "The {item} is ready!".
# If the orders list is empty, return "All orders have been fulfilled!"
# 3) list_orders: returns the item names of the orders taken, otherwise, an empty list.
# 4) due_amount: returns the total amount due for the orders taken.
# 5) cheapest_item: returns the name of the cheapest item on the menu.
# 6) drinks_only: returns only the item names of type drink from the menu.
# 7) food_only: returns only the item names of type food from the menu.
# IMPORTANT: Orders are fulfilled in a FIFO (first-in, first-out) order.
#**************************************************************************************
class CoffeShop:
    def __init__(self, name: str, menu: dict):
        self.name = name
        self.menu = menu
        self.orders = []

    def add_order(self, item):
        item_names = []
        for menu_item in self.menu:
            item_names.append(menu_item['name'])
        if item in item_names:
           self.orders.append(item)
        else:
            return 'This item is currently unavailable!'

    def fulfill_order(self):
        if self.orders != []:
            item = self.orders.pop(0)
            return f'The {item} is ready!'
        else:
            return 'All orders have been fulfilled!'

#{'name': 'burger', 'type': 'food', 'price': 15}
    def list_orders(self):
        return self.orders

    def due_amount(self):
        amount = 0
        for order in self.orders:
            for item in self.menu:
                if item['name'] == order:
                    amount += item['price']
        return amount

    def cheapest_item(self):
        cheapest_item = self.menu[0]
        for item in self.menu:
            if item['price'] < cheapest_item['price']:
                cheapest_item = item
        return cheapest_item


    def drinks_only(self):
        drinks = []
        for item in self.menu:
            if item['type'] == 'drink':
                drinks.append(item['name'])
        return drinks

    def food_only(self):
        food = []
        for item in self.menu:
            if item['type'] == 'food':
                food.append(item['name'])
        return food

menu = [{'name': 'burger', 'type': 'food', 'price': 15}, {'name': 'sandwich', 'type': 'food', 'price': 10},
        {'name': 'coke', 'type': 'drink', 'price': 2}, {'name': 'coffee', 'type': 'drink', 'price': 3}]

cafe = CoffeShop('Mac', menu)

cafe.add_order('coffee')
print(cafe.orders)
print(cafe.due_amount())
cafe.add_order('burger')
cafe.add_order('coke')
print(cafe.orders)
print(cafe.list_orders())
print(cafe.food_only())
print(cafe.drinks_only())
print(cafe.cheapest_item())
print(cafe.fulfill_order())
print(cafe.due_amount())