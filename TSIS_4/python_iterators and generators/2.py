"""
Write a program using generator to print
the even numbers between 0 and n in comma separated form where n is input from console.
"""


def Generator_even():
    my_list = range(int(input()))
    for i in my_list:
        if i % 2 == 0:
            yield i


my_generator = Generator_even()
My_arr = []
for i in my_generator:
    My_arr.append(i)

print(My_arr)
