#-*- coding: utf-8 -*-

#Za pomocą techniki programowania dynamicznego napisać program obliczający wartości funkcji P(i, j).
#Porównać z wersją rekurencyjną programu.
#Wskazówka: Wykorzystać tablicę dwuwymiarową (np. słownik) do przechowywania wartości funkcji.
#Wartości w tablicy wypełniać kolejno wierszami.

#P(0, 0) = 0.5,
#P(i, 0) = 0.0 dla i > 0,
#P(0, j) = 1.0 dla j > 0,
#P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.

import time

def P(i=5,j=5):
    if(isinstance(i,int)and isinstance(i,int))and(i>=0 and j>=0):
        if(i==0 and j==0):
            return 0.5
        elif(i==0):
            return 1
        elif(j==0):
            return 0
        elif(i<j):
            Matrix=[[0 for k in range(0,j+1)] for l in range(0,j+1)] #istnieje jakas lepsza metoda do zadelkarowania macierzy, ktora bylaby niekwadratowa?
        else:
            Matrix = [[0 for k in range(0, i+1)] for l in range(0, i+1)]

        for k in range(i+1):
            Matrix[k][0] = 0
            for l in range(j+1):
                Matrix[0][l]=1
        Matrix[0][0]=0.5

        for k in range(1,i+1):
            for l in range(1,j+1):
                Matrix[k][l]=0.5*(Matrix[k-1][l]+Matrix[k][l-1])

    else:
        raise ValueError("Argumentami moga byc tylko wartosci typu int, dodatnie")
    return Matrix[k][l]


def Pr(i=5,j=5):
    if(isinstance(i,int)and isinstance(i,int))and(i>=0 and j>=0):
        if(i==0 and j==0):
            return 0.5
        elif(i==0):
            return 1
        elif(j==0):
            return 0
        return 0.5*(Pr(i-1,j)+Pr(i,j-1))
    else:
        raise ValueError("Argumentami moga byc tylko wartosci typu int, dodatnie")

def Porownanie(i,j):
    start=time.clock()
    P(i,j)
    timeP=time.clock()-start

    start=time.clock()
    Pr(i,j)
    timePr=time.clock()-start

    print "Czas obliczania funkcji P w sposob dynamiczny dla i="+str(i)+", j="+str(j)+ " wynosi "+str(timeP)+" s"
    print "Czas obliczania funkcji P w sposob rekurencyjny dla i="+str(i)+", j="+str(j)+ " wynosi "+str(timePr)+" s"

    #przykladowe wyniki

    #Czas obliczania funkcji P w sposob dynamiczny dla i = 15, j = 15 wynosi 0.000124014034968 s
    #Czas obliczania funkcji P w sposob rekurencyjny dla i = 15, j = 15 wynosi 192.065826222 s

    #Czas obliczania funkcji P w sposob dynamiczny dla i = 10, j = 10 wynosi 0.000121020592744 s
    #Czas obliczania funkcji P w sposob rekurencyjny dla i = 10, j = 10 wynosi 0.225076065505 s

i=2
j=4
print P(3,4)
Porownanie(10,10)

import unittest

class TestFrac(unittest.TestCase):
    def setUp(self):pass

    def test_P(self):
        self.assertEqual(P(1,1),0.5)
        self.assertEqual(P(10,10),0.5)
        self.assertEqual(P(3,4),0.65625)
        self.assertEqual(P(2,3),0.6875)
        self.assertEqual(P(0, 0), 0.5)
        self.assertEqual(P(3, 0), 0)
        self.assertEqual(P(0, 5), 1)
        with self.assertRaisesRegexp(ValueError, "Argumentami moga byc tylko wartosci typu int, dodatnie"):
            P("a",3)
        with self.assertRaisesRegexp(ValueError, "Argumentami moga byc tylko wartosci typu int, dodatnie"):
            P(8,-3)

    def test_Pr(self):
        self.assertEqual(Pr(1,1),0.5)
        self.assertEqual(Pr(10,10),0.5)
        self.assertEqual(Pr(3,4),0.65625)
        self.assertEqual(Pr(2,3),0.6875)
        self.assertEqual(Pr(0, 0), 0.5)
        self.assertEqual(Pr(3, 0), 0)
        self.assertEqual(Pr(0, 5), 1)
        with self.assertRaisesRegexp(ValueError, "Argumentami moga byc tylko wartosci typu int, dodatnie"):
            Pr("a",3)
        with self.assertRaisesRegexp(ValueError, "Argumentami moga byc tylko wartosci typu int, dodatnie"):
            Pr(8,-3)
    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()  # wszystkie testy
