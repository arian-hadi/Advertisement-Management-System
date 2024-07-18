from abc import ABC

class Sell(ABC):
    def  __init__(self, price_per_meter,has_discount ,convertable, *args, **kwargs):
        self.price_per_meter = price_per_meter
        self.has_discount = has_discount
        self.convertable = convertable
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(f"prince per_meter = {self.price_per_meter}\t Has discount: {self.has_discount}\t Convertable: {self.convertable}")

    

class Rent(ABC):
    def __init__(self,initial_price, monthly_price, convertable,discountable, *args, **kwargs):
        self.initial_price = initial_price
        self.monthley_price = monthly_price
        self.convertable = convertable
        self.discountable = discountable
        super().__init__(*args, **kwargs)
        
    def show_price(self):
         print(f"for Rent\n initial_price = {self.initial_price}\t monthly_price: {self.monthley_price}\t Convertable: {self.convertable}\t Discountable: {self.discountable}")

    
