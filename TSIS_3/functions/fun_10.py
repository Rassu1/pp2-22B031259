"""
Write a Python function that takes a list and
returns a new list with unique elements of the first list.
Note: don't use collection set.
"""


def unique(spisok):
    new_spisok = []
    for a in spisok:
        if a not in new_spisok:
            new_spisok.append(a)
    return new_spisok


spisok = [1, 2, 3, 3, 2, 1, 2, 3]

print(unique(spisok))
