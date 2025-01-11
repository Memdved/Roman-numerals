"""Модуль для тестирования."""


import unittest
from roman_numerals import RomanNumeral


class TestRomanNumeral(unittest.TestCase):
    """Класс для тестирования римских цифр."""

    def test_int_to_roman(self):
        """Тестирование метода int_to_roman.

        Проверяет, что метод int_to_roman правильно преобразует целые числа в римские цифры.
        """
        self.assertEqual(str(RomanNumeral(1)), 'I')
        self.assertEqual(str(RomanNumeral(4)), 'IV')
        self.assertEqual(str(RomanNumeral(9)), 'IX')
        self.assertEqual(str(RomanNumeral(58)), 'LVIII')
        self.assertEqual(str(RomanNumeral(1994)), 'MCMXCIV')

    def test_add(self):
        """Тестирование метода __add__.

        Проверяет, что метод __add__ правильно складывает римские цифры.
        """
        self.assertEqual(str(RomanNumeral(1) + 1), 'II')
        self.assertEqual(str(RomanNumeral(1) + RomanNumeral(2)), 'III')
        self.assertEqual(str(RomanNumeral(1) + RomanNumeral(3)), 'IV')

    def test_sub(self):
        """Тестирование метода __sub__.

        Проверяет, что метод __sub__ правильно вычитает римские цифры.
        """
        self.assertEqual(str(RomanNumeral(3) - RomanNumeral(1)), 'II')
        self.assertEqual(str(RomanNumeral(4) - RomanNumeral(1)), 'III')
        self.assertEqual(str(RomanNumeral(5) - RomanNumeral(1)), 'IV')

    def test_mul(self):
        """Тестирование метода __mul__.

        Проверяет, что метод __mul__ правильно умножает римские цифры.
        """
        self.assertEqual(str(RomanNumeral(2) * RomanNumeral(2)), 'IV')
        self.assertEqual(str(RomanNumeral(2) * RomanNumeral(3)), 'VI')
        self.assertEqual(str(RomanNumeral(2) * RomanNumeral(4)), 'VIII')

    def test_truediv(self):
        """Тестирование метода __truediv__.

        Проверяет, что метод __truediv__ правильно делит римские цифры.
        """
        self.assertEqual(str(RomanNumeral(4) / RomanNumeral(2)), 'II')
        self.assertEqual(str(RomanNumeral(6) / RomanNumeral(2)), 'III')
        self.assertEqual(str(RomanNumeral(8) / RomanNumeral(2)), 'IV')

    def test_floordiv(self):
        """Тестирование метода __floordiv__.

        Проверяет, что метод __floordiv__ правильно делит римские цифры.
        """
        self.assertEqual(str(RomanNumeral(4) // RomanNumeral(2)), 'II')
        self.assertEqual(str(RomanNumeral(6) // RomanNumeral(2)), 'III')
        self.assertEqual(str(RomanNumeral(8) // RomanNumeral(2)), 'IV')

    def test_mod(self):
        """Тестирование метода __mod__.

        Проверяет, что метод __mod__ правильно вычисляет остаток от деления римских цифр.
        """
        self.assertEqual(str(RomanNumeral(4) % RomanNumeral(2)), '')
        self.assertEqual(str(RomanNumeral(6) % RomanNumeral(4)), 'II')
        self.assertEqual(str(RomanNumeral(5) % RomanNumeral(2)), 'I')


if __name__ == '__main__':
    unittest.main()
