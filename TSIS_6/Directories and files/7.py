"""
Write a Python program to copy the contents of a file to another file
"""
with open("free.txt", "r") as source_file:
    with open("free2.txt", "w") as sec_file:
        sec_file.write(source_file.read())