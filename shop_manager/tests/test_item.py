from lib.item import Item

def test_construct():
    item = Item(1, "T-Shirt - 'I S2 BH'" , 35, 80)
    
    assert item.id == 1
    assert item.name == "T-Shirt - 'I S2 BH'"

def test_eq():
    item1 = Item(1, "T-Shirt - 'I S2 BH'" , 35, 80)
    item2 = Item(1, "T-Shirt - 'I S2 BH'" , 35, 80)

    assert item1 == item2

def test_repr():
    item = Item(1, "T-Shirt - 'I S2 BH'" , 35, 80)

    assert str(item) == "Item(1, T-Shirt - 'I S2 BH', 35, 80)"