#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User}

    def do_create(self, line):
        """Create a new instance of BaseModel, save it and print the id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Print the string representation of an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        storage = FileStorage()
        storage.reload()
        all_objs = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key not in all_objs:
            print("** no instance found **")
        else:
            print(all_objs[key])

    def do_destroy(self, line):
        """Delete an instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        storage = FileStorage()
        storage.reload()
        all_objs = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key not in all_objs:
            print("** no instance found **")
        else:
            del all_objs[key]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances"""
        args = line.split()
        storage = FileStorage()
        storage.reload()
        all_objs = storage.all()
        if len(args) == 0:
            print([str(obj) for obj in all_objs.values()])
        else:
            class_name = args[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            print([str(obj) for key, obj in all_objs.items() if key.startswith(class_name)])

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        storage = FileStorage()
        storage.reload()
        all_objs = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key not in all_objs:
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
        setattr(all_objs[key], attribute_name, attribute_value)
        all_objs[key].save()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print("")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
