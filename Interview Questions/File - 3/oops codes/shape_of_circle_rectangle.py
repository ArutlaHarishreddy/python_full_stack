#Implement inheritance with a base class `Shape` and derived classes `Circle` and `Rectangle` with an `area()` method.

from math import pi

class Shape:
    def area(self,):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return pi*self.radius ** 2
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width

circle=Circle(5)
rectangle=Rectangle(2,4)

print(circle.area()),print(rectangle.area())

