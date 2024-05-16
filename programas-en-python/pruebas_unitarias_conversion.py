import unittest

def conversion(valor, medida):
    if medida == "mm":
        return valor * 1000
    elif medida == "cm":
        return valor * 100
    elif medida == "dm":
        return valor * 10 
    elif medida == "km":
        return valor / 1000
    else:
        return "¡Error! medida no válida"
    
class TestFunctionConversion(unittest.TestCase):

    def test_conversion_mm(self):
        self.assertEqual(conversion(4, "mm"), 4000)

    def test_conversion_cm(self):
        self.assertEqual(conversion(4, "cm"), 400)
    
    def test_conversion_dm(self):
        self.assertEqual(conversion(4, "dm"), 40)
    
    def test_conversion_km(self):
        self.assertEqual(conversion(4, "km"), 0.004)

    def test_conversion_error(self):
        self.assertEqual(conversion(4, "metros"), "¡Error! medida no válida")

if __name__ == "__main__":
    unittest.main()
