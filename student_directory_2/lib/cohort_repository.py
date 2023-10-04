from lib.database_connection import DatabaseConnection
from lib.cohort import Cohort
from lib.student import Student

class CohortRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        rows = self.connection.execute(
            "SELECT * FROM cohorts;"
        )
        cohorts = []
        for row in rows:
            cohort = Cohort(row['id'], row['name'], row['starting_date'])
            cohorts.append(cohort)
        return cohorts
    
    def find(self, id):
        rows = self.connection.execute(
            "SELECT * FROM cohorts WHERE id = %s", [id]
        )
        row = rows[0]
        return Cohort(row['id'], row['name'], row['starting_date'])
    
    def find_with_students(self, cohort_id):
        rows = self.connection.execute(
            "SELECT cohorts.id AS cohort_id, cohorts.name AS cohort_name, cohorts.starting_date, students.id AS student_id, students.name AS student_name FROM cohorts JOIN students ON cohorts.id = students.cohort_id WHERE cohorts.id = %s", [cohort_id]
        )
        students = []
        for row in rows:
            student = Student(row['student_id'], row['student_name'], row['cohort_id'])
            students.append(student)
        cohort = Cohort(rows[0]['cohort_id'], rows[0]['cohort_name'], rows[0]['starting_date'], students)
        return cohort