import unittest

# Función que retorna True si un número es par
def is_even(n):
    return n % 2 == 0

# Clase con los casos de prueba
class TestIsEvenFunction(unittest.TestCase):

# Caso 1. Es par 
# Debería ser True el resultado
    def test_is_even(self):
        self.assertTrue(is_even(4)) # assertTrue evalúa si retorna True la función

# Caso 2. Es impar
# Debería ser False el resultado
    def test_is_odd(self):
        self.assertFalse(is_even(7)) # assertFalse evalúa si retorna False la función

# Ejecución de las pruebas
if __name__ == "__main__":
    unittest.main()