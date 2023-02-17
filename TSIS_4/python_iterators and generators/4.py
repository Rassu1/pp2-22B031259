"""
Implement a generator called squares to yield the square of all numbers from (a) to (b).
Test it with a "for" loop and print each of the yielded values.
"""


def createGenerator():
    my_list = range(int(input()), int(input()))
    for i in my_list:
        yield i * i


my_generator = createGenerator()
for i in my_generator:
    print(i)
