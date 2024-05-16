import unittest

def lista_ordenada(lista):
    lista.sort()
    return lista

class TestFuncionListaOrdenada(unittest.TestCase):

    def test_lista_desordenada(self):
        self.assertEqual(lista_ordenada([3,2,1]), [1,2,3])

    def test_lista_ordenada(self):
        self.assertEqual(lista_ordenada([1,2,3]), [1,2,3])

    def test_lista_vacia(self):
        self.assertEqual(lista_ordenada([]), [])
    
    def test_lista_repetida(self):
        self.assertListEqual(lista_ordenada([1,1,1,1,1]), [1,1,1,1,1])
    
    def test_lista_letras(self):
        self.assertEqual(lista_ordenada(['a', 'e', 'z', 'o']), ['a', 'e', 'o', 'z'])

if __name__ == "__main__":
    unittest.main()