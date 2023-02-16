import random
import json

class Partie:
    def __init__(self,datePartie, nomJoueur1, nomJoueur2, listeReponsesJ1
                 ,listeReponsesJ2, nb_bonnesrepJ1, nb_bonnesrepJ2, pointageJ1
                 ,pointageJ2):
       self.datePartie = datePartie
       self.nomJoueur1 = nomJoueur1
       self.nomJoueur2 = nomJoueur2
       self.listeReponsesJ1 = listeReponsesJ1
       self.listeReponsesJ2 = listeReponsesJ2
       self.nb_bonnesrepJ1 = nb_bonnesrepJ1
       self.nb_bonnesrepJ2 = nb_bonnesrepJ2
       self.pointage1 = pointageJ1
       self.pointage2 = pointageJ2
       
    
    # methode __repr__
    def __repr__ (self):
        return self.datePartie + self.nomJoueur1 +self.nomJoueur2
       
    
    # mthode affiche tous les attributs 
    def afficherPartie(self):
        print("Date: " + self.datePartie)
        print("Joueur 1: " + self.nomJoueur1)
        print("Joueur 2: " + self.nomJoueur2)
        print("Liste de réponse <Joueur 1>: " + self.listeReponsesJ1)
        print("Liste de réponse <Joueur 2>: " + self.listeReponsesJ2)
        print("Nombre de bonne réponse <Joueur 1>: " + self.nb_bonnesrepJ1)
        print("Nombre de bonne réponse <Joueur 2>: " + self.nb_bonnesrepJ2)
           
        


# page de jeu 
def reglementJeu():
    print("|----------------------------------------------------------|")
    print("|      Travail Pratique 1 - Quiz - Namir Kas Nasrallah     |")
    print("|----------------------------------------------------------|")
    print("| Choissisez la bonne réponse pour chaque question (a/b/c) |")
    print("|                    2 joueurs max                         |")
    print("|----------------------------------------------------------|")


reglementJeu()


# nom des joueurs 
nomJ1 = input(" Nom du joueur 1:  ")
while nomJ1 == "":
    print(" ** Non invalide ! **")
    nomJ1 = input(" Nom du joueur 1:  ")

nomJ2 = input(" Nom du joueur 2:  ")
while nomJ2 == "":
    print(" ** Non invalide ! **")
    nomJ2 = input(" Nom du joueur 2:  ")
    


# selection random 
ordre = random.randint(1 , 2)
if ordre == 1:
    joueur1 = nomJ1
    joueur2 = nomJ2
else:
    joueur1 = nomJ2
    joueur2 = nomJ1


print("|----------------------------------------------------------|")
print("|              ordre de réponse aux questions              |")
print("|----------------------------------------------------------|")
print("| 1- " + joueur1)
print("| 2- " + joueur2)
print("|----------------------------------------------------------|")


# lecture dun fichier JSON

with open ("questions.json", encoding='utf-8') as fichier:
    data = json.load(fichier)

cpt = 0
listeReponsesJ1 = []
listeReponsesJ2 = []
nb_bonnesrepJ1 = 0
nb_bonnesrepJ2 = 0
pointageJ1 = 0 
pointageJ2 = 0

#