"""
Write a function that takes in a list of integers and returns True if it contains 007 in order
"""


def spy_game(nums):
    count = 0
    for i in nums:
        if i == 0 and count == 0:
            count = 1
        if i == 0 and count == 1:
            count = 2
        if i == 7 and count == 2:
            return True
    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))
