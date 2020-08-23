"""main function for the creator"""

import os
import sys
from generate_base import generate_base
from controller import build_controller
from advanced_edit import advanced_menu

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
    controller = build_controller()
    generate_base(controller.project_path,
                  controller.software_rev,
                  controller.bp_slots,
                  controller.creator,
                  controller.processor_type,
                  controller.processor_major,
                  controller.processor_minor,
                  controller.project_path
                  )
    print("Project Created Successfully.")
    while True:
        print(f'Create New Project (N), Edit {controller.project_name} (E), Close Editor (C):')
        sel = input('>>>')
        if sel.lower() == "n":
            main()
        elif sel.lower() == "e":
            advanced_menu(controller.project_path)
            #Continuing the project
        elif sel.lower() == "c":
            sys.exit()

if __name__ == "__main__":
    main()
