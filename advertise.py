from base import Base
from estate import *
from deal import *


class RentHouse(Base,Rent, House):
    def detail(self):
        self.show_desription()
        self.show_price()

class SellHouse(Base,Sell, House):
    def detail(self):
        self.show_desription()
        self.show_price()

class RentApartment(Base ,Rent, Apartment):
    def detail(self):
        self.show_desription()
        self.show_price()

class SellApartment(Base ,Sell, Apartment):
    def detail(self):
        self.show_desription()
        self.show_price()
        
    def __str__(self):
        return f"area = {self.area}, year = {self.built_year}"

class RentStore(Base ,Rent, Store):
    def detail(self):
        self.show_desription()
        self.show_price()

class SellStore(Base ,Sell, Store):
    def detail(self):
        self.show_desription()
        self.show_price()