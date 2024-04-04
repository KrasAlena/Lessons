'''
Write a function filter_documents that takes a MongoDB collection, a field name, an equal value,
and a not equal value as parameters. The function should return a list of documents from the
collection where the specified field is equal to the equal value and not equal to the not equal value.
'''
from pymongo import MongoClient
from pprint import pprint


def filter_documents(collection, field, e, ne):
    e_result = list(collection.find({field: e}))
    ne_result = list(collection.find({field: {'$ne': ne}}))
    return e_result, ne_result


def main():
    client = MongoClient('localhost', 27017)
    db = client['School']
    collection = db['Students']
    filtered_documents = filter_documents(collection, 'age', 20, 19)
    for document in filtered_documents:
        pprint(document)


if __name__ == '__main__':
    main()