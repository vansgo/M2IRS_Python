import sys
import os
from donnees import recup_data
from donnees import Pays

def affiche_infos_pays (pays):
         print(f"Capitale: {pays["capital"][0]}\nContinent: {pays["region"]}\nSuperficie: {pays["area"]} m²\nPopulation: {pays["population"]} habitants\n" )

def infos_pays(country):
   
    list_pays = recup_data()
    trouve = False
    for pays in list_pays:

        pays_r = pays["translations"]["fra"]["common"].replace("-", " ").lower()
        country_r = country.replace("-", " ").lower()
     
        if pays_r == country_r:
            print(f"Voici les infos sur {country} :")
            affiche_infos_pays(pays)
            trouve = True
            break
    
    if not trouve:
        print("Pays non trouve. Erreur de syntaxe ?")

class Terminal (Pays):
    
    project_name = "Country informations Terminal"
    project_version = float(1.0)

    def init(self):
        self.terminal_state = "LOADING"
        self.app_launch()

    def app_launch(self):

        self.terminal_clear_operation()
        print(f"#############################################\nWelcome to the {Terminal.project_name}\n############################################\n")
        
        country = input("Veuillez écrire un pays : ")
        infos_pays(country)



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
   
