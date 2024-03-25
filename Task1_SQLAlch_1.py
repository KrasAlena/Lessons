
# https://github-com.translate.goog/DonatasNoreika/python1lygis/wiki/Duomenų-bazės-2?_x_tr_sl=lt&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp
'''
TASK 1
Create an app that:

It would allow entering employees: name, surname, date of birth, position, salary, since when working
(the date would be determined automatically, according to the current date).
Data would be stored in a database using SQLAlchemy ORM (without SQL queries)
User could add, view, delete and update employees.
'''
import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///hr.db')
Base = declarative_base()

class Employees(Base):
    __tablename__ = 'Employees'
    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    surname = Column('surname', String)
    birth_date = Column('birth_date', String)
    position = Column('position', String)
    salary = Column('salary', Float)
    employment_date = Column('employment_date', DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, surname, birth_date, position, salary):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.position = position
        self.salary = salary

    def __repr__(self):
        return (f'{self.id} | Name: {self.name} {self.surname} | Date of birth: {self.birth_date} | '
                f'Position: {self.position} | Salary: {self.salary} | Started working from {self.employment_date}')

Base.metadata.create_all(engine)