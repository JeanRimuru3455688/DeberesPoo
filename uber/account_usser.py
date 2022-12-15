from account import Account

class User(Account):
    def __init__(self, id, nombre, edad, mail, telefono):
        super().__init__(id, nombre, edad, mail, telefono)