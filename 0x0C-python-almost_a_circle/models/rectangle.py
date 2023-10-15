#!/usr/bin/python3
from base import Base
class Rectangle(Base):
    """Rectangle class"""
def __init__(self,width, height, x=0, y=0, id=None):
    Super().__init__(id)
    self.width = width
    self.hight = height
    self.x = x
    self.y = y
def Width(self):
    """getter for width"""
    return self.__width
def width (width):
    """set get the width of rectangle"""
    return self.__width
def width(self, value):
    if type(value)  != int:
        raise TypeError("width must be integer")
    if value <= 0:
        raise ValueError("width must be > 0")
    self.__width = value
def height(self):
    """self get hight"""
    return self.__height
 def height(self, value):
    if type(value) != int:
        raise TypeError("height must be an integer")
    self.__height = value
def x(self):
    """set/get x coordinate"""
    return self.___x
def x(self, value):
    if type(value) !=int:
        raise TypeError("x must be integer")
    if value < 0:
        raise ValueError("x must be >=0")
    self.__x = value
def y(self):
    return self.__y
def y(self, value):
    if type(value) != int:
        raise TypeError("y must be an integer")
    if value < 0:
        raise ValueError("y must be >= 0")
    self.__y = value
def area(sel):
    return self.width * self.hight
def display(self):
    if self.width == 0 or self.hight == 0:
        print("")
        return
    [print("") for y in range(self.y)]
    for h in range(self.height):
        [print("",end="") for x in range(self.x)]
        [print("#",end="")for w in range(self.width)]
        print("")
def update(self, *args, **kwargs):
    if args and len(args) !=0:
        a = 0
        for arg in args:
            if a == 0:
                if arg is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                    elif a == 1:
                        self.width = arg
                    elif a == 2:
                        self.height = arg
                    elif a == 3:
                        self.x = arg
                    elif a == 4:
                        self.y = arg
                    a += 1
                elif kwargs and len(kwargs) != 0:
                    for k, v in kwargs.items():
                        if k == "id":
                            if v is None:
                                self.__init__(self.width,self.height,self.x, self.y)
                                else:
                                    self.id = v
                            elif k == "width":
                                self.width = v
                            elif k == "height"
                                 self.height = v
                            elif k == "x":
                                self.x = v
                            elif k == "y":
                                self.y = v
def to_dictionary(self):
    return{
        "id": self.id,
        "width": self.width,
        "height": self.height,
        "x": self._x
        "y": self.y
    }
def __str__(self):
    return "[Rectangle] ({}) {}/{}.format(self.id, self.x, self.y, self.width, self.height)"