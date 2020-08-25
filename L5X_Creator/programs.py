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
        """Builds XML data for tags and writes to file
        """
        path = self.project_path+".L5X"
        xml = ET.parse(path)
        root = xml.getroot()
        modules = root.find("./Controller/Programs")
        new_tag = ET.SubElement(modules, 'Program')
        new_tag.attrib["Name"] = self.prog_name
        new_tag.attrib["TestEdits"] = "false"
        new_tag.attrib["MainRouineName"] = self.main_rout_name
        new_tag.attrib["Disabled"] = "false"
        new_tag.attrib["UseAsFolder"] = "false"
        indent(root)
        xml.write(path, encoding="utf-8", xml_declaration=True)

def tag_build(path):
    """simply contains user selection for what module type to add"""
    print("Add another tag? (Y/N)")
    sel = input(">>>")
    if sel.lower() == "y":
        tag_build_data(path)
    elif sel.lower() == "n":
        return

def tag_build_data(project_path):
    """Gets user input data on a comm module and passes it to the build comms class

    Args:
        project_path (string): path to project as defined in main
    """
    print("Building New Comm Module.")
    tag_name = input("enter the tag name:\n>>>")
    tag_type = input("Enter the tag type (base/alias):\n>>>")
    data_type = input("enter the tag data type (ex DINT):\n>>>")
    radix = input("enter the tag radix (ex Decimal):\n>>>")
    constant = input("constant? (true/false):\n>>>")
    external_access = input("Enter the external access:\n>>>")
    tags = BuildTags(project_path,
                     tag_name,
                     tag_type,
                     data_type,
                     radix,
                     constant,
                     external_access
                     )
    tags.build_tags_xml()