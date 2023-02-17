"""
Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
'аб*?'
"""

import re

file = open('rows.txt', encoding="utf8")


def text_match(text):
    patterns = 'аб*?'
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
