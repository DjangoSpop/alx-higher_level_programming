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
def width    
