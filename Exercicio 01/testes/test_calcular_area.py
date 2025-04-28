from src.calcular_area import Calcular_area
from src.medidas import Medida

def test_CT0009():
    medida = Medida(volume=0, lado=0)
    calc = Calcular_area(metrica='cubo', medidas=medida)
    assert calc.calcular_area() == 0

def test_CT0010():
    medida = Medida(volume=27, lado=3)
    calc = Calcular_area(metrica='cubo', medidas=medida)
    assert calc.calcular_area() == 6 * (3 ** 2)  # 6 * 9 = 54

def test_CT0011():
    medida = Medida(volume=64, lado=4)
    calc = Calcular_area(metrica='cubo', medidas=medida)
    assert calc.calcular_area() == 6 * (4 ** 2)  # 6 * 16 = 96
