#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it to the JSON file, and print the id"""
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
        """Print the string representation of an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in storage.all():
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = args[0] + "." + args[1]
        if obj_key in storage.all():
            print(storage.all()[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in storage.all():
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = args[0] + "." + args[1]
        if obj_key in storage.all():
            del storage.all()[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances based on the class name"""
        args = arg.split()
        objects = []
        if not args:
            for obj in storage.all().values():
                objects.append(str(obj))
        elif args[0] not in storage.all():
            print("** class doesn't exist **")
            return
        else:
            for key, obj in storage.all().items():
                if key.split('.')[0] == args[0]:
                    objects.append(str(obj))
        print(objects)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in storage.all():
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = args[0] + "." + args[1]
        if obj_key not in storage.all():
            print("** no instance found **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[obj_key]
        setattr(obj, args[2], args[3].strip('"'))
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
