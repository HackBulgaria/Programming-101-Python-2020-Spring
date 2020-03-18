import unittest
from fraction import Fraction


class TestFraction(unittest.TestCase):
    def test_cannot_instantiate_fraction_with_zero_denominator(self):
        exception = None

        try:
            Fraction(1, 0)
        except AssertionError as exc:
            exception = exc

        self.assertIsNotNone(exception)

    def test_fractions_string_representation_is_as_expected_one(self):
        fraction1 = Fraction(1, 3)
        fraction2 = Fraction(-1, 3)
        fraction3 = Fraction(2, 4)

        self.assertEqual(str(fraction1), '1/3')
        self.assertEqual(str(fraction2), '-1/3')
        self.assertEqual(str(fraction3), '2/4')

    def test_fractions_equalization_with_equal_fractions(self):
        fraction1 = Fraction(1, 5)
        fraction2 = Fraction(1, 5)

        self.assertTrue(fraction1 == fraction2, 'Fractions are not equal')

    def test_fractions_equalization_with_equal_nonsimpified_fractions(self):
        fraction1 = Fraction(1, 3)
        fraction2 = Fraction(3, 9)

        self.assertTrue(fraction1 == fraction2, 'Fractions are not equal')

    def test_simplified_fraction_is_preserved_after_simplification(self):
        fraction = Fraction(1, 5)

        expected = Fraction(1, 5)

        self.assertEqual(fraction.simplify(), expected)

    def test_fraction_is_simplified_as_expected(self):
        fraction = Fraction(10, 50)

        expected = Fraction(1, 5)

        self.assertEqual(fraction.simplify(), expected)

    def test_addition_fractions_works_correct_for_non_simplifiable_result_with_equal_denominator(self):
        fraction1 = Fraction(1, 5)
        fraction2 = Fraction(2, 5)

        result = fraction1 + fraction2

        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 5)

    def test_addition_fractions_works_correct_for_non_simplifiable_result_with_non_equal_denominator(self):
        fraction1 = Fraction(1, 7)
        fraction2 = Fraction(2, 6)

        result = fraction1 + fraction2

        self.assertEqual(result.numerator, 10)
        self.assertEqual(result.denominator, 21)


if __name__ == '__main__':
    unittest.main()
