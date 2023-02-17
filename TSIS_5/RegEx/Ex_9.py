"""
Write a Python program to insert spaces between words starting with capital letters.
"""

import re


def capital_words_spaces(str1):
    return re.sub(r"(\w)([A-Z])" or "(\w)([А-Я])" , r"\1 \2", str1)


def capital_words_spaces_join(str1):
    return " ".join(re.findall(r'[a-zA-Z][^A-Z]*' or r'[а-яА-Я][^А-Я]*', str1))


file = open('rows.txt', encoding="utf8")

a = True
b = 0

while a:
    file_line = file.readline()

    a = capital_words_spaces(file_line)

    print(capital_words_spaces_join(a))

    if not file_line:
        print("End Of File")
        a = False

file.close()
