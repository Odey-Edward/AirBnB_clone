#!/usr/bin/env python3

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program\n"""
        return True

    def emptyline(self):
        return cmd.Cmd.precmd(self, "")

    def default(self, error_meg):
        print(error_meg)

    def do_create(self, line):
        """create a new BaseModel instance\n"""
        command = cmd.Cmd.parseline(self, line)
        if command[0]:
            if command[0] == "BaseModel":
                model = BaseModel()
                model.save()
                print(model.id)
            else:
                __class__.default(self, "** class doesn't exist **")
        else:
            __class__.default(self, "** class name missing **")

    def do_show(self, line):
        """Prints the string representation of an instance
based on the class name and id\n"""

        command = cmd.Cmd.parseline(self, line)

        if command[0]:
            if command[0] == "BaseModel":
                if command[1]:
                    all_objects = storage.all()
                    for key in all_objects:
                        if key[10:] == command[1]:
                            print(all_objects[key])
                            return
                    __class__.default(self, "** no instance found **")
                else:
                    __class__.default(self, "** instance id missing **")
            else:
                __class__.default(self, "** class doesn't exist **")
        else:
            __class__.default(self, "** class name missing **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

        command = cmd.Cmd.parseline(self, line)

        if command[0]:
            if command[0] == "BaseModel":
                if command[1]:
                    all_objects = storage.all()
                    for key in all_objects:
                        if key[10:] == command[1]:
                            del storage._FileStorage__objects[key]
                            storage.save()
                            return
                    __class__.default(self, "** no instance found **")
                else:
                    __class__.default(self, "** instance id missing **")
            else:
                __class__.default(self, "** class doesn't exist **")
        else:
            __class__.default(self, "** class name missing **")

    @staticmethod
    def print_obj():
        obj_array = []
        all_object = storage.all()

        for key in all_object:
            obj_array.append(all_object[key])
        print(obj_array)

    def do_all(self, line):
        """Prints all string representation of all instances\
based or not on the class name"""

        command = cmd.Cmd.parseline(self, line)

        if command[0]:
            if command[0] == "BaseModel":
                __class__.print_obj()
            else:
                __class__.default(self, "** class doesn't exist **")
        else:
            __class__.print_obj()

    def do_update(self, line):
        command = cmd.Cmd.parseline(self, line)

        if command[0]:
            if command[0] == "BaseModel":
                if command[1]:
                    args = command[1].split()
                    all_objects = storage.all()
                    for key in all_objects:
                        if key[10:] == args[0]:
                            if len(args) > 1:
                                if len(args) > 2:
                                    storage.\
                                     _FileStorage__objects[key][args[1]]\
                                     = args[2].strip('"')
                                    storage.save()
                                    return
                                else:
                                    self.default("** value missing **")
                                    return
                            else:
                                self.\
                                    default("** attribute name missing **")
                                return
                    self.default("** no instance found **")
                else:
                    self.default("** instance id missing **")
            else:
                self.default("** class doesn't exist **")
        else:
            self.default("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
