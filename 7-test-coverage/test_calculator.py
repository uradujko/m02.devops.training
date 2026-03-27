import unittest
import calculator


class TestCalculator(unittest.TestCase):

    # --- add ---
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(calculator.add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(calculator.add(0, 5), 5)

    # --- subtract ---
    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)

    def test_subtract_negative_result(self):
        self.assertEqual(calculator.subtract(3, 7), -4)

    def test_subtract_zero(self):
        self.assertEqual(calculator.subtract(5, 0), 5)

    # --- multiply ---
    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(calculator.multiply(5, 0), 0)

    def test_multiply_negative(self):
        self.assertEqual(calculator.multiply(-2, 3), -6)

    def test_multiply_large(self):
        self.assertEqual(calculator.multiply(1000, 1000), 1000000)

    # --- divide ---
    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

    def test_divide_negative(self):
        self.assertEqual(calculator.divide(-10, 2), -5)

    # --- power ---
    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)

    def test_power_zero_exponent(self):
        self.assertEqual(calculator.power(5, 0), 1)

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(calculator.power(2, -1), 0.5)

    # --- square_root ---
    def test_square_root(self):
        self.assertEqual(calculator.square_root(16), 4)

    def test_square_root_zero(self):
        self.assertEqual(calculator.square_root(0), 0)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            calculator.square_root(-1)

    # --- modulo ---
    def test_modulo(self):
        self.assertEqual(calculator.modulo(10, 3), 1)

    def test_modulo_even(self):
        self.assertEqual(calculator.modulo(10, 2), 0)

    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.modulo(10, 0)

    # --- is_even ---
    def test_is_even_true(self):
        self.assertTrue(calculator.is_even(4))

    def test_is_even_false(self):
        self.assertFalse(calculator.is_even(3))

    def test_is_even_zero(self):
        self.assertTrue(calculator.is_even(0))

    def test_is_even_negative(self):
        self.assertTrue(calculator.is_even(-2))

    # --- is_positive ---
    def test_is_positive_true(self):
        self.assertTrue(calculator.is_positive(5))

    def test_is_positive_false(self):
        self.assertFalse(calculator.is_positive(-3))

    def test_is_positive_zero(self):
        self.assertFalse(calculator.is_positive(0))

    # --- factorial ---
    def test_factorial(self):
        self.assertEqual(calculator.factorial(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(calculator.factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(calculator.factorial(1), 1)

    def test_factorial_large(self):
        self.assertEqual(calculator.factorial(10), 3628800)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            calculator.factorial(-1)


if __name__ == "__main__":
    unittest.main()
