# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.
#
# Other abilities of a Circle instance:
#
# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
# Be able to put them in a list and sort them
# Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles

class Circle:
    circles = []

    def __init__(self, radius=0, diameter=0):
        if (radius == 0) != (diameter == 0):
            if radius > 0:
                diameter = radius * 2
            else:
                radius = diameter/2
        elif diameter/radius != 2:
            raise ValueError("Please, choose correct values for radius/diameter of the circle")
        self.area = round(3.14159 * (radius**2), 2)
        self.radius = radius
        self.diameter = diameter
        Circle.circles.append(self)

    def __lt__(self, other):
        if self.area < other.area:
            return True
        return False

    def __eq__(self, other):
        if self.area == other.area:
            return True
        return False

    def __gt__(self, other):
        if self.area > other.area:
            return True
        return False

    def __add__(self, other):
        new_area = self.area + other.area
        new_r = round((new_area/3.14159) ** 0.5, 2)
        # Circle.circles.append(Circle(new_r))
        return Circle(new_r)

    def __str__(self):
        return f"This circle's area is: {self.area}"

    def __repr__(self):
        return f"Circle with area of: {self.area}"


c1 = Circle(4, 8)
c4 = Circle(4)
c2 = Circle(7)
c5 = Circle(2)
c6 = Circle(1)
print(c1.__dict__)
print(Circle.circles)
print(c1+c2)
print(Circle.circles)
print(c1.area, c2.area)
print(Circle.circles[2].area, Circle.circles[2].radius)
c3 = Circle.circles[2]
print(c1 == c4)

sorted_list = sorted(Circle.circles)
print(sorted_list)
