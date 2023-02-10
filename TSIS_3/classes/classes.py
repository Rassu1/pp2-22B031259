"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
"""


class java():

    def __init__(self):
        self.name = ""

    def getString(self):
        self.name = input()

    def printString(self):
        print(self.name.upper())


name = java()

name.getString()

name.printString()
