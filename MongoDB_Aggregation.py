import os
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.command_cursor import CommandCursor
from pymongo.database import Database
from pymongo.cursor import Cursor
from pymongo.errors import OperationFailure, WriteError
from pprint import pprint
from typing import Dict, Any, Union, Mapping


def aggregate_documents(collection: Collection, pipeline: Dict[str, Any]) -> CommandCursor[
    Union[Mapping[str, Any], Any]]:
    try:
        return collection.aggregate(pipeline)
    except (OperationFailure, WriteError) as e:
        print(f'An error occurred: {e}')
        return None


# Retrieve MongoDB password from environment variable
mongo_password = os.environ.get('MONGO_PASSWORD')

# Establish a connection to the MongoDB server
try:
    client: MongoClient = MongoClient(f'mongodb+srv://alenakrasinskiene:{mongo_password}@cluster0.vacwkhr.mongodb.net/')
    db: Database = client['sample_mflix']
    collection: Collection = db['movies']
except OperationFailure as e:
    print(f'Failed to connect to MongoDB: {e}')
    exit(1)

# Define the aggregation pipeline
pipeline: Dict[str, Any] = [
    # Stage 1: Match documents with a specific genre
    {"$match": {"genres": "Western"}},

    # Stage 2: Project only the required fields
    {"$project": {
        "_id": 1,
        "title": 1,
        "plot": 1,
        "genres": 1,
        "runtime": 1,
        "cast": 1,
        "released": 1,
        "directors": 1,
        "awards": 1,
        "imdb": 1
    }},

    # Stage 3: Sort documents by release date in descending order
    {"$sort": {"released": -1}},

    # Stage 4: Limit the output to 5 documents
    {"$limit": 5}
]

# Call the aggregate_documents function
result: Cursor = aggregate_documents(collection, pipeline)

if result:
    doc_count = 0

# Iterate over the cursor and print the aggregated documents
    for doc in result:
        pprint(doc)
        doc_count += 1

    print('Total documents: ', doc_count)