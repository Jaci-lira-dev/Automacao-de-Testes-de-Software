class Calcular_area():
    def __init__(self, metrica, medidas):
        self.metrica = metrica
        self.medidas = medidas
        
    def calcular_area(self):
        return 6 * (self.medidas.get_lado() ** 2)
    
    def calcular_volume(self):
        lado = self.medidas.get_lado()
        return lado ** 3
