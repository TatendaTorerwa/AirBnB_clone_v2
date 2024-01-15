#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        if cls is None:
            return self,__objects
        else:
            filtered_dict = {}
            for key, value in self.__objects.items():
                if type(value) is cls:
                    filtered_dict[key] = value
                    return filterd_dict

    def new(self, obj):
        """Adds a new object to the storage dictionary"""
        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes the storage dictionary to the JSON file"""
        my_dict = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserializes the JSON file to the storage dictionary"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in json.load(f).items():
                    obj = eval(value["__class__"])(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj is not None:
            obj_key = obj.to_dict()['__clas__'] + '.' = obj.id
            if obj_key in self.__objects.keys():
                del self.__objects[obj_key]

    def close(self):
        """Calls reload()"""
        self.reload()
