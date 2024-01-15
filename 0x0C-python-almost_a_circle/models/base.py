#!/usr/bin/python3
"""defines a class Base"""
import json
import csv
import os


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
                json_file.write(Base.to_json_string([obj.to_dictionary()
                                                     for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation json_string"""

        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        if not os.path.exists(f"{cls.__name__}.json"):
            return []
        else:
            with open(f"{cls.__name__}", "r") as json_file:
                reader = json.load(json_file)

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of
        JSON strings."""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes and deserializes in CSV"""
        with open(f"{cls.__name__}.csv", "w") as csv_file:
            writer = csv.writer(csv_file)
        for obj in list_objs:
            writer.writerow(list(obj.__dict__.values()))

    @classmethod
    def load_from_file_csv(cls):
        with open(f"{cls.__name__}.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            return [cls(*row) for row in reader]
