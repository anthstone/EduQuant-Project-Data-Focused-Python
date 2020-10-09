import os

# taken from https://www.tutorialspoint.com/how-to-clear-screen-in-python
def screen_clear():
    if os.name == "posix":
        _ = os.system("clear")
    else:
        _ = os.system("cls")
