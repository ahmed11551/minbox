import unittest
import math
from shapes.shapes import Circle, Triangle, calculate_area

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(1)
        self.assertAlmostEqual(circle.area(), math.pi)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_triangle_right_angled(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angled())

    def test_calculate_area(self):
        circle = Circle(1)
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(circle), math.pi)
        self.assertAlmostEqual(calculate_area(triangle), 6.0)

if __name__ == '__main__':
    unittest.main()
