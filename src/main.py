
import os
import sys

from terminal import Terminal 
from panda3D import Panda3DApplication
from app_tkinter import GUIApplication

def main(application_mode: str ="Terminal"):

    match application_mode:
        case "Terminal":
            print("c'est rentré dans terminal")
            terminal_instance = Terminal()
            terminal_instance.init()
        case "Panda 3D":
            panda3d_instance = Panda3DApplication()
            panda3d_instance.run()
        case "Custom Tkinter":
            tkinter_instance = GUIApplication()
            tkinter_instance.mainloop()
        case _:
            "This command is unavailable"

if __name__=="__main__":
    main("Custom Tkinter")