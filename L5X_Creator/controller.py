"""Creates the controller class to be referenced everywhere.
"""

from directory_creator import create_dir

class Controller():
    """controller class contains all data needed to build a base blank project"""
    def __init__(self,
                 project_name,
                 project_path,
                 software_rev,
                 bp_slots,
                 creator,
                 processor_type,
                 processor_major,
                 processor_minor
                 ):
        self.project_name = project_name
        self.project_path = project_path
        self.software_rev = software_rev
        self.bp_slots = bp_slots
        self.creator = creator
        self.processor_type = processor_type
        self.processor_major = processor_major
        self.processor_minor = processor_minor


def build_controller():
    """builds the controller class to be used in generating base data"""
    project_name = input("Please enter the project name:\n>>>")
    project_path = create_dir(project_name)
    print(f'New Directory created at {project_path}.')
    software_rev = input("Enter software version (ex 24.02):\n>>>")
    bp_slots = input("Enter the size of the backplane:\n>>>")
    creator = input("Enter the name of the project creator:\n>>>")
    processor_type = input("Enter the processor type (ex 1756-L72):\n>>>")
    processor_major = input("Enter the major rev of the processor (ex 24):\n>>>")
    processor_minor = input("Enter the minor rev of the processor (ex 11):\n>>>")
    controller = Controller(project_name,
                            project_path,
                            software_rev,
                            bp_slots,
                            creator,
                            processor_type,
                            processor_major,
                            processor_minor)
    return controller
