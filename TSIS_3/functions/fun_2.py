"""
Read in a Fahrenheit temperature.
Calculate and display the equivalent centigrade temperature.
The following formula is used for the conversion: C = (5 / 9) * (F – 32)
"""


def From_far_to_c(f):
    return (5.0 / 9.0) * (f - 32)


print(From_far_to_c(int(input())))

print()
