"""creates directory for main
"""

import os
from restart import restart

def create_dir(project_name):
    """Creates directory named after project name"""
    while True:
        current = os.getcwd()
        print(f"Current directory is {current}.")
        print("Enter path where project subfolder is created:")
        workdir = input(">>>")
        path = os.path.join(workdir, project_name)
        if workdir == '@restart':
            restart()
        else:
            if os.path.isdir(path) is False:
                try:
                    os.mkdir(path)
                except OSError:
                    print(f"Creation of directory {path} failed. Check Syntax")
                else:
                    print(f"Successfully created new working directory {path}")
                os.chdir(path)
                return path
            else:
                print(f"Path '{path}' already exists. Try again.")
