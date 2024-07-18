from advertise import RentApartment,SellApartment, RentStore,SellStore,SellHouse,RentHouse
from sample import create_samples
class Handler():
    ADVERTISMENT_TYPES = {
        1: SellApartment, #2:RentApartment, 
        3: SellHouse, 4: RentHouse, 
        # 5:SellStore, 6: RentStore 
    }

    SWITHCES ={
        "r": "get_reports",
        "s": "show_all" 
    }

    def get_reports(self):
        for adv in self.ADVERTISMENT_TYPES.values():
            adv_name = adv.__name__  # Get the class name
            count = adv.manager.count()
            print(f"Advertisement Type: {adv_name}\nNumber of Available Listings: {count}\n{'-'*40}")

    def show_all(self):
        for adv in self.ADVERTISMENT_TYPES.values():
            for obj in adv.object_list:
                print (f"All: {obj.detail()}\n{'-'*70}")


    def run(self):
        print("")
        print("WELCOME")
        for key in self.SWITHCES:
            print(f"Press {key} for getting {self.SWITHCES[key]}\n")
        user_input = input("Type the letter of the action (r/s): ")
        switch  = self.SWITHCES.get(user_input, None)
        if switch is None:
            print("Invalid input")
            self.run()
        choice = getattr(self, switch, None)
        choice()
        self.run()





if __name__ == "__main__":
    create_samples()
    Handler().run()