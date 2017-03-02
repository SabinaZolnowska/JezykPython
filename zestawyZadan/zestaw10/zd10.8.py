#-*- coding: utf-8 -*-

#Stworzyć ADT w postaci kolejki losowej, z której elementy będą pobierane w losowej kolejności.
#Zadbać o to, aby każda operacja była wykonywana w stałym czasie, niezależnie od liczby elementów w kolejce.

import random

class RandomQueue:
    def __init__(self, size=5):
        self.n = size + 1  # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0  # pierwszy do pobrania
        self.tail = 0  # pierwsze wolne

    def insert(self, item):
        if self.is_full():
            raise IndexError("Kolejka jest przepelniona")
        else:
            self.items[self.tail] = item
            self.tail = (self.tail + 1) % self.n

    def remove(self):
        if self.is_empty():
            raise IndexError("Brak elementow w kolejce")
        else:
            positionElement=random.randint(0, self.tail-1)
            data = self.items[positionElement]
            self.items[positionElement] = self.items[self.tail-1]  # na miejsce usuwanego elementu wkladamy ostatni element
            self.tail=self.tail-1 # usuwamy referencje do ostatniego elementu
            return data


    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n - 1) % self.n == self.tail


import unittest

class TestRandomQueue(unittest.TestCase):

    def setUp(self): pass

    def test_is_empty(self):
        self.assertEqual(RandomQueue(5).is_empty(), True)
        self.assertEqual(RandomQueue().is_empty(), True)
        self.assertEqual(RandomQueue(0).is_empty(), True)
        kolejka = RandomQueue(5)
        kolejka.insert(5)
        self.assertEqual(kolejka.is_empty(), False)
        kolejka.remove()
        self.assertEqual(kolejka.is_empty(), True)

    def test_is_full(self):
        self.assertEqual(RandomQueue(3).is_full(), False)
        self.assertEqual(RandomQueue().is_full(), False)
        self.assertEqual(RandomQueue(0).is_full(), True)
        kolejka = RandomQueue(2)
        kolejka.insert(1)
        self.assertEqual(kolejka.is_full(), False)
        kolejka.insert(2)
        self.assertEqual(kolejka.is_full(), True)

    def test_remove(self):
        with self.assertRaisesRegexp(IndexError, "Brak elementow w kolejce"):
            RandomQueue(3).remove()
        with self.assertRaisesRegexp(IndexError, "Brak elementow w kolejce"):
            RandomQueue().remove()
        kolejka = RandomQueue(5)
        kolejka.insert(3)
        self.assertEqual(kolejka.remove(), 3)

    def test_Insert(self):
        kolejka = RandomQueue(3)
        kolejka.insert(3)
        kolejka.insert(2)
        kolejka.insert(1)
        with self.assertRaisesRegexp(IndexError, "Kolejka jest przepelniona"):
            kolejka.insert(3)
            kolejka.remove()
            kolejka.insert(2)

    def tearDown(self): pass

    if __name__ == '__main__':
        unittest.main()  # uruchamia wszystkie testy
