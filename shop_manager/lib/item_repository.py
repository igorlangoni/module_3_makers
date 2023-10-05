from lib.item import Item

class ItemRepository:
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
    
    def create_item(self, item):
        self.connection.execute(
            "INSERT INTO items (name, price, quantity) VAlUES (%s, %s, %s)",
            [item.name, item.price, item.quantity]
        )
        return None