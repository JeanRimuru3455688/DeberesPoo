from car import Car

class UberFlash(Car):
    encargos    = bool
    pesoMax        = int
    
    def __init__(self, placa, modelo, color, año, matricula, encargos, pesoMax, driver):
        super().__init__(placa, modelo, color, año, matricula, driver)
        self.encargos   = encargos
        self.pesoMax    = pesoMax