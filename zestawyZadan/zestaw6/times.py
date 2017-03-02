#-*- coding: utf-8 -*-

#W pliku times.py zdefiniować klasę Time wraz z potrzebnymi metodami.
#Odcinek czasu jest określony przez liczbę sekund.
#Napisać kod testujący moduł times.

class Time:
    """Klasa reprezentująca odcinek czasu."""

    def __init__(self, s=0):
        """Zwraca instancję klasy Time."""
        self.s = int(s)

    def __str__(self):
        """Zwraca string 'hh:mm:ss'."""
        h = self.s / 3600
        sec = self.s - h * 3600
        m = sec / 60
        sec = sec - m * 60
        return "{0:02d}:{1:02d}:{2:02d}".format(h, m, sec)

    def __repr__(self):
        """Zwraca string 'Time(s)'."""
        return "Time({0})".format(self.s)

    def __add__(self, other):
        """Dodawanie odcinków czasu."""
        return Time(self.s + other.s)

    def __cmp__(self, other):           # porównywanie, -1|0|+1
        """Porównywanie odcinków czasu."""
        return cmp(self.s, other.s)

    def __int__(self):                  # int(time1)
        """Konwersja odcinka czasu do int."""
        return self.s

# Kod testujący moduł.

import unittest

class TestTime(unittest.TestCase):
    def setUp(self):pass

    #test_print

    def test_print(self):
        self.assertEqual(Time(60).__str__(),"00:01:00")
        self.assertEqual(Time(60).__repr__(),"Time(60)")
        self.assertEqual(Time(0).__str__(),"00:00:00")
        self.assertEqual(Time(0).__repr__(),"Time(0)")
        self.assertEqual(Time(61).__str__(),"00:01:01")
        self.assertEqual(Time(61).__repr__(),"Time(61)")
        self.assertEqual(Time(671).__str__(),"00:11:11")
        self.assertEqual(Time(671).__repr__(),"Time(671)")
        self.assertEqual(Time(3600).__str__(),"01:00:00")
        self.assertEqual(Time(3600).__repr__(),"Time(3600)")
        self.assertEqual(Time(3661).__str__(),"01:01:01")
        self.assertEqual(Time(3661).__repr__(),"Time(3661)")

    #test_add

    def test_add(self):
        self.assertEqual(Time(1).__add__(Time(2)), Time(3))
        self.assertEqual(Time(10).__add__(Time(10)),Time(20))
        self.assertEqual(Time(0).__add__(Time(0)), Time(0))

    #test_cmp

    def test_cmp(self):
        self.assertEqual(Time(10).__cmp__(Time(10)),0)
        self.assertEqual(Time(3).__cmp__(Time(1)), 1)
        self.assertEqual(Time(1).__cmp__(Time(3)), -1)
        self.assertEqual(Time(0).__cmp__(Time(0)),0)

    #test_int

    def test_int(self):
        self.assertEqual(Time(10).__int__(),10)
        self.assertEqual(Time(0).__int__(),0)
        self.assertEqual(Time(3601).__int__(),3601)

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy