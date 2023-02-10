"""
Write a program which can filter prime numbers in a list by using filter function.
Note: Use lambda to define anonymous functions.
"""

def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

prime = list(filter(lambda x: is_prime(x) == True, nums))

print(prime)
