"""
Write a program to solve a classic puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?
create function: solve(numheads, numlegs):
"""


def solve(numheads, numlegs):
    for i in range(numheads + 1):
        j = numheads - i
        if 2 * i + 4 * j == numlegs:
            return i, j
    return "Error"


print(solve(int(input()), int(input())))
