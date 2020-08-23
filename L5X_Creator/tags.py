

import xml.etree.ElementTree as ET
from indent import indent

class BuildTags():
    """Builds the output module from input function"""
    def __init__(self,
                 project_path,
                 tag_name,
                 tag_type,
                 data_type,
                 radix,
                 constant,
                 external_access,
                ):
        self.project_path = project_path
        self.tag_name = tag_name
        self.tag_type = tag_type
        self.data_type = data_type
        self.radix = radix
        self.constant = constant
        self.external_access = external_access

    def build_tags_xml(self):
        """Builds XML data for tags and writes to file
        """
        path = self.project_path+".L5X"
        xml = ET.parse(path)
        root = xml.getroot()
        modules = root.find("./Controller/Tags")
        new_tag = ET.SubElement(modules, 'Tag')
        new_tag.attrib["Name"] = self.tag_name
        new_tag.attrib["TagType"] = self.tag_type
        new_tag.attrib["DataType"] = self.data_type
        new_tag.attrib["Radix"] = self.radix
        new_tag.attrib["Constant"] = self.constant
        new_tag.attrib["ExternalAccess"] = self.external_access
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
