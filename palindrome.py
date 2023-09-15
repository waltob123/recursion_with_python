#!/usr/bin/python3
# palindrome.py
# checks if a string of characters is a palindrome

def palindrome(string: str) -> bool:
    '''
    checks if a string is a palindrome

    Args:
        `string (str)`: string to check

    Return:
        `True (bool)`: true if string is palindrome
        `False (bool)`: flase if string is not a palindrome
    '''

    # base case
    if len(string) == 0 or len(string) == 1:
        return True

    i = 0
    j = len(string)
    if string[i] == string[j-1]:
        return palindrome(string[i+1:j-1])
    return False
