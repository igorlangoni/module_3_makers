import datetime

class Order:
    def __init__(self, id, customer, date, item):
        self.id = id
        self.customer = customer
        self.item = item
        self.date = str(date)[:10]
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Order({self.id}, {self.customer}, {self.date}, {self.item})"