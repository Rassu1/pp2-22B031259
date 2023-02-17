"""
Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
"""


def count_upper_lower(string):
    num_upper = 0
    num_lower = 0

    for char in string:
        if char.isupper():
            num_upper += 1
        elif char.islower():
            num_lower += 1

    return num_upper, num_lower


my_string = "Hello World, then Hello ALL MY SIMPLE CODE!"
result = count_upper_lower(my_string)
print(result)
