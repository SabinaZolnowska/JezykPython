#-*- coding: utf-8 -*-

#Poprawić metodę get(), aby w przypadku pustej kolejki zwracała wyjątek.
#Poprawić metodę put() w tablicowej implementacji kolejki, aby w przypadku przepełnienia kolejki zwracała wyjątek.
#Napisać kod testujący kolejkę.


class Queue:
    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0           # pierwszy do pobrania
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise IndexError("Kolejka jest przepelniona")
        else:
            self.items[self.tail] = data
            self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise IndexError("Brak elementow w kolejce")
        else:
            data = self.items[self.head]
            self.items[self.head] = None      # usuwam referencję
            self.head = (self.head + 1) % self.n
            return data

import unittest

class TestQueue(unittest.TestCase):

    def setUp(self): pass

    def test_is_empty(self):
        self.assertEqual(Queue(5).is_empty(), True)
        self.assertEqual(Queue().is_empty(),True)
        self.assertEqual(Queue(0).is_empty(),True)
        kolejka=Queue(5)
        kolejka.put(5)
        self.assertEqual(kolejka.is_empty(),False)
        kolejka.get()
        self.assertEqual(kolejka.is_empty(),True)

    def test_is_full(self):
        self.assertEqual(Queue(3).is_full(),False)
        self.assertEqual(Queue().is_full(),False)
        self.assertEqual(Queue(0).is_full(),True)
        kolejka=Queue(2)
        kolejka.put(1)
        self.assertEqual(kolejka.is_full(),False)
        kolejka.put(2)
        self.assertEqual(kolejka.is_full(),True)

    def test_get(self):
        with self.assertRaisesRegexp(IndexError, "Brak elementow w kolejce"):
            Queue(3).get()
        with self.assertRaisesRegexp(IndexError, "Brak elementow w kolejce"):
            Queue().get()
        kolejka=Queue(5)
        kolejka.put(3)
        self.assertEqual(kolejka.get(),3)
        kolejka.put(5)
        kolejka.put(8)
        self.assertEqual(kolejka.get(),5)

    def test_put(self):
        kolejka=Queue(3)
        kolejka.put(3)
        kolejka.put(2)
        kolejka.put(1)
        with self.assertRaisesRegexp(IndexError, "Kolejka jest przepelniona"):
            kolejka.put(3)
        kolejka.get()
        kolejka.put(2)


    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
