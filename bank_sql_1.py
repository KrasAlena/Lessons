'''
To make a program that would allow entering persons, banks, assigning bank accounts to persons.

The person has a name, surname, personal identification number, phone number. number.
The bank has a name, address, bank code, SWIFT code
An account has a number, balance, assignee and bank
A person can have many accounts in the same or different banks
Make a database diagram (it can be shown to the teacher).
Create an application with a UI in the console that would allow entering individuals, banks, accounts.
Allow the user to view their accounts and their information, add or withdraw money from them. It would
also allow general viewing of all banks, users, accounts and their information.
'''
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid

engine = create_engine('sqlite:///bank_system.db')
Base = declarative_base()


class Bank(Base):
    __tablename__ = 'bank'
    swift = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    bank_address = Column(String)
    bank_code = Column(Integer)


class Person(Base):
    __tablename__ = 'person'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    surname = Column(String)
    phone_number = Column(String)

    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __repr__(self):
        return f'ID: {self.id} | Name: {self.name} {self.surname} | Phone number: {self.phone_number}'


class Account(Base):
    __tablename__ = 'account'
    acc_number = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    balance = Column(Float)
    acc_holder = Column(UUID, ForeignKey('person.id'))
    bank_id = Column(UUID, ForeignKey('bank.swift'))


Base.metadata.create_all(engine)
