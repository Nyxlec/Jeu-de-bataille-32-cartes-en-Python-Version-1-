import random

class Carte:

    def __init__(self, valeur, couleur):

        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):

        return f"{self.valeur} de {self.couleur}"

def creer_paquet():

    valeurs = ["7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
    couleurs = ["Pique", "Coeur", "Carreau", "Trèfle"]

    paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
    
    random.shuffle(paquet)
    return paquet

