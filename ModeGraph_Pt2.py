import tkinter as tk
from tkinter import *
from tkinter import  ttk, Tk,Button
import json


class Fenetre: 
    def __init__(self, principal):
        self.principal = principal
        principal.title("Namir Kas Nasrallah - Quiz - Tp1")
        principal.geometry("300x400")


        #bouton 
        self.btn_afficher = Button(principal, 
                                   text="Affichage données",
                                   command=self.affichageDate,
                                   borderwidth= 4,
                                   height=2, width=20)
        self.btn_afficher.pack(side=BOTTOM,)#ajouter dans la fenetre
        

        #comboBox 
        self.dateChoisi = tk.StringVar()
        self.dateCombo = ttk.Combobox(principal, width=25,
                                      textvariable= self.dateChoisi)
        self.dateCombo['values'] = " "
        self.dateCombo['state'] = "readonly"
        self.dateCombo.pack() #ajouter dans la fenetre
        self.dateCombo.bind('<<ComboboxSelected>>',self.onSelectCombo)
        
        #listBox 
        self.lst_npmJoueur = tk.Listbox(principal,height=3,width=25)
        self.lst_npmJoueur.bind("<<ListboxSelect>>", self.onSelectlistBox)
        self.lst_npmJoueur.pack()#ajouter dans la fenetre

        #text
        self.listReponse = tk.Text(principal, width=19, height=10)
        self.listReponse.pack() #ajouter dans la fenetre 

        #Labels 
        #poitage des joueurs 
        self.lbl_poitageJ = Label(principal, text="Poitage du Joueurs: ",background="gray")
        self.lbl_poitageJ.pack()
        
        #nombre de bonne reponse 
        self.lbl_nbrBonneRep = Label(principal, text="Nombre de bonne reponse: ",background="gray")
        self.lbl_nbrBonneRep.pack()
    
        
    def affichageDate(self):
        #click et dois afficher la date 
        print(ListePartie)
        
        for i in ListePartie:
            self.dateCombo['values'] += (i.datePartie,)
        
        my_label = tk.Label(root,text="Date Ajouter !")
        my_label.pack(side=BOTTOM)
        
            
 
    def onSelectCombo(self, evt): 
        #Afficher les 2 joueur de la partie 
        self.lst_npmJoueur.delete(0,1)
        self.lst_npmJoueur.insert(END,ListePartie[self.dateCombo.current()].nomJoueur1)
        self.lst_npmJoueur.insert(END,ListePartie[self.dateCombo.current()].nomJoueur2)
        
            
    def onSelectlistBox(self, evt): 
        self.listReponse.delete("1.0","end")
        joueur1_2 = self.lst_npmJoueur.curselection()[0]
        #TODO Joueur 1
        if joueur1_2 == 0:
            #parcourire le fichie 
            for i in range (len(ListePartie[self.dateCombo.current()].listeReponsesJ1)):
                self.listReponse.insert(END, str(ListePartie[self.dateCombo.current()].listeReponsesJ1[i]))
            #afficher les points 
            self.lbl_poitageJ['text'] = "Poitage du Joueurs: "+str(ListePartie[self.dateCombo.current()].pointageJ1)
            self.lbl_nbrBonneRep['text'] = "Nombre de bonne reponse: "+str(ListePartie[self.dateCombo.current()].nb_bonnesrepJ1)
        #TODO Joueur 2
        else:
            for i in range (len(ListePartie[self.dateCombo.current()].listeReponsesJ2)):
                self.listReponse.insert(END, str(ListePartie[self.dateCombo.current()].listeReponsesJ2[i]))
            #afficher les points 
            self.lbl_poitageJ['text'] = "Poitage du Joueurs: "+str(ListePartie[self.dateCombo.current()].pointageJ2)
            self.lbl_nbrBonneRep['text'] = "Nombre de bonne reponse: "+str(ListePartie[self.dateCombo.current()].nb_bonnesrepJ2)

            

        
               
    
# ======= creation de la class =======
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
        self.pointageJ1 = pointageJ1
        self.pointageJ2 = pointageJ2
       
    
    # methode __repr__
    def __repr__ (self):
        return self.datePartie +" "+self.nomJoueur1 +" "+self.nomJoueur2 + " " +self.listeReponsesJ1 +" "+self.listeReponsesJ2 +" "+ str(self.nb_bonnesrepJ1) + " " + str(self.nb_bonnesrepJ2) + " " + str(self.pointageJ1) + " " +str(self.pointageJ2)
       
    
    # mthode affiche tous les attributs 
    def afficherPartie(self):
        print("Date: " + str(self.datePartie))
        print("Joueur 1: " + self.nomJoueur1)
        print("Joueur 2: " + self.nomJoueur2)
        print("Liste de réponse <Joueur 1>: " + str(self.listeReponsesJ1))
        print("Liste de réponse <Joueur 2>: " + str(self.listeReponsesJ2))
        print("Nombre de bonne réponse <Joueur 1>: " + str(self.nb_bonnesrepJ1))
        print("Nombre de bonne réponse <Joueur 2>: " + str(self.nb_bonnesrepJ2))
        
   
#creation du tableau de partieè
ListePartie = []
with open ("InfoPartie.json", encoding='utf-8') as fichier:
    data = json.load(fichier)
    for valeur in data['resultats']:
        partie = Partie(str(valeur['Date']).replace(" ", "-"), str(valeur['NomJ1']),str(valeur['NomJ2']),
        str(valeur['ListeReponseJ1']),str(valeur['ListeReponseJ2']), str(valeur['nbrBonneRepJ1']),
        str(valeur['nbrBonneRepJ2']),str(valeur['PointageJ1']),str(valeur['PointageJ2']))

        ListePartie.append(partie)

   
root = Tk()
app = Fenetre(root)
root.configure(bg="gray")
root.mainloop()

