#-*- coding: utf-8 -*-

#W pliku rectangles.py zdefiniować klasę Rectangle wraz z potrzebnymi metodami.
#Wykorzystać wyjątek ValueError do obsługi błędów. Napisać kod testujący moduł rectangles.

from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
    # Chcemy, aby x1 <= x2, y1 <= y2.
        if((isinstance(x1,int)or isinstance(x1,float))and (isinstance(y1,int) or isinstance(y1,float))and
            (isinstance(x2,int) or isinstance(x2,float))  and (isinstance(y2,int) or isinstance(y2,float))):
            if(x1!=x2 and y1!=y2):
                if(x1>x2):
                    tmp=x1
                    x1=x2
                    x2=tmp
                if(y1>y2):
                    tmp=y1
                    y1=y2
                    y2=tmp
                self.pt1 = Point(x1, y1)
                self.pt2 = Point(x2, y2)
            else:
                raise ValueError("Bledne wspolrzedne wierzcholkow")
        else:
            raise ValueError("Wprowadzono bledne dane w konstruktorze")


    def __str__(self):              # "[(x1, y1), (x2, y2)]"
        return "["+self.pt1.__str__()+", "+self.pt2.__str__()+"]"

    def __repr__(self):             # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle("+str(self.pt1.x)+", "+str(self.pt1.y)+", "+str(self.pt2.x)+", "+str(self.pt2.y)+")"

    def __eq__(self, other):        # obsługa rect1 == rect2
        if(isinstance(other,Rectangle)):
            return self.pt1.__eq__(other.pt1) and self.pt2.__eq__(other.pt2)
        else:
            raise ValueError("Argumentem nie jest prostokat")

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self.__eq__(other)

    def center(self):               # zwraca środek prostokąta
        tmp=self.pt2-self.pt1
        tmp.x=float(tmp.x)/2
        tmp.y=float(tmp.y)/2
        return self.pt1+tmp

    def area(self):                 # pole powierzchni
        width = self.pt2.x-self.pt1.x
        height =self.pt2.y-self.pt1.y
        area=width*height
        if(area<0):
            return area*(-1)
        else:
            return area

    def move(self, x, y):         # przesunięcie o (x, y)
        if((isinstance(x,int) or isinstance(x,float)) and (isinstance(y,int) or isinstance(y,float))):
        #sprawdz czy int/float
            return Rectangle(self.pt1.x+x,self.pt1.y+y,self.pt2.x+x,self.pt2.y+y)
        else:
            raise ValueError("Wprowadzono bledne dane w przesuniecia")

    def intersection(self, other):  # część wspólna prostokątów
        if(self.pt1.x>other.pt2.x and self.pt1.y<other.pt2.y):
            if(self.pt2.x>=other.pt2.x and self.pt2.y>=other.pt2.y):
                #(self, x1=0, y1=0, x2=0, y2=0):
                return Rectangle(self.pt1.x,self.pt1.y,other.pt2.x,other.pt2.y).area()

    def cover(self, other):         # prostąkąt nakrywający oba

        def max(x1,x2):
            if(x1>x2):
                return x1
            else:
                return x2

        def min(x1,x2):
            if(x1>x2):
                return x2
            else:
                return x1

        if(isinstance(other,Rectangle)):
            #nie branie pod uwage tych co sie nie nakladaja
            wpX=max(self.pt1.x,other.pt1.x)
            wkX=min(self.pt2.x,other.pt2.x)
            czwX=wkX-wpX

            wpY=max(self.pt1.y,other.pt1.y)
            wkY=min(self.pt2.y,other.pt2.y)
            czwY=wkY-wpY

            if((czwX<=0) or (czwY<=0)):
                return 0
            else:
                tmpx1=max(self.pt1.x, other.pt1.x)
                tmpy1=max(self.pt1.y, other.pt1.y)
                tmpx2=min(self.pt2.x, other.pt2.x)
                tmpy2=min(self.pt2.y, other.pt2.y)
                return Rectangle(tmpx1,tmpy1,tmpx2,tmpy2).area()
        else:
            raise ValueError("Argument nie jest prostokatem")

    def make4(self):               # zwraca listę czterech mniejszych
        tmp=self.center()
        return [Rectangle(self.pt1.x, self.pt1.y, tmp.x, tmp.y), Rectangle(tmp.x, tmp.y, self.pt2.x, self.pt2.y), Rectangle(self.pt1.x,tmp.y, tmp.x,self.pt2.y), Rectangle(tmp.x,self.pt1.y,self.pt2.x,tmp.y)]

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):

    def setUp(self):pass

    def test_init(self):
        self.assertEqual(Rectangle(3,3,2,2),Rectangle(2,2,3,3))
        self.assertEqual(Rectangle(3.5, 3.2, 2, 2), Rectangle(2, 2, 3.5, 3.2))
        with self.assertRaisesRegexp(ValueError, "Bledne wspolrzedne wierzcholkow"):
            Rectangle(2,2,2,2)
        with self.assertRaisesRegexp(ValueError, "Wprowadzono bledne dane w konstruktorze"):
            Rectangle(2, 2, 2, "abc")

    def test_print(self):
        self.assertEqual(str(Rectangle(4,3,2,1)),"[(2, 1), (4, 3)]")
        self.assertEqual(str(Rectangle(-2,-3,4,6)),"[(-2, -3), (4, 6)]")
        self.assertEqual(str(Rectangle(4.5, 3, 2.4, 1)), "[(2.4, 1), (4.5, 3)]")
        self.assertEqual(repr(Rectangle(0,0,2,2)),"Rectangle(0, 0, 2, 2)")
        self.assertEqual(repr(Rectangle(-0,-2,1,3)),"Rectangle(0, -2, 1, 3)")
        self.assertEqual(repr(Rectangle(-0.3, -2, 1.8, 3)), "Rectangle(-0.3, -2, 1.8, 3)")

    def test_eq(self):
        self.assertTrue(Rectangle(3,3,2,2).__eq__(Rectangle(2,2,3,3)))
        self.assertTrue(Rectangle(-0,0,2,2).__eq__(Rectangle(2,2,0,0)))
        self.assertFalse(Rectangle(2,3,4,5).__eq__(Rectangle(-2,-3,-4,-5)))
        self.assertFalse(Rectangle(2.5,3,4,5).__eq__(Rectangle(2,3,4,5)))

    def test_ne(self):
        self.assertFalse(Rectangle(3,3.5,2,2).__ne__(Rectangle(2,2,3,3.5)))
        self.assertFalse(Rectangle(-0,0,2,2).__ne__(Rectangle(2,2,0,0)))
        self.assertTrue(Rectangle(2,3,4,5).__ne__(Rectangle(-2,-3,-4,-5)))
        self.assertTrue(Rectangle(2.5,3,4,5).__ne__(Rectangle(2,3,4,5)))

    def test_center(self):
        self.assertEqual(Rectangle(-2,-2,4,4).center(),Point(1,1))
        self.assertEqual(Rectangle(-4,-4,-2,-2).center(),Point(-3,-3))
        self.assertEqual(Rectangle(8,8,4,4).center(),Point(6,6))
        self.assertEqual(Rectangle(3,3,2,2).center(),Point(2.5,2.5))
        self.assertEqual(Rectangle(-0,1,2,-3.5).center(),Point(1,-1.25))
        with self.assertRaisesRegexp(ValueError, "Bledne wspolrzedne wierzcholkow"):
            Rectangle(1,2,1,2).center()

    def test_area(self):
        self.assertEqual(Rectangle(-2,-2,4,4).area(),36)
        self.assertEqual(Rectangle(-0,0,1,1).area(),1)
        self.assertEqual(Rectangle(-3.5,-5.5,-10,-12).area(),42.25)

    def test_move(self):
        self.assertEqual(Rectangle(0,0,1,1).move(2,2),Rectangle(2,2,3,3))
        self.assertEqual((Rectangle(2, 4, 8.5, 10.2).move(3, 3)), Rectangle(5, 7, 11.5, 13.2))
        self.assertEqual((Rectangle(-2, -4, -8.5, -10.1).move(3, 3)), Rectangle(1, -1, -5.5, -7.1))
        #self.assertEqual(Rectangle(-2, -4, -8.5, -10.7).move(3, 3),Rectangle(-5.5,-7.7,1,-1))
        self.assertAlmostEqual((Rectangle(-2, -4, -8.5, -10.7).move(3, 3).pt1.x), -5.5,7) #istnieje jakas lepsza funckja zeby porwnywac obiekty ktore zawieraja float?
        self.assertAlmostEqual((Rectangle(-2, -4, -8.5, -10.7).move(3, 3).pt1.y), -7.7, 7)
        self.assertAlmostEqual((Rectangle(-2, -4, -8.5, -10.7).move(3, 3).pt2.x), 1, 7)
        self.assertAlmostEqual((Rectangle(-2, -4, -8.5, -10.7).move(3, 3).pt2.y), -1, 7)
        #self.assertEqual((Rectangle(-2, -4, -8.5, -10.2).move(3, 3)), Rectangle(1, -1, -5.5, -7.2))
        #self.assertEqual((Rectangle(-2,-4,-8.5,-10.2).move(3,3)),Rectangle(-5.5,-7.2,1,-1))
        #self.assertEqual(Rectangle(0,0,2.3,2).move(-3,-4),Rectangle(-3,-4,-0.7,-2))
        self.assertEqual(Rectangle(3.5,3.5,10.2,10.2).move(0,0),Rectangle(3.5,3.5,10.2,10.2))
        with self.assertRaisesRegexp(ValueError, "Wprowadzono bledne dane w przesuniecia"):
            Rectangle(2, 2, 3, 3).move("abc",0)

    def test_cover(self):
        self.assertEqual(Rectangle(0,0,2,2).cover(Rectangle(0,0,3,3)),4)
        self.assertEqual(Rectangle(0,0,2,2).cover(Rectangle(-1,-1,8,8)),4)
        self.assertEqual(Rectangle(0,0,2,2).cover(Rectangle(2,2,3,3)),0)
        self.assertEqual(Rectangle(2.5,2.5,0,0).cover(Rectangle(1,1,5,5)),2.25)
        self.assertEqual(Rectangle(-2.5, -2.5, 0, 0).cover(Rectangle(-1, -1, -5, -5)), 2.25)
        self.assertEqual(Rectangle(2,2,4,4).cover(Rectangle(2,2,4,4)),4)
        with self.assertRaisesRegexp(ValueError, "Argument nie jest prostokatem"):
            Rectangle(2, 2, 3, 3).cover("abc")

    def test_make4(self):
        self.assertEqual(Rectangle(0,0,2,2).make4(),[Rectangle(0,0,1,1),Rectangle(1,1,2,2),Rectangle(0,1,1,2),Rectangle(1,0,2,1)])
        self.assertEqual(Rectangle(-2,-2,3,4).make4(),[Rectangle(-2,-2,0.5,1),Rectangle(0.5,1,3,4),Rectangle(-2,1,0.5,4),Rectangle(0.5,-2,3,1)])
        self.assertEqual(Rectangle(1,1,0,0).make4(),[Rectangle(0,0,0.5,0.5),Rectangle(0.5,0.5,1,1),Rectangle(0,0.5,0.5,1),Rectangle(0.5,0,1,0.5)])

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy