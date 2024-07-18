from user import User
from random import choice
from estate import *
from advertise import *
import manager
first_name = ["Arian", "Ali", "Behnam"]
last_name = ["Hadi", "Torabi", "Marashi"]
phones = ["1234568", "8546874", "1234567","424232423", "454512264"]


def create_samples():
    for phone in phones:
        User(choice(first_name), choice(last_name), phone)

    # for user in User.object_list:
    #     print(f"{user.id}\t {user.fullname}\t {user.phone_number}")

    region1 = Region(name = "anadolu")
    region2 = Region(name = "Europe")

    renthouse1 =RentHouse(
        initial_price= 100, monthly_price= 20, convertable = False, discountable= True,
        user = User.object_list[2], area = 60, built_year = 2004, num_rooms = 4,
        region = region1, address = "Kartal",has_garden=True, number_of_floors=2
    )

    sellhouse1 = SellHouse(
        price_per_meter= 3500, has_discount= True, convertable= False,
        user = User.object_list[3], area = 22, built_year = 2000, num_rooms = 3,
        region = region2, address = "Kadiköy", has_garden = True, number_of_floors = 5
    )

    sellapartment1 = SellApartment(
        price_per_meter= 3500, has_discount= True, convertable= False, 
        user = User.object_list[1], area = 90, built_year = 2004, num_rooms = 4,
        region = region1, address = "Kartal",has_elavator=True, has_parking= True,
        floor = 3
    )


    sellapartment2 = SellApartment(
        price_per_meter= 3000, has_discount= True, convertable= False, 
        user = User.object_list[-1], area = 120, built_year = 2004, num_rooms = 6,
        region = region1, address = "Kartal",has_elavator=True, has_parking= True,
        floor = 3
    )
    

    # test = SellApartment.manager.search(area__min=80, area__max = 110)
    # print(f"result = ", test)


    print("#" * 20, "\tSamples created\t" ,"#" * 20)