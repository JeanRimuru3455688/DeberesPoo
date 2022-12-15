class Madre:
    nombre = str
    apellido = str
    edad = int
    ciudad = str
    
    def __init__(self, nombre, apellido, edad, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad = ciudad
    
    def bienvenida(self, hijo):
        return f"Buenas noches {hijo.nombre} bienvenido a la casa, la cena esta lista en el horno, yo me encuentro de viaje en  {self.ciudad} att: {self.nombre} {self.apellido}"
    

    