from pymongo import MongoClient
from pymongo.errors import OperationFailure, WriteError
from pprint import pprint

client = MongoClient('localhost', 27017)
db = client['School']
collection = db['Mentors']

validation_rules = {
    'validator': {
        '$jsonSchema': {
            'bsonType': 'object',
            'required': ['name', 'age', 'contact'],
            'properties': {
                'name': {
                    'bsonType': 'string'
                },
                'age': {
                    'bsonType': 'int',
                    'minimum': 0
                },
                'contact': {
                    'bsonType': 'object',
                    'required': ['email', 'phone'],
                    'properties': {
                        'email': {
                            'bsonType': 'string',
                            'pattern': '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
                        },
                        'phone': {
                            'bsonType': 'string',
                            'pattern': '^[0-9]{10}$'
                        }
                    }
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
    except WriteError as er:
        pprint(er.details)


document1 = {
    'name': 'Mike', 'age': 35, 'email': 'test@gmail.com'
}

document2 = {
    'name': 'Don', 'age': 31, 'contact': {'email': '123@mail.com', 'phone': '1234567890'}
}

insert_doc(document2)


