import sqlite3

with sqlite3.connect("car_washing.db") as conn:
    c = conn.cursor()

    # c.execute("""CREATE TABLE IF NOT EXISTS customers (
    # first_name text,
    # last_name text,
    # phone_number text,
    # gender text,
    # car_id integer
    # )""")
    #
    # c.execute("""CREATE TABLE IF NOT EXISTS cars (
    # plate_number text,
    # make text,
    # model text,
    # year integer
    # )""")
    #
    # new_customers = [
    # ("Jonas", "Jonaitis", "+37088885", "Male", 2),
    # ("Petras", "Jonaitis", "+370888885", "Male", 4),
    # ("Inga", "Guod", "+370878885", "Female", 5),
    # ("John", "Smit", "+370838885", "N/A", 1),
    # ("Isa", "Wall", "+370885885", "Female", 3),
    # ("Isa", "Wall", "+370888485", "Male", 6),
    #
    # ]
    #
    # c.executemany("""INSERT INTO customers VALUES(?,?,?,?,?)""",
    # new_customers)
    #
    # new_cars = [
    # ("AVB154", "Porsche", "911", 2017),
    # ("GNG123", "BMW", "525", 2005),
    # ("GTG123", "Opel", "Zefira", 2005),
    # ("GNG923", "Mini", "Super", 2012),
    # ("GNG923", "Peugout", "500", 2002),
    # ("GNG923", "Nissan", "Q", 2014),
    # ]
    #
    # c.executemany("""INSERT INTO cars VALUES(?,?,?,?)""",
    # new_cars)
    '''
    Show first name, last name, plate number of each car owner
    '''
    c.execute('''
        SELECT customers.first_name, customers.last_name, cars.plate_number
        FROM customers
        LEFT JOIN cars
        ON customers.car_id = cars.rowid
    ''')
    print(c.fetchall())
    '''
    Last names, car make, car year of all owners
    '''
    c.execute('''
        SELECT customers.last_name, cars.make, cars.year
        FROM customers
        LEFT JOIN cars
        ON customers.car_id = cars.rowid
    ''')
    print(c.fetchall())
    '''
    First name, car make, phone number for all male customers. Order the result in a descending alphabetical manner
    '''
    c.execute('''
        SELECT first_name, phone_number
        FROM customers
        WHERE gender = 'Male'
    ''')
    print(c.fetchall())
    '''
    The phone numbers of all car owners whose cars are between 2010 and 2020
    '''
    c.execute('''
        SELECT customers.phone_number
        FROM customers
        JOIN cars
        ON customers.car_id = cars.rowid
        WHERE cars.year BETWEEN 2010 AND 2020
    ''')
    print(c.fetchall())

    '''
    Count the makes of all cars
    '''
    c.execute('SELECT make, COUNT(*) as count FROM cars GROUP BY make')
    print(c.fetchall())

    '''
    Count the amount of which gender customers our car wash db has
    '''
    c.execute('''
        SELECT gender, COUNT(*) as count 
        FROM customers 
        GROUP BY gender''')
    print(c.fetchall())

'''
Difficult:
Write a function that creates fake data for your database (for example, generate names, last names, phone numbers,
cars info, etc). At first, don't worry about the fact that the names are random collection of letters "ksdfjhasdAASD".
Later, think about how this could be improved and actual names be generated. Perhaps make a fixed list of names, last names, car makes, models to choose from and generate pick them randomly
'''
import sqlite3
from faker import Faker

conn = sqlite3.connect('test.db')
c = conn.cursor()


def generate_name():
    fake = Faker()
    full_name = fake.name().split()
    first_name = full_name[0]
    last_name = full_name[1]
    return first_name, last_name


def generate_clients(n):
    for _ in range(n):
        first_name, last_name = generate_name()
        c.execute('INSERT INTO customers (first_name, last_name) VALUES (?, ?)', (first_name, last_name))
    conn.commit()
    print(f'{n} clients generated and inserted into the database.')


generate_clients(10)

conn.close()
