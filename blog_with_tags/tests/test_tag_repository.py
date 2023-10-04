from lib.tag import Tag
from lib.post import Post
from lib.tag_repository import TagRepository

def test_finding_by_post_given_id_1(db_connection):
    db_connection.seed("seeds/posts_tags_db.sql")
    repo = TagRepository(db_connection)
    result = repo.find_by_post(1)
    assert result == Post(1, 'How to use Git', [
        Tag(1, 'coding', [])
    ])
    
def test_finding_by_post_given_id_2(db_connection):
    db_connection.seed("seeds/posts_tags_db.sql")
    repo = TagRepository(db_connection)
    result = repo.find_by_post(3)
    assert result == Post(3, 'Using a REPL', [
        Tag(1, 'coding', []),
        Tag(3, 'cooking', []),
        Tag(4, 'education', [])
    ])