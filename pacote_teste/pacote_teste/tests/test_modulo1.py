import unittest
from pacote_teste.modulo1 import funcao1

class TestModulo1(unittest.TestCase):
    def test_funcao1(self):
        self.assertEqual(funcao1(), "Hello from modulo1")

if __name__ == '__main__':
    unittest.main()