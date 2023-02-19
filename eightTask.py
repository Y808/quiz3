"""
Write a Python class named Rectangle constructed from length and width
and a method that will compute the area of a rectangle
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_area(self):
        return self.length * self.width


r1 = Rectangle(4, 5)
print(r1.rectangle_area())
