'''
Task Nr.3:
With your own tool, create of database of grocery store. Store consist three different categories of items
(lets say electronics, fruits, food etc.). The items as minimum should have these fields: name, price, quantity,
year made (YYYY-MM-DD). Task:

Get all electronic items monetary value made 1 years, 2 months and 12 days from today.
Get average price for all items/categories in the store.
Get all items which names starts with letter a, and cost is between 10 and 100.
Find all item names (only) for prices > 50 and quantity < 10.
'''
from pymongo import MongoClient
from pymongo.errors import OperationFailure, WriteError
from faker import Faker
import random
from datetime import datetime, timedelta
from pprint import pprint
import re


class StoreManager:
    def __init__(self, host: str, port: int, db_name: str, db_collection: str):
        self.client = client = MongoClient(host, port)
        self.db = client[db_name]
        self.collection = self.db[db_collection]
        self.create_validation()

    def create_validation(self):
        validator = {
            '$jsonSchema': {
                'bsonType': 'object',
                'required': ['name', 'price', "quantity", 'date'],
                'properties': {
                    'name': {'bsonType': 'string'},
                    'price': {'bsonType': 'double', 'minimum': 0.5, 'maximum': 100},
                    'quantity': {'bsonType': 'int', 'minimum': 101, 'maximum': 1000},
                    'date': {'bsonType': 'date'}
                }
            }
        }
        self.db.create_collection(self.collection.name, validator=validator)

    def generate_data(self, category, names):
        fake = Faker()
        for name in names:
            item = {
                'name': name,
                'price': round(random.uniform(0.5, 100), 2),
                'quantity': random.randint(1, 100),
                'date': datetime.combine(fake.date_this_decade(), datetime.min.time())
            }
            self.collection.insert_one(item)

    def get_items_by_date(self, collection_name):
        collection = self.db[collection_name]
        date_threshold = datetime.now() - timedelta(days=1*365 + 2*30 + 12)
        items = collection.find({'date': {'$gte': date_threshold}})
        return list(items)

    def get_average_price(self, collection_name):
        collection = self.db[collection_name]
        pipeline = [
            {"$group": {"_id": None, "avg_price": {"$avg": "$price"}}}
        ]
        result = collection.aggregate(pipeline)
        return round(list(result)[0]['avg_price'], 2)

    def get_items_by_name_and_price(self, collection_name, name_start, min_price, max_price):
        collection = self.db[collection_name]
        regexp_pattern = f"^{name_start}[a-zA-Z]*"
        items = collection.find({"name": {"$regex": regexp_pattern, "$options": "i"}, "price": {"$gte": min_price, "$lte": max_price}},
                                {"_id": 0})
        return list(items)


def main():
    mongodb_host = 'localhost'
    mongodb_port = 27017
    database_name = 'Store'

    electronics = StoreManager(mongodb_host, mongodb_port, database_name, 'electronics')
    fruits = StoreManager(mongodb_host, mongodb_port, database_name, 'fruits')
    food = StoreManager(mongodb_host, mongodb_port, database_name, 'food')

    electronics_names = ['laptop', 'phone', 'tablet', 'TV', 'camera']
    fruits_names = ['apple', 'banana', 'orange', 'strawberry', 'kiwi']
    food_names = ['bread', 'milk', 'cheese', 'eggs', 'yogurt']

    categories = [(electronics, electronics_names), (fruits, fruits_names), (food, food_names)]

    for category, names in categories:
        category.generate_data(category, names)

    food_items = electronics.get_items_by_date('food')
    for item in food_items:
        print(item)

    avg_price_fruits = fruits.get_average_price('fruits')
    print(f'Average price for fruits: {avg_price_fruits}')

    electronic_item = electronics.get_items_by_name_and_price('electronics', 't', 10, 100)
    pprint(electronic_item)


if __name__ == '__main__':
    main()


