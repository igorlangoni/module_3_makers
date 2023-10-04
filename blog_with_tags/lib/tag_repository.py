from lib.post   import Post
from lib.tag import Tag

class TagRepository:
    def __init__ (self, connection):
        self.connection = connection
    
    def find_by_post(self, post_id):
        rows = self.connection.execute(
            "SELECT tags.id AS tag_id, tags.name, posts.id AS post_id, posts.title "\
                "FROM tags "\
                "JOIN posts_tags ON posts_tags.tag_id = tags.id "\
                "JOIN posts ON posts_tags.post_id = posts.id "\
                "WHERE posts.id = %s", [post_id]
        )
        tags = []
        
        for row in rows:
            tag = Tag(row['tag_id'], row['name'])
            tags.append(tag)
        
        post = Post(rows[0]['post_id'], rows[0]['title'], tags)
        return post