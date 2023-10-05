from lib.database_connection import DatabaseConnection
from lib.order_repository import OrderRepository
from lib.item_repository import ItemRepository
from lib.item import Item
from lib.order import Order

class Application:
    def __init__(self):
        # Connect to the database
        self.connection = DatabaseConnection()
        self.connection.connect()
        # Seed with some seed data
        self.connection.seed("seeds/shop_management.sql")
    
    def run(self):
        # Retrieve all items/orders
        items_repository = ItemRepository(self.connection)
        items = items_repository.all_items()
        orders_repository = OrderRepository(self.connection)
        orders = orders_repository.all_orders()
        
        # asks the user for some input
        print('Welcome to LOJA DO GALO!\n\n')
        print('What do you want to do?\n')
        print("1 - See list of items\n")
        print("2 - See list of orders\n")
        print("3 - Create item\n")
        print("4 - Create order\n")
        answer = int(input("Enter your choice: "))
        print('\n')

        if answer == 1:
            for item in items:
                print(f"{item.id} - {item.name} - Unit Price: {item.price}£ - In Stock: {item.quantity}")
            
        if answer == 2:
            for order in orders:
                print(f"{order.id} - Customer: {order.customer} - Date: {order.date} - Item: {order.item}")
        
        if answer == 3:
            item_name = input('Enter item name: ')
            item_price = int(input('Enter item unit price: '))
            item_quant = int(input('Enter item available quantity: '))
            new_item = Item(None, item_name, item_price, item_quant)
            items_repository.create_item(new_item)
            print(f"{new_item} - Item added succesfully")
        
        if answer == 4:
            order_customer = input('Enter customer name: ')
            order_item = input('Enter item: ')
            new_order = Order(None, order_customer, None, order_item)
            orders_repository.create_order(new_order)
            print(f"{new_order} - Order added succesfully")

if __name__ == '__main__':
    app = Application()
    app.run()





