#!/usr/bin/env python3
""" console base"""

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """quit command to exit """
        return True

    def do_EOF(self, arg):
        """exit the program using EOF"""
        print()
        return True

    def emptyline(self):
        """do nothing when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
