"""
Implement a generator that returns all numbers from (n) down to 0.
"""


def createGenerator():
    my_list = range(int(input()), -1, -1)
    for i in my_list:
        yield i


my_generator = createGenerator()
for i in my_generator:
    print(i)
