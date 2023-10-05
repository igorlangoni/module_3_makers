from lib.order import Order

def test_construct():
    order = Order(1, 'Igor', '05/10/2023', 'Home Kit')

    assert order.id == 1
    assert order.customer == 'Igor'
    assert order.date == '05/10/2023'
    assert order.item == 'Home Kit'

def test_eq():
    order1 = Order(1, 'Igor', '05/10/2023', 'Home Kit')
    order2 = Order(1, 'Igor', '05/10/2023', 'Home Kit')

    assert order1 == order2

def test_repr():
    order = Order(1, 'Igor', '05/10/2023', 'Home Kit')

    assert str(order) == "Order(1, Igor, 05/10/2023, Home Kit)"