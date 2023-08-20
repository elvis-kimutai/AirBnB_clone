#!/usr/bin/python3
""" the console base"""


import cmd
import re
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, arg):
        """do quit command to exit"""
        return True

    def do_EOF(self, arg):
        """exits the program using EOF"""
        print()
        return True

    def emptyline(self):
        """do nothing when empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates new instance of a class and save it"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        new_instance = HBNBCommand.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
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

    def do_destroy(self, arg):
        """Destroys an  instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.classes:
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
            print("** no instance found **")

    def do_all(self, arg):
        """Print string representations of instances"""
        args = arg.split()

        if len(args) > 0 and args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")

        else:
            instances = []

            for instance in storage.all().values():
                if len(args) > 0 and args[0] == instance.__class__.__name__:
                    instances.append(instance.__str__())
                elif len(args) == 0:
                    instances.append(instance.__str__())

            print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def default(self, arg):
        """Default behaviour for cmd"""
        ins_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "create": self.do_create,
            "count": self.do_count
        }
        match = re.search(r"\.", arg)
        if match is not None:

            args = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", args[1])

            if match is not None:
                command = [args[1][:match.span()[0]], match.group()[1:-1]]

                if command[0] in ins_dict.keys():
                    call = "{} {}".format(args[0], command[1])

                    return ins_dict[command[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """Count the number of instances of a class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        instance_count = 0
        for instance in storage.all().values():
            if instance.__class__.__name__ == class_name:
                instance_count += 1

        print(instance_count)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
