from src.medidas import Medida

def test_CT0006():
    medida = Medida(volume=0, lado=0)
    assert medida.get_lado() == 0
    assert medida.get_volume() == 0

def test_CT0007():
    medida = Medida(volume=8, lado=2)
    assert medida.get_lado() == 2
    assert medida.get_volume() == 8

def test_CT0008():
    medida = Medida(volume=27, lado=3)
    assert medida.get_lado() == 3
    assert medida.get_volume() == 27
