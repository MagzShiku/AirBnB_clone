#!/usr/bin/python3

"""
This module provides a command line interface for the program
"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This class provides methods for handling commands in the program CLI
    """
    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_create(self, arg):
        """
        This method creates a new instance of an object

        Usage: create <class_name>
        """
        if not arg:
            print("** Missing class name **")
            return
        try:
            class_name = arg.split()[0]
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    # Editing this method
    def do_show(self, line):
        """
        This method prints the string representation of an instance

        Usage: show <class_name> <id>
        """
        if not line:
            print("** class name missing **")
            return

        args = line.split()  # edit
        class_name = args[0]
        if class_name not in self.classes:
            print("** Class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        This method deletes an instance

        Usage: destroy <class_name> <id>
        """
        if not line:
            print("** class name missing **")
            return

        args = line.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** No instance found **")

    def do_all(self, line):
        """
        This method prints all string representations of instances

        Usage: all [class_name]
        """
        args = line.split()
        all_instances = []

        if not args:
            for obj in storage.all().values():
                all_instances.append(str(obj))
        else:
            class_name = args[0]
            if class_name not in self.classes:
                print("** Class doesn't exist **")
                return

            for obj in storage.all().values():
                if obj.__class__.__name__ == class_name:
                    all_instances.append(str(obj))

        print(all_instances)

    def do_update(self, line):
        """
        This method updates an instance by adding or updating an attribute

        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = line.split()
        if len(args) != 4:
            print("** Usage: update < class_name > < id > \
                  < attribute_name > \"<attribute_value>\" **")
            return

        class_name, obj_id, attr_name, attr_value = args[0], args[1], args[2],
        args[3]
        if class_name not in self.classes:
            print("** Class doesn't exist **")
            return

        obj_key = class_name + "." + obj_id
        if obj_key not in storage.all():
            print("** No instance found **")
            return

        obj = storage.all()[obj_key]
        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_count(self, line):
        """
        This method counts the number of objects of a specified class

        Usage: count <class_name>
        """
        args = line.split()
        if len(args) != 1:
            print("** Usage: count <class_name> **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** Class doesn't exist **")
            return

        count = sum(1 for obj in storage.all().values()
                    if obj.__class__.__name__ == class_name)
        print(count)

    def do_EOF(self, line):
        """
        This method ends the command line interpreter

        Usage: CTRL+D
        """
        print()  # Edit 00
        return True

    def do_quit(self, line):
        """
        This method quits the command line interpreter

        Usage: quit
        """
        return True

    def emptyline(self):
        """
        This method ignores empty lines (ENTER)
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
