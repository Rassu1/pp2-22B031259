"""
You are given list of numbers separated by spaces.
Write a function filter_prime
which will take list of numbers as an agrument and returns only prime numbers from the list.
"""


def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def returnPrime(num):
    return list(filter(lambda x: is_prime(x), num))


print(returnPrime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
