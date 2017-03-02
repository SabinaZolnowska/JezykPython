#-*- coding: utf-8 -*-

#W pliku points.py zdefiniować klasę Point wraz z potrzebnymi metodami.
#Punkty są traktowane jak wektory zaczepione w początku układu współrzędnych, o końcu w położeniu (x, y).
#Napisać kod testujący moduł points.

import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x=0, y=0):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):              # zwraca string "(x, y)"
        return "("+str(self.x)+", "+str(self.y)+")"

    def __repr__(self):             # zwraca string "Point(x, y)"
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"
        #return "Point"+self.__str__()

    def __eq__(self, other):        # obsługa point1 == point2
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):        # obsługa point1 != point2
        return not ((self.x == other.x) and (self.y == other.y))
        #return not self.__eq__(other)

    # Punkty jako wektory 2D.
    def __add__(self, other):       # v1 + v2
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):       # v1 - v2
        return Point(self.x-other.x, self.y-other.y)

    def __mul__(self, other):       # v1 * v2, iloczyn skalarny
        return self.x*other.x + self.y*other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):               # długość wektora
        return math.sqrt(math.pow(self.x,2)+math.pow(self.y,2))

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):

    def setUp(self):pass

    def test_print(self):
        self.assertEqual(Point(3,4).__str__(),"(3, 4)")
        self.assertEqual(Point(3,4).__repr__(),"Point(3, 4)")
        self.assertEqual(Point(0, 0).__str__(), "(0, 0)")
        self.assertEqual(Point(0, 0).__repr__(),"Point(0, 0)")
        self.assertEqual(Point(-3, 4).__str__(), "(-3, 4)")
        self.assertEqual(Point(-3,4).__repr__(),"Point(-3, 4)")

    def test_eq(self):
        self.assertFalse(Point(0,0).__eq__(Point(1,2)))
        self.assertFalse(Point(-1,1).__eq__(Point(1,1)))
        self.assertTrue(Point(-3,2).__eq__(Point(-3,2)))
        self.assertTrue(Point(-0,0).__eq__(Point(0,0)))

    def test_ne(self):
        self.assertTrue(Point(0,0).__ne__(Point(1,2)))
        self.assertTrue(Point(-1,1).__ne__(Point(1,1)))
        self.assertFalse(Point(-3,2).__ne__(Point(-3,2)))
        self.assertFalse(Point(-0,0).__ne__(Point(0,0)))

    def test_add(self):
        self.assertEqual(Point(1,2).__add__(Point(2,3)),Point(3,5))
        self.assertEqual(Point(0,0).__add__(Point(0,5)),Point(0,5))
        self.assertEqual(Point(-5,-2).__add__(Point(2,8)),Point(-3,6))

    def test_sub(self):
        self.assertEqual(Point(1,2).__sub__(Point(2,3)),Point(-1,-1))
        self.assertEqual(Point(0,0).__sub__(Point(0,5)),Point(0,-5))
        self.assertEqual(Point(5,-2).__sub__(Point(2,8)),Point(3,-10))

    def test_mul(self):
        self.assertEqual(Point(0,0).__mul__(Point(1,2)),0)
        self.assertEqual(Point(2,5).__mul__(Point(1,1)),7)
        self.assertEqual(Point(-2,2).__mul__(Point(3,-3)),-12)

    def test_cross(self):
        self.assertEqual(Point(0,0).cross(Point(3,5)),0)
        self.assertEqual(Point(2,5).cross(Point(1,1)),-3)
        self.assertEqual(Point(-2,2).cross(Point(3,-3)),0)

    def test_length(self):
        self.assertEqual(Point(0,0).length(),0)
        self.assertEqual(Point(2,2).length(),math.sqrt(8))
        self.assertEqual(Point(4,0).length(),4)
        self.assertEqual(Point(-3,4).length(),5)

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy