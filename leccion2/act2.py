import pytest
import unittest
import problemas

def test_fibonacci():
    x = 6
    resultado = 8
    assert resultado == problemas.fibonacci(x)
    
def test_calcularEdad():
    x = "01/02/1999"
    resultado = 23
    assert resultado == problemas.calcularEdad(x)
    
def test_suma():
    x = 233.4
    y = 16.5
    resultado = 249.9
    assert resultado == problemas.suma(x,y)
    
def test_potencia():
    x = 4
    y = 10
    resultado = 1048576
    assert resultado == problemas.potencia(x,y)
    
def test_saludar():
    x = "Juan"
    resultado = "Buenos días, Juan"
    assert resultado == problemas.saludar(x)
    
class PruebasUnitarias(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(problemas.fibonacci(10), 34)
    def test_calcularEdad(self):
        self.assertEqual(problemas.calcularEdad("15/12/2005"), 16)
    def test_suma(self):
        self.assertEqual(problemas.suma(6,4), 10)
    def test_potencia(self):
        self.assertEqual(problemas.potencia(2,8), 256)
    def test_saludar(self):
        self.assertEqual(problemas.saludar("Pepe"), "Buenos días, Pepe")
        
        
if __name__ == "__main__":
    unittest.main()