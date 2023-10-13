#!/usr/bin/env python3
"""Definition of the HBNB command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The HBNBCommand interpreter class"""

    prompt = "(hbnb) "
    valid_class = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program\n"""
        return True

    def emptyline(self):
        """method called when line is empty"""
        return cmd.Cmd.precmd(self, "")

    def default(self, error_meg):
        """medthod called if command do not exist"""
        print(error_meg)

    @staticmethod
    def switch(obj, command):
        """check and create valid class"""

        if command == "BaseModel":
            model = BaseModel()
            model.save()
            print(model.id)
        elif command == "User":
            user = User()
            user.save()
            print(user.id)
        elif command == "Place":
            place = Place()
            place.save()
            print(place.id)
        elif command == "State":
            state = State()
            state.save()
            print(state.id)
        elif command == "City":
            city = City()
            city.save()
            print(city.id)
        elif command == "Amenity":
            amenity = Amenity()
            amenity.save()
            print(amenity.id)
        elif command == "Review":
            review = Review()
            review.save()
            print(review.id)
        else:
            __class__.default(obj, "** class doesn't exist **")

    def do_create(self, line):
        """create a new BaseModel instance\n"""
        command = cmd.Cmd.parseline(self, line)
        if command[0]:
            __class__.switch(self, command[0])
        else:
            __class__.default(self, "** class name missing **")

    def do_show(self, line):
        """Prints the string representation of an instance
based on the class name and id\n"""

        command = cmd.Cmd.parseline(self, line)

        if command[0]:
            if command[0] in __class__.valid_class:
                if command[1]:
                    all_objects = storage.all()
                    for key in all_objects:
                        if key[10:] == command[1] or\
                            key[5:] == command[1] or\
                            key[6:] == command[1] or\
                            key[8:] == command[1] or\
                            key[7:] == command[1]:
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
            if command[0] in __class__.valid_class:
                if command[1]:
                    all_objects = storage.all()
                    for key in all_objects:
                        if key[10:] == command[1] or\
                            key[5:] == command[1] or\
                            key[6:] == command[1] or\
                            key[8:] == command[1] or\
                            key[7:] == command[1]:
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
        """print all stored class"""
        obj_array = []
        all_object = storage.all()

        for key in all_object:
            obj_array.append(all_object[key])
        print(obj_array)

    @staticmethod
    def print_base_model(obj_id):
        """print all BaseModel class"""
        model_array = []
        all_object = storage.all()

        for key in all_object:
            if key[:9] == obj_id:
                model_array.append(all_object[key])

        print(model_array)

    @staticmethod
    def print_user(obj_id):
        """print all User class"""
        user_array = []
        all_object = storage.all()

        for key in all_object:
            if key[:4] == obj_id:
                user_array.append(all_object[key])

        print(user_array)

    @staticmethod
    def print_place(obj_id):
        """print all Place class string representation"""
        place_array = []
        all_object = storage.all()

        for key in all_object:
            if key[:5] == obj_id:
                place_array.append(all_object[key])

        print(place_array)

    @staticmethod
    def print_state(obj_id):
        """print all State class"""
        state_array = []
        all_object = storage.all()

        for key in all_object:
            if key[:5] == obj_id:
                state_array.append(all_object[key])

        print(state_array)

    @staticmethod
    def print_city(obj_id):
        """print all City class"""
        city_array = []
        all_object = storage.all()

        for key in all_object:
            if key[:4] == obj_id:
                city_array.append(all_object[key])

        print(city_array)

    @staticmethod
    def print_amenity(obj_id):
        """print all amenity class"""
        amenity_array = []
        all_object = storage.all()

        for key in all_object:
            if key[:7] == obj_id:
                amenity_array.append(all_object[key])

        print(amenity_array)

    @staticmethod
    def print_review(obj_id):
        """print all Review class"""
        review_array = []
        all_object = storage.all()

        for key in all_object:
            if key[:6] == obj_id:
                review_array.append(all_object[key])

        print(review_array)

    def do_all(self, line):
        """Prints all string representation of all instances\
based or not on the class name"""

        command = cmd.Cmd.parseline(self, line)

        if command[0]:
            if command[0] == "BaseModel":
                __class__.print_base_model(command[0])
            elif command[0] == "User":
                __class__.print_user(command[0])
            elif command[0] == "Place":
                __class__.print_place(command[0])
            elif command[0] == "State":
                __class__.print_state(command[0])
            elif command[0] == "City":
                __class__.print_city(command[0])
            elif command[0] == "Amenity":
                __class__.print_amenity(command[0])
            elif command[0] == "Review":
                __class__.print_review(command[0])
            else:
                __class__.default(self, "** class doesn't exist **")
        else:
            __class__.print_obj()

    def do_update(self, line):
        """Updates an instance based on the class name and id"""

        command = cmd.Cmd.parseline(self, line)

        if command[0]:
            if command[0] in __class__.valid_class:
                if command[1]:
                    args = command[1].split()
                    all_objects = storage.all()
                    for key in all_objects:
                        if key[10:] == args[0] or\
                            key[5:] == args[0] or\
                            key[6:] == args[0] or\
                            key[8:] == args[0] or\
                            key[7:] == args[0]:
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
