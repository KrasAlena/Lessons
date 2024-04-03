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



