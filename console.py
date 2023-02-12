#!/usr/bin/python3
"""
The console v: 0.0.1
Contains the entry point of the command interpreter
"""
import cmd
# import models
# import json

class HBNBCommand(cmd.Cmd):
    """
    Custom console class
    """

    prompt = '(hbnb)'
    def do_EOF(self, line):
        """Quits command interpreter with ctrl+d
            Args:
                line(args): input argument for quiting
                    the terminal
        """
        return True

    def do_quit(self, line):
        """Handles the 'quit' command
        Args:
            line(args): input argument for quiting
            the terminal
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()