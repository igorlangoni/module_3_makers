from lib.database_connection import DatabaseConnection
from lib.movie_repository import MovieRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/movie_directory_2.sql")

# Retrieve all artists
movie_repository = MovieRepository(connection)
print(movie_repository.find(2))


