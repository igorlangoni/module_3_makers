from lib.student import Student

"""
Test constructing with properties
"""

def test_construct():
    student = Student(1, 'Igor', 1)
    assert student.id == 1
    assert student.name ==  'Igor'
    assert student.cohort_id == 1

def test_equality():
    student1 = Student(1, 'Igor', 1)
    student2 = Student(1, 'Igor', 1)
    assert student1 == student2

def test_formatting():
    student = Student(1, 'Igor', 1)
    assert str(student) == "Student(1, Igor, 1)"