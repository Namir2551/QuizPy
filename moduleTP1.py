import random
import json
import datetime
import codecs
import os.path

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
        print("Date: " + str(self.datePartie))
        print("Joueur 1: " + self.nomJoueur1)
        print("Joueur 2: " + self.nomJoueur2)
        print("Liste de réponse <Joueur 1>: " + str(self.listeReponsesJ1))
        print("Liste de réponse <Joueur 2>: " + str(self.listeReponsesJ2))
        print("Nombre de bonne réponse <Joueur 1>: " + str(self.nb_bonnesrepJ1))
        print("Nombre de bonne réponse <Joueur 2>: " + str(self.nb_bonnesrepJ2))
           
        


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


# parcour json 
for key in data:
    cpt+=1 #compteur s
    print(cpt,")",key['q'])
    print("<a>", key['a'])
    print("<b>", key['b'])
    print("<c>", key['c'])
    
    
    print()
    if cpt%2 != 0: #Joueur 1 selon la selection
        question = input(joueur1+", Entrez votre reponse (a/b/c): ")
        while question != 'a' and question != 'b' and question != 'c':
            print(" ** Choix invalide ** ")
            question = input(joueur1+", Entrez votre reponse (a/b/c): ")
        #reponse 
        listeReponsesJ1.append(key[question])
        if question == key['rep']:
            print("Bonne reponse!")
            nb_bonnesrepJ1 +=1 # ajoue des nbr de bonnes reponses 
            pointageJ1 +=key['pts'] # ajoue des pts 
            #listeReponsesJ1.append(key[question]) #ajoue dans la liste les bonnes reponses 
            
        
        else:
            
            replique = input("Mauvaise reponse, réplique à " + joueur2 + " entrez votre réponse (a/b/c): ")
            while replique != 'a' and replique != 'b' and replique != 'c':
                print(" ** Choix invalide ** ")
                replique = input("Mauvaise reponse, réplique à " + joueur2 + " entrez votre réponse (a/b/c): ")
            listeReponsesJ2.append(key[question])
            if replique == key['rep']:
                print("Bonne réponse !")
                #point + joueur2
                nb_bonnesrepJ2 +=1
                pointageJ2 +=key['pts'] # ajoue des pts
                #listeReponsesJ2.append(key[question])
            else:
                print("Mauvaise réponse :(")
                print("La bonne reponse été: <", key['rep'],">")
                

    if cpt%2 == 0: #Joueur 2 selon la selection
        question = input(joueur2+", Entrez votre reponse (a/b/c)")
        while question != 'a' and question != 'b' and question != 'c':
            print(" ** Choix invalide ** ")
            question = input(joueur2+", Entrez votre reponse (a/b/c)")
        #reponse
        listeReponsesJ2.append(key[question])
        if question == key['rep']:
            print("Bonne reponse!")
            # point + 
            nb_bonnesrepJ2 +=1
            pointageJ2 +=key['pts'] # ajoue des pts
            #listeReponsesJ2.append(key[question])
            
        else:
            replique = input("Mauvaise reponse, réplique à " + joueur1 + " entrez votre réponse (a/b/c): ")
            while replique != 'a' and replique != 'b' and replique != 'c':
                print(" ** Choix invalide ** ")
                replique = input("Mauvaise reponse, réplique à " + joueur1 + " entrez votre réponse (a/b/c): ")
            listeReponsesJ1.append(key[question])
            if replique == key['rep']:
                print("Bonne réponse !")
                #point + joueur2
                nb_bonnesrepJ1 +=1
                pointageJ1 +=key['pts']
                #listeReponsesJ1.append(key[question])
            else:
                print("Mauvaise réponse :(")
                print("La bonne reponse été: <", key['rep'],">")
                
#creation objet 
partie = Partie(str(datetime.datetime.today()),joueur1,joueur2,listeReponsesJ1,listeReponsesJ2
                ,nb_bonnesrepJ1,nb_bonnesrepJ2, pointageJ1,pointageJ2)

print("=====================================")
#Affichage 
print(joueur1)
print("Les points: ", pointageJ1)
print("Le nombre de bonne réponse: " , nb_bonnesrepJ1)
print()
print(joueur2)
print("Les points: ", pointageJ2)
print("Le nombre de bonne réponse: " , nb_bonnesrepJ2)
print("====================================")

#Donnes a mettre dans json 
partie_data = {
                "Date":partie.datePartie,
                "NomJ1": partie.nomJoueur1,
                "ListeReponseJ1": partie.listeReponsesJ1,
                "nbrBonneRepJ1":partie.nb_bonnesrepJ1,
                "PointageJ1":partie.pointage1,
                "NomJ2":partie.nomJoueur2,
                "ListeReponseJ2":partie.listeReponsesJ2,
                "nbrBonneRepJ2":partie.nb_bonnesrepJ2,
                "PointageJ2": partie.pointage2
                }

#json writing

 # si le fichier existe 
if os.path.exists("InfoPartie.json"):
    print()
    print("====================================")
    with open("InfoPartie.json",encoding='utf-8') as fichier_json:#lire 
        data2 = json.load(fichier_json)
        taille = len(data2["resultats"])
            
    with codecs.open("InfoPartie.json", "a", encoding='utf-8') as InfoPartie:
        InfoPartie.seek(-4,2) #le curseur 
        InfoPartie.truncate()
        if taille >= 1:
            InfoPartie.write(",")
        #ajouter les informations dans le fichier json 
        json.dump(partie_data, InfoPartie, ensure_ascii=False, indent=4, sort_keys=True)
        InfoPartie.write("\n    ]")
        InfoPartie.write("\n}")   
    print("Les données JSON sont enregistrées !!") 
    print() 
          
#Si non message d'erreur
else:
    print()
    print("==================  ATTENTION  ==================")
    print("=    Fichier non disponible création en cours.. =")
    with open("InfoPartie.json","w") as fichierJson:
        fichierJson.write('{')
        fichierJson.write('\n   "resultats":[')
        json.dump(partie_data,fichierJson, ensure_ascii=False, indent=4, sort_keys=True)
        fichierJson.write('\n     ]')
        fichierJson.write('\n}')
    print("=    Fichier JSON creer !!    =")
    print()

