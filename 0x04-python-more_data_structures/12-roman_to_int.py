#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for dig in range(len(roman_string)):
        if dig > 0 and vals[roman_string[dig]] > vals[roman_string[dig - 1]]:
            result += vals[roman_string[dig]] - (2*vals[roman_string[dig - 1]])
        else:
            result += vals[roman_string[dig]]
    return result
