from lib.book_repository import BookRepository
from lib.book import Book

"""
When calling #all
Returns a list with all Book objects in the repository
"""

def test_calling_all(db_connection):
    db_connection.seed("seeds/book_store.sql")
    book_repository = BookRepository(db_connection)
    result = book_repository.all()
    assert result == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton')
    ]
