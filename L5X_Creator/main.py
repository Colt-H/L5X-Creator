"""main function for the creator"""

import os
from directory_creator import create_dir
from generate_base import generate_base

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
        print("Cancel all changes and return to beginning at any time by typing '@restart'.")
        project_name = input("Please enter the project name:\n>>>")
        project_path = create_dir(project_name)
        print(f"New Directory created at {project_path}.")
        fw_version = input("Enter firmware version:\n>>>")
        bp_slots = input("Enter the size of the backplane:\n>>>")
        creator = input("Enter the name of the project creator:\n>>>")
        processor_type = input("Enter the processor type (ex 1756-L72):\n>>>")
        processor_major = input("Enter the major revision of the processor (ex 24):\n>>>")
        processor_minor = input("Enter the minor revision of the processor (ex 24):\n>>>")
        generate_base(project_name, fw_version, bp_slots, creator, processor_type, processor_major, processor_minor, project_path)

if __name__ == "__main__":
    main()
