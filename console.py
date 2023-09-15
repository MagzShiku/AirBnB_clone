#!/usr/bin/python3

"""
This module provides a command line interface for the program
"""

import cmd
from models import storage
from models.base_model import BaseModel, classes
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    This class provides methods for handling commands in the program CLI
    """
    prompt = "(hbnb) "

    def do_create(self, line):
        """
        This method creates a new instance of an object

        Usage: create <class_name>
        """
        args = line.split()
        if not args:
            print("** Missing class name **")
            return

        class_name = args[0]
        if class_name not in classes:
            print("** Class doesn't exist **")
            return

        new_instance = classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """
        This method prints the string representation of an instance

        Usage: show <class_name> <id>
        """
        args = line.split()
        if len(args) != 2:
            print("** Usage: show <class_name> <id> **")
            return

        class_name, obj_id = args[0], args[1]
        if class_name not in classes:
            print("** Class doesn't exist **")
            return

        obj_key = class_name + "." + obj_id
        if obj_key not in storage.all():
            print("** No instance found **")
            return

        print(storage.all()[obj_key])

    def do_destroy(self, line):
        """
        This method deletes an instance

        Usage: destroy <class_name> <id>
        """
        args = line.split()
        if len(args) != 2:
            print("** Usage: destroy <class_name> <id> **")
            return

        class_name, obj_id = args[0], args[1]
        if class_name not in classes:
            print("** Class doesn't exist **")
            return

        obj_key = class_name + "." + obj_id
        if obj_key not in storage.all():
            print("** No instance found **")
            return

        del storage.all()[obj_key]
        storage.save()

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
            if class_name not in classes:
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
        if class_name not in classes:
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
        if class_name not in classes:
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
