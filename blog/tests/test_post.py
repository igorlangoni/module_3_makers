from lib.post import Post

def test_init():
    post = Post(1, 'title', 'content')
    assert post.id == 1
    assert post.title == 'title'

def test_eq():
    post1 = Post(1, 'title', 'content')
    post2 = Post(1, 'title', 'content')
    
    assert post1 == post2

def test_repr():
    post = Post(1, 'title', 'content')

    assert str(post) == "Post(1, title, content, [])"
