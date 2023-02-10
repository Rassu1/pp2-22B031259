"""
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere
"""


def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i:i + 2] == [3, 3]:
            return True
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
