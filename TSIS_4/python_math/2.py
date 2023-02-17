"""
Write a Python program to calculate the area of a trapezoid.
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5
(a+b)*h/2
"""


def area_of_trapezoid(height, base_1, base_2, ):
    return (base_1 + base_2) / 2 * height


height = int(input())
base_1 = int(input())
base_2 = int(input())

print(area_of_trapezoid(height, base_1, base_2))
