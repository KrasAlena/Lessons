# **************************************************************************************
# EXERCISE 1
# Create a table named Students with the following columns:
#
# id (integer, primary key)
# name (text)
# age (integer)
# grade (text)
# **************************************************************************************
import sqlite3

conn = sqlite3.connect('students.db')
c = conn.cursor()

with conn:
    c.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER, PRIMARY KEY, 
                name TEXT,
                age INTEGER,
                grade TEXT
            )
        ''')
    # **************************************************************************************
    # Insert some data
    # **************************************************************************************
    c.execute('''
            INSERT INTO students (name, age, grade) VALUES 
            ('Thomas', 17, 'A'), 
            ('Erika', 18, 'B'), 
            ('Silvia', 19, 'A'),
            'John', 20, 'C'), 
            ('Monica', 21, 'B'), 
            ('Paul', 21, 'B')
        ''')
    # **************************************************************************************
    # Retrieve all records from the Students table.
    # Retrieve only the names of all students.
    # Retrieve the names and ages of all students.
    # Retrieve the names of students aged 20 or younger.
    # Retrieve the names of students in grade "A".
    # **************************************************************************************
    c.execute('SELECT * FROM students')
    c.execute('SELECT name FROM students')

