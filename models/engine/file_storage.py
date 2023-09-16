#!/usr/bin/python3
"""
This serializes instances to a JSON file and deserializes JSON file to instances
"""


import json


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to
    instances
    """
    # __file_path: String to json file
    __file_path = "file.json"
    # __objects: dictionary - empty but will store all objects by
    # <class name>.id (ex: to store a BaseModel object with id=12121212,
    # the key will be BaseModel.12121212)
    __objects = {}

    def all(self):
        """
        a public instancemethd that retuens the directory __objects
        """
        return self.__objects

    def new(self, obj):
        """
        a public instance method
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        info = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(info, file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file 
        (__file_path) exists ;otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, "r") as file:
                info = json.load(file)
                for key, value in info.items():
                    class_name, obj_id = key.split(".")
                    if class_name in globals():
                        class_ = globals()[class_name]
                        obj = class_(**value)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass
