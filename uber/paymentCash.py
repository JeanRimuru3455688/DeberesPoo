from  payment import Payment

class  PaymentCash(Payment):
    
    def __init__(self, id, ammount, user, driver, type):
        super().__init__(id, ammount, user, driver, type)
        
