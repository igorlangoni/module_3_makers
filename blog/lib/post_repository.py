from lib.comment import Comment
from lib.post import Post

class PostRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def find_with_comments(self, id):
        rows = self.connection.execute(
            "SELECT posts.id as post_id, posts.title, posts.content as post_content, comments.id as comment_id, comments.content as comment_content, comments.author, comments.post_id "\
                "FROM posts JOIN comments ON comments.post_id = posts.id WHERE posts.id = %s", [id]
        )
        comments = []
        for row in rows:
            comment = Comment(row['comment_id'], row['comment_content'], row['author'], row['post_id'])
            comments.append(comment)
        
        return Post(rows[0]['post_id'], rows[0]['title'], rows[0]['post_content'], comments)