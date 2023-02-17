"""
Write a Python program with builtin function to multiply all the numbers in a list
"""
from functools import reduce

multiply = lambda x, y: x * y
numbers = [2, 3, 5, 10, 15]
result = reduce(multiply, numbers)
print(result)
