import unittest
from Sistema_Numeracion import *
class TestConversionFunctions(unittest.TestCase):

    def test_decimal_a_binario(self):
        self.assertEqual(decimal_a_binario(10), '1010')
        self.assertEqual(decimal_a_binario(0), '0')
        self.assertEqual(decimal_a_binario(127), '1111111')
        self.assertEqual(decimal_a_binario(256), '100000000')

    def test_decimal_a_octal(self):
        self.assertEqual(decimal_a_octal(10), '12')
        self.assertEqual(decimal_a_octal(0), '0')
        self.assertEqual(decimal_a_octal(127), '177')
        self.assertEqual(decimal_a_octal(256), '400')

    def test_decimal_a_hexadecimal(self):
        self.assertEqual(decimal_a_hexadecimal(10), 'A')
        self.assertEqual(decimal_a_hexadecimal(0), '0')
        self.assertEqual(decimal_a_hexadecimal(127), '7F')
        self.assertEqual(decimal_a_hexadecimal(256), '100')

    def test_binario_a_decimal(self):
        self.assertEqual(binario_a_decimal('1010'), 10)
        self.assertEqual(binario_a_decimal('0'), 0)
        self.assertEqual(binario_a_decimal('1111111'), 127)
        self.assertEqual(binario_a_decimal('100000000'), 256)

    def test_binario_a_octal(self):
        self.assertEqual(binario_a_octal('1010'), '12')
        self.assertEqual(binario_a_octal('0'), '0')
        self.assertEqual(binario_a_octal('1111111'), '177')
        self.assertEqual(binario_a_octal('100000000'), '400')

    def test_binario_a_hexadecimal(self):
        self.assertEqual(binario_a_hexadecimal('1010'), 'A')
        self.assertEqual(binario_a_hexadecimal('0'), '0')
        self.assertEqual(binario_a_hexadecimal('1111111'), '7F')
        self.assertEqual(binario_a_hexadecimal('100000000'), '100')

    def test_octal_a_decimal(self):
        self.assertEqual(octal_a_decimal('12'), 10)
        self.assertEqual(octal_a_decimal('0'), 0)
        self.assertEqual(octal_a_decimal('177'), 127)
        self.assertEqual(octal_a_decimal('400'), 256)

    def test_octal_a_binario(self):
        self.assertEqual(octal_a_binario('12'), '1010')
        self.assertEqual(octal_a_binario('0'), '0')
        self.assertEqual(octal_a_binario('177'), '1111111')
        self.assertEqual(octal_a_binario('400'), '100000000')

    def test_octal_a_hexadecimal(self):
        self.assertEqual(octal_a_hexadecimal('12'), 'A')
        self.assertEqual(octal_a_hexadecimal('0'), '0')
        self.assertEqual(octal_a_hexadecimal('177'), '7F')
        self.assertEqual(octal_a_hexadecimal('400'), '100')

    def test_hexadecimal_a_decimal(self):
        self.assertEqual(hexadecimal_a_decimal('A'), 10)
        self.assertEqual(hexadecimal_a_decimal('0'), 0)
        self.assertEqual(hexadecimal_a_decimal('7F'), 127)
        self.assertEqual(hexadecimal_a_decimal('100'), 256)

    def test_hexadecimal_a_binario(self):
        self.assertEqual(hexadecimal_a_binario('A'), '1010')
        self.assertEqual(hexadecimal_a_binario('0'), '0')
        self.assertEqual(hexadecimal_a_binario('7F'), '1111111')
        self.assertEqual(hexadecimal_a_binario('100'), '100000000')


if __name__ == '__main__':
    unittest.main()
