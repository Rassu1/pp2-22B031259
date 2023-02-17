"""
Write a python program to convert snake case string to camel case string.
"""

file = open('rows.txt', encoding="utf8")


def snake_to_camel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


print(snake_to_camel('python_exercises'))

a = True
b = 0

while a:
    file_line = file.readline()

    print(snake_to_camel(file_line))

    if not file_line:
        print("End Of File")
        a = False

file.close()