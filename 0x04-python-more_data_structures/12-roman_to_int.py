#!/usr/bin/python3
def roman_to_int(roman_string):
    if is not roman_string or type(roman_string) != str:
        return 0
    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_new = 0
    for p in range(len(roman_string)):
        if p > 0 and roman_d[roman_string[p]] > roman_d[roman_string[p - 1]]:
            roman_new += roman_d[roman_string[p]] - 2 * \
                        roman_d[roman_string[p - 1]]
        else:
            roman_new += roman_d[roman_string[p]]
    return roman_new
