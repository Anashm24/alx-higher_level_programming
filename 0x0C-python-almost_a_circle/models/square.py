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
        for index, arg in enumerate(args):
            if index == 0:
                self.id = arg
            if index == 1:
                self.size = arg
            elif index == 2:
                self.x = arg
            elif index == 3:
                self.y = arg
    
        if not args:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
