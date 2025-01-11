"""Roman numeral module."""

import abc


class BaseRomanNumeral(abc.ABC):
    """A class to describe the operation of Roman numerals."""

    @abc.abstractmethod
    def __init__(self, int_representation: int) -> None:
        pass

    @abc.abstractmethod
    def __str__(self) -> str:
        pass

    @abc.abstractmethod
    def __int__(self) -> int:
        pass

    @abc.abstractmethod
    def int_to_roman(self, num: int) -> str:
        """Method to convert a number to Roman numerals.

        :param num: Number to convert.
        :type num: int
        :return: Roman numeral.
        :rtype: str
        """

    @abc.abstractmethod
    def roman_to_int(self, roman: str) -> int:
        """Method to convert a Roman numeral to a number.
        :param roman: Roman numeral to convert.
        :type roman: str
        :return: Number.
        :rtype: int
        """

    @abc.abstractmethod
    def __add__(self, other: "BaseRomanNumeral") -> "BaseRomanNumeral":
        pass

    @abc.abstractmethod
    def __sub__(self, other: "BaseRomanNumeral") -> "BaseRomanNumeral":
        pass

    @abc.abstractmethod
    def __mul__(self, other: "BaseRomanNumeral") -> "BaseRomanNumeral":
        pass

    @abc.abstractmethod
    def __truediv__(self, other: "BaseRomanNumeral") -> "BaseRomanNumeral":
        pass

    @abc.abstractmethod
    def __floordiv__(self, other: "BaseRomanNumeral") -> "BaseRomanNumeral":
        pass

    @abc.abstractmethod
    def __mod__(self, other: "BaseRomanNumeral") -> "BaseRomanNumeral":
        pass


class RomanNumeral(BaseRomanNumeral):
    """Roman numeral class."""

    def __init__(self, representation: int | str) -> None:
        if isinstance(representation, int):
            self.__int_representation = representation
            self.__roman_num = self.int_to_roman(self.__int_representation)
        else:
            self.__roman_num = representation
            self.__int_representation = self.roman_to_int(self.__roman_num)

    def __int__(self) -> int:
        return self.__int_representation

    def __str__(self) -> str:
        return self.__roman_num

    def roman_to_int(self, roman: str) -> int:
        """Метод для преобразования римской цифры в число.

        :param roman: Римская цифра для преобразования.
        :type roman: str
        :return: Число.
        :rtype: int
        """
        roman_to_int_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        int_val = 0
        for i, char in enumerate(roman):
            if i > 0 and roman_to_int_map[char] > roman_to_int_map[roman[i - 1]]:
                int_val += roman_to_int_map[char] - 2 * roman_to_int_map[roman[i - 1]]
            else:
                int_val += roman_to_int_map[char]
        return int_val


    def int_to_roman(self, num: int) -> str:
        val: list[int] = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb: list[str] = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]

        roman_num: str = ""
        iteration: int = 0
        while num > 0:
            for _ in range(num // val[iteration]):
                roman_num += syb[iteration]
                num -= val[iteration]
            iteration += 1
        return roman_num

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.__int_representation + int(other))
        return RomanNumeral(self.__int_representation + int(RomanNumeral(other)))

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.__int_representation - int(other))
        return RomanNumeral(self.__int_representation - int(RomanNumeral(other)))

    def __mul__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.__int_representation * int(other))
        return RomanNumeral(self.__int_representation * int(RomanNumeral(other)))

    def __truediv__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.__int_representation // int(other))
        return RomanNumeral(self.__int_representation // int(RomanNumeral(other)))

    def __floordiv__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.__int_representation // int(other))
        return RomanNumeral(self.__int_representation // int(RomanNumeral(other)))

    def __mod__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.__int_representation % int(other))
        return RomanNumeral(self.__int_representation % int(RomanNumeral(other)))
