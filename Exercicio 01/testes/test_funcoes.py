
from funcoes import cubo

def test_CT0001():
    assert cubo(0) == 0

def test_CT0002():
    assert cubo(1) == 1

def test_CT0003():
    assert cubo(2) == 8

def test_CT0004():
    assert cubo(-2) == -8

def test_CT0005():
    assert cubo(10) == 1000
