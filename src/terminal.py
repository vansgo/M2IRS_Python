import sys
import os

from application import Application

class Terminal (Application):

    project_name = "Python Terminal"
    project_version = float(1.0)

    def init(self):
        self.terminal_state = "LOADING"
        self.app_launch()

    def app_launch(self):

        self.terminal_clear_operation()
        print(f"Welcome to the {Terminal.project_name}")

    def app_main_menu(self):
        print("Main menu\n 1) Start Game\n 2) Options\n 3) Quit\n")

    def app_option(self): ...

    def app_quit(self):
        exit()

    def terminal_clear_operation(self):
        if(sys.platform =="win32"):
            os.system('cls')
        elif(sys.platform == "darwin"):
            os.system("clear")
        else:
            os.system('cls')
    