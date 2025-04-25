from src.medidas import Medida
from src.Calcular_area import Calcular_area

# Exemplo de lado
lado = 3
volume = lado ** 3
cubo = Cubo(volume, lado)

calculo = CalcularArea("metragem", cubo)

print(f"Lado do cubo: {cubo.get_lado()} m")
print(f"Volume do cubo: {calculo.calcular_volume()} m³")
print(f"Área da superfície do cubo: {calculo.calcular_area()} m²")
