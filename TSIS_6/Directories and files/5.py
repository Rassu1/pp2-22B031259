"""
Write a Python program to write a list to a file.
"""

my_list = ["apple", "banana", "orange", "pear"]

with open("free.txt", "w") as f:
    for item in my_list:
        f.write("{}\n".format(item))