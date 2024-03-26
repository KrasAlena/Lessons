import uuid

from sqlalchemy import create_engine
from bank_sql_1 import Bank, Person, Account
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///bank_system.db')
Session = sessionmaker(bind=engine)
session = Session()
""":type: sqlalchemy.orm.Session"""

session.commit()


def main():
    def main_menu():
        print('Welcome to the Bank System Console App')
        print('1. Add Person')
        print('2. Add Bank')
        print('3. Add Account')
        print('4. View Account Information')
        print('5. Transfer')
        print('6. Delete account')
        print('0. Exit')

        user_choice = input('Enter your choice: ')

        return user_choice

    def add_person():
        print('Adding a new person')
        name = input('Enter person\'s name: ')
        surname = input('Enter person\'s surname: ')
        phone_number = input('Enter person\'s phone number: ')

        new_person = Person(name=name, surname=surname, phone_number=phone_number)

        session.add(new_person)
        session.commit()

    def add_bank():
        print('Adding a new bank')
        bank_name = input('Enter bank\'s name: ')
        bank_address = input('Enter bank\'s address: ')
        bank_code = input('Enter bank\'s code: ')

        new_bank = Bank(name=bank_name, bank_address=bank_address, bank_code=bank_code)

        session.add(new_bank)
        session.commit()

    def add_account():
        print('Adding a new account')
        person_surname = input('Enter your surname: ')
        person = session.query(Person).filter_by(surname=person_surname).first()

        if person:
            print(f'We are creating a new account for {person}')

            banks = session.query(Bank).all()
            print('Available banks:')
            for bank in banks:
                print(bank.name)

            bank_name = input('Choose the bank from the list: ')
            user_bank = session.query(Bank).filter_by(name=bank_name).first()

            if user_bank:
                balance = float(input('Enter initial balance: '))
                new_account = Account(balance=balance, acc_holder=person.id, bank_id=user_bank.swift)
                print(type(person.id))

                session.add(new_account)
                session.commit()
        else:
            print(f'Sorry, we don\'t have any {person.name} {person.surname} in our client list')

    def view_account_info():
        user_surname = input('Enter your surname: ')
        accounts_info = (session.query(Account, Person, Bank).join(Person)
                         .join(Bank).filter(Person.surname == user_surname).all())
        if accounts_info:
            print(f'Information for {user_surname}:')
            for account_info in accounts_info:
                account, person, bank = account_info
                print(f'Account holder: {person.name} {person.surname}\nBank: {bank.name}\n'
                      f'Balance: {account.balance}\n========================')
        else:
            print(f'No accounts found for {user_surname}')

    def transfer():
        user_surname = input('Enter your surname: ')
        person = session.query(Person).filter_by(surname=user_surname).first()
        if person:
            accounts = session.query(Account).filter_by(acc_holder=person.id).all()
            if accounts:
                print('Your accounts:')
                for account in accounts:
                    print(f'Account number: {account.acc_number}. Balance: {account.balance}')
                from_acc = uuid.UUID(input('Enter your account to transfer from: '))
                to_acc = uuid.UUID(input('Enter your account to transfer to: '))
                # raise an error
                amount = float(input('Enter the amount to transfer: '))

                transfer_from = session.query(Account).filter_by(acc_number=from_acc).first()
                transfer_to = session.query(Account).filter_by(acc_number=to_acc).first()

                if transfer_from and transfer_to:
                    if transfer_from.balance >= amount:
                        transfer_from.balance -= amount
                        transfer_to.balance += amount

                        session.commit()

    def delete_account():
        user_surname = input('Enter your surname: ')
        person = session.query(Person).filter_by(surname=user_surname).first()
        if person:
            accounts = session.query(Account).filter_by(acc_holder=person.id).all()
            if accounts:
                print('Your accounts:')
                for account in accounts:
                    print(f'Account number: {account.acc_number}. '
                          f'Balance: {account.balance}')
                acc_to_delete = uuid.UUID(input('Enter what account you want to delete: '))
                for account in accounts:
                    if account.acc_number == acc_to_delete:
                        session.query(Account).filter_by(acc_number=acc_to_delete).delete()
                        print(f'Your account {account.acc_number} was deleted successfully!')
                        session.commit()
                    else:
                        print('Account not found')


    while True:
        choice = main_menu()

        if choice == '1':
            add_person()
        elif choice == '2':
            add_bank()
        elif choice == '3':
            add_account()
        elif choice == '4':
            view_account_info()
        elif choice == '5':
            transfer()
        elif choice == '6':
            delete_account()
        elif choice == '0':
            print('Exiting...')
            break
        else:
            print('Try again!')


if __name__ == '__main__':
    main()
