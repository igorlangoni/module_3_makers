from lib.album  import Album

"""
When constructing an album
With the fields id, title, release_year and artist_id
These are reflected in the instance properties 
"""

def test_constructed_fields():
    album = Album(1, 'Reunion', 1998, 1)
    assert album.id == 1

def test_equality():
    album1 = Album(None, 'Construçåo', 1970, None)
    album2 = Album(None, 'Construçåo', 1970, None)
    assert album1 == album2

def test_formatting():
    album = Album(None, 'Construçåo', 1970, None)
    assert str(album) == "Album(None, Construçåo, 1970, None)"