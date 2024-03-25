# **************************************************************************************
# EXERCISE 2
#
# https://github.com/robotautas/kursas/blob/master/DB/db4/uzduotis.md
# **************************************************************************************
import sqlite3
from faker import Faker
import random


def create_database():
    with sqlite3.connect('store.db') as conn:
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS customer (
            id INTEGER PRIMARY KEY,
            f_name VARCHAR(100) NOT NULL,
            l_name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE
        )""")

        c.execute("""CREATE TABLE IF NOT EXISTS status (
            id INTEGER PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        )""")

        c.execute("""CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price FLOAT
        )""")

        c.execute("""CREATE TABLE IF NOT EXISTS order_ (
            id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            date_ DATE,
            status_id INTEGER,
            FOREIGN KEY (customer_id) REFERENCES customer (id),
            FOREIGN KEY (status_id) REFERENCES status (id)
        )""")

        c.execute("""CREATE TABLE IF NOT EXISTS product_order (
            order_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            FOREIGN KEY (product_id) REFERENCES product (id),
            FOREIGN KEY (order_id) REFERENCES order_ (id)
        )""")

        statuses = ['approved', 'in progress', 'fulfilled', 'rejected']
        for status in statuses:
            c.execute('INSERT OR IGNORE INTO status (name) VALUES (?)', (status,))

        conn.commit()


fake = Faker()


def generate_customers(num_customers):
    with sqlite3.connect('store.db') as conn:
        c = conn.cursor()
        for _ in range(num_customers):
            f_name = fake.first_name()
            l_name = fake.last_name()
            email = fake.email()
            c.execute('INSERT INTO customer (f_name, l_name, email) VALUES (?, ?, ?)', (f_name, l_name, email))
        conn.commit()
        print(f'{num_customers} customers inserted.')


def generate_products(num_products):
    with sqlite3.connect('store.db') as conn:
        c = conn.cursor()
        for _ in range(num_products):
            name = fake.word()
            price = round(random.uniform(1, 1000), 2)
            c.execute('INSERT INTO product (name, price) VALUES (?, ?)', (name, price))
        conn.commit()
        print(f'{num_products} products inserted.')


def generate_orders(num_orders):
    with sqlite3.connect('store.db') as conn:
        c = conn.cursor()
        for _ in range(num_orders):
            customer_id = random.randint(1, 3)  # Assuming at least 3 customers exist
            date_ = fake.date()
            status_id = random.randint(1, 4)  # Assuming at least 4 statuses exist
            c.execute('INSERT INTO order_ (customer_id, date_, status_id) VALUES (?, ?, ?)', (customer_id, date_, status_id))
            order_id = c.lastrowid
            # Random number of products for each order (1 to 3)
            num_products = random.randint(1, 3)
            for _ in range(num_products):
                product_id = random.randint(1, 5)  # Assuming at least 5 products exist
                quantity = random.randint(1, 10)  # Random quantity between 1 and 10
                c.execute('INSERT INTO product_order (order_id, product_id, quantity) VALUES (?, ?, ?)', (order_id, product_id, quantity))
        conn.commit()
        print(f'{num_orders} orders inserted.')


# Create database and tables
create_database()

# Generate data
generate_customers(3)
generate_products(10)
generate_orders(5)