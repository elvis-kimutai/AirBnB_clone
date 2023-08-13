""" file storage class """
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """
    A class that serializes instances to a JSON file and
    deserializes back to instance"""
    __file_path = "file.json"
    __objects = {}

    # Include the new classes in the dictionary
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def all(self):
        """Returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to __objects dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Adds new object to __objects dictionary"""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes JSON file and restores the object and
        if the file does not exist it does nothing
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    if class_name in FileStorage.classes:
                        class_obj = FileStorage.classes[class_name]
                        FileStorage.__objects[key] = class_obj(**value)
        except FileNotFoundError:
            pass

