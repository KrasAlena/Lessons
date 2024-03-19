'''
+ Select all data from the "EMPLOYEES" table.
+ Select all data from the column "BIRTH_DATA" in the table "EMPLOYEE".
+ Select all data from the columns "NAME", "LAST NAME", "POSITIONS" - in the table "EMPLOYEES".
+ Select the different values from the DEPARTMENT_NAME column in the EMPLOYEES table.
+ Select all data about employees who work in the Production department.
+ Select the data for Giedrius's position
+ Select all data about employees whose date of birth is 19-09-1986
+ Select the names of employees whose last name is Sabutis
+ Select data (name and surname) about programmers from the Production department
+ Insert a new employee into the "EMPLOYEES" table by filling in all the required fields (name, surname, date of birth, position and department name).
+ Insert a new employee into the "EMPLOYEES" table, filling only the fields (name, surname, date of birth). Leave the position and department name blank.
+ Fill in the remaining blank fields in the EMPLOYEES table in the record you inserted earlier. Assign the position and department to the employee.
+ Delete the record in the EMPLOYEES table that has a date of birth that you created.
+ Insert two employees with the last name Antanaitis whose duties would be "Programmer".
+ Change the position of both Antanaitis to "Tester" in one sentence.
+ Count how many Testers work in the company.
'''
import sqlite3

conn = sqlite3.connect('darbuotojai.db')
c = conn.cursor()

with conn:
    c.execute('SELECT * FROM darbuotojai')
    print(c.fetchall())
    c.execute('SELECT GIMIMO_DATA FROM darbuotojai')
    print(c.fetchall())
    c.execute('SELECT VARDAS, PAVARDĖ, PAREIGOS FROM darbuotojai')
    print(c.fetchall())
    c.execute('SELECT DISTINCT SKYRIUS_PAVADINIMAS FROM darbuotojai')
    print(c.fetchall())
    c.execute('SELECT * FROM darbuotojai WHERE SKYRIUS_PAVADINIMAS = "Gamybos"')
    print(c.fetchall())
    c.execute('SELECT PAREIGOS FROM darbuotojai WHERE VARDAS = "Giedrius"')
    print(c.fetchall())
    c.execute('SELECT * FROM darbuotojai WHERE GIMIMO_DATA = "1986-09-19"')
    print(c.fetchall())
    c.execute('SELECT VARDAS FROM darbuotojai WHERE PAVARDĖ = "Sabutis"')
    print(c.fetchall())
    c.execute('SELECT VARDAS, PAVARDĖ FROM darbuotojai WHERE PAREIGOS = "Programuotojas" AND SKYRIUS_PAVADINIMAS = '
              '"Gamybos"')
    print(c.fetchall())
    # c.execute('INSERT INTO darbuotojai (VARDAS, PAVARDĖ, GIMIMO_DATA, PAREIGOS, SKYRIUS_PAVADINIMAS) VALUES ("Rasa", '
    #           '"Kirslite", "1984-08-11", "Buhalterė", "Finansų")')
    # c.execute('INSERT INTO darbuotojai (VARDAS, PAVARDĖ, GIMIMO_DATA) VALUES ("Tomas", "Jonaitis", "1990-01-13")')
    # c.execute('''
    #     UPDATE darbuotojai
    #     SET PAREIGOS = 'Programuotojas', SKYRIUS_PAVADINIMAS = 'Gamybos'
    #     WHERE VARDAS = 'Tomas' AND PAVARDĖ = 'Jonaitis';
    # ''')
    # c.execute('DELETE from darbuotojai WHERE GIMIMO_DATA = "1990-01-13"')
    # c.execute('INSERT INTO darbuotojai (PAVARDĖ, PAREIGOS) VALUES ("Antanaitis", "Programuotojas"), ("Antanaitis", "Programuotojas")')
    # c.execute('''
    #     UPDATE darbuotojai
    #     SET PAREIGOS = 'Testuotojas'
    #     WHERE PAVARDĖ = 'Antanaitis';
    # ''')
    c.execute('''
        SELECT COUNT(*) AS TesterCount
        FROM darbuotojai
        WHERE PAREIGOS = 'Testuotojas';
    ''')
    print(c.fetchall())

# **************************************************************************************
# EXERCISE 2
# Create an app that:
# A database would be created
# A table would be created with the columns title, lecturer and duration of the lecture
# Three lectures would be created: ('Management', 'Donatus', 40), ('Python', 'Donatus', 80) and ('Java', 'Tomas', 80)
# Only lectures longer than 50 would be printed
# Updated the title of the lecture "Python" to "Python Programming"
# Delete a lecture taught by "Tomas"
# Print all lectures (full table)
# **************************************************************************************
import sqlite3


def create_database(db_name):
    conn = sqlite3.connect(f'{db_name}')
    conn.cursor()
    return conn


def create_table(conn):
    with conn:
        conn.execute('''
                CREATE TABLE IF NOT EXISTS lectures (
                    title TEXT, 
                    lecturer TEXT,
                    lecture_duration INTEGER
                )
            ''')


def insert_data(conn, data):
    with conn:
        conn.executemany('''
            INSERT INTO lectures (title, lecturer, lecture_duration) VALUES (?, ?, ?)
        ''', data)


def print_long_lectures(conn):
    with conn:
        c = conn.cursor()
        c.execute('''
            SELECT title, lecturer, lecture_duration FROM lectures WHERE lecture_duration > 50
        ''')
        long_lectures = c.fetchall()
        for lecture in long_lectures:
            print(lecture)


def update_title(conn):
    with conn:
        c = conn.cursor()
        c.execute('''
            UPDATE lectures SET title = "Python Programming" WHERE title = "Python"
        ''')


def delete_lecture(conn, condition):
    with conn:
        c = conn.cursor()
        c.execute('''
            DELETE FROM lectures WHERE {}
        '''.format(condition))


def print_table(conn, table_name):
    with conn:
        c = conn.cursor()
        c.execute('''
            SELECT * FROM {}
        '''.format(table_name))
        all_lectures = c.fetchall()
        for lecture in all_lectures:
            print(lecture)


def main():
    db_name = input('Enter the name of your database (ex. test.db): ')
    conn = create_database(db_name)
    create_table(conn)
    lectures_data = [
        ('Management', 'Donatus', 40),
        ('Python', 'Donatus', 80),
        ('Java', 'Tomas', 80)
    ]
    insert_data(conn, lectures_data)
    print_long_lectures(conn)
    update_title(conn)
    delete_lecture(conn, 'lecturer = "Tomas"')
    print_table(conn, 'lectures')


if __name__ == '__main__':
    main()

