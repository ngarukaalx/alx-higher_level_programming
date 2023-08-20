#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numbers = {
            'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
            'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
            'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
            'M': 1000
            }
    prev, total = 0, 0

    for i in roman_string:
        value = roman_numbers.get(i, 0)
        total += value - 2 * prev if value > prev else value
        prev = value
    return total
