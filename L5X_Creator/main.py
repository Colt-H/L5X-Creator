"""main function for the creator"""

import os
from directory_creator import create_dir
from generate_base import generate_base
from modules import io_build

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
    controller = {} #need to convert to class....
    controller["project_name"] = input("Please enter the project name:\n>>>")
    controller["project_path"] = create_dir(controller["project_name"])
    print(f'New Directory created at {controller["project_path"]}.')
    controller["software_rev"] = input("Enter software version (ex 24.02):\n>>>")
    controller["bp_slots"] = input("Enter the size of the backplane:\n>>>")
    controller["creator"] = input("Enter the name of the project creator:\n>>>")
    controller["processor_type"] = input("Enter the processor type (ex 1756-L72):\n>>>")
    controller["processor_major"] = input("Enter the major rev of the processor (ex 24):\n>>>")
    controller["processor_minor"] = input("Enter the minor rev of the processor (ex 11):\n>>>")
    generate_base(controller["project_path"],
                  controller["software_rev"],
                  controller["bp_slots"],
                  controller["creator"],
                  controller["processor_type"],
                  controller["processor_major"],
                  controller["processor_minor"],
                  controller["project_path"]
                  )
    print("Project Created Successfully.")
    while True:
        print(f'Create New Project (N), Edit {controller["project_name"]} (E), Close Editor (C):')
        sel = input('>>>')
        if sel.lower() == "n":
            main()
        elif sel.lower() == "e":
            io_build(controller["project_path"])
            #Continuing the project
        elif sel.lower() == "c":
            break

if __name__ == "__main__":
    main()
