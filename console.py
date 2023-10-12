#!/usr/bin/env python3

import cmd

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    
    def do_quit(self, command):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, command):
        """EOF command to exit the program\n"""
        return True

    def emptyline(self):
        return cmd.Cmd.precmd(self, "")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
