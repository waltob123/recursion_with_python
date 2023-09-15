#!/usr/bin/python3
# decimal_to_binary.py
# converts a decimal number to a binary


def convert_decimal_to_binary(dec_number: int) -> str:
    '''
    Takes in a decimal number and converts it to binary

    Args:
        `dec_number (int)`: decimal number to convert

    Return:
        `binary (str)`: resulting binary from operation
    '''

    # base case
    if dec_number == 0:
        return ''

    d = dec_number // 2
    binary = dec_number % 2
    return convert_decimal_to_binary(d) + str(binary)
