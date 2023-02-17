"""
Write a Python program to find sequences of lowercase letters joined with a underscore.
'^[a-z]+_[a-z]+$'
"""

import re

file = open('rows.txt', encoding="utf8")


def text_match(text):
    patterns = '^[а-я]+_[а-я]+$'
    if re.search(patterns, text):
        return True
    else:
        return False


a = True
b = 0

while a:
    file_line = file.readline()

    if text_match(file_line):
        print(file_line)

    b += 1

    if not file_line:
        print("End Of File")
        a = False

file.close()
