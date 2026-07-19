

class Rectangle:
    def __init__(self, width, height):
        #To make an attribute private, we prefix them with an underscore this tells you and other developers that these attributes, they're ment to be protected, they're internal. we shouldn't access the widths and heights directly outside of this class. Technically we could by printing "print(rectangle1._width)" We get 3 and 4 but we do get a warning saying "Access to protected member _width of a class"That applies to height as well. Our width and height are only ment to be used outside of this class. If we need to get the width and the height, we would need to do so through the getter methods provided by the property decorator.
        #
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.2f}cm"

    @property
    def height(self):
        return f"{self._height:.2f}cm"

    #So that's teh point of using a getter mehod, we can add additional logic when reading one of these attributes when we try to get them

    #We can also add setter methods of we would like to set or write these attribtes e,g:

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height must be greater than 0")

rectangle = Rectangle(3, 4)

rectangle.width = 11

class Rectangle:
    def __init__(self, width, height):
        #To make an attribute private, we prefix them with an underscore this tells you and other developers that these attributes, they're ment to be protected, they're internal. we shouldn't access the widths and heights directly outside of this class. Technically we could by printing "print(rectangle1._width)" We get 3 and 4 but we do get a warning saying "Access to protected member _width of a class"That applies to height as well. Our width and height are only ment to be used outside of this class. If we need to get the width and the height, we would need to do so through the getter methods provided by the property decorator.
        #
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.2f}cm"

    @property
    def height(self):
        return f"{self._height:.2f}cm"

    #So that's teh point of using a getter mehod, we can add additional logic when reading one of these attributes when we try to get them

    #We can also add setter methods of we would like to set or write these attribtes e,g:

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height must be greater than 0")
        #When using these setter methods, we can se this additional logic when writing or changing one of these attributes. These are setter methods

    #We would create a deleter keyword,
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")

rectangle1 = Rectangle(3, 4)

rectangle1.width = 5
rectangle1.height = 6

#If we need to delete an attribute, here's how
#We would use the delete keyword.

del rectangle1.width
del rectangle1.height


#print(rectangle._width)
#print(rectangle._height)

#Well everybody that's everything about @property.
