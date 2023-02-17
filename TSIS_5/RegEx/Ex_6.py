"""
Write a Python program to replace all occurrences of space, comma, or dot with a colon.
"""

import re


file = open('rows.txt', encoding="utf8")


a = True
b = 0

while a:
    file_line = file.readline()

    print(re.sub("[ ,.]", ":", file_line))

    if not file_line:
        print("End Of File")
        a = False

file.close()

