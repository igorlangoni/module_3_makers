from lib.movie import Movie

class MovieRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        pass

    def find(self, id):
        rows = self.connection.execute(
            "SELECT * FROM movies WHERE id = %s", [id])
        row = rows[0]
        return Movie(row['id'], row['title'], row['genre'], row['release_year'])