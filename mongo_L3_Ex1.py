'''
Instructions:

- Connect to a MongoDB server running on localhost.
- Create a new database named 'exercise_db' and a collection named 'exercise_collection'.
- Define the following JSON schema validation rules for the collection:
- The document must be an object.
- The 'name' field is required and must be a string.
- The 'age' field is required and must be an integer between 18 and 99.
- The 'email' field is required and must be a string containing a valid email address.
- Insert three documents into the collection, one that satisfies the validation rules and two that violate
the validation rules.
- Print all the documents in the collection.
- Clean up by dropping the collection and closing the MongoDB connection.
'''
from pymongo import MongoClient
from pymongo.errors import OperationFailure, WriteError
from pprint import pprint

client = MongoClient('localhost', 27017)
db = client['exercise_db']
collection = db['exercise_collection']

validation_rules = {
    'validator': {
        '$jsonSchema': {
            'bsonType': 'object',
            'required': ['name', 'age', 'email'],
            'properties': {
                'name': {
                    'bsonType': 'string'
                },
                'age': {
                    'bsonType': 'int',
                    'minimum': 18,
                    'maximum': 99
                },
                'email': {
                    'bsonType': 'string',
                    'pattern': '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
                }
            }
        }
    }
}

try:
    db.command('collMod', collection.name, **validation_rules)
except OperationFailure as e:
    print(e.details['errmsg'])


def insert_doc(document):
    try:
        collection.insert_one(document)
        print(f'{document} inserted successfully')
    except WriteError as er:
        pprint(er.details['errInfo'])


document1 = {
    'name': 'Mike', 'age': 35, 'email': 'test@gmail.com'
}

document2 = {
    'name': 'Don', 'age': 31, 'email': '123@mail.com'
}

document3 = {
    'name': 'Alice', 'age': 17, 'email': 'smth@mail.com'
}

# insert_doc(document1)
# insert_doc(document2)
# insert_doc(document3)
insert_doc(document3)