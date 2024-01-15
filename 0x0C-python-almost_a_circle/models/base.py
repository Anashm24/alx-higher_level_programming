#!/usr/bin/python3
"""defines a class Base"""
import json


class Base:
    """this class is the base of all other classes"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries"""
        
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of
        list_objs to a file"""
         
        with open(f"{cls.__name__}.json", "w") as json_file:
            if not list_objs:
                json_file.write("[]")
            else:
                json_file.write(Base.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string 
        representation json_string"""
        
        if not json_string:
            return []
        else:
            return json.loads(json_string)
