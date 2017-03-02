#-*- coding: utf-8 -*-

#W pliku fracs.py zdefiniować klasę Frac wraz z potrzebnymi metodami.
#Wykorzystać wyjątek ValueError do obsługi błędów w ułamkach.
#Dodać możliwości dodawania liczb (int, long) do ułamków (działania lewostronne i prawostronne).
#Rozważyć możliwość włączenia liczb float do działań na ułamkach [Wskazówka: metoda float.as_integer_ratio()].
#Napisać kod testujący moduł fracs.

class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        if((isinstance(x,int) or isinstance(x,long)) and (isinstance(y,int) or (isinstance(y,long)))):
            if(y==0):
                raise ValueError("Mianownik podany jako 0")
            elif(y<0):
                self.x=-x
                self.y=-y
            else:
                self.x = x
                self.y = y
        elif(isinstance(x,float) and (isinstance(y,int) or isinstance(y,long))):
            self.x=__ToFrac__(x).x
            self.y=__ToFrac__(x).y*y
            if (self.y < 0):
                self.x = -self.x
                self.y = -self.y
        elif((isinstance(x,int) or isinstance(x,long)) and isinstance(y,float)):
            self.x=x*__ToFrac__(y).y
            self.y=__ToFrac__(y).x
            if (self.y < 0):
                self.x = -self.x
                self.y = -self.y
        elif(isinstance(x,float) and isinstance(y,float)):
            self.x=__ToFrac__(x).x*__ToFrac__(y).y
            self.y=__ToFrac__(x).y*__ToFrac__(y).x
            if (self.y < 0):
                self.x = -self.x
                self.y = -self.y
        else:
            raise ValueError("Podane wartosci nie sa initger, long albo float")

    def __str__(self):              # zwraca "x/y" lub "x" dla y=1
        if(self.y!=1):
            return str(self.x)+"/"+str(self.y)
        else:
            return str(self.x)

    def __repr__(self):        # zwraca "Frac(x, y)"
        return "Frac(" + str(self.x) +", " + str(self.y)+")"

    def __cmp__(self, other):     # porównywanie
        tmp=self-other
        if(tmp.x==0):
            return 0
        elif(tmp.x>=0):
            return 1
        else:
            return -1

    def __add__(self, other):       # frac1+frac2, frac+int
        if(not isinstance(other, Frac)):
            other=__ToFrac__(other)
        if(self.y==other.y):
            return Frac(self.x+other.x,self.y)
        else:
            return Frac(self.x*other.y+other.x*self.y, other.y*self.y)


    __radd__=__add__              # int+frac

    def __sub__(self, other):     # frac1-frac2, frac-int
        if (not isinstance(other, Frac)):
            other =__ToFrac__(other)
        if(self.y==other.y):
            return Frac(self.x-other.x,self.y)
        return Frac(self.x*other.y-other.x*self.y,other.y*self.y)

    def __rsub__(self, other):      # int-frac
        # tutaj self jest int, a other jest frac!
        if (not isinstance(other, Frac)):
            other =__ToFrac__(other)
        if(self.y==other.y):
            return Frac(other.x-self.x,self.y)
        return Frac(other.x*self.y-self.x*other.y, other.y*self.y)

    def __mul__(self, other):     # frac1*frac2, frac*int
        if (not isinstance(other, Frac)):
            other =__ToFrac__(other)
        return Frac(other.x*self.x, other.y*self.y)

    __rmul__ = __mul__              # int*frac

    def __div__(self, other):       # frac1/frac2, frac/int
        if (not isinstance(other, Frac)):
            other = __ToFrac__(other)
        if(other.x!=0):
            return Frac(self.x*other.y, self.y*other.x)
        else:
            raise ValueError("Nie mozna dzielic przez 0")

    def __rdiv__(self, other):      # int/frac
        if (not isinstance(other, Frac)):
            other = __ToFrac__(other)
        if(self.x!=0):
            return Frac(other.x*self.y, other.y*self.x)
        else:
            raise ValueError("Nie mozna dzielic przez 0")

    # operatory jednoargumentowe
    def __pos__(self):              # +frac = (+1)*frac
        self.x*1
        return self

    def __neg__(self):              # -frac = (-1)*frac
        self.x=self.x*-1
        return self

    def __invert__(self):           # odwrotnosc: ~frac
        if(self.x!=0):
            return Frac(self.y, self.x)
        else:
            raise ValueError("Nie mozna wykonac odwrotnosci")

    def __float__(self):           # float(frac)
        return float(float(self.x)/float(self.y))

