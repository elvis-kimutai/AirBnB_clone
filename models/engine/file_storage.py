#!/usr/bin/python3
"""
Contains FileStorage class model

"""
import json

class FileStorage:
    """
    A class that serialize objects to JSON file 
    and deseralize it back to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary of objects
        """
        return self.__objects

    def new(self, obj):
        """
        Adds new object to __objects dictionary
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes stored objects and saves them to a JSON file
        """
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """
        Deserializes JSON file and restores the objects
        and if the file does not exist it does nothing
        """
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objs = json.load(file)
                for key, value in loaded_objs.items():
                    class_name = key.split('.')[0]
                    self.__objects[key] = globals()[class_name](**value)
        except FileNotFoundError:
            pass
