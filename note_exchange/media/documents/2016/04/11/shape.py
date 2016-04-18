# Authors Jacob Fisbaugh, Taylor Ripke, Chase Nouhan (Mentioned he may redo in a different language)

class Shape(object):
    def __init__(self, color):
        self.color = color

    def get_area(self):
        pass

    def to_string(self):
        return str(self.color)


class Rectangle(Shape):

    def __init__(self, color, length, width):
        Shape.__init__(self, color)
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def to_string(self):
        return super(Rectangle, self).to_string() + " " + str(self.length) + " " + str(self.width) + " " + str(self.get_area())

class Triangle(Shape):

    def __init__(self, color, base, height):
        Shape.__init__(self, color)
        self.base = base
        self.height = height

    def get_area(self):
        half_base = self.base/2
        print half_base
        return half_base * self.height
    def to_string(self):
        return super(Triangle, self).to_string() + " " + str(self.base) + " " + str(self.height) + " " + str(self.get_area())

print "Shape:"
shape = Shape('red')
print shape.color

print "Rectangle:"
rectangle = Rectangle('blue', 10, 11)
print rectangle.to_string()
print rectangle.get_area()

print "Triangle:"
triangle = Triangle('yellow', 4, 6)
print triangle.to_string()
print triangle.get_area()
