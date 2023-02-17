"""
Write a Python program to split a string at uppercase letters.
"""

import re

file = open('rows.txt', encoding="utf8")

a = True
b = 0

while a:
    file_line = file.readline()

    print(re.findall('[А-Я][^А-Я]*', file_line))

    if not file_line:
        print("End Of File")
        a = False

file.close()
