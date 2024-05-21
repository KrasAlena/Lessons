from students import StudentsDBManager
import pytest
from unittest.mock import patch, Mock


# def test_create_student():
#     # mock_create.return_value = 'mock_student_id'
#     db_manager = Mock()
#     db_manager.create_student.result.inserted_id = 'mock_student_id'
#     student_id = db_manager.create_student('John', 'Doe', 'S001', 1990, 'American', 'Law')
#
#     assert student_id is not None


def test_create_student():
    db_manager = Mock()
    db_manager.create_student.return_value = 'mock_student_id'
    student_id = db_manager.create_student('John', 'Doe', 'S001', 1990, 'American', 'Law')

    assert student_id == 'mock_student_id'