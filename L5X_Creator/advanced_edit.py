"""contains the advanced functions of the editor after creating a base file"""

import sys
from modules import io_build
from tags import tag_build

def advanced_menu(path):
    sel = input("Add (I)O, (T)ags, (P)rogram, t(A)sks, or (Q)uit.\n>>>")
    if sel.lower() == 'q':
        sys.exit()
    elif sel.lower() == 'i':
        io_build(path)
    elif sel.lower() == 't':
        tag_build(path)
    # elif sel.lower() == 'p':
    #     program_build(path)
    # elif sel.lower() == 'a':
    #     task_build(path)
