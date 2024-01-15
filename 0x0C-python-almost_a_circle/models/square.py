#!/usr/bin/python3
"""defines a Square class"""
from rectangle import Rectangle


class Square(Rectangle):
    """class that represent a square"""
    
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        
    @property
    def size(self):
        """gettet for size"""
        return self.width
    
    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value
    
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        arg_list = list(args)
        if len(arg_list) > 0:
            self.id = arg_list[0]
        if len(arg_list) > 1:
            self.size = arg_list[1]
        if len(arg_list) > 2:
            self.x = arg_list[2]
        if len(arg_list) > 3:
            self.y = arg_list[3]
    
        if not arg_list:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
