"""creates directory for main
"""

import os

def create_dir():
    current = os.getcwd()
    print(f"Current directory is {current}.")
    print("To create a subfolder in this directory, simply enter the name of the folder. To create a folder elsewhere, enter full path:")
    print("Please enter the working directory:")
    path = input(">>>")
    try:
        os.mkdir(path)
    except OSError:
        print(f"Creation of directory {path} failed. Check Syntax")
    else:
        print(f"Successfully created new working directory {path}")
    os.chdir(path)
