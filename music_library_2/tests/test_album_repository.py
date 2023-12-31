from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When running #all
returns a list with all albums in the DB
"""

def test_all_returns_all_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    result = repository.all()
    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]

def test_find_returns_the_specific_album(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = AlbumRepository(db_connection)
    result = repository.find(3)
    assert result == Album(3, 'Waterloo', 1974, 2)

"""
When calling create and an album
And then printing the list of albums
The created album is shown in list
"""

def test_creating_an_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, 'Reunion', 1998, None)

    assert repository.create(album) == None
    
    result = repository.all()
    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
        Album(13, 'Reunion', 1998, None)
    ]

"""
When calling Delete with an id
and then printing the list
the removed album does not show
"""

def test_deleting_an_album_with_id(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    assert repository.delete(11) == None
    result = repository.all()
    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]
