import unittest

# Definir la función a probar
def sum(a, b):
    return a + b

# Definir los casos de prueba
class TestSumFunction(unittest.TestCase):

    # Caso de prueba con números positivos
    def test_sum_positive_numbers(self):
        self.assertEqual(sum(4, 3), 7) # assertEqual(función, resultado esperado)

    # Caso de prueba con números negativos
    def test_sum_negative_numbers(self):
        self.assertEqual(sum(-2, -4), -6)

    # Caso de prueba con mix de números
    def test_sum_mix_numbers(self):
        self.assertEqual(sum(-1, 0), -1)
        self.assertEqual(sum(8, -8), 0)
        self.assertEqual(sum(0, 0), 0)

# Cuando se ejecute el archivo se correrán los casos de prueba
if __name__ == "__main__":
    unittest.main()
