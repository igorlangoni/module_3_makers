from lib.item import Item
from lib.shop_repository import ShopRepository

def test_showing_all_items(db_connection):
    db_connection.seed("seeds/shop_management.sql")
    repo = ShopRepository(db_connection)

    result = repo.all_items()

    assert result == [
        Item(1, 'Atletico Mineiro 2023 Home Kit', 80, 50),
        Item(2, 'Atletico Mineiro 2023 Away Kit', 75, 30),
        Item(3, 'Atletico Mineiro 2023 Junior Kit', 50, 50),
        Item(4, 'Football - Size 5, adidas', 50, 100),
        Item(5, 'Football - Size 5, nike', 60, 100),
        Item(6, 'Atletico Mineiro Jumper', 150, 30),
        Item(7, 'T-Shirt - I S2 BH', 35, 80),
        Item(8, 'Autographed Home Kit', 200, 15),
        Item(9, 'Football Boots, various sizes, adidas', 65, 100),
        Item(10, 'Football Boots, various sizes, nike', 65, 100)
    ]

def test_showing_all_items(db_connection):
    db_connection.seed("seeds/shop_management.sql")
    repo = ShopRepository(db_connection)