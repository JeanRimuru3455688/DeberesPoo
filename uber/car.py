from account_driver import Driver

class Car(Driver):
    placa     = str
    modelo    = str
    color     = str
    año       = str
    matricula = str
    driver = Driver("", "", "", "", "", "")
    
    def __init__(self, placa, modelo, color, año, matricula, driver):
        self.placa = placa
        self.modelo = modelo
        self.color = color
        self.año = año
        self.matricula = matricula
        self.driver =  driver
            
            