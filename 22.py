
#the super function is used in the child's class to call methods from a parent's class called the superclass (superclass)
#Allows you to extend the functionality of the different methods
#Within a child's class, you could use is within a constructor to assign an attributes that all of it's siblings have in common such as color or if that shape is filled. When used within any other method, you can extend the functionality of that method. And well yeah that is the super function in python.

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

#Extending the functionality
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

        #What we're about to do here is called method overriding

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm")

        #This is called method overriding. If a child shares a similar method with a parent, you'll use the child's version and not the parent's.

        #If you would like to extend the functionality of a method, from a parent, you could use the super function e.g you want to se the describe function of the parent and the child too,

        super().describe()



class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm")

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm")

circle = Circle("red", True, 5)
square = Square("blue", False, 6)
triangle = Triangle("yellow", True, 7, 8)

circle.describe()
