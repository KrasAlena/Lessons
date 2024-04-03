'''
Task Nr.1 : Create the CLI application, that would populate MongoDB database with random data.
The input should ask for :
- database name
- collection name
- field name with types (string, number, date string objects etc.) with range of values
(lets say field name = price, then value is number (float, int) which is random number from a(min) to b(max) )
- number of documents to create.
'''
from pymongo import MongoClient
from faker import Faker
import random
from random_word import RandomWords


def generate_random_data(string_field, number_field, date_field):
    faker = Faker()
    random_word = RandomWords().get_random_word()
    random_float = round(random.uniform(0.0, 1000.0), 2)
    random_int = random.randint(1, 100)
    random_date = faker.date_between(start_date='-30y', end_date='today').strftime('%Y-%m-%d')
    return {
        string_field: random_word,
        number_field: random_float,
        date_field: random_date
    }


def main():
    client = MongoClient('localhost', 27017)
    db_name = input('Inter a name for the database: ')
    db = client[db_name]
    collection_name = input('Enter a name for the collection: ')
    collection = db[collection_name]
    string_field = input('Enter a name for the string-type field: ')
    number_field = input('Enter a name for the number-type field: ')
    date_field = input('Enter a name for the date-type field: ')
    docs_amount = int(input('How many documents do you want to create: '))
    for _ in range(docs_amount):
        data = generate_random_data(string_field, number_field, date_field)
        collection.insert_one(data)

    print(f'{docs_amount} documents inserted into {collection_name} of the {db_name} database.')


if __name__ == '__main__':
    main()
