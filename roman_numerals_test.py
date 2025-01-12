"""Testing module."""

import unittest
from roman_numerals import RomanNumeral


class TestRomanNumeral(unittest.TestCase):
    """A class for testing Roman numerals."""

    def test_int_to_roman(self):
        """Test int_to_roman method.

        Checks that the int_to_roman method correctly converts integers to Roman numerals.
        """
        self.assertEqual(str(RomanNumeral(1)), "I")
        self.assertEqual(str(RomanNumeral(4)), "IV")
        self.assertEqual(str(RomanNumeral(9)), "IX")
        self.assertEqual(str(RomanNumeral(58)), "LVIII")
        self.assertEqual(str(RomanNumeral(1994)), "MCMXCIV")

    def test_add(self):
        """Testing the __add__ method.

        Verifies that the __add__ method correctly adds Roman numerals.
        """
        self.assertEqual(str(RomanNumeral(1) + 1), "II")
        self.assertEqual(str(RomanNumeral(1) + RomanNumeral(2)), "III")
        self.assertEqual(str(RomanNumeral(1) + RomanNumeral(3)), "IV")

    def test_sub(self):
        """Testing the __sub__ method.

        Verifies that the __sub__ method correctly subtracts Roman numerals.
        """
        self.assertEqual(str(RomanNumeral(3) - RomanNumeral(1)), "II")
        self.assertEqual(str(RomanNumeral(4) - RomanNumeral(1)), "III")
        self.assertEqual(str(RomanNumeral(5) - RomanNumeral(1)), "IV")

    def test_mul(self):
        """Testing the __mul__ method.

        Verifies that the __mul__ method multiplies Roman numerals correctly.
        """
        self.assertEqual(str(RomanNumeral(2) * RomanNumeral(2)), "IV")
        self.assertEqual(str(RomanNumeral(2) * "III"), "VI")
        self.assertEqual(str(RomanNumeral(2) * RomanNumeral(4)), "VIII")

    def test_truediv(self):
        """Testing the __truediv__ method.

        Verifies that the __truediv__ method correctly divides Roman numerals.
        """
        self.assertEqual(str(RomanNumeral(4) / RomanNumeral(2)), "II")
        self.assertEqual(str(RomanNumeral(6) / RomanNumeral(2)), "III")
        self.assertEqual(str(RomanNumeral(8) / RomanNumeral(2)), "IV")

    def test_floordiv(self):
        """Testing the __floordiv__ method.

        Verifies that the __floordiv__ method correctly divides Roman numerals.
        """
        self.assertEqual(str(RomanNumeral(4) // RomanNumeral(2)), "II")
        self.assertEqual(str(RomanNumeral(6) // RomanNumeral(2)), "III")
        self.assertEqual(str(RomanNumeral(8) // RomanNumeral(2)), "IV")

    def test_mod(self):
        """Testing the __mod__ method.

        Verifies that the __mod__ method correctly calculates
        the remainder from dividing Roman numerals.
        """
        self.assertEqual(str(RomanNumeral(4) % RomanNumeral(2)), "")
        self.assertEqual(str(RomanNumeral(6) % RomanNumeral(4)), "II")
        self.assertEqual(str(RomanNumeral(5) % RomanNumeral(2)), "I")


if __name__ == "__main__":
    unittest.main()
