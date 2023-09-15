#!/usr/bin/python3
# reverse_string.py
# reverses a string of characters

def reverse_string(input_string: str) -> str:
    '''
    takes a string and reverses it

    Args:
        `input_string (str)`: string to reverse

    Return:
        `reverse_string (function)`: reversed_string
    '''
    i = len(input_string)

    # base case
    if i <= 0:
        return ''
    return input_string[i-1] + reverse_string(input_string[:i-1])
