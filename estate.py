from region import Region
from base import *
from user import User
from abc import ABC

class Estate(ABC):
    def __init__(self, user, area, built_year, num_rooms, region, address,*args, **kwargs):
        self.seller = user
        self.area = area
        self.built_year = built_year
        self.num_rooms = num_rooms
        self.region = region
        self.address = address
        super().__init__(*args, **kwargs)
    
    @abstractmethod
    def show_desription(self):
        pass


class Apartment(Estate):
    def __init__(self, has_elavator, has_parking, floor, *args, **kwargs):
        self.has_elavator = has_elavator
        self.has_parking = has_parking
        self.floor = floor
        super().__init__(*args, **kwargs)
    def show_desription(self):
        print(f"Apartment = {self.id}")

class House(Estate):
    def __init__(self, has_garden, number_of_floors,*args, **kwargs):
        self.has_garden = has_garden
        self.number_of_floors = number_of_floors
        super().__init__(*args, **kwargs)
    def show_desription(self):
        print(f"House = {self.id}")

        

class Store(Estate):
    def show_desription(self):
        print(f"Store = {self.id}")

        