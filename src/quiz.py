from random import randint
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox,  QLineEdit, QHBoxLayout
from PyQt5.QtGui import QPixmap
import requests
from io import BytesIO
from PyQt5.QtCore import Qt
from donnees import recup_data

# Vérifie si le pays donné par le user est valide
def check_reponse(pays, reponse_user):
    user = reponse_user.replace("-", " ").lower()
    pays_r = pays["translations"]["fra"]["common"].replace("-", " ").lower() 

    if pays_r == user:
        return 1
    else:
        return 0

class FlagWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quiz Drapeau")
        self.msg_box = QMessageBox()

        self.indice_pays = 0
        self.score = 0
        self.valide = 1
        self.list_pays = recup_data()

        # Créez un label et chargez une image
        self.label = QLabel(self)
        

        self.label.setAlignment(Qt.AlignCenter)

        # Barre de saisie
        self.input_line = QLineEdit(self)
        self.input_line.setPlaceholderText("Tapez un mot ici")
        self.input_line.setStyleSheet("QLineEdit { height: 50px; font-size: 20px; }")
        
        # Bouton valider pour récupérer le mot saisi
        get_text_button = QPushButton("Valider", self)
        get_text_button.clicked.connect(self.display_reponse)
        get_text_button.setStyleSheet("QPushButton { height: 60px; font-size: 16px; }")

        # Bouton quitter pour afficher le score et fermer la fenetre
        quit_button = QPushButton("Quitter", self)
        quit_button.clicked.connect(self.score_and_close)
        quit_button.setStyleSheet("QPushButton { height: 60px; font-size: 16px; }")

        # Layout horizontal 
        h_input_layout = QHBoxLayout()
        h_input_layout.addWidget(self.input_line)
        h_input_layout.addWidget(get_text_button)

        # Layout vertical
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addStretch()
        h_layout.addWidget(self.label)
        h_layout.addStretch()

        v_layout.addStretch()
        v_layout.addLayout(h_layout)
        v_layout.addStretch()

        v_layout.addLayout(h_input_layout)
        v_layout.addWidget(quit_button)  # Ajout du bouton Quitter en bas


        v_layout.addWidget(self.input_line)

        self.setLayout(v_layout)

        self.resize(800, 600)

        #Affichage d'un premier drapeau
        url_drapeau = self.list_pays[self.indice_pays]["flags"]["png"]
        response = requests.get(url_drapeau)
        image_data = BytesIO(response.content)
        pixmap = QPixmap()
        pixmap.loadFromData(image_data.read())

        if pixmap.isNull():
            QMessageBox.critical(self, "Erreur", "L'image n'a pas pu être chargée. Vérifiez le chemin de l'image.")
        else:
            self.label.setPixmap(pixmap)
            self.input_line.clear() 

        

    def display_reponse(self):
        # Récupérer le texte de la barre de saisie
        user_text = self.input_line.text()
        self.valide = check_reponse(self.list_pays[self.indice_pays],user_text)

        #Si l'utilisateur a deviné le bon pays
        if self.valide:
            self.msg_box.setWindowTitle("Conclusion")
            self.msg_box.setText("Bonne réponse")
            self.score +=1
            self.msg_box.buttonClicked.connect(self.on_msg_box_button_clicked)
            self.msg_box.exec_()
        
        else:
            self.msg_box.setWindowTitle("Conclusion")
            self.msg_box.setText("Mauvaise réponse")
            self.msg_box.buttonClicked.connect(self.on_msg_box_button_clicked)
            self.msg_box.exec_()

    def on_msg_box_button_clicked(self):
        self.msg_box.buttonClicked.disconnect(self.on_msg_box_button_clicked)
        self.indice_pays = (self.indice_pays + 1) % len(self.list_pays)
        self.load_flag()

    def load_flag(self):
        
        url_drapeau = self.list_pays[self.indice_pays]["flags"]["png"]
        response = requests.get(url_drapeau)
        image_data = BytesIO(response.content)
        pixmap = QPixmap()
        pixmap.loadFromData(image_data.read())

        if pixmap.isNull():
            QMessageBox.critical(self, "Erreur", "L'image n'a pas pu être chargée. Vérifiez le chemin de l'image.")
        else:
            self.label.setPixmap(pixmap)
            self.input_line.clear() 
            
    def score_and_close(self):
        score_message = f"Votre score final est : {self.score}"
        QMessageBox.information(self, "Score Final", score_message)
        self.close()