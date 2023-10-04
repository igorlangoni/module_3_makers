from lib.cohort import Cohort

def test_constructing():
    cohort = Cohort(1, 'Chocolate', 'sept 23')
    assert cohort.id == 1
    assert cohort.name == 'Chocolate'
    assert cohort.starting_date == 'sept 23'

def test_equality():
    cohort1 = Cohort(1, 'Chocolate', 'sept 23')
    cohort2 = Cohort(1, 'Chocolate', 'sept 23')
    assert cohort1 == cohort2

def test_formatting():
    cohort = Cohort(1, 'Chocolate', 'sept 23')
    assert str(cohort) == "Cohort(1, Chocolate, sept 23)"