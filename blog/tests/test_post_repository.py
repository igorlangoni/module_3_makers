from lib.post_repository import PostRepository
from lib.comment import Comment
from lib.post import Post

def test_finding_post_with_comments(db_connection):
    db_connection.seed("seeds/blog.sql")
    repo = PostRepository(db_connection)
    post = repo.find_with_comments(1)

    assert post.id == 1
    assert post.title == 'Success'
    assert post.content == 'I got the job!'