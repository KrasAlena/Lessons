#*******************************************
# __str__
#*******************************************
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


p = Person("John", 30)
print(p) # Person(name=John, age=30)

#*******************************************
# __repr__
#*******************************************
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"


p = Person("John", 30)
print(p) # Person('John', 30)
print(repr(p)) # Person('John', 30)

#*******************************************
# __eq__
#*******************************************
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __eq__(self, other: 'Person') -> bool:
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False


p1 = Person("John", 30)
p2 = Person("John", 30)
p3 = Person("Jane", 25)

print(p1 == p2) # True
print(p1 == p3) # False

#*******************************************
# __add__
#*******************************************
class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector') -> 'Vector':
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("unsupported operand type(s) for +: 'Vector' and '{}'".format(type(other).__name__))


v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3.x, v3.y) # 4 6

#*******************************************
# __len__
#*******************************************
class MyList:
    def __init__(self, items: list):
        self.items = items

    def __len__(self) -> int:
        return len(self.items)


ml = MyList([1, 2, 3, 4, 5])
print(len(ml)) # 5

#*******************************************
# __bool__
#*******************************************
class MyNumber:
    def __init__(self, num: int):
        self.num = num

    def __bool__(self):
        return bool(self.num)


mn = MyNumber(5)
print(bool(mn)) # True
mn2 = MyNumber(0)
print(bool(mn2)) # False

#*******************************************
# __getitem__
#*******************************************
class MyDict:
    def __init__(self, data: dict):
        self.data = data

    def __getitem__(self, key: str):
        return self.data[key]


md = MyDict({'a':1, 'b':2})
print(md['a']) # 1

#*******************************************
# __missing__
#*******************************************
class MyDict(dict):
    def __missing__(self, key: str):
        return 'default'


md = MyDict({'a': 1, 'b': 2})
print(md['a'])  # 1
print(md['c'])  # default

#**************************************************************************************
# EXERCISE 1
# Create a class called Product that takes a name and price as parameters and has
# __str__ and __repr__ methods defined.
#
# The __str__ method should return a string in the format "Product: name, Price: price"
# The __repr__ method should return a string in the format "Product('name', price)"
#**************************************************************************************
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'Product: {self.name}, Price: {self.price}$'

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"


p = Product('paper', 30)
print(p)
print(repr(p))

#**************************************************************************************
# EXERCISE 2
# Create a class called MyQueue that has __bool__, __repr__ and __len__ methods defined.
#
# The __bool__ method should return True if the queue has any items and False if it is empty.
# The __repr__ method should return a string in the format MyQueue(items) where items is
# the list of items in the queue.
# The __len__ method should return the number of items in the queue.
#**************************************************************************************
class MyQueue:
    def __init__(self, items: list):
        self.items = items

    def __bool__(self):
        return bool(self.items)

    def __repr__(self):
        return f'MyQueue {self.items}'

    def __len__(self):
        return len(self.items)


queue = MyQueue([])

print(len(queue))
print(bool(queue))
print(repr(queue))

#**************************************************************************************
# EXERCISE 3
# Create a class called Book that takes title, author, and ISBN as parameters. The class
# should have __bool__, __repr__, __len__, __str__, __eq__, __add__, and __getitem__ methods defined.
#
# The __bool__ method should return True if the book has a title, False otherwise.
# The __repr__ method should return a string in the format "Book(title, author, ISBN)"
# where title, author and ISBN are the respective attributes of the class
# The __len__ method should return the number of pages of the book
# The __str__ method should return a string in the format "title by author (ISBN)"
# The __eq__ method should compare two books and return True if both ISBN are the same
# and False otherwise.
# The __add__ method should add two books and return a new book object that contains the
# contents of both books concatenated and the title of the new book should be the title of the first book
# The __getitem__ method should return the title of the book if the index passed is 0,
# and the author of the book if the index passed is 1.
#**************************************************************************************
class Book:
    def __init__(self, title: str, author: str, ISBN: int, pages_number: int):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.pages_number = pages_number

    def __bool__(self):
        return len(self.title) != 0

    def __repr__(self):
        return f'Book({self.title}, {self.author}, {self.ISBN})'

    def __len__(self):
        return self.pages_number

    def __str__(self):
        return f'{self.title} by {self.author} ({self.ISBN})'

    def __eq__(self, other: 'Book') -> bool:
        if isinstance(other, Book):
            return self.ISBN == other.ISBN
        return False

    def __add__(self, other):
        if isinstance(other, Book):
            if other.author == self.author:
                author = self.author
            else:
                author = self.author + ', ' + other.author
            return Book(self.title, author, self.ISBN, other.pages_number + self.pages_number)
        raise TypeError()

    def __getitem__(self, ind: int):
        if ind == 0:
            return self.title
        elif ind == 1:
            return self.author
        raise IndexError('The index doesn\'t exist')


book1 = Book('Alice in Wonderland', 'Lewis Caroll', 90871456869, 313)
book2 = Book('Harry Potter', 'J.K. Rowling', 9780545582889, 500)

# Test __bool__ method
print(bool(book1))
print(bool(Book('', '', 0, 0)))

# Test __repr__ method
print(repr(book1))

# Test __len__ method
print(len(book1))

# Test __str__ method
print(str(book1))

# Test __eq__ method
print(book1 == book2)

# Test __add__ method
book3 = book1 + book2
print(book3)
print(len(book3))

# Test __getitem__ method
print(book1[0])
print(book1[1])