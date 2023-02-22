from tkinter import Tk, Label, Button


class Fenetre: 
    def __init__(self, principal):
        self.principal = principal
        principal.title("Namir Kas Nasrallah - Quiz - Tp1")
        principal.geometry("600x400")


        #bouton 
        self.btn_afficher = Button(principal, 
                                   text="Affichage données",
                                   command=self.affichageData)
        self.btn_afficher.pack()
    
    def affichageData(self):
        print("bajour")
        

root = Tk()
app = Fenetre(root)
root.mainloop()

