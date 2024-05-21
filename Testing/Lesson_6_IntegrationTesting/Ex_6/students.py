from pprint import pprint

from pymongo import MongoClient


class StudentsDBManager:
    def __init__(self, host: str, port: int, db_name: str):
        self.client = client = MongoClient(host, port)
        self.db = client[db_name]
        self.collection = self.db['students']

# (name, surname, student id, year of birth, nationality, faculty)
    def create_student(self, name: str, surname: str, student_id: str, year_of_birth: int, nationality: str, faculty: str):
        existing_student = self.collection.find_one({'student_id': student_id})
        if existing_student:
            return f'Student with ID {student_id} already exists'
        student = {
            'name': name,
            'surname': surname,
            'student_id': student_id,
            'year_of_birth': year_of_birth,
            'nationality': nationality,
            'faculty': faculty
        }
        result = self.collection.insert_one(student)
        print(result)
        return result.inserted_id

    def get_student(self, criteria: dict):
        return list(self.collection.find(criteria))

    def update_student_info(self, criteria: dict, updated_data: dict):
        result = self.collection.update_many(criteria, {'$set': updated_data})
        return result.modified_count

    def delete_student(self, criteria: dict):
        result = self.collection.delete_many(criteria)
        return result.deleted_count


def main():
    mongodb_host = 'localhost'
    mongodb_port = 27017
    database_name = 'students'

    db_manager = StudentsDBManager(mongodb_host, mongodb_port, database_name)

    student_id1 = db_manager.create_student('John', 'Doe', 'S001', 1990, 'American', 'Law')
    student_id2 = db_manager.create_student('Maria', 'Rueja', 'S002', 1989, 'Mexican', 'Computer Science')
    student_id3 = db_manager.create_student('Paolo', 'Cerutti', 'S003', 1991, 'Italian', 'Marketing')
    student_id4 = db_manager.create_student('John', 'Woo', 'S004', 1990, 'Chinese', 'Marketing')

    print(f'Created students with IDs: {student_id1}, {student_id2}, {student_id3}, {student_id4}')

    students = db_manager.get_student({'name': 'John'})
    print('Found students: ')
    for student in students:
        print(student)

    student_list = db_manager.get_student({})
    pprint(student_list[0]['surname'])

    # update_count = db_manager.update_student_info({'student_id': 'S001'}, {'surname': 'Doe Jr.'})
    # print(f'Updated student count: {update_count}')
    #
    # delete_count = db_manager.delete_student({'student_id': 'S004'})
    # print(f'Deleted student count: {delete_count}')


if __name__ == '__main__':
    main()