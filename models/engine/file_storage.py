#!/usr/bin/python3
"""
This serializes instances to a JSON file and deserializes
JSON file to instances
"""


import json


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to
    instances
    """

    __file_path = "file.json"
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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        it also serializes all the new classes
        """
        info = {}
        for key, obj in self.__objects.items():
            class_name, obj_id = key.split(".")
            my_classes = "Place", "State", "City", "Amenity", "Review"
            if class_name in [my_classes]:
                info[key] = obj.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(info, file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ;otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)

        this method incldes deserialization of new classes
        Read the JSON file and load its contents into the info dictionary
        Iterate over the info dictionary and check the class of each object.
        If the class is one of the new classes, create an instance of the
        class using the **value syntax and store it in the __objects
        dictionary.
        """
        try:
            with open(self.__file_path, "r") as file:
                info = json.load(file)
                for key, value in info.items():
                    class_name, obj_id = key.split(".")
                    my_classes = "Place", "State", "City", "Amenity", "Review"
                    if class_name in [my_classes]:
                        class_ = eval(class_name)
                        obj = class_(**value)
                        self.__objects[key] = obj

        except FileNotFoundError:
            pass
