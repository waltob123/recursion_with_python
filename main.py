#!/usr/bin/python3
# main.py
# main file to run python modules


from reverse_string import reverse_string
from palindrome import palindrome
from decimal_to_binary import convert_decimal_to_binary


if __name__ == '__main__':
    # run reverse_string
    strings = ['black', 'hello', 'kayak', 'racecar', 'madam', 'ball', 'apple']
    decimal_values = [25, 100, 10, 67, 4123, 64, 123, 62]

    reversed_strings_results = [reverse_string(string) for string in strings]
    palindrome_results = [palindrome(string) for string in strings]
    binary_values = [convert_decimal_to_binary(decimal_value) for
                     decimal_value in decimal_values]

    print(reversed_strings_results)
    print(palindrome_results)
    print(binary_values)
