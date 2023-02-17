"""
Write a Python program that invoke square root function after specific milliseconds.
Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858
"""
import math
import time


def square_root_with_delay(number, delay_ms):
    print((delay_ms / 1000, "in seconds"))
    time.sleep(delay_ms / 1000)
    result = math.sqrt(number)
    return result


my_number = 25100
my_delay_ms = 2123
result = square_root_with_delay(my_number, my_delay_ms)
print(result)
