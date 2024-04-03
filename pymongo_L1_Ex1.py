from pymongo import MongoClient


class LibraryManager:
    def __init__(self, host: str, port: int, db_name: str):
        self.client = client = MongoClient(host, port)
        self.db = client[db_name]
        self.collection = self.db['books']

    #Crud
    def create_book(self, book_data: dict):
        existing_book = self.collection.find_one(book_data)
        if existing_book:
            self.collection.update_one(book_data, {'$inc': {'count': 1}})
        else:
            book_data['count'] = 1
            result = self.collection.insert_one(book_data)
            return result.inserted_id

    #cRud
    def read_book(self, criteria: dict):
        return self.collection.find(criteria)

    #crUd
    def update_book(self, criteria: dict, updated_data: dict):
        result = self.collection.update_many(criteria, {'$set': updated_data})
        return result.modified_count

    #cruD
    def delete_book(self, criteria: dict):
        result = self.collection.delete_many(criteria)
        return result.deleted_count


def main():
    mongodb_host = 'localhost'
    mongodb_port = 27017
    database_name = 'Library'

    library_manager = LibraryManager(mongodb_host, mongodb_port, database_name)

    book1_data = {'title': 'Book 1', 'author': 'John Doe', 'year': 2020}
    book2_data = {'title': 'Book 2', 'author': 'Jane Smith', 'year': 2021}
    library_manager.create_book(book1_data)
    # library_manager.create_book(book2_data)

    criteria = {'author': 'John Doe'}
    books = library_manager.read_book(criteria)
    print('Books by John Doe:', list(books))

    criteria = {'year': {'$lt': 2021}}
    updated_data = {'status': 'archived'}
    # modified_count = library_manager.update_book(criteria, updated_data)
    # print('Modified', modified_count, 'documents')

    criteria = {'author': 'John Doe'}
    # deleted_count = library_manager.delete_book(criteria)
    # print('Deleted', deleted_count, 'documents')


if __name__ == '__main__':
    main()