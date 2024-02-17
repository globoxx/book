#site utilise pour apprendre a utiliser tkinter:
#https://stackoverflow.com/
#https://www.pythontutorial.net/tkinter/
#https://docs.python.org/3/library/tkinter.html

from msilib.schema import CheckBox
from tkinter import *
from random import *

def charPossible(maj, nombre, charSpeciaux, charAmbigu):#genere tous les characteres possibles du mot de passe dans une liste avec les conditions données par les checkboxs
    charPossible = []
    for i in range(97, 123):
        if charAmbigu == False or i != 108: #enlève le l miniscule si charAmbigu est true
            charPossible.append(chr(i)) #la fonction chr() transforme un int en charactere ascii
    if maj == True:
        for i in range(65, 91):
            if charAmbigu == False or (i != 73 and i != 79): #enlève le o et le i majuscule si charAmbigu est true
                charPossible.append(chr(i))
    if nombre == True:
        for i in range(48, 58):
            if charAmbigu == False or i != 48: #enlève le 0 si charAmbigu est true
                charPossible.append(chr(i))
    if charSpeciaux == True:
        for i in range(33, 48):
            charPossible.append(chr(i))
        for i in range(58, 65):
            charPossible.append(chr(i))
        for i in range(91, 97):
            charPossible.append(chr(i))
        for i in range(123, 127):
            charPossible.append(chr(i))
    return charPossible

def motDePasse(longueur, maj, nombre, charSpeciaux, charAmbigu, longueurPossible): #creer le mot de passe a partir de la liste des characteres
    if longueur <= 25 and longueurPossible == True: #la longueur est arbitraire, on pourrait mettre quelque chose de bien plus elevee
        char = charPossible(maj, nombre, charSpeciaux, charAmbigu)
        password = ""
        for i in range(longueur):
            password = password + char.pop(randint(0, len(char)-1)) #len(char) - 1 car la list commence a l'element 0 jusqu'a len(char) - 1 
        return password
    else:
        return ""

def generation(longueur, maj, nombre, charSpeciaux, charAmbigu, longueurPossible): #fait pareille que modDePasse() mais s'active avec la pression du bouton generer et met le resultat dans la zone copyable sur le GUI 
    if longueurPossible == True:    
        resultatVar.set(motDePasse(int(longueur), maj, nombre, charSpeciaux, charAmbigu, longueurPossible))
        
def longueurCheck(x):   #regarde si il y a des lettres dans la longueur return True si ce n'est paa le cas
    str(x)
    longueurPossible = True
    for i in x:
        if str.isdigit(i) == False:
            longueurPossible = False
    return longueurPossible
    

#declaration variable tkinter + fenêtre
root = Tk()
root.title("generateur")
resultatVar=StringVar()
resultatVar.set("")
longueurVar = StringVar()
longueurVar.set(16) #valeur de base de longueur
majVar = BooleanVar()
majVar.set(1) #valeur de base des booleans (True)
numberVar = BooleanVar()
numberVar.set(1)
charSpeciauxVar = BooleanVar()
charSpeciauxVar.set(1)
charAmbiguVar = BooleanVar()
charAmbiguVar.set(1)

#creation des objets dans la fenêtre tkinter + la geometrie et le mainloop
result = Entry(root, state="readonly", textvariable=resultatVar, width=30) #zone de resultat, l'affichage du resultat s'inspire de https://www.daniweb.com/programming/software-development/threads/316754/selectable-label-with-tkinter
result.grid(row=0, column=0, columnspan=2, pady=20, sticky=N)

longueurLabel = Label(root, text="longueur (max 25)")
longueurLabel.grid(row=1, column=0, sticky=W)

longueurEntrybox = Entry(root, width=3, textvariable=longueurVar) #entree de la longueur
longueurEntrybox.grid(row=1,column=1, sticky=E)

majLabel=Label(root, text="inclus majuscule")
majLabel.grid(row=2,column=0, sticky=W)

majCheckBox = Checkbutton(root, variable=majVar) #checkbox majuscule
majCheckBox.grid(row=2, column=1, sticky=E)

numberLabel = Label(root, text="inclus nombre")
numberLabel.grid(row=3,column=0, sticky=W)

numberCheckBox = Checkbutton(root,variable=numberVar) #checkbox nombre
numberCheckBox.grid(row=3, column=1, sticky=E)

charSpeciauxLabel = Label(root, text="inclus characteres speciaux")
charSpeciauxLabel.grid(row=4,column=0, sticky=W)

charSpeciauxCheckBox = Checkbutton(root, variable=charSpeciauxVar) #checkbox characteres speciaux
charSpeciauxCheckBox.grid(row=4, column=1, sticky=E)

charAmbiguLabel = Label(root, text="supprime charactere ambigu (l, I, 0, O)") 
charAmbiguLabel.grid(row=5,column=0, sticky=W)

charAmbiguCheckBox = Checkbutton(root, variable=charAmbiguVar) #checkbox characteres ambigus
charAmbiguCheckBox.grid(row=5, column=1, sticky=E)

#bouton de generation qui utilise les fonctions plus haut
genererButton = Button(root,text="generer", command= lambda: generation(longueurVar.get(), majVar.get(), numberVar.get(), charSpeciauxVar.get(), charAmbiguVar.get(), longueurCheck(longueurVar.get())))
genererButton.grid(row=6, column=0, columnspan=2)

quitButton = Button(root, text="quitter",command=quit) #bouton pour quitter
quitButton.grid(row=7, column=0, columnspan=2)

root.resizable(False, False)    #root n'est plus agrandissable en x et en y (https://stackoverflow.com/questions/37446710/how-to-make-a-tkinter-window-not-resizable)
root.geometry("270x300")
root.mainloop()