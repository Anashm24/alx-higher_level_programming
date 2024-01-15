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
