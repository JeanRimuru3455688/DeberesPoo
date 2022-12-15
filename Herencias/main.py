class persona:
    nombre   = str
    apellido = str
    edad     = int
    
    def __init__(self,nombre,apellido,edad):
        self.nombre    = nombre
        self. apellido = apellido
        self.edad      = edad
        
if __name__ == "__main__":
     Alisson = persona ("Alisson", "Cumbajin",21  )  
     Lenin   = persona ("Lenin", "Montalvo",19) 
     print(vars (Alisson))
     print(Lenin.edad)

class Persona2:
     nombre   = str
     apellido = str
     edad     = int
     correo   = str

     def __init__(self, nombre, apellido, edad, correo):
         self.nombre    = nombre
         self.apellido  = apellido
         self.edad      = edad  
         self.correo    = correo
        
     def __str__(self):
         return  f"hola me llamo {self.nombre} {self.apellido}, tengo {self.edad} años y mi correo es {self.correo}"
    
p2 = Persona2("Diego", "Yanez" , 19, "dada@yavirac.edu.ec")
print(p2)

class persona3:
    nombre     = str
    apelllido  = str
    edad       = int 
    carrera    = str
    semestre   = str
    
    def __init__(self, nombre, apellido, edad, carrera, semestre):
        self.nombre     = nombre
        self.apelllido  = apellido
        self.edad       = edad
        self.carrera    = carrera
        self.semestre   = semestre
    
    def bienvenida(self):
        print("Bienvenido " , self.nombre , self.apelllido,"tienes", self.edad, "años",  " y eres de " , self.semestre , " semestre de la carrera de ", self.carrera)

p3 = persona3("Diego", "Yanez", 19, "Marketing", "Tercer")
p4 = persona3("Alejandra", "Guala", 29, "Artes Culinarias", "Primer")
p5 = persona3("Alejandra", "Agila", 21, "Gestion de Riesgos", "Cuarto")

p3.bienvenida()
p4.bienvenida()
p5.bienvenida()

class persona4:
    nombre   = str
    edad     = int

    def __init__(self, nombre, edad):
        self.nombre   = nombre
        self.edad     = edad

    def conversar(self, otra_persona):
        return f"Hola {otra_persona.nombre}, tienes {self.edad}, verdad?. Yo me llamo {self.nombre} y tengo {self.edad}"

p6 = persona4("David", 22)
p7 = persona4("Nayeon", 27)
p8 = persona4("Momo", 26)
p9 = persona4("Mina", 25)

print(p6.conversar(p7))
print(p8.conversar(p9))