#!/usr/bin/python3
"""Contains the entry point of the command interpreter:"""
import cmd
import sys
import json


class HBNBCommand(cmd.Cmd):
    """Definition for the class HBNBCommand."""
    c_prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}

    def do_quit(self, arg):
        """Quit function to exit program"""
        exit()

    def do_EOF(self, arg):
        """EOF function to exit program"""
        print('')
        exit()

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
