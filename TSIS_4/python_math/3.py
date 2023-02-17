"""
Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625

num_of_size * sqrt(len) / 4 tan (pi / num_of_size)
"""

from math import tan, pi

num_of_size = float(input())

len_of_size = float(input())

print(num_of_size * (len_of_size ** 2) / (4 * tan(pi / num_of_size)))
