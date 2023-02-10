"""
Create a generator that generates the squares of numbers up to some number N.
"""

My_generator = (x * x for x in range(int(input())))
for j in My_generator:
    print(j)


def createGenerator():
    my_list = range(int(input()))
    for i in my_list:
        yield i * i


my_generator = createGenerator()
for i in my_generator:
    print(i)
