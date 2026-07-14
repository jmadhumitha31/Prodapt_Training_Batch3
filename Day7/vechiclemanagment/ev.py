from car import Car
class Ev(Car):
    def __init__(self,brand,model,year,battery_capacity,owner=None):
        super().__init__(brand,model,year,owner)
        self.battery_capacity=battery_capacity

    def start_engine(self):
        print(f"The electric engine of the {self.brand} {self.model} is starting silenty")

    def charge_battery(self):
        print(f"the battery of the {self.brand} {self.model} is charging. Battery capacity:{self.battery_capacity} khw")