from lib.book import Book

"""
WHen constructing a book object
With fields: id, title, author_name
These are reflected in the properties
"""

def test_constructing_book():
    book = Book(1, 'The Godfather', 'Mario Puzo')
    assert book.id == 1
    assert book.title == 'The Godfather'
    assert book.author_name == 'Mario Puzo'

def test_identical_instances_are_equal():
    book1 = Book(1, 'The Godfather', 'Mario Puzo')
    book2 = Book(1, 'The Godfather', 'Mario Puzo')
    assert book1 == book2

def test_formatting_instance():
    book = Book(1, 'The Godfather', 'Mario Puzo')
    assert str(book) == "Book(1, The Godfather, Mario Puzo)" 