# Import modules section.
import os


def clear():
    # For Windows environment
    if os.name == 'nt':
        os.system('cls')

    # For Linux/Unix environment
    else:
        os.system("clear")
