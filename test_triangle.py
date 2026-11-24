import unittest

import triangle


class TriangleAreaTestCase(unittest.TestCase):
    def test_zero_area(self):
        self.assertEqual(triangle.area(10, 0), 0)

    def test_integer_area(self):
        self.assertEqual(triangle.area(6, 4), 12)

    def test_fractional_area(self):
        self.assertAlmostEqual(triangle.area(3, 5), 7.5)

    def test_float_area(self):
        self.assertAlmostEqual(triangle.area(2.5, 4), 5.0)


class TrianglePerimeterTestCase(unittest.TestCase):
    def test_zero_perimeter(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_equilateral_perimeter(self):
        self.assertEqual(triangle.perimeter(5, 5, 5), 15)

    def test_right_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_perimeter_order_independent(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), triangle.perimeter(5, 3, 4))

    def test_float_perimeter(self):
        self.assertAlmostEqual(triangle.perimeter(1.5, 2.5, 3.0), 7.0)


if __name__ == "__main__":
    unittest.main()