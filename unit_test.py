import unittest
import math
from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rec_area, perimeter as rec_perimeter
from square import area as sq_area, perimeter as sq_perimeter 
from triangle import area as tri_area, perimeter as tri_perimeter

class CircleTestCase(unittest.TestCase):

    def test_area(self):
        
        self.assertAlmostEqual(circle_area(2), math.pi * 2 * 2, places=5) 
        self.assertAlmostEqual(circle_area(0), 0, places=5)
        self.assertAlmostEqual(circle_area(2147483647), math.pi * 2147483647 * 2147483647, places=5) 
        self.assertAlmostEqual(circle_area(-8), "Negative number was detected: Circle::area", places=5) 
    
    def test_perimeter(self):
        
        self.assertAlmostEqual(circle_perimeter(2), 2 * math.pi * 2, places=5)
        self.assertAlmostEqual(circle_perimeter(0), 0, places=5)  
        self.assertAlmostEqual(circle_perimeter(2147483647), 2 * math.pi * 2147483647, places=5)
        self.assertAlmostEqual(circle_perimeter(-6), "Negative number was detected: Circle::perimetr", places=5)

#test for rectangle
class RectangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(rec_area(-5, -6), "Negative number was detected: Rectangle::area")
        self.assertEqual(rec_area(0, 5), 0)
        self.assertEqual(rec_area(7, 2), 14)
        self.assertEqual(rec_area(2147483647, 2147483647), 2147483647*2147483647)

    def test_perimeter(self):
        self.assertEqual(rec_perimeter(-5 , -6), "Negative number was detected: Rectangle::perimetr")
        self.assertEqual(rec_perimeter(0, 5), 10)
        self.assertEqual(rec_perimeter(7, 2), 18)
        self.assertEqual(rec_perimeter(2147483647, 2147483647), 2147483647*2 + 2147483647*2)
#test for square
class SquareTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(sq_area(-5), "Negative number was detected: Square::area")
        self.assertEqual(sq_area(0), 0)
        self.assertEqual(sq_area(2147483647), 2147483647*2147483647)
        self.assertEqual(sq_area(10), 100)

    def test_perimeter(self):
        self.assertEqual(sq_perimeter(-5), "Negative number was detected: Square::perimetr")
        self.assertEqual(sq_perimeter(0), 0)
        self.assertEqual(sq_perimeter(2147483647), 2147483647*4)
        self.assertEqual(sq_perimeter(10), 40)

#test for triangle
class TriangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(tri_area(-4, -5), "Negative number was detected: Triangle::area")
        self.assertEqual(tri_area(3, 6), 9)
        self.assertEqual(tri_area(2147483647, 2), 2147483647 * 2 / 2)
        self.assertEqual(tri_area(7, 8), 28)

    def test_perimeter(self):
        self.assertEqual(tri_perimeter(-4, -5, -6), "Negative number was detected: Triangle::perimetr")
        self.assertEqual(tri_perimeter(3, 4, 5), 12)
        self.assertEqual(tri_perimeter(6, 8, 10), 24)
        self.assertEqual(tri_perimeter(2147483647, 2147483647, 2147483647), 2147483647+2147483647+2147483647)

if __name__ == "__main__":
    unittest.main()