def __ToFrac__(x):
    if isinstance(x, Frac):
        return x
    elif isinstance(x, int):
        return Frac(x)
    elif isinstance(x,float):
        L=float.as_integer_ratio(x)
        return Frac(L[0], L[1])
    elif isinstance(x,long):
        return Frac(x)
    else:
        raise ValueError("Bledne dane wejsciowe")





# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase):
    def setUp(self):pass

    def test_print(self):
        self.assertEqual(Frac(2,3).__str__(),"2/3")
        self.assertEqual(Frac(2.5, 3).__str__(), "5/6")
        self.assertEqual(Frac(2.5, -3).__str__(), "-5/6")
        self.assertEqual(Frac(2,3).__repr__(),"Frac(2, 3)")
        self.assertEqual(Frac(4,1).__str__(),"4")
        self.assertEqual(Frac(5,1).__repr__(), "Frac(5, 1)")
        self.assertEqual(Frac(5, -1).__repr__(), "Frac(-5, 1)")
        with self.assertRaisesRegexp(ValueError, "Mianownik podany jako 0"):
            Frac(2,0).__str__()
        with self.assertRaisesRegexp(ValueError, "Mianownik podany jako 0"):
            Frac(5,0).__repr__()
        with self.assertRaisesRegexp(ValueError, "Podane wartosci nie sa initger, long albo float"):
            Frac("Abc",2).__str__()
        with self.assertRaisesRegexp(ValueError, "Podane wartosci nie sa initger, long albo float"):
            Frac("zwa",2).__repr__()
        with self.assertRaisesRegexp(ValueError, "Podane wartosci nie sa initger, long albo float"):
            Frac(3.5,"ab")

    def test_cmp(self):
        self.assertEqual(Frac(2,3).__cmp__(Frac(4,6)),0)
        self.assertEqual(Frac(2, 3).__cmp__(Frac(3, 6)), 1)
        self.assertEqual(Frac(2, 3).__cmp__(Frac(5, 6)), -1)
        self.assertEqual(Frac(-3).__cmp__(Frac(9,-3)),0)
        self.assertEqual(Frac(-3).__cmp__(Frac(8,-3)),-1)
        self.assertEqual(Frac(-3).__cmp__(Frac(-10,3)),1)
        self.assertEqual(Frac(0).__cmp__(Frac(0,2)),0)
        self.assertEqual(Frac(3.5).__cmp__(Frac(7,2)),0)
        self.assertEqual(Frac(574208952489741, 2).__cmp__(Frac(1148417904979482,4)),0)
        self.assertEqual(Frac(574208952489741, 2).__cmp__(Frac(1148417904979480, 4)), 1)
        self.assertEqual(Frac(574208952489741, 2).__cmp__(Frac(1148417904979484, 4)), -1)

    def test_add(self):
        self.assertEqual(Frac(1, 2)+Frac(2,1), Frac(5,2))
        self.assertEqual(Frac(3.5)+1,Frac(9,2))
        self.assertEqual(1+Frac(3.5), Frac(9, 2))
        self.assertEqual(1 + Frac(0), Frac(1, 1))
        self.assertEqual(1 + Frac(-3.5), Frac(-5, 2))
        self.assertEqual(2.5 + Frac(-3.5), Frac(-2, 2))
        self.assertEqual(287104476244869 + Frac(3,2),Frac(574208952489741,2))
        self.assertEqual(Frac(3, 2)+287104476244869, Frac(574208952489741, 2))

    def test_sub(self):
        self.assertEqual(Frac(1, 2)-(Frac(2,1)), Frac(-3,2))
        self.assertEqual(Frac(3.5)-1,Frac(5,2))
        self.assertEqual(1 - Frac(3.5), Frac(-5, 2))
        self.assertEqual(1 - Frac(0), Frac(1, 1))
        self.assertEqual(1 - Frac(-3.5), Frac(9, 2))
        self.assertEqual(2.5 - Frac(-3.5), Frac(12, 2))
        self.assertEqual(287104476244869 - Frac(3, 2), Frac(574208952489735, 2))
        self.assertEqual(Frac(3, 2) - 287104476244869, Frac(-574208952489735, 2))


    def test_mul(self):
        self.assertEqual(Frac(1, 2) * (Frac(2, 1)), Frac(2, 2))
        self.assertEqual(Frac(3.5) * 1, Frac(7, 2))
        self.assertEqual(1 * Frac(3.5), Frac(-7, -2))
        self.assertEqual(1 * Frac(0), Frac(0))
        self.assertEqual(1 * Frac(-3.5), Frac(-7, 2))
        self.assertEqual(2.5 * Frac(-3.5), Frac(-35, 4))
        self.assertEqual(287104476244869 * Frac(3, 2), Frac(861313428734607, 2))
        self.assertEqual(Frac(-3, 2) * 287104476244869, Frac(-861313428734607, 2))

    def test_div(self):
        self.assertEqual(Frac(1, 2) / (Frac(2, 1)), Frac(1, 4))
        self.assertEqual(Frac(3.5) / 1, Frac(7, 2))
        self.assertEqual(1 / Frac(3.5), Frac(-2, -7))
        self.assertEqual(Frac(0)/1, Frac(0))
        self.assertEqual(1 / Frac(-3.5), Frac(-2, 7))
        self.assertEqual(2.5 / Frac(-3.5), Frac(-10, 14))
        self.assertEqual(287104476244869 / Frac(3, 2), Frac(574208952489738, 3))
        self.assertEqual(Frac(-3, 2) / 287104476244869, Frac(-3, 574208952489738))
        with self.assertRaisesRegexp(ValueError, "Nie mozna dzielic przez 0"):
            1 / Frac(0)

    def test_pos(self):
        self.assertEqual(Frac(1,2).__pos__(),Frac(1,2))
        self.assertEqual(Frac(3,2).__pos__(),Frac(3,2))
        self.assertEqual(Frac(3, 2).__pos__(), Frac(-3, -2))
        self.assertEqual(Frac(-3,2).__pos__(),Frac(-3,2))
        self.assertEqual(Frac(-3,2).__pos__(),Frac(3,-2))
        self.assertEqual(Frac(-3.5).__pos__(),Frac(-7,2))
        self.assertEqual(Frac(0, 2).__pos__(), Frac(0))
        self.assertEqual(Frac(287104476244869).__pos__(), Frac(287104476244869,1))

    def test_neg(self):
        self.assertEqual(Frac(1, 2).__neg__(), Frac(-1, 2))
        self.assertEqual(Frac(3, 2).__neg__(), Frac(-3, 2))
        self.assertEqual(Frac(3, 2).__neg__(), Frac(3, -2))
        self.assertEqual(Frac(-3, 2).__neg__(), Frac(3, 2))
        self.assertEqual(Frac(-3, 2).__neg__(), Frac(3, 2))
        self.assertEqual(Frac(-3.5).__neg__(), Frac(-7, -2))
        self.assertEqual(Frac(0,2).__neg__(),Frac(0))
        self.assertEqual(Frac(287104476244869).__neg__(), Frac(-287104476244869, 1))

    def test_invert(self):
        self.assertEqual(Frac(1, 2).__invert__(), Frac(2))
        self.assertEqual(Frac(3, 2).__invert__(), Frac(2, 3))
        self.assertEqual(Frac(3, 2).__invert__(), Frac(-2, -3))
        self.assertEqual(Frac(-3, 2).__invert__(), Frac(-2, 3))
        self.assertEqual(Frac(-3, 2).__invert__(), Frac(2, -3))
        self.assertEqual(Frac(-3.5).__invert__(), Frac(2, -7))
        self.assertEqual(Frac(287104476244869).__invert__(), Frac(1,287104476244869))
        with self.assertRaisesRegexp(ValueError, "Nie mozna wykonac odwrotnosci"):
            Frac(0,2).__invert__()

    def test_float(self):
        self.assertEqual(float(Frac(1,2)),0.5)
        self.assertEqual(float(Frac(1, -2)), -0.5)
        self.assertEqual(float(Frac(3, 2)), 1.5)
        self.assertEqual(float(Frac(3, -2)), -1.5)
        self.assertEqual(float(Frac(-3, 2)), -1.5)
        self.assertEqual(float(Frac(-0, 2)), 0)
        self.assertEqual(float(Frac(-3.5)), -3.5)
        self.assertEqual(float(Frac(1, 0.5)), 2)
        self.assertEqual(float(Frac(287104476244869)),287104476244869)
        #self.assertEqual(float(Frac(10.2)),10.2) #istnieje jakis sposob zeby funckja float.as_integer_ratio(float x) zwracala cos ladniejszego dla 10.2 jak 102 i 10 niz 2 wartosci long?

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()  # wszystkie testy


