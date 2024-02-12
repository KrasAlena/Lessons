from dataclasses import dataclass



@dataclass
class Point:
    x: float
    y: float

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

#**************************************************************************************
# EXERCISE 1
# You have been asked to create a simple inventory management system for a small retail
# store. You need to define a Product class using the dataclass module that represents
# a product in the store. Each Product should have a unique ID, a name, a description,
# a price, and a quantity in  stock. You also need to implement a method calculate_total_cost
# that calculates the total cost of a given number of items of the product, taking into
# account any discounts that may apply.
#**************************************************************************************
from dataclasses import dataclass
@dataclass
class Product:
    ID: int
    name: str
    description: str
    price: float
    stock: int
    discount: int = 0

    def calculate_total_cost(self, qty):
        total_cost = self.price * qty
        if self.discount > 0:
            total_cost -= total_cost * (self.discount / 100)
        return total_cost


p = Product(166363, 'laptop', 'MacBook Pro, Apple M2 Pro chip, 16 GB', 1999.90, 570, 10)
print(p.calculate_total_cost(13))

#**************************************************************************************
# EXERCISE 2
# Create a set of data classes to model an online bookstore management system.
# The classes should include Author, Book, Customer, and Order. Your goal is to design
# a system that enables the management of books, authors, customers, and orders in an
# online bookstore.
#
# Author Class:
# Attributes: author_id (int), name (str), birth_year (int)).

# Book Class:
# Attributes: book_id (int), title (str), author (Author), publication_year (int),
# price (float), quantity_in_stock (int).
# Add a method sell that reduces the quantity_in_stock when a book is sold.

# Customer Class:
# Attributes: customer_id (int), name (str), email (str).

# Order Class:
# Attributes: order_id (int), customer (Customer), books (List[Book]),
# total_price (float), status (str) - either "Pending" or "Shipped".
# Initialize the attributes in the __init__ method (override).
# Add a method calculate_total_price that calculates the total price of the order
# based on the books' prices and quantities.
# Add a method ship_order that changes the order status to "Shipped" and updates the
# stock quantity for each book.
#**************************************************************************************
from dataclasses import dataclass
from typing import List

@dataclass
class Author:
    author_id: int
    name: str
    birth_year: int

@dataclass
class Book:
    book_id: int
    title: str
    author: Author
    publication_year: int
    price: float
    quantity_in_stock: int

    def sell(self):
        if self.quantity_in_stock > 0:
            self.quantity_in_stock -= 1
        else:
            print(f'Book "{self.title}" is currently unavailable.')

@dataclass
class Customer:
    customer_id: int
    name: str
    email: str


@dataclass
class Order:
    order_id: int
    customer: Customer
    books: List[Book]
    total_price: float
    status: str = 'Pending'

    def __init__(self, order_id: int, customer: Customer, books: List[Book], status: str):
        self.order_id = order_id
        self.customer = customer
        self.books = books
        self.total_price = 0
        self.status = 'Pending'

    def calculate_total_price(self):
        total = sum(book.price for book in self.books)
        return total

    def ship_order(self):
        if self.status == 'Pending':
            for book in self.books:
                book.sell()
            self.status = 'Shipped'
            print(f'Order {self.order_id} has been shipped.')
        else:
            print(f'Order {self.order_id} has already been shipped.')


author1 = Author(1234, 'Lewis Caroll', 1832)
author2 = Author(6578, 'Agatha Christie', 1890)

book1 = Book(76457, 'Murder on the Orient Express', author2, 1934, 20.0, 113)
book2 = Book(76458, 'Alice in Wonderland', author1, 1965, 15.7, 103)

book1.sell()
print(book1.quantity_in_stock)

customer1 = Customer(5674, 'John Doe', 'jonh.doe@example.com')

order1 = Order(46535, customer1, [book1, book1, book2], '')
print(order1.calculate_total_price())
order1.ship_order()

print(book1.quantity_in_stock)
print(book2.quantity_in_stock)

#**************************************************************************************
# EXERCISE 3
# You need to create a program to manage a list of books in a library. Each book has a
# title, an author, a publication year, and an ISBN. You need to define a Book class
# using the dataclass module that contains attributes for these properties. You also
# need to implement a Library class that manages a list of books. The Library class
# should allow you to add and remove books from the library, search for books by title
# or author, and display the list of books currently in the library.
#**************************************************************************************
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    publication_year: int
    ISBN: str

    def __repr__(self):
        return f'Book: {self.title}, {self.author}, {self.publication_year}, {self.ISBN}'
@dataclass
class Library:
    book_list: []

    def add_book(self, Book):
        if Book not in self.book_list:
            self.book_list.append(Book)
        else:
            print(f'{Book.title} by {Book.author} is already in the library list')

    def remove_book(self, Book):
        if Book in self.book_list:
            self.book_list.remove(Book)
        else:
            raise ValueError(f'There is no {Book.title} by {Book.author} in our library')

    def search_book_by_title(self, title):
        found = False
        for book in self.book_list:
            if book.title == title:
                print(book)
                found = True
        if not found:
            print(f'Book with title "{title}" isn\'t in our list')

    def search_book_by_author(self, author):
        found = False
        for book in self.book_list:
            if book.author == author:
                print(book)
                found = True
        if not found:
            print(f'Book by "{author}" isn\'t in our list')

    def get_book_list(self):
        return self.book_list


book1 = Book('Murder on the Orient Express', 'Agatha Christie', 1934, '1934-20-0-113')
book2 = Book('Alice in Wonderland', 'Lewis Carroll', 1865, '1965-27-11-1100')
book3 = Book('Pillow problems', 'Lewis Carroll', 1893, '1965-27-11-1100')

library = Library([])
library.add_book(book1)
library.add_book(book2)

print(library.get_book_list())

library.remove_book(book1)
print(library.get_book_list())

library.search_book_by_title('Screem')
# library.search_book_by_title('Alice in Wonderland')

library.add_book(book3)
library.search_book_by_author('Lewis Carroll')

#**************************************************************************************
# EXERCISE 4
# You are tasked with designing an advanced Employee Management System using Python
# data classes, functional programming operations, and various methods for analysis
# and manipulation of employee data.
#
# Employee Class:
# Create a data class named Employee to represent an employee. The class should have
# attributes for employee_id, name, age, salary, and department.
#
# Department Class: Create a data class named Department to represent a department.
# The class should have attributes for department_id, name, and employe (List[Employee]).
# Add a method named average_salary that calculates and returns the average salary of
# employees in the department.

# EmployeeManagement Class: Create a data class named EmployeeManagement to manage
# multiple departments and employees. The class should have an attribute for departments
# (List[Department]).
# Add a method named total_salary that calculates and returns the total salary of all
# employees in the organization.
# Add a method named get_employees_in_age_range that takes a minimum and maximum age
# and returns a list of employees within that age range.
# Add a method named sort_employees_by_salary that returns a sorted list of employees
# by their salary in descending order.
# Add a method named filter_employees_by_department that takes a department name and
# returns a list of employees in that department.
#
# Functional Operations:
# Utilize functional programming operations such as map, filter, and sorted where
# appropriate in the implementation of the methods. Demonstrate the use of these
# operations to enhance the readability and efficiency of your code.
#
# Test Cases:
# Create a sample dataset with multiple employees and departments to thoroughly test
# your system. Use the implemented methods to perform various analyses, such as
# calculating average salaries, sorting employees, and filtering employees by criteria.
#**************************************************************************************
from dataclasses import dataclass
from typing import List

@dataclass
class Employee:
    employee_id: str
    name: str
    age: int
    salary: float
    department: 'Department'

@dataclass
class Department:
    department_id: str
    name: str
    employees: List[Employee]

    def average_salary(self):
        if len(self.employees) == 0:
            return 0
        total_salary = sum(map(lambda employee: employee.salary, self.employees))
        return round(total_salary / len(self.employees), 2)


@dataclass
class EmployeeManagement:
    departments: List[Department]

    def total_salary(self):
        total = sum(department.average_salary() * len(department.employees) for department in self.departments)
        return total

    def get_employees_in_age_range(self, min_age, max_age):
        employees_in_range = []
        for department in self.departments:
            for employee in department.employees:
                if min_age <= employee.age <= max_age:
                    employees_in_range.append(employee)
        return employees_in_range

    def sort_employees_by_salary(self):
        all_employees = [employee for department in self.departments for employee in department.employees]
        sorted_employees = sorted(all_employees, key=lambda employee: employee.salary, reverse=True)
        return sorted_employees

    def filter_employees_by_department(self, department_name):
        for department in self.departments:
            if department_name == department.name:
                return department.employees


employee1 = Employee('0978675', 'John Doe', 27, 2500.5, None)
employee2 = Employee('0978676', 'Jack Smith', 31, 2700.0, None)
employee3 = Employee('0978677', 'Jane Black', 21, 1800.1, None)
employee4 = Employee('0978678', 'Kelly Bird', 43, 3000.0, None)
employee5 = Employee('0978679', 'Ann White', 41, 2600.7, None)

department1 = Department('0913', 'HR', [employee3, employee5])
department2 = Department('0910', 'Marketing', [employee1, employee2, employee4])

print(department1.average_salary())
print(department2.average_salary())

org = EmployeeManagement([department1, department2])

print(org.total_salary())
print(org.get_employees_in_age_range(25, 35))
print(org.sort_employees_by_salary())
print(org.filter_employees_by_department('HR'))
print(org.filter_employees_by_department('Marketing'))

