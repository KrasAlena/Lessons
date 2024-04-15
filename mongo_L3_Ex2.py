'''
Connect to a MongoDB server running on localhost.
Create a new database named 'shopping_db' and a collection named 'shopping_collection'.
Define the following JSON schema validation rules for the collection:
The document must be an object.
The 'name' field is required and must be a string.
The 'age' field is required and must be an integer between 18 and 99.
The 'email' field is required and must be a string containing a valid email address.
The 'address' field is required and must be an object.
The 'address' object must have the 'street', 'city', and 'postal_code' fields, each being a required string.
Insert three documents into the collection, one that satisfies the validation rules and two that violate the validation rules.
Print all the documents in the collection.
Clean up by dropping the collection and closing the MongoDB connection.
'''
from pymongo import MongoClient
from pymongo.errors import OperationFailure, WriteError
from pprint import pprint

client = MongoClient('localhost', 27017)
db = client['shopping_db']
collection = db['shopping_collection']

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
                },
                'address': {
                    'bsonType': 'object',
                    'required': ['street', 'city', 'postal_code'],
                    'properties': {
                        'street': {
                            'bsonType': 'string'
                        },
                        'city': {
                            'bsonType': 'string'
                        },
                        'postal_code': {
                            'bsonType': 'string'
                        }
                    }
                }
            }
        }
    }
}

try:
    db.create_collection(collection.name, validator=validation_rules['validator'])
except OperationFailure as e:
    print(e.details['errmsg'])


def insert_doc(document):
    try:
        collection.insert_one(document)
        print(f'{document} inserted successfully')
    except WriteError as er:
        pprint(er.details['errInfo'])


document1 = {
    'name': 'John Doe',
    'age': 25,
    'email': 'john@example.com',
    'address': {'street': '123 Main St', 'city': 'Vilnius', 'postal_code': '12345'}
}

document2 = {
    'name': 'Jane Smith',
    'age': 17,  # Invalid age
    'email': 'jane.example.com',  # Invalid email
    'address': {'street': '456 Elm St', 'city': 'Milan', 'postal_code': '67890'}
}

document3 = {
    'name': 'Alice Johnson',
    'age': 30,
    'email': 'alice@example.com',
    'address': {'street': 789, 'city': 'Paris', 'postal_code': '45678'} # Invalid street
}

insert_doc(document1)
insert_doc(document2)
insert_doc(document3)

print('All documents in the collection:')
for doc in collection.find():
    pprint(doc)

collection.drop()
client.close()