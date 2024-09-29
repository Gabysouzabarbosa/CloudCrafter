import unittest


# Funções de exemplo para serem testadas
def soma(a, b):
    return a + b


def multiplica(a, b):
    return a * b


def eh_par(n):
    return n % 2 == 0


def para_maiusculas(texto):
    return texto.upper()


class TestUnitarios(unittest.TestCase):

    def test_soma_valores_positivos(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_valores_negativos(self):
        self.assertEqual(soma(-1, -1), -2)

    def test_soma_valor_positivo_negativo(self):
        self.assertEqual(soma(-1, 1), 0)

    def test_multiplica_valores(self):
        self.assertEqual(multiplica(2, 5), 10)

    def test_eh_par(self):
        self.assertTrue(eh_par(4))
        self.assertFalse(eh_par(3))

    def test_para_maiusculas(self):
        self.assertEqual(para_maiusculas('teste'), 'TESTE')


if __name__ == '__main__':
    unittest.main()
