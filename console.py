#!/usr/bin/python3
"""
Console DOC
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """
    Class Doc
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        DOC
        """
        return True

    def do_EOF(self, args):
        """
        DOCs
        """
        return True

    def emptyline(self):
        """
        Docs
        """
        pass

    def do_create(self, arg):
        """
        Docs
        """
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                if args_array[0] == "BaseModel":
                    obj = BaseModel()
                    obj.save()
                    print(obj.id)
                elif args_array[0] == "User":
                    obj = User()
                    obj.save()
                    print(obj.id)
                elif args_array[0] == "State":
                    obj = State()
                    obj.save()
                    print(obj.id)
                elif args_array[0] == "City":
                    obj = City()
                    obj.save()
                    print(obj.id)
                elif args_array[0] == "Amenity":
                    obj = Amenity()
                    obj.save()
                    print(obj.id)
                elif args_array[0] == "Place":
                    obj = Place()
                    obj.save()
                    print(obj.id)
                elif args_array[0] == "Review":
                    obj = Review()
                    obj.save()
                    print(obj.id)
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
        Docs
        """
        allowed_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                class_name = args_array[0]
                if class_name in allowed_classes:
                    if len(args_array) > 1:
                        objs_dict = models.storage.all()
                        search_string = "{}.{}".format(class_name, args_array[1])
                        if search_string in objs_dict:
                            print(objs_dict[search_string])
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
        Docs
        """
        allowed_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                class_name = args_array[0]
                if class_name in allowed_classes:
                    if len(args_array) > 1:
                        objs_dict = models.storage.all()
                        search_string = "{}.{}".format(class_name, args_array[1])
                        if search_string in objs_dict:
                            del(objs_dict[search_string])
                            models.storage.save()
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")           
    
    def do_all(self, arg):
        """
        Docs
        """
        allowed_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                class_name = args_array[0]
                if class_name in allowed_classes:
                    final_list = []
                    for key, value in models.storage.all().items():
                        if (class_name in key):
                            final_list.append(str(value))
                    print(final_list)
                else:
                    print("** class doesn't exist **")
        else:
            final_list = []
            for key, value in models.storage.all().items():
                final_list.append(str(value))
            print(final_list)

    def do_update(self, arg):
        """
        Docs
        """
        allowed_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                class_name = args_array[0]
                if class_name in allowed_classes:
                    if len(args_array) > 1:
                        objs_dict = models.storage.all()
                        search_string = "{}.{}".format(class_name, args_array[1])
                        if search_string in objs_dict:
                            if len(args_array) > 2:
                                if len(args_array) > 3:
                                    if (args_array[3] not in ["created_at", "updated_at", "id"]):
                                        setattr(objs_dict[search_string], str(args_array[2]), str(args_array[3])) 
                                else:
                                    print("** value missing **")
                            else:
                                print("** attribute name missing **")
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_User(self, arg):
        """
        Docs
        """
        allowed_methods = [".all()"]
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                command_method = args_array[0]
                if command_method in allowed_methods:
                    if command_method == ".all()":
                        final_list = []
                        for key, value in models.storage.all().items():
                            if ("User" in key):
                                final_list.append(str(value))
                        print(final_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
