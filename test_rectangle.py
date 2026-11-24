import unittest

import rectangle


class RectangleAreaTestCase(unittest.TestCase):
    def test_zero_area(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_square_area(self):
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_rectangle_area(self):
        self.assertEqual(rectangle.area(3, 5), 15)

    def test_area_commutative(self):
        self.assertEqual(rectangle.area(3, 7), rectangle.area(7, 3))

    def test_float_area(self):
        self.assertAlmostEqual(rectangle.area(2.5, 4), 10.0)


class RectanglePerimeterTestCase(unittest.TestCase):
    def test_zero_perimeter(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_square_perimeter(self):
        self.assertEqual(rectangle.perimeter(10, 10), 40)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle.perimeter(3, 5), 16)

    def test_perimeter_commutative(self):
        self.assertEqual(rectangle.perimeter(3, 7), rectangle.perimeter(7, 3))

    def test_float_perimeter(self):
        self.assertAlmostEqual(rectangle.perimeter(2.5, 4), 13.0)


if __name__ == "__main__":
    unittest.main()