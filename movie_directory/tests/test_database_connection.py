# This is an example of how to use the DatabaseConnection class
from lib.movie_repository import MovieRepository
from lib.movie import Movie

"""
When I seed the database
I get some records back
"""
def test_database_connection(db_connection):
    # Seed the database with some test data
    db_connection.seed("seeds/database_connection.sql")

    # Insert a new record
    db_connection.execute("INSERT INTO test_table (name) VALUES (%s)", ["second_record"])

    # Retrieve all records
    result = db_connection.execute("SELECT * FROM test_table")

    # Assert that the results are what we expect
    assert result == [
        {"id": 1, "name": "first_record"},
        {"id": 2, "name": "second_record"}
    ]

# def test_calling_all_returns_movies(db_connection):
#     db_connection.seed("seeds/movie_directory.sql")
#     movie_repository = MovieRepository(db_connection)
#     result = movie_directory.all()
#     assert result == [
#         Movie(1, 'Oppenheimer', 'Comedy', 2023),
#         Movie(2, 'Barbie', 'Horror', 2023),
#         Movie(3, 'The Lion King', 'Romance', 1994),
#         Movie(4, 'Star Wars: A New Hope', 'Comedy', 1980),
#         Movie(5, 'Morbius', 'Horror', 2022)
#     ]

def test_find_returns_specific_movie(db_connection):
    db_connection.seed("seeds/movie_directory_2.sql")
    movie_repository = MovieRepository(db_connection)
    result = movie_repository.find(5)
    assert result == Movie(5, 'Morbius', 'Horror', 2022)
