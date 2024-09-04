import unittest
from main import is_fibonacci  # Importa a função is_fibonacci do arquivo main.py

class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        # Testa números que estão na sequência de Fibonacci
        self.assertTrue(is_fibonacci(5))
        self.assertTrue(is_fibonacci(21))
        self.assertTrue(is_fibonacci(34))
        
        # Testa números que não estão na sequência de Fibonacci
        self.assertFalse(is_fibonacci(22))
        self.assertFalse(is_fibonacci(4))
        self.assertFalse(is_fibonacci(35))

if __name__ == '__main__':
    unittest.main()
