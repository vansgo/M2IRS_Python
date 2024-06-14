from donnees import Pays
from carte import Carte
from carte import MainWindow
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from terminal import Terminal 

def main(application_mode: str ="Terminal"):
    
    match application_mode:
        case "Terminal":
            terminal_instance = Terminal()
            terminal_instance.init()
        case "Interface graphique PyQt":

            pays_instance = Pays()
            list_dict = pays_instance.recup()

            carte_instance = Carte()
            carte_instance = carte_instance.carte_init(list_dict)

            app = QApplication(sys.argv)
            window = MainWindow()
            window.show()
            sys.exit(app.exec_())
        case _:
            "This command is unavailable"
    

#Main guard
if __name__== "__main__" :
    main("Interface graphique PyQt")
