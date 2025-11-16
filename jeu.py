from cartes import creer_paquet
from joueur import Joueur

class Jeu:

    def __init__(self):

        paquet = creer_paquet()

        self.joueur1 = Joueur("Joueur 1")
        self.joueur2 = Joueur("Joueur 2")

        # Distribuer 16 cartes à chaque joueur
        self.joueur1.paquet = paquet[:16]
        self.joueur2.paquet = paquet[16:]

    def comparer_cartes(self, carte1, carte2):

        """Compare deux cartes et renvoie 1 si carte1 gagne, -1 si carte2 gagne, 0 si égalité"""

        ordre = ["7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]

        if ordre.index(carte1.valeur) > ordre.index(carte2.valeur):
            return 1
        
        elif ordre.index(carte1.valeur) < ordre.index(carte2.valeur):
            return -1
        
        else:
            return 0

    def jouer_tour(self):

        """Fait jouer un tour complet"""
        c1 = self.joueur1.jouer_carte()
        c2 = self.joueur2.jouer_carte()

        if c1 and c2:

            print(f"{self.joueur1.nom} joue {c1} VS {self.joueur2.nom} joue {c2}")
            resultat = self.comparer_cartes(c1, c2)

            if resultat == 1:
                self.joueur1.ajouter_cartes([c1, c2])
                print(f"{self.joueur1.nom} gagne ce tour\n")

            elif resultat == -1:
                self.joueur2.ajouter_cartes([c1, c2])
                print(f"{self.joueur2.nom} gagne ce tour\n")

            else:
                print("Égalité ! Les cartes sont perdues\n")

        return self.joueur1.paquet and self.joueur2.paquet

    def jouer(self):

        """Boucle de jeu jusqu'à ce qu'un joueur gagne"""
        tour = 1

        while self.jouer_tour():

            tour += 1

        if self.joueur1.paquet:
            print(f"{self.joueur1.nom} a gagné le jeu en {tour} tours !")
            
        else:
            print(f"{self.joueur2.nom} a gagné le jeu en {tour} tours !")
