class Joueur:

    def __init__(self, nom):

        self.nom = nom
        self.paquet = []

    def jouer_carte(self):

        if self.paquet:
            return self.paquet.pop(0)
        
        return None

    def ajouter_cartes(self, cartes_gagnees):
        
        self.paquet.extend(cartes_gagnees)

