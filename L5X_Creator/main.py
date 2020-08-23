"""main function for the creator"""

import os
from generate_base import generate_base
from modules import io_build
from controller import build_controller

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
            io_build(controller.project_path)
            #Continuing the project
        elif sel.lower() == "c":
            break

if __name__ == "__main__":
    main()
