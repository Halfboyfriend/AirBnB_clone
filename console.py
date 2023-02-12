#!/usr/bin/python3
"""
The console v: 0.0.1
Contains the entry point of the command interpreter
"""
import cmd
# import models
# import json

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb)'
    def do_EOF(self, line):
        """
        EOF to exit the program
        :return: True
        """
        return True

    def do_quit(self, line):
        "Quit command to exit the program"
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()