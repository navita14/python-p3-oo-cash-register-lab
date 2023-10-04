#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.prices = []
        self.quantity= []

    def add_item(self, name, price,quantity = 1):
        for _ in range(quantity):
            self.items.append(name)
            self.prices.append(price)  
        self.total += (price * quantity)
        self.quantity.append(quantity)
        

    def apply_discount(self):
        self.total *= (1 - (self.discount / 100))
        if self.discount > 0:
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")


    def void_last_transaction(self):
        last_quant = self.quantity.pop()
        for _ in range(last_quant):
            self.items.pop()
            price = self.prices.pop()
        self.total -= (price * last_quant)
       


    



    
 


         



