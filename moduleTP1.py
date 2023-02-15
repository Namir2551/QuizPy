

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
nomJ1 = input("Nom du joueur 1:  ")
while nomJ1 == "":
    print("Non invalide !")
    nomJ1 = input("Nom du joueur 1:  ")

nomJ2 = input("Nom du joueur 2:  ")
while nomJ2 == "":
    print("Non invalide !")
    nomJ2 = input("Nom du joueur 2:  ")
    
ListeJoueur = list([nomJ1, nomJ2])

# selection random 



