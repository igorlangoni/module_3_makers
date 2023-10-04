from lib.tag import Tag

def test_construct():
    tag = Tag(1, 'coding')
    
    assert tag.id == 1
    assert tag.name == 'coding'

def test_eq():
    tag1 = Tag(1, 'coding')
    tag2 = Tag(1, 'coding')
    
    assert tag1 == tag2

def test_repr():
    tag = Tag(1, 'coding')

    assert str(tag) == "Tag(1, coding, [])"