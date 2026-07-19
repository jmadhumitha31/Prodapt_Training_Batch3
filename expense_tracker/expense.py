from exceptions import InvalidAmountError

class Expense:


    #constructor
    def __init__(self,expense_id,date,category,description,amount):
   
        if amount<=0:
            raise InvalidAmountError("Amount should be graeter then zero")   
        self.expense_id=expense_id
        self.date=date
        self.category=category
        self.description=description
        self.amount=amount

    def to_list(self):
        return [
            self.expense_id,
            self.date,
            self.category,
            self.description,
            self.amount
        ]