# Jeu de bataille 32 cartes en Python ♠️♣️♥️♦️


Petit projet Python qui simule le classique jeu de bataille avec 32 cartes (7 à As). 

Deux joueurs s’affrontent en comparant leurs cartes à chaque tour jusqu’à ce qu’un joueur ait toutes les cartes.


# 📝 Description du projet

- **32 cartes** : 7, 8, 9, 10, Valet, Dame, Roi, As (4 couleurs)  
- **Deux joueurs** qui s’affrontent à chaque tour  
- **Programmation orientée objet (POO)** : classes `Carte`, `Joueur` et `Jeu`  
- **Structure multi-fichiers** : chaque classe dans un fichier séparé  
- **Objectif pédagogique** : pratique de Python, POO et organisation d’un projet multi-fichiers



# 📂 Structure du projet

**bataille/**
-  main.py # Lance le jeu
-  cartes.py # Classe Carte et création du paquet
-  joueur.py # Classe Joueur
- jeu.py # Logique du jeu
-  README.md # Ce fichier

# 🚨 Infos 

Le jeu peut parfois tourner très longtemps, voire presque indéfiniment.

 **Fichier à modifier :**

- Fichier : **jeu.py**
- Fonction : **jouer(self)**
- Lignes à modifier : remplacer la boucle while self.jouer_tour(): par une version avec limite de tours .

#  🚩Améliorations pour Version 2 (en préparation)

1. Gestion complète des égalités comme dans le vrai jeu 
2. Interface graphique avec tkinter ou pygame
3. Mode joueur contre ordinateur
4. Statistiques du jeu (nombre de tours, cartes jouées, cartes gagnées)

# 🪧Crédit

Projet open-source pour apprentissage personnel.
Vous pouvez utiliser et modifier ce projet pour vos propres expériences.

Lecomte Dorian 
