class Route:
    inicio      = [int, int]
    fin         = [int, int]
    tiempoAprox = int
    distanciaKm = int
    
    def __init__(self, inicio, fin,tiempoAprox, distanciaKm):
        self.inicio         = inicio
        self.fin            = fin
        self.tiempoAprox    = tiempoAprox
        self.distanciaKm    = distanciaKm