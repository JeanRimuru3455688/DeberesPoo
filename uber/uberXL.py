from car import Car

class UberXL(Car):
    asientos = int
    
    
    def __init__(self, placa, modelo, color, año, matricula, asientos, driver):
        super().__init__(placa, modelo, color, año, matricula, driver)
        self.asientos  = asientos