from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.album import Album

class Application():
    def __init__(self):
        # Connect to the database
        self.connection = DatabaseConnection()
        self.connection.connect()
        
        # Seed with some seed data
        self.connection.seed("seeds/music_library.sql")
    
    def run(self):
        # Retrieve all artists
        artist_repository = ArtistRepository(self.connection)
        artists = artist_repository.all()
        # Retrieve all albums
        album_repository = AlbumRepository(self.connection)
        albums = album_repository.all()
        # Print the question and the options
        print("What would you like to do?\n\n1 - List all albums\n2 - List all artists\n\n")
        # Receives the answer and stores in a variable
        answer = int(input("Enter your choice: "))
    
        if answer == 1:
            print("\nHere is a list of albums:")
            for album in albums:
                print(f"{album.id} - {album.title}")
            print('\n')
        else:
            print("\nHere is a list of artists:")
            for artist in artists:
                print(f"{artist.id} - {artist.name}")
            print('\n')

if __name__ == '__main__':
    app = Application()
    app.run()


