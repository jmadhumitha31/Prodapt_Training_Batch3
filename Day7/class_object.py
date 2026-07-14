class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
        self.__owner=None ##private  
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
car1=Car("Toyoto","Camry",2020)
car2=Car("Mahindra","Civic",2019)
car1.set_owner("Madhu")
print(car1.get_owner())
car2.start_engine()
car2.show_info()
car1.set_owner("madhunkhoidwi")
print(car2.get_owner())