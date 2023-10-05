from lib.order import Order
from lib.order_repository import OrderRepository

def test_listing_all_orders(db_connection):
    db_connection.seed("seeds/shop_management.sql")
    repo = OrderRepository(db_connection)

    result = repo.all_orders()

    assert result == [
        Order(1, 'Igor', '2023-10-05','Atletico Mineiro 2023 Home Kit'),
        Order(2, 'Igor', '2023-10-05','Atletico Mineiro 2023 Away Kit'),
        Order(3, 'Vitor', '2023-10-05', 'Football - Size 5, adidas'),

    ]

def test_create_order(db_connection):
    db_connection.seed("seeds/shop_management.sql")
    repo = OrderRepository(db_connection)
    order = Order(None, 'José', None, 'Football Boots, various sizes, adidas')
    repo.create_order(order)
    result = repo.all_orders()

    assert result == [
        Order(1, 'Igor', '2023-10-05','Atletico Mineiro 2023 Home Kit'),
        Order(2, 'Igor', '2023-10-05','Atletico Mineiro 2023 Away Kit'),
        Order(3, 'Vitor', '2023-10-05', 'Football - Size 5, adidas'),
        Order(4, 'José', '2023-10-05', 'Football Boots, various sizes, adidas')

    ]