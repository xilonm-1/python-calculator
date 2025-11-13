import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add_positive(self):
        self.assertEqual(self.calc.add(2, 2), 4)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-5, -3), -8)

    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_negative_result(self):
        self.assertEqual(self.calc.subtract(3, 7), -4)

    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(7, 0), 0)

    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_with_remainder(self):
        self.assertAlmostEqual(self.calc.divide(7, 2), 3)

    def test_modulo_normal(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_exect(self):
        self.assertEqual(self.calc.modulo(6, 3),0)

    

if __name__ == '__main__':
    unittest.main()