"""
Define a functino histogram() that takes a list of integers and prints a histogram to the screen.
For example, histogram([4, 9, 7]) should print the following:
"""


def histogram(num):
    for i in num:

        str = ""

        while i > 0:
            str += '*'
            i = i - 1
        print(str)


num = [4, 9, 7]

histogram(num)
