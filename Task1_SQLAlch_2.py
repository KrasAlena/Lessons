from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Task1_SQLAlch_1 import Employees

engine = create_engine('sqlite:///hr.db')
Session = sessionmaker(bind=engine)
session = Session()
""":type: sqlalchemy.orm.Session"""

employee1 = Employees('John', 'Doe', '2000-03-12', 'developer', 3800)
session.add(employee1)
session.commit()

employee2 = Employees('Stacy', 'White', '1995-08-01', 'PM', 4200)
session.add(employee2)
session.commit()

employees = session.query(Employees).all()

for employee in employees:
    print(employee)