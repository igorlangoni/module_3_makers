from lib.post import Post
from lib.tag import Tag

class PostRepository():
    def __init__(self, connection):
        self.connection = connection
    
    def find_by_tag(self, tag_id):
        rows = self.connection.execute(
            "SELECT posts.id as post_id, posts.title, tags.id as tag_id, tags.name "\
                "FROM posts "\
                    "JOIN posts_tags ON posts_tags.post_id = posts.id "\
                    "JOIN tags ON posts_tags.tag_id = tags.id "\
                    "WHERE tags.id = %s", [tag_id] 
        )
        posts = []
        for row in rows:
            post = Post(row['post_id'], row['title'])
            posts.append(post)
        
        tag = Tag(rows[0]['tag_id'], rows[0]['name'], posts)
        return posts