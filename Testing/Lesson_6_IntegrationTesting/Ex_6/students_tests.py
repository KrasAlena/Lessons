from students import StudentsDBManager
import pytest


@pytest.fixture(scope='module')
def db_manager():
    mongodb_host = 'localhost'
    mongodb_port = 27017
    test_database_name = 'test_students'
    db_manager = StudentsDBManager(mongodb_host, mongodb_port, test_database_name)

    db_manager.collection.delete_many({})

    yield db_manager

    db_manager.collection.delete_many({})


def test_create_student(db_manager):
    student_id = db_manager.create_student('John', 'Doe', 'S001', 1990, 'American', 'Law')
    assert student_id is not None
    student = db_manager.get_student({'student_id': 'S001'})
    assert len(student) == 1
    assert student[0]['surname'] == 'Doe'


def test_get_student(db_manager):
    student_id = db_manager.create_student('John', 'Doe', 'S001', 1990, 'American', 'Law')
    students = db_manager.get_student({'student_id': 'S001'})
    assert students[0]['name'] == 'John'
    assert students[0]['surname'] == 'Doe'
    assert students[0]['student_id'] == 'S001'
    assert students[0]['year_of_birth'] == 1990
    assert students[0]['nationality'] == 'American'
    assert students[0]['faculty'] == 'Law'


def test_update_student_info(db_manager):
    student_id = db_manager.create_student('John', 'Doe', 'S001', 1990, 'American', 'Law')
    update_count = db_manager.update_student_info({'student_id': 'S001'}, {'surname': 'Doe Jr.'})
    assert update_count == 1
    students = db_manager.get_student({'student_id': 'S001'})
    assert students[0]['surname'] == 'Doe Jr.'


def test_delete_student(db_manager):
    student_id = db_manager.create_student('John', 'Doe', 'S001', 1990, 'American', 'Law')
    delete_count = db_manager.delete_student({'student_id': 'S001'})
    assert delete_count == 1
    students = db_manager.get_student({})
    assert len(students) == 0


def test_studentsDB_manager(db_manager):
    # create 3 students
    student_id1 = db_manager.create_student('John', 'Doe', 'S001', 1990, 'American', 'Law')
    student_id2 = db_manager.create_student('Maria', 'Rueja', 'S002', 1989, 'Mexican', 'Computer Science')
    student_id3 = db_manager.create_student('Paolo', 'Cerutti', 'S003', 1991, 'Italian', 'Marketing')

    # get all students
    students = db_manager.get_student({})
    assert len(students) == 3

    # get 1 exact student
    students = db_manager.get_student({'student_id': 'S001'})

    # update their info
    students_count = db_manager.update_student_info({'student_id': 'S001'}, {'surname': 'Doe Jr.'})
    assert students_count == 1
    students = db_manager.get_student({'student_id': 'S001'})
    student_surname = students[0]['surname']
    assert student_surname == 'Doe Jr.'

    # get another student
    students = db_manager.get_student({'student_id': 'S002'})

    # delete them
    delete_count = db_manager.delete_student({'student_id': 'S002'})
    assert delete_count == 1

    # get all students
    students = db_manager.get_student({})
    assert len(students) == 2