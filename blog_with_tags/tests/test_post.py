from lib.post import Post

def test_construct():
    post = Post(1, 'GitHub basics')
    
    assert post.id == 1
    assert post.title == 'GitHub basics'

def test_eq():
    post1 = Post(1, 'GitHub basics')
    post2 = Post(1, 'GitHub basics')
    
    assert post1 == post2

def test_repr():
    post = Post(1, 'GitHub Basics')

    assert str(post) == "Post(1, GitHub Basics, [])"