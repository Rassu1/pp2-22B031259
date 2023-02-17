"""
Write a Python program to test whether a given path exists or not.
If the path exist find the filename and directory portion of the given path.
"""

import os


def test_path(path):
    if os.path.exists(path):
        dirname, filename = os.path.split(path)
        return f"The path exists. Filename: {filename}, Directory: {dirname}"
    else:
        return "The path does not exist."

path_1 = 'C:\\Users\\User\\PycharmProjects\\pythonProject'
path = "/home/user/my_file.txt"
result = test_path(path)
print(result)
result = test_path(path_1)
print(result)