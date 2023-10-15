#!/usr/bin/python3
class Base :
    __nb_objects = 0
def __init__(self, id = None):
    self.id = id
    if self.id is not None:
        self.id = id 
    base.__nb_objects += 1
    
