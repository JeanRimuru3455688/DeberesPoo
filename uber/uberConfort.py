from car import Car

class UberConfort(Car):
    aceptado    = bool
    tapizdo     = str
    asientos    = int
    
    def __init__(self, placa, modelo, color, año, matricula, aceptado, tapizado, asientos, driver):
        super().__init__(placa, modelo, color, año, matricula, driver)
        self.aceptado   = aceptado
        self.tapizdo    = tapizado
        self.asientos   = asientos