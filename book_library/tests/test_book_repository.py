from lib.book_repository import BookRepository
from lib.book   import  Book

"""
When calling #all in the repository
all instances of book are reflected in the list
"""

def test_calling_all_returns_list_with_all_books(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    result = repository.all()
    assert result == [
        Book('Nineteen Eighty-Four', 'George Orwell'),
        Book('Mrs Dalloway', 'Virginia Woolf'),
        Book('Emma', 'Jane Austen'),
        Book('Dracula', 'Bram Stoker'),
        Book('The Age of Innocence', 'Edith Wharton')
    ]
