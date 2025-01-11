## Русский
# Римские цифры

Этот модуль предоставляет класс для работы с римскими цифрами - `RomanNumeral`.

## Установка

Этот модуль не требует установки, так как он представляет собой простой Python-файл.

## Использование

```python
from roman_numerals import RomanNumeral

# Создание римской цифры
num = RomanNumeral(1)

# Преобразование римской цифры в строку
print(str(num))  # Вывод: I

# Преобразование римской цифры в целое число
print(int(num))  # Вывод: 1

# Сложение римских цифр
print(num + 1)  # Вывод: II

# Вычитание римских цифр
print(num - RomanNumeral(1))  # Вывод: I

# Умножение римских цифр
print(num * 2)  # Вывод: II

# Деление римских цифр
print(num / RomanNumeral(2))  # Вывод: I

# Целочисленное деление римских цифр
print(num // RomanNumeral(2))  # Вывод: I

# Остаток от деления римских цифр
print(num % RomanNumeral(2))  # Вывод: I
```

▌Тестирование

Для тестирования этого модуля вы можете использовать стандартный модуль unittest в Python. Пример тестового кода можно найти в файле test_roman_numerals.py.

▌Лицензия

Этот модуль распространяется под лицензией MIT.
#
#
#

## English
# Roman numerals

This module provides a class for working with Roman numerals - `RomanNumeral`.

## Installation

This module does not require installation as it is a simple Python file.

## Usage

```python
from roman_numerals import RomanNumeral

# Create a Roman numeral
num = RomanNumeral(1)

# Convert the Roman numeral to a string
print(str(num))  # Output: I

# Convert Roman numeral to an integer
print(int(num))  # Output: 1

# Adding Roman numerals
print(num + 1) # Output: II

# Subtraction of Roman numerals
print(num - RomanNumeral(1)) # Output: I

# Multiplication of Roman numerals
print(num * 2) # Output: II

# Division of Roman numerals
print(num / RomanNumeral(2)) # Output: I

# Integer division of Roman numerals
print(num // RomanNumeral(2)) # Output: I

# The remainder of Roman numerals division
print(num % RomanNumeral(2)) # Output: I
```

▌Testing

You can use the standard unittest module in Python to test this module. Sample test code can be found in the file test_roman_numerals.py.

▌License

This module is distributed under the MIT license.
