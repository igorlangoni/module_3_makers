from lib.order import Order
from lib.item import Item
from lib. item_repository import ItemRepository

class OrderRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def all_orders(self):
        rows = self.connection.execute(
            "SELECT * FROM orders;"
        )
        orders = []
        for row in rows:
            order = Order(row['id'], row['customer'], row['date'], row['item'])
            orders.append(order)
        return orders
    
    def create_order(self, order):
        self.connection.execute(
            "INSERT INTO orders (customer, item) VALUES (%s, %s)",
            [order.customer, order.item]
        )
        # TRYING TO REDUCE ITEM QUANTITY
        repo = ItemRepository(self.connection)
        items = repo.all_items()
        for item in items:
            if item.name == order.item:
                self.connection.execute(
                    "UPDATE items SET quantity = %s WHERE items.name = %s", [item.quantity-1, item.name]
                )
        return None
