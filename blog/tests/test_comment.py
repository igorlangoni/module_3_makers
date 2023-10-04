from lib.comment import Comment

def test_initialising():
    comment = Comment(1, 'Content1', 'Author1', 1)
    
    assert comment.id == 1
    assert comment.author_name == 'Author1' 

def test_repr():
    comment = Comment(1, 'Content1', 'Author1', 1)

    assert str(comment) == "Comment(1, Content1, Author1, 1)"

def test_eq():
    comment_1 = Comment(1, 'Content1', 'Author1', 1)
    comment_2 = Comment(1, 'Content1', 'Author1', 1)

    assert comment_1 == comment_2
