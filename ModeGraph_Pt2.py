import tkinter as tk
from tkinter import *
from tkinter import  ttk, Tk
from tkinter import Button, Listbox



class Fenetre: 
    def __init__(self, principal):
        self.principal = principal
        principal.title("Namir Kas Nasrallah - Quiz - Tp1")
        principal.geometry("300x400")


        #bouton 
        self.btn_afficher = Button(principal, 
                                   text="Affichage données",
                                   command=self.affichageData)
        self.btn_afficher.pack(side=BOTTOM)#ajouter dans la fenetre
        

        #comboBox 
        self.dateChoisi = tk.StringVar()
        self.dateCombo = ttk.Combobox(principal, width=22,
                                      textvariable= self.dateChoisi)
    
        self.dateCombo['values'] = ("coco","zozo","toto")
        self.dateCombo['state'] = "readonly"
        self.dateCombo.pack() #ajouter dans la fenetre
        self.dateCombo.bind('<<ComboboxSelected>>',self.onSelect)
        
        #listBox 
        lst_npmJoueur = tk.Listbox(principal,height=3,width=25)
        lst_npmJoueur.insert(1,"Joueur 1")
        lst_npmJoueur.insert(2,"Joueur 2")
        lst_npmJoueur.bind("<<ListBoxSelect>>", self.onSelectlistBox)
        lst_npmJoueur.pack()#ajouter dans la fenetre

        #text
        self.listReponse = tk.Text(principal, width=19, height=10)
        self.listReponse.pack() #ajouter dans la fenetre 

        #Labels 
        #poitage des joueurs 
        self.lbl_poitageJ = Label(principal, text="Poitage du Joueurs: ")
        self.lbl_poitageJ.pack()
        
        #nombre de bonne reponse 
        self.lbl_nbrBonneRep = Label(principal, text="Nombre de bonne reponse: ")
        self.lbl_nbrBonneRep.pack()
    
    def affichageData(self):
        pass
        
    def affichageDate(self):
        pass
    
    def onSelect(self, evt):
        date = self.dateCombo.get()
    
    def onSelectlistBox(self, evt):
        pass  

        

root = Tk()
app = Fenetre(root)
root.mainloop()

