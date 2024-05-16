import unittest

def es_impar(num):
    if num % 2 != 0: 
        return True
    elif num == 0:
        return 0
    else:
        return False
    
class TestFuncionEsImpar(unittest.TestCase):

    # Caso donde el número es impar
    def test_numero_impar(self):
        self.assertTrue(es_impar(3))

    # Caso donde el número es par
    def test_numero_par(self):
        self.assertFalse(es_impar(2))

    # Caso donde el número es cero
    def test_numero_cero(self):
        self.assertEqual(es_impar(0), 0)

# Ejecutar todas las pruebas
if __name__ == "__main__":
    unittest.main()


