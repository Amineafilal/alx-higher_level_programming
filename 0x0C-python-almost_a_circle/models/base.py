#!/usr/bin/python3
"""This module represent the first class Base"""
import json
import csv

class Base:
    """This class of base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ This class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                json_string = f.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                obj_data = [
                    obj.__dict__[key]
                    for key in obj.__dict__
                    if key != "__class__"
                ]
            writer.writerow(obj_data)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes objects from a CSV file."""
        filename = cls.__name__ + ".csv"
        obj_list = []
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    obj = cls(
                        int(row[1]),
                        int(row[2]),
                        int(row[3]),
                        int(row[4]),
                        int(row[0])
                    )
                elif cls.__name__ == "Square":
                    obj = cls(
                        int(row[1]),
                        int(row[2]),
                        int(row[3]),
                        int(row[0])
                    )
                obj_list.append(obj)
        return obj_list
