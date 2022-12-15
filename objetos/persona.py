class persona:
    nombre        = str
    edad          = int
    centroEstudio = str
    def __init__(self,nombre,edad, centroEstudio):
        self.nombre        = nombre 
        self.edad          = edad
        self.centroEstudio = centroEstudio
        
    def conversar (self,otra_persona):
        return f'Hola {otra_persona.nombre} me llamo {self.nombre}, y estudio en la  {self.centroEstudio} '  
    
if __name__== "__main__" :
    Persona1 = persona("Juan", 18, "espe")
    Persona2 = persona("Alison", 28, "uce") 
    
    print(Persona1.conversar(Persona2))  
    