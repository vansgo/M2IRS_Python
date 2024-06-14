from donnees import Pays
import folium
from folium import Map
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout,QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from quiz import FlagWindow

#Ajout de 1 marqueur par pays
def ajout_marqueurs(carte_init,data):

    folium.Marker(
    location=[data["latlng"][0], data["latlng"][1]],
    popup=folium.Popup(f"""
        <div style="font-family: Arial, sans-serif; font-size: 14px;">
            <h4 style="margin-bottom: 5px; text-decoration: underline;"><strong>{data["translations"].get("fra", {}).get("common", "N/A")}</strong></h4>
            <p style="margin: 0;"><strong>Capitale:</strong> {data.get("capital", "N/A")[0]}</p>
            <p style="margin: 0;"><strong>Continent:</strong> {data.get("region", "N/A")}</p>
            <p style="margin: 0;"><strong>Superficie:</strong> {data.get("area", "N/A")} m²</p>
            <p style="margin: 0;"><strong>Population:</strong> {data.get("population", "N/A")} habitants </p>
            <strong>Drapeau:</strong>
            <img src="{data["flags"].get("png","N/A")}" alt="Drapeau" style="width: 50px; vertical-align: middle; margin-left: 5px;">
        </div>
    """, max_width=250),
    tooltip=data["translations"].get("fra", {}).get("common", "N/A")
).add_to(carte_init)

class Carte:

    def __init__(self) -> None:
       ...
    
    def carte_init(self,list_pays):
        provider = 'https://tile.jawg.io/jawg-dark/{z}/{x}/{y}{r}.png?access-token=3muP4SP1F7Ms6fBq4n8MvsdsZjTEZ7DkglSktjdW1Dx1epPacPF9i995MDfpOupb'
        attrib = '<a href="https://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; <b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        carte_init = Map(location=[0,0], zoom_start=2, tiles = provider,attr=attrib)

        for pays in list_pays:
            ajout_marqueurs(carte_init,pays)

        carte_init.save("carte1.html")
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application Géographie")

        # Widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)

        # Bouton pour générer la carte
        self.button_generate_map = QPushButton("Voir carte interactive")
        self.button_generate_map.setStyleSheet("font-size: 24px; padding: 20px; background-color: lightblue;")  
        layout.addWidget(self.button_generate_map,alignment=Qt.AlignCenter)
        self.button_generate_map.clicked.connect(self.generate_map)

        # Pour afficher la carte venant d'un fichier HTML
        self.webview = QWebEngineView()
        layout.addWidget(self.webview)

        #Bouton quiz
        self.button_quiz = QPushButton("Quiz Drapeaux")
        self.button_quiz.setStyleSheet("font-size: 24px; padding: 20px; background-color: lightgreen;")
        layout.addWidget(self.button_quiz,alignment=Qt.AlignCenter)
        self.button_quiz.clicked.connect(self.show_flag_window)

        self.resize(800, 600)  
    
    def generate_map(self):
        
        chemin = "C:/Users/vanes/Projet_PythonIRS/carte1.html"
        url = QUrl.fromLocalFile(chemin) 
        self.webview.setUrl(url)
        
        # Cacher le bouton après avoir généré la carte
        self.button_generate_map.setVisible(False)
        self.button_quiz.setVisible(False)

    def show_flag_window(self):
        self.flag_window = FlagWindow()
        self.flag_window.show()


def main():
    ...
    #carte_instance = Carte()
    #carte_instance = carte_instance.carte_init()
  #  app = QApplication(sys.argv)
  #  window = MainWindow()
  #  window.show()
   # sys.exit(app.exec_())
    
#Main guard
if __name__=="__main__":
    main()
