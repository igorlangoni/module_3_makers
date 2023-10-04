from lib.book import Book

"""
When constructing a book
With title and author fields
These are reflected in the instances properties
"""

def test_constructing_with_fields():
    book = Book('The Godfather', 'Mario Puzo')
    assert book.title == 'The Godfather'