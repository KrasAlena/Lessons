from pymongo import MongoClient
from pprint import pprint
from pymongo.database import Database


mongodb_host = 'localhost'
mongodb_port = 27017
database_name = 'School'

client = MongoClient(mongodb_host, mongodb_port)
db = client[database_name]

db_names = client.list_database_names()
for db_name in db_names:
    print(db_name)

collection_list = db.list_collection_names()
print(collection_list)

collection = db['Students']

# new_teacher = {
#     'name': 'Thomas',
#     'age': 40
# }
#
# collection.insert_one(new_teacher)

result = collection.find({'subjects.teacher.name': 'David'})

pprint(list(result))





def transfer():
    user_surname = input('Enter your surname: ')
    from_acc_number = uuid.UUID(input('Enter your account to transfer from: '))
    to_acc_number = uuid.UUID(input('Enter your account to transfer to: '))
    amount = float(input('Enter the amount to transfer: '))

    transfer_from = accounts_collection.find_one({'acc_holder.surname': user_surname, 'acc_number': from_acc_number})
    transfer_to = accounts_collection.find_one({'acc_number': to_acc_number})

    if transfer_from and transfer_to:
        if transfer_from['balance'] >= amount:
            accounts_collection.update_one({'_id': transfer_from['_id']}, {'$inc': {'balance': -amount}})
            accounts_collection.update_one({'_id': transfer_to['_id']}, {'$inc': {'balance': amount}})
            print('Transfer successful!')
        else:
            print('Insufficient funds in the transfer from account')
    else:
        print('Account not found')


def delete_account():
    user_surname = input('Enter your surname: ')
    person = persons_collection.find_one({'surname': user_surname})

    if person:
        accounts = accounts_collection.find({'acc_holder': person['_id']})

        print(f'Accounts for {user_surname}:')
        for account in accounts:
            print(f'Account ID: {account["_id"]}. Account number: {account["acc_number"]}. Balance: {account["balance"]}')

        acc_id_to_delete = input('Enter the ID of the account you want to delete: ')
        account_to_delete = accounts_collection.find_one({'acc_holder': person['_id'], '_id': ObjectId(acc_id_to_delete)})

        if account_to_delete:
            accounts_collection.delete_one({'acc_holder': person['_id'], '_id': ObjectId(acc_id_to_delete)})
            print(f'Account {acc_id_to_delete} deleted successfully!')
        else:
            print('Account not found')
    else:
        print('Person not found')



