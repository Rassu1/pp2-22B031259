"""
Write the definition of a Point class. Objects from this class should have a
a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points
"""

class Point():

    def __init__(self,x,y):
        self.coordinates_x = x
        self.coordinates_y = y


    def show(self):
        return self.coordinates_x, self.coordinates_y

    def move(self):
        return self.coordinates_x * 2 + 2,self.coordinates_y * 2 + 2

    def dist(self):
        return self.coordinates_x - self.coordinates_y

a = int(input())

b = int(input())

rect = Point(a,b)

print(rect.show())

print(rect.move())

print(rect.dist())


