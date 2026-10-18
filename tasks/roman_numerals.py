"""
Программа преобразует римские числа в арабские
и арабские числа в римские.
"""

roman_values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

int_values = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

def roman_to_int(roman):
    """
    Переводит римское число в арабское.

    roman — римское число в виде строки.
    Возвращает соответствующее целое число.
    """
    result = 0

    for i in range(len(roman)):
        if i + 1 < len(roman) and roman_values[roman[i]] < roman_values[roman[i + 1]]:
            result -= roman_values[roman[i]]
        else:
            result += roman_values[roman[i]]

    return result

def int_to_roman(number):
    """
    Переводит арабское число в римское.

    number — целое число.
    Возвращает римское число в виде строки.
    """
    result = ""

    for value, symbol in int_values.items():
        while number >= value:
            result += symbol
            number -= value

    return result

roman_tests = ["IV", "IX", "XLI", "XCIX", "MMXXII"]

for roman in roman_tests:
    print(roman, "-", roman_to_int(roman))

print(int_to_roman(4))
print(int_to_roman(9))
print(int_to_roman(41))
print(int_to_roman(99))
print(int_to_roman(2022))
