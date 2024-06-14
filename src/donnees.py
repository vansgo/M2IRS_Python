import requests
import pandas
import json

def recup_data():
    ...
    url = "https://restcountries.com/v3.1/all"
    requete = requests.get(url) #requete HTTP GET (requete contient le code réponse)

    if requete.status_code != 200:
        print ("Erreur Requete HTTP")
    
    else:
        # Récupération du contenu dans un format JSON
        data = requete.json()
        
        if not data:
            print ("Erreur récuperation au format JSON")
        
        else:

            # Contenu JSON copié dans un fichier
            fileJSON = open("data_monde.json","w", encoding="utf-8")
            json.dump(data, fileJSON, ensure_ascii=False, indent=4)
            fileJSON.close()

            # Contenu du fichier = liste de dictionnaires
            # On met ce contenu dans la variable data_dict
            with open("data_monde.json","r", encoding="utf-8") as fileJSON:
                data_dict = json.load(fileJSON)

    return data_dict  
            

class Pays:

    def __init__(self) -> None:
        ...

    def recup(self):
        return recup_data()

    #data correspond à un pays = un dictionnaire
    def creer_un_pays (self,data):
        self.nom = data["name"]["common"]
        self.continent = data["region"]

    def affiche_pays (self):
         print(f"Nom: {self.nom}\nContinent:{self.continent}\n")
    

