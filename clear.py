#Python does not have a built-in console clearing function, so we need to import the "os" module
import os

def clear_console():
    #Window's name in the "os" module is "nt" (which stands for Windows NT/New Technology)
    if os.name == "nt":
        #The "cls" command is in fact the console clearing command (Command Prompt)
        os.system("cls")
    else:
        #The "clear" command is for Linux, Mac, etc.
        os.system("clear")