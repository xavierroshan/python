# Strategy pattern
# Shopping cart -> Item (item and price), payment_stragery (method and amount)

from abc import ABC, abstractmethod

# Context
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.item = []
        self.payment_strategy=payment_strategy
        
    def add_item(self,item):
        self.item.append(item)
        
    def payment_amount(self):
        return sum(item['price'] for item in self.item)
        
    def check_out(self):
        total = self.payment_amount()
        self.payment_strategy.pay(total)
        
#Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self):
        pass
    
#Concrete PaymentStrategy
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Pay the {amount} using credit card")
        
class Paypal(PaymentStrategy):
    def pay(self, amount):
        print(f"Pay the {amount} using paypal")
        
class Cash(PaymentStrategy):
    def pay(self, amount):
        print(f"Pay the {amount} using cash")
        

credit_card_payment = CreditCardPayment()
paypal_payment = Paypal ()
cash_payment = Cash ()

shopping_cart_cc = ShoppingCart(credit_card_payment)
shopping_cart_paypal = ShoppingCart(paypal_payment)
shopping_cart_cash = ShoppingCart(cash_payment)
shopping_cart_cc.add_item({'Item':'watch', 'price':500, 'Item':'headphone', 'price': 200})
shopping_cart_cc.add_item({'Item':'ipad', 'price':400, 'Item':'earphone', 'price': 100})
shopping_cart_cc.check_out()
shopping_cart_paypal.add_item({'Item':'iwatch', 'price':300, 'Item':'desk', 'price': 300})
shopping_cart_paypal.add_item({'Item':'iphone', 'price':800, 'Item':'monitor', 'price': 400})
shopping_cart_paypal.check_out()
shopping_cart_cash.add_item({'Item':'macbook', 'price':1000, 'Item':'keyboard', 'price': 250})
shopping_cart_cash.check_out()








        
        