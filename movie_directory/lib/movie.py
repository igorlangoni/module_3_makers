class Movie:
    def __init__(self, id, title, genre, release_year):
        self.id = id
        self.title = title
        self.genre = genre
        self.release_year = release_year
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Movie({self.id}, {self.title}, {self.genre}, {self.release_year})"