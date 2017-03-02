#-*- coding: utf-8 -*-

#Poprawić implementację tablicową stosu tak, aby korzystała z wyjątków w przypadku pojawienia się błędu.
#Metoda pop() ma zgłaszać błąd w przypadku pustego stosu. Metoda push() ma zgłaszać błąd w przypadku przepełnienia stosu.
#Napisać kod testujący stos.

class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise IndexError("Przepelnienie stosu")
        else:
            self.items[self.n] = data
            self.n = self.n + 1


    def pop(self):
        if self.is_empty():
            raise IndexError("Brak elementow na stosie")
        else:
            self.n = self.n - 1
            data = self.items[self.n]
            self.items[self.n] = None    # usuwam referencję
            return data

import unittest

class TestStack(unittest.TestCase):

    def setUp(self): pass

    def test_is_empty(self):
        self.assertEqual(Stack(5).is_empty(), True)
        self.assertEqual(Stack().is_empty(),True)
        self.assertEqual(Stack(0).is_empty(),True)
        stos=Stack(5)
        stos.push(5)
        self.assertEqual(stos.is_empty(),False)
        stos.pop()
        self.assertEqual(stos.is_empty(),True)

    def test_is_full(self):
        self.assertEqual(Stack(3).is_full(),False)
        self.assertEqual(Stack().is_full(),False)
        self.assertEqual(Stack(0).is_full(),True)
        stos=Stack(2)
        stos.push(1)
        self.assertEqual(stos.is_full(),False)
        stos.push(2)
        self.assertEqual(stos.is_full(),True)

    def test_pop(self):
        with self.assertRaisesRegexp(IndexError, "Brak elementow na stosie"):
            Stack(3).pop()
        with self.assertRaisesRegexp(IndexError, "Brak elementow na stosie"):
            Stack().pop()
        stos=Stack(5)
        stos.push(3)
        self.assertEqual(stos.pop(),3)
        stos.push(5)
        stos.push(8)
        self.assertEqual(stos.pop(),8)

    def test_put(self):
        stos=Stack(3)
        stos.push(3)
        stos.push(2)
        stos.push(1)
        with self.assertRaisesRegexp(IndexError, "Przepelnienie stosu"):
            stos.push(3)
        stos.pop()
        stos.push(2)


    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy



