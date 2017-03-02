#-*- coding: utf-8 -*-

#Zaimplementować algorytm obliczający pole powierzchni trójkąta, jeżeli dane są trzy liczby będące długościami jego boków.
#Jeżeli podane liczby nie spełniają warunku trójkąta, to program ma generować wyjątek ValueError.

import math

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if (isinstance(a,float)or isinstance(a,long) or isinstance(a,int))and (isinstance(b,float)or isinstance(b,long) or isinstance(b,int))and (isinstance(c,float)or isinstance(c,long) or isinstance(c,int)):
        if a>0 and b>0 and c>0:
            try:
                area=(math.sqrt((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c)))/4
                if area == 0:
                    raise ValueError()
                return area
            except ValueError:
                return "Bledne dlugosci bokow trojkata"
        else:
            raise ValueError("Dlugosci bokow trojkata nie moga byc ujemne lub zerowe")
    else:
        raise ValueError("Podano bledny typ argumentow")

import unittest

class TestFrac(unittest.TestCase):
    def setUp(self):pass

    def test_heron(self):
        self.assertEqual(heron(12,13,5),30)
        self.assertEqual(heron(3,4,5),6)
        self.assertEqual(round(heron(7,3,8),2),10.39)
        self.assertEqual(heron(10,2,4),"Bledne dlugosci bokow trojkata")
        self.assertEqual(heron(10,5,5),"Bledne dlugosci bokow trojkata")
        with self.assertRaisesRegexp(ValueError,"Dlugosci bokow trojkata nie moga byc ujemne lub zerowe"):
            heron(0,1,2)
        with self.assertRaisesRegexp(ValueError, "Dlugosci bokow trojkata nie moga byc ujemne lub zerowe"):
            heron(-5, 3, 4)
        with self.assertRaisesRegexp(ValueError,"Podano bledny typ argumentow"):
            heron("abc",3,12)

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()  # wszystkie testy