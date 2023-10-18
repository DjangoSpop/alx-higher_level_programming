from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def area(self):
        if __name__ = "__main__":
            r1 = Rectangle(3, 2)
            print(r1.area())
            
            r2 = Rectangle(2, 10)
            print(r2.area())
            
            r3 = Rectangle(8, 7, 0, 0, 12)
            print(r3.area())
            
    def display(self):
        if __name__ = "__main__":
            r1 = Rectangle(4, 6)
            r1.display()
            
            r2 = Rectangle(2, 2)
            r2.display()
"""Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>

You can overwrite it but dont forget to call the parent class with super() since we implemented previously a logic inside this method."""

def __str__(self):
    return f"[Rectangle] ({id(self)}) {self.x}/{self.y} - {self.width}/{self.height}"
    
    # def update(self, *args):
    #     if args:
    #         arg_count = len(args)
    #         if arg_count >= 1:
    #             self.id = args[0]
    #         if arg_count >= 2:
    #             self.width = args[1]
    #         if arg_count >= 3:
    #             self.height = args[2]
    #         if arg_count >= 4:
    #             self.x = args[3]
    #         if arg_count >= 5:
    #             self.y = args[4]