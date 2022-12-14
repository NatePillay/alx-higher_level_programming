#!/usr/bin/python3
""" a class that defines a rectangle"""


class Rectangle:
    """A class that will define the dimensions of rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
        Args:
            width: rep the width of the rectangle
            height: rep the height of the rectangle
        Raises:
            TypeError: if the size is not an integer
            ValueError: if the size is less then zero
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """retrieves the width"""
            return self.__width

        @width.setter
        def width(self, value):
            """sets width"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """retrieves the height"""
            return self.__height

        @height.setter
        def height(self, value):
            """retrieves the height"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

        def area(self):
            """Returns the area of a rectangle"""
            return (self.width * self.height)

        def perimeter(self):
            """Returns the perimeter of a rectangle"""
            if self.__width == 0 or self.__height == 0:
                return (0)
            return ((self.width * 2) + (self.height * 2))

        def __str__(self):
            """Returns a shape made with #'s"""
            if not self.perimeter:
                return ("")
            return ('\n'.join('#' * seld.width for x in range(self.height)))
        
        def __repr__(self):
            """modifies repr object"""
            return ("Rectangle({}, {})".format(self.width, self.height))
