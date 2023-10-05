from lib.item import Item

class ShopRepository:
    def __init__(self, connection):
        self.connection = connection

    def all_items(self):
        rows = self.connection.execute(
            "SELECT * FROM items;"
        )
        items = []
        for row in rows:
            item = Item(row['id'], row['name'], row['price'], row['quantity'])
            items.append(item)
        return items