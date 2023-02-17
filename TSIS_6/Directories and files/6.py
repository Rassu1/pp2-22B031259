"""
Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
"""
for i in range(65, 91):
    letter = chr(i)
    filename = letter + ".txt"
    with open(filename, "w") as f:
        f.write("This is file %s.\n" % filename)