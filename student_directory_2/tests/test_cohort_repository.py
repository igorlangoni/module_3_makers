from lib.cohort import  Cohort
from lib.student import Student
from lib.cohort_repository import CohortRepository

def test_calling_all_shows_all_in_list(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    cohort_repository = CohortRepository(db_connection)
    result = cohort_repository.all()
    assert result == [
        Cohort(1, 'chocolate', 'sept 23'),
        Cohort(2, 'marshmallow', 'apr 23'),
        Cohort(3, 'cake', 'jan 23')
    ]

def test_finding(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    cohort_repository = CohortRepository(db_connection)
    result = cohort_repository.find(1)
    assert result == Cohort(1, 'chocolate', 'sept 23')

def test_finding_with_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    cohort_repository = CohortRepository(db_connection)
    result = cohort_repository.find_with_students(1)
    assert result == Cohort(1, 'chocolate', 'sept 23', [
        Student(1, 'Igor', 1),
        Student(3, 'Alex', 1),
        Student(5, 'Keziah', 1),
        Student(7, 'Fatma', 1 )
    ])
