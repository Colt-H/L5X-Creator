"""
Creates a class to build a comm module from
"""

import xml.etree.ElementTree as ET

# class io_build:

#     def __init__(self):
#     def build_comms():
#     def build_input():
#     def build_output():
#     def write_to_file():

class BuildComms():
    """Builds the comm module from input function"""
    def __init__(self,
                 comm_module_type,
                 module_name,
                 ip_address,
                 bp_slot,
                 major_rev,
                 minor_rev,
                 ekey_state,
                 project_path):
        self.comm_module_type = comm_module_type
        self.ip_address = ip_address
        self.bp_slot = bp_slot
        self.major_rev = major_rev
        self.minor_rev = minor_rev
        self.ekey_state = ekey_state
        self.project_path = project_path
        self.module_name = module_name

    def build_comms_xml(self):
        """Builds XML data for comm modules and writes to file
        """
        path = self.project_path+".L5X"
        xml = ET.parse(path)
        root = xml.getroot()
        modules = root.find("./Controller/Modules")
        new_module = ET.SubElement(modules, 'Module')
        new_module.attrib["Name"] = self.module_name
        new_module.attrib["CatalogNumber"] = self.comm_module_type
        new_module.attrib["Vendor"] = "1"
        new_module.attrib["ProductType"] = "12"
        new_module.attrib["ProductCode"] = "166"
        new_module.attrib["Major"] = self.major_rev
        new_module.attrib["Minor"] = self.minor_rev
        new_module.attrib["ParentModule"] = "Local"
        new_module.attrib["Inhibited"] = "false"
        new_module.attrib["MajorFault"] = "false"
        new_module_ekey = ET.SubElement(new_module, 'EKey')
        new_module_ekey.attrib["State"] = self.ekey_state
        new_module_ports = ET.SubElement(new_module, 'Ports')
        new_module_port_data = ET.SubElement(new_module_ports, 'Port')
        new_module_port_data.attrib["ID"] = "1"
        new_module_port_data.attrib["Address"] = self.bp_slot
        new_module_port_data.attrib["Type"] = "ICP"
        new_module_port_data.attrib["Upstream"] = "true"
        xml.write(path)

def io_build(project_path):
    """simply contains user selection for what module type to add"""
    print("select a type to add, (C)omm module, (I)nput card, (O)utput card.")
    sel = input(">>>")
    if sel.lower() == "c":
        comm_module_data(project_path)
    elif sel.lower() == "i":
        input_card_data(project_path)
    elif sel.lower() == "o":
        output_card_data(project_path)

def comm_module_data(project_path):
    """Gets user input data on a comm module and passes it to the build comms class

    Args:
        project_path (string): path to project as defined in main
    """
    print("Building New Comm Module.")
    comm_module_type = input("Enter module type (ex 1756-EN2T):\n>>>")
    module_name = input("Enter the name of the module:\n>>>")
    ip_address = input("Enter the IP address:\n>>>")
    bp_slot = input("Enter the backplane slot:\n>>>")
    major_rev = input("Enter the major revision:\n>>>")
    minor_rev = input("Enter the minor revision:\n>>>")
    ekey_state = input("Enter the Electronic Keying State:\n>>>")
    comms = BuildComms(comm_module_type,
                       module_name,
                       ip_address,
                       bp_slot,
                       major_rev,
                       minor_rev,
                       ekey_state,
                       project_path)
    comms.build_comms_xml()

def input_card_data(project_path):
    """Will eventually be able to add input cards"""
    pass

def output_card_data(project_path):
    """Will eventually be able to add output cards"""
    pass
