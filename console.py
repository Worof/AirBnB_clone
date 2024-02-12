#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand:
    """Entry point of the command interpreter"""
    
    def do_create(self, arg):
        """Create a new instance of BaseModel"""
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
        class_name = args[0]
        instance_id = args[1]
        try:
            objects = FileStorage().all()
            key = "{}.{}".format(class_name, instance_id)
            print(objects[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = args[1]
        try:
            objects = FileStorage().all()
            key = "{}.{}".format(class_name, instance_id)
            del objects[key]
            FileStorage().save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        objects = FileStorage().all()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return
        args = arg.split()
        if args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in objects.values() if args[0] == obj.__class__.__name__])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = args[1]
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        try:
            objects = FileStorage().all()
            key = "{}.{}".format(class_name, instance_id)
            obj = objects[key]
            setattr(obj, args[2], args[3])
            obj.save()
        except KeyError:
            print("** no instance found **")