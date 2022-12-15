from car import Car

class UberPET(Car):
    transportePet       = bool
    
    
    def __init__(self, placa, modelo, color, año, matricula, transportePet,  driver):
        super().__init__(placa, modelo, color, año, matricula, driver)
        self.transportePet = transportePet