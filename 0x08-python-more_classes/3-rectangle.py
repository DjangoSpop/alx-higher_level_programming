class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = 0  # Private attribute for width
        self._height = 0  # Private attribute for height
        self.width = width  # Call the setter for width
        self.height = height  # Call the setter for height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str[:-1]  # Remove the last newline

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

# Example usage:
# Creating an instance of the Rectangle class
rect = Rectangle(4, 5)

# Accessing attributes and calling methods
print(rect.area())       # Outputs 20 (4 * 5)
print(rect.perimeter())  # Outputs 18 (2 * (4 + 5))

# Printing the rectangle using __str__
print(rect)  # Outputs:
# ####
# ####
# ####
# ####
# ####

# Creating an instance with zero width and height
empty_rect = Rectangle(0, 0)
print(empty_rect)  # Outputs an empty string
