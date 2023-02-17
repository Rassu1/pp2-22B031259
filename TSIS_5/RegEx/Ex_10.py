"""
Write a Python program to convert a given camel case string to snake case.
"""


def camel_to_snake(camel_string):
    snake_list = []
    for i, c in enumerate(camel_string):
        if c.isupper() and i > 0:
            snake_list.append('_')
        snake_list.append(c.lower())
    return ''.join(snake_list)


file = open('rows.txt', encoding="utf8")

a = True
b = 0

while a:
    file_line = file.readline()
    file_line = "".join(file_line.split())
    print(camel_to_snake(file_line))

    if not file_line:
        print("End Of File")
        a = False

file.close()

