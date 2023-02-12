#!/usr/bin/python3
"""
Module file_storage serializes and
deserializes JSON types
"""

import json


class FileStorage():

    """
        Custom class for file storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns dict representation of all objects
        """
        return self.__objects

    def new(self, object):
        """
        sets in __objects the object with the key
               <object class name>.id
        Args:
            object(obj): object to write
        """
        self.__objects[object.__class__.__name__ + '.' + str(object)] = object

    def save(self):
        """
            serializes __objects to the JSON file
            (path: __file_path)
        """
        with open(self.__file_path, 'w+') as file:
            json.dump({key: value.to_dict() for key, value in self.__objects.items()}, file, indent=4)

    def reload(self):
        """
            deserializes the JSON file to __objects, if the JSON
            file exists, otherwise nothing happens)
        """
        try:
            with open(self.__file_path, 'r') as file:
                dt = json.loads(file.read())
                for value in dt.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))

        except Exception:
            pass




