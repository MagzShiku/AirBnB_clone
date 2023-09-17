#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn't execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
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
        """Deletes an instance"""
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

    def do_all(self, arg):
        """Prints all string representations of instances"""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                class_name = eval(arg).__name__
                print([str(obj) for obj in objects.values() if obj.__class__.__name__ == class_name])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
