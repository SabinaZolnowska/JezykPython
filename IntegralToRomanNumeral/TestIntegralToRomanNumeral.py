# -*- coding: utf-8 -*-

from IntegralToRomanNumeral import IntegralToRomanNumeral
import unittest

class TestIntegralToRomanNumeral(unittest.TestCase):

    def setUp(self):
        pass

    def test__init__(self):
        self.assertEqual(IntegralToRomanNumeral(0).integralNumeral, 0)
        self.assertEqual(IntegralToRomanNumeral(4000).integralNumeral, 4000)
        self.assertEqual(IntegralToRomanNumeral(3500).integralNumeral, 3500)
        self.assertEqual(IntegralToRomanNumeral("test").integralNumeral, "test")
        self.assertEqual(IntegralToRomanNumeral(1).integralNumeral, 1)
        self.assertEqual(IntegralToRomanNumeral(15.5).integralNumeral, 15.5)


    def testifCorrectIntegral(self):

        #jak sprawdzić czy funkcja zadziała poprawnie jeśli nie zwraca nic w przypadku poprawnych danych wejściowych?

        with self.assertRaisesRegex(ValueError, "Given value isn't integral"):
           self.assertEqual(IntegralToRomanNumeral("test23").ifCorrectIntegral())

        with self.assertRaisesRegex(ValueError, "Given value isn't integral"):
            self.assertEqual(IntegralToRomanNumeral("23something").ifCorrectIntegral())

        with self.assertRaisesRegex(ValueError, "Given value isn't integral"):
            self.assertEqual(IntegralToRomanNumeral(25.5).ifCorrectIntegral())

        with self.assertRaisesRegex(ValueError, "Incorrect value"):
            self.assertEqual(IntegralToRomanNumeral(0).ifCorrectIntegral())

        with self.assertRaisesRegex(ValueError, "Incorrect value"):
            self.assertEqual(IntegralToRomanNumeral(-120).ifCorrectIntegral())

        with self.assertRaisesRegex(ValueError, "Incorrect value"):
            self.assertEqual(IntegralToRomanNumeral(4000).ifCorrectIntegral())

        with self.assertRaisesRegex(ValueError, "Incorrect value"):
            self.assertEqual(IntegralToRomanNumeral(9801).ifCorrectIntegral())

    def testintegralToRomanNumeral(self):

        #jak napisać test, który sprawdzi czy wywołana funkcja ifCorrectIntegral() wyrzuciła wyjątek w testintegralToRomanNumeral()?

        self.assertEqual(IntegralToRomanNumeral(1).integralToRomanNumeral(), "I")
        self.assertEqual(IntegralToRomanNumeral(3999).integralToRomanNumeral(), "MMMCMXCIX")
        self.assertEqual(IntegralToRomanNumeral(100).integralToRomanNumeral(), "C")
        self.assertEqual(IntegralToRomanNumeral(23).integralToRomanNumeral(),"XXIII")
        self.assertEqual(IntegralToRomanNumeral(1818).integralToRomanNumeral(),"MDCCCXVIII")

if __name__ == '__main__':
    unittest.main()