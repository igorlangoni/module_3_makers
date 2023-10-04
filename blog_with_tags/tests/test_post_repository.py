from lib.post import Post
from lib.tag import Tag
from lib.post_repository import PostRepository

def test_finding_by_tag(db_connection):
    db_connection.seed("seeds/posts_tags_db.sql")
    repo = PostRepository(db_connection)
    result = repo.find_by_tag(2)
    
    assert result == [
        Post(4, 'My weekend in Edinburgh'),
        Post(6, 'A foodie week in Spain')
    ]

def test_finding_by_tag_given_coding(db_connection):
    db_connection.seed("seeds/posts_tags_db.sql")
    repo = PostRepository(db_connection)
    result = repo.find_by_tag(1)
    
    assert result == [
        Post(1, 'How to use Git'),
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
        Post(7, 'SQL basics')
    ]