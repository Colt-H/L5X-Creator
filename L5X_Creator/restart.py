"""whatever code is required to return to main"""

def restart():
    """Will eventually delete folder and all that"""
    print("Are you sure you want to restart? (Y/N)")
    sel = input(">>>")
    if sel == "Yes" or sel == "Y" or sel == "y":
        return
    else:
        pass
