"""
Write a Python program to count the number of lines in a text file.
"""
file = open('rows.txt', encoding="utf8")
a = True
b = 0

while a:
    file_line = file.readline()

    b += 1

    if not file_line:
        a = False

file.close()
print(b)
