from abc import ABC, abstractmethod
from email.mime import base


class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__ (self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__ (self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__ (self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


#circle = Circle()
#Our circle identifies as a Circle() and since our circle class inherits rom the shape class, it's also considered a shape. It has 2 forms, it's a circle and it's a shape. But it isn't a square or a triangle.
#This also applies to both triangle and square.
#square = Square()
#triangle = Triangle()

class Pizza(Circle):
    def __init__ (self, topping, radius):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("peperoni", 15)]

#Our pizza is considered a pizza, it inherits from the circle class so it's also considered a circle (and our circle class inherits from the shape class) and it's also considered a shape so it would make sense for it to fit into the list of shapes because our pizza also identifies as a shape So that's polymorphism
for sape in shapes:
    print(f"{sape.area()}cm^2")
