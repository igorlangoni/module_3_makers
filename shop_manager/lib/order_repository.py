from lib.order import Order

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
            "INSERT INTO orders (customer, item) VALUES ('José', 'Football Boots, various sizes, adidas')"
        )
        return None
