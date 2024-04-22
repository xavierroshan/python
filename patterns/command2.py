# Receiver
class Chef:
    def make_food(self):
        print("Make food as per order")
class Bartender:
    def make_food(self):
        print("Mix drink as per the order")
        
#command interface
class Order:
    def make_order(self):
      pass
#concrete class
class FoodOrder(Order):
    def __init__(self,order):
        self.order=order
    def make_order(self):
        self.order.make_food()
class DrinksOrder(Order):
    def __init__(self,order):
        self.order=order
    def make_order(self):
        self.order.make_food()
        
#trigger
class Waiter:
    def __init__(self):
        self.orderlist = []
    def add_orders(self, order):
        if order not in self.orderlist:
            self.orderlist.append(order)
    def order_waiter(self):
        for order in self.orderlist:
            order.make_order()
        
chef = Chef()
bartender = Bartender()
food_order = FoodOrder(chef)
drinks_order = DrinksOrder(bartender)
waiter = Waiter()
waiter.add_orders(food_order)
waiter.add_orders(drinks_order)
waiter.order_waiter()
    

