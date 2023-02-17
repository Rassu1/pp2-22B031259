"""
Write a Python program with builtin function that checks whether a passed string is palindrome or not.
"""


def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


my_string = "rAceAr"
result = is_palindrome(my_string)
print(result)
