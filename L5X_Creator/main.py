"""main function for the creator"""

import os
from directory_creator import create_dir

def startup():
    """Gets terminal size, displays title"""
    os.system('cls')
    size = os.get_terminal_size()
    center = size[0] / 2
    print("L5x Creation Tool".center(int(center)))

def clear():
    """Clears the Terminal"""
    os.system('cls')

def main():
    """Main Routine calling separate functions and containing main loop"""
    startup()
    while True:
        print("hello")
        break

if __name__ == "__main__":
    main()
