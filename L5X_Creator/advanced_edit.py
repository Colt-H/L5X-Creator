"""contains the advanced functions of the editor after creating a base file"""

import sys
from modules import io_build
from tags import tag_build
from programs import prog_build

def advanced_menu(path):
    """Simple Menu for advanced editing

    Parameters
    ----------
    path : path to project
        [description]
    """
    sel = input("Add (I)O, (T)ags, (P)rogram, t(A)sks, or (Q)uit.\n>>>")
    if sel.lower() == 'q':
        sys.exit()
    elif sel.lower() == 'i':
        io_build(path)
    elif sel.lower() == 't':
        tag_build(path)
    elif sel.lower() == 'p':
        prog_build(path)
    # elif sel.lower() == 'a':
    #     task_build(path)
