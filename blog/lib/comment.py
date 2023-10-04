class Comment:
    def __init__(self, id, contents, author_name, post_id):
        self.id = id
        self.contents = contents
        self.author_name = author_name
        self.post_id = post_id
    
    def __repr__(self):
        return f"Comment({self.id}, {self.contents}, {self.author_name}, {self.post_id})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__