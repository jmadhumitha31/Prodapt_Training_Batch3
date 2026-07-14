from exception import OwnerAlreadyExistsError, InvalidBatteryCapacityError
class Car:
    def __init__(self,brand,model,year,owner=None):
        self.brand=brand
        self.model=model
        self.year=year
        self.__owner=owner ##private  
    def start_engine(self):
        print(f"The engine of the {self.brand} {self.model} is starting")

    def show_info(self):
        print(f"Car info:{self.year} {self.brand} {self.model}")
    
    def set_owner(self,owner):
        if not self.__owner:
            self.__owner=owner
        else:
            print(f"The Car already has an owner:{self.__owner}.Cannot change owner.") 

    def get_owner(self):
        return self.__owner