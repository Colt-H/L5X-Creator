"""Generate programs from user input"""

import xml.etree.ElementTree as ET
from indent import indent

class BuildProgs():
    """Builds the program from input function"""
    def __init__(self,
                 project_path,
                 prog_name,
                 main_rout_name,
                ):
        self.project_path = project_path
        self.prog_name = prog_name
        self.main_rout_name = main_rout_name

    def build_prog_xml(self):
        """Builds XML data for programs and writes to file
        """
        path = self.project_path+".L5X"
        xml = ET.parse(path)
        root = xml.getroot()
        modules = root.find("./Controller/Programs")
        new_prog = ET.SubElement(modules, 'Program')
        new_prog.attrib["Name"] = self.prog_name
        new_prog.attrib["TestEdits"] = "false"
        new_prog.attrib["MainRoutineName"] = self.main_rout_name
        new_prog.attrib["Disabled"] = "false"
        new_prog.attrib["UseAsFolder"] = "false"
        new_prog_routines = ET.SubElement(new_prog, "Routines")
        new_prog_base_routine = ET.SubElement(new_prog_routines, "Routine")
        new_prog_base_routine.attrib["Name"] = "MainRoutine"
        new_prog_base_routine.attrib["Type"] = "RLL"
        indent(root)
        xml.write(path, encoding="utf-8", xml_declaration=True)

def prog_build(path):
    """simply contains user selection for adding programs"""
    print("Add another program? (Y/N)")
    sel = input(">>>")
    if sel.lower() == "y":
        prog_build_data(path)
    elif sel.lower() == "n":
        return

def prog_build_data(project_path):
    """Gets user input data on a program and passes it to the build prog class

    Args:
        project_path (string): path to project as defined in main
    """
    print("Building New Program.")
    prog_name = input("enter the program name:\n>>>")
    main_rout_name = input("Enter the main routine name:\n>>>")
    progs = BuildProgs(project_path,
                       prog_name,
                       main_rout_name,
                       )
    progs.build_prog_xml()
