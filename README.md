# Roman Numeral Module
This module provides a class for working with Roman numerals. The RomanNumeral class allows you to convert between Roman numerals and integers, as well as perform arithmetic operations with Roman numerals.

## Usage
To use the RomanNumeral class, you can create an instance of the class with either an integer or a Roman numeral string:
```Python
from roman_numeral import RomanNumeral

# Create a RomanNumeral instance with an integer
num1 = RomanNumeral(10)

# Create a RomanNumeral instance with a Roman numeral string
num2 = RomanNumeral("X")
```
### You can then perform arithmetic operations with the RomanNumeral instances:

```Python
# Addition
result = num1 + num2
print(result)  # Output: XX

# Subtraction
result = num1 - num2
print(result)  # Output: 0

# Multiplication
result = num1 * num2
print(result)  # Output: C

# Division
result = num1 // num2
print(result)  # Output: I

# Modulus
result = num1 % num2
print(result)  # Output: 0
```

### You can also compare RomanNumeral instances using comparison operators:

```Python
# Equality
print(num1 == num2)  # Output: True

# Inequality
print(num1 != num2)  # Output: False

# Less than
print(num1 < num2)  # Output: False

# Less than or equal to
print(num1 <= num2)  # Output: True

# Greater than
print(num1 > num2)  # Output: False

# Greater than or equal to
print(num1 >= num2)  # Output: True
```

# License
This module is licensed under the MIT License. See the LICENSE file for more information.