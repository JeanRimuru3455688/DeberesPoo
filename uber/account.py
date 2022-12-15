class Account:
    id       = int
    nombre   = str
    edad     = int
    mail     = str
    telefono = int
    
    def __init__(self, id, nombre, edad, mail, telefono):
        self.id       = id
        self.nombre   = nombre
        self.edad     = edad
        self.mail     = mail
        self.telefono = telefono