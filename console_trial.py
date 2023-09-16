#!/usr/bin/python3
"""
This is a module that defines the command line interface for the application
by using the cmd.Cmd module
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """
     This is the class that contains all the method for the application
     for handling commands in the programs command line interface
     """


classes = {
        "BaseModel": BAseModel,
        "User": User,
        "State": State,
        "Amenity": Amenity,
        "Place": Place,
        "City": City,
        "Review": Review
        }
prompt = "hbnb "


def do_EOF(self, line):
    """ This method exits the interpreter cleanly """
    print()
    return 1


def do_quit(self, line):
    """This method defines a quit command to exit the program"""
    return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
