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
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    # Editing this method
    def do_show(self, arg):
        """
        This method prints the string representation of an instance

        Usage: show <class_name> <id>
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            instance = storage.all().get(f"{args[0]}.{args[1]}")
            if instance:
                print(instance)
            else:
                print("** no instance found **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        This method deletes an instance

        Usage: destroy <class_name> <id>
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 1:
            print("** instance id missing **")
            return
        try:
            instance = storage.all()[f"{args[0]}.{args[1]}"]
            del storage.all()[f"{args[0]}.{args[1]}"]
            storage.save()
        except KeyError:
            print("** no instance found **")

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
                print("** class doesn't exist **")
                return

            for obj in storage.all().values():
                if obj.__class__.__name__ == class_name:
                    all_instances.append(str(obj))

        print(all_instances)

    def do_update(self, arg):
        """
        This method updates an instance by adding or updating an attribute

        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            instance = storage.all()[f"{args[0]}.{args[1]}"]
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(instance, args[2], eval(args[3]))
            instance.save()
        except KeyError:
            print("** no instance found **")

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
