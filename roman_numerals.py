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

    def __init__(self, int_representation: int) -> None:
        self.__int_representation = int_representation
        self.__roman_num = self.int_to_roman(self.__int_representation)

    def __int__(self) -> int:
        return self.__int_representation

    def __str__(self) -> str:
        return self.__roman_num

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
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

    def __add__(self, other: "BaseRomanNumeral") -> "BaseRomanNumeral":
        return RomanNumeral(self.__int_representation + int(other))

    def __sub__(self, other: "BaseRomanNumeral") -> "BaseRomanNumeral":
        return RomanNumeral(self.__int_representation - int(other))

    def __mul__(self, other: "BaseRomanNumeral") -> "BaseRomanNumeral":
        return RomanNumeral(self.__int_representation * int(other))

    def __truediv__(self, other: "BaseRomanNumeral") -> "BaseRomanNumeral":
        return RomanNumeral(self.__int_representation // int(other))

    def __floordiv__(self, other: "BaseRomanNumeral") -> "BaseRomanNumeral":
        return RomanNumeral(self.__int_representation // int(other))

    def __mod__(self, other: "BaseRomanNumeral") -> "BaseRomanNumeral":
        return RomanNumeral(self.__int_representation % int(other))
