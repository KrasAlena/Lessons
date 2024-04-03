from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)
db = client['bank_system']
persons_collection = db['persons']
bank_collection = db['banks']
accounts_collection = db['accounts']


def main():
    def main_menu():
        print('Welcome to the Bank System Console App')
        print('1. Add Person')
        print('2. Add Bank')
        print('3. Add Account')
        print('4. View Account Information')
        print('5. Delete account')
        print('0. Exit')

        user_choice = input('Enter your choice: ')

        return user_choice

    def add_person():
        print('Adding a new person')
        name = input('Enter person\'s name: ')
        surname = input('Enter person\'s surname: ')
        phone_number = input('Enter person\'s phone number: ')

        new_person = {
            'name': name,
            'surname': surname,
            'phone_number': phone_number
        }

        persons_collection.insert_one(new_person)

    def add_bank():
        print('Adding a new bank')
        bank_name = input('Enter bank\'s name: ')
        bank_address = input('Enter bank\'s address: ')
        bank_code = input('Enter bank\'s code: ')

        new_bank = {
            'name': bank_name,
            'address': bank_address,
            'code': bank_code
        }

        bank_collection.insert_one(new_bank)

    def add_account():
        print('Adding a new account')
        person_surname = input('Enter your surname: ')
        person = persons_collection.find_one({'surname': person_surname})

        if person:
            print(f'We are creating a new account for {person_surname}')

            banks = bank_collection.find()
            print('Available banks:')
            for bank in banks:
                print(bank['name'])

            bank_name = input('Choose the bank from the list: ')
            user_bank = bank_collection.find_one({'name': bank_name})

            if user_bank:
                balance = float(input('Enter initial balance: '))
                new_account = {
                    'balance': balance,
                    'acc_holder': person['_id'],
                    'bank_id': user_bank['_id']
                }

                accounts_collection.insert_one(new_account)
        else:
            print(f'Sorry, we don\'t have any {person.name} {person.surname} in our client list')

    def view_account_info():
        user_surname = input('Enter your surname: ')
        accounts_info = accounts_collection.aggregate([
            {
                '$lookup': {
                    'from': 'persons',
                    'localField': 'acc_holder',
                    'foreignField': '_id',
                    'as': 'person'
                }
            },
            {
                '$unwind': '$person'
            },
            {
                '$lookup': {
                    'from': 'banks',
                    'localField': 'bank_id',
                    'foreignField': '_id',
                    'as': 'bank'
                }
            },
            {
                '$unwind': '$bank'
            },
            {
                '$match': {
                    'person.surname': user_surname
                }
            }
        ])

        for account_info in accounts_info:
            print(f"Account holder: {account_info['person']['name']} {account_info['person']['surname']}")
            print(f"Bank: {account_info['bank']['name']}")
            print(f"Balance: {account_info['balance']}")
            print("========================")

    def delete_account():
        user_surname = input('Enter your surname: ')
        person = persons_collection.find_one({'surname': user_surname})

        if person:
            accounts = accounts_collection.find({'acc_holder': person['_id']})

            print(f'Accounts for {user_surname}:')
            for account in accounts:
                print(
                    f'Account ID: {account["_id"]}. Balance: {account["balance"]}')

            acc_id_to_delete = input('Enter the ID of the account you want to delete: ')
            account_to_delete = accounts_collection.find_one(
                {'acc_holder': person['_id'], '_id': ObjectId(acc_id_to_delete)})

            if account_to_delete:
                accounts_collection.delete_one({'acc_holder': person['_id'], '_id': ObjectId(acc_id_to_delete)})
                print(f'Account {acc_id_to_delete} deleted successfully!')
            else:
                print('Account not found')
        else:
            print('Person not found')

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
            delete_account()
        elif choice == '0':
            print('Exiting...')
            break
        else:
            print('Try again!')


if __name__ == '__main__':
    main()