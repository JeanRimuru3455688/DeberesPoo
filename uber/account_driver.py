from account import Account

class Driver(Account):
    licencia = str
    
    def __init__(self, id, nombre, edad, mail, telefono, licencia):
        super().__init__(id, nombre, edad, mail, telefono)
        self.licencia = licencia
        