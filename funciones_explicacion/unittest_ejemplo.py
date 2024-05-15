import unittest

def sum(a, b):
    return a + b

class TestSumFunction(unittest.TestCase):

    def test_sum_positive_numbers(self):
        self.assertEqual(sum(2, 3), 5)

    def test_sum_negative_numbers(self):
        self.assertEqual(sum(-2, -3), -5)

    def test_sum_mixed_numbers(self):
        self.assertEqual(sum(2, -3), -1)
        self.assertEqual(sum(-2, 3), 1)

if __name__ == "__main__":
    unittest.main()


    