"""
Define a function with a generator which can iterate the numbers,
which are divisible by 3 and 4, between a given range 0 and n.
"""


def createGenerator():
    my_list = range(int(input()))
    for i in my_list:
        if i % 3 == 0 and i % 4 == 0:
            yield i


my_generator = createGenerator()
for i in my_generator:
    print(i)
