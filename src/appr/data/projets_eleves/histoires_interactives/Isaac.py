def poser_question(question, choix_possibles):
    reponse = input(question + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + str(choix_possibles))
    return reponse



def dragon_ball():
    print("Bienvenue dans le monde de Dragon Ball !!! ")
    print("tu es un sayan")
    Mission_Sayan()
        
        
def Mission_Sayan():
    print("Ta mission est de tuer les Dieux et les humains")
    print("Tu as besoin d'avoir une arme")
    choix = poser_question("allez chercher une arme ou se battre sans arme ?",["oui", "non"] )
    if choix == "oui" :
        arriver_fôret()
    elif choix == "non" :
        rencontres_Dieu()
        

def arriver_fôret():
    choix = poser_question("rentres-tu dans la fôret ?",[ "oui", "non"])
    if choix == "oui" :
        print("rentrez dans la fôret")
        rencontres_Dieu()
    elif choix == "non" :
        print("tu rencontres un humain particulièrement gentil donc tu n'oses pas remplir ta mission soudain, il te propose une épée mais tu dois le protéger")
        choix = poser_question("prendre l'épée ?",[ "oui","non"])
        if choix == "oui" :
            print("lorsque tu prends l'épée tu sens un pouvoir excpetionnel")
            inventaire.append("épée")
            rencontres_Dieu()
        elif choix == "non" :
            rencontres_Dieu()
            
def rencontres_Dieu():
    print(" vous tombez face à face devant un dieu")
    if "épée" in inventaire:
        print("vous utiliser votre arme pour combattre le Dieu")
        rencontres_sayan()
    else:
        print("tu as de la chance, le dieu t'as laissé en vie et t'as emprisonné dans une cellule de son château")
        prisonnier()
        

def rencontres_sayan():
    global vie 
    print("tu as reussi à tuer le dieu. Malheureusement, c'était le plus faible et il t'as grièvement blessé et tu as perdu 75 points de vie sur 100")
    vie = vie - 75
    print("tu rencontres un autre sayen qui te promet de te soigner si tu lui passes ton arme")
    choix = poser_question("passer l'arme ?",["oui","non"])
    if choix == "oui" :
        print("le sayen te soigne et tu reprends les 75 points de vie que tu avais perdu")
        print("tu rencontres un autre Dieu mais tu n'as pas d'arme donc tu meurs")
        print("LOOOOOOOOOSSSSSEEEEEERRRR")
        dragon_ball()
    elif choix == "non" :
        print("tu meurs à cause de ta blessure")
        print("LOOOOOOOOOSSSSSEEEEEERRRR")
        dragon_ball()
        
def prisonnier():
    choix = poser_question("Rester enfermer sans rien faire ?",["oui","non"])
    if choix == "oui" :
        print("Une panique général éclata dans le château à cause d'un sois disant humain avec une arme surpuissante ce qui t'as laissa une opportunité de sortir de ta cellule sans encombrement")
        print("Tu arrives à aller dans la salle du roi des Dieux puis tu mangea une perle qui t'activas tout tes pouvoirs de sayens. Avec ces pouvoirs tu tuent tout les Dieux")
        print("Tu remarques que l'humain qui a mis la pagaille dans le château des Dieux est encore en vie mais il est blessé et va bientôt mourir")
        choix = poser_question("le soigner ?",["oui", "non"])
        if choix == "oui" :
            print("tu meurs car tu as trop utilisé tes pouvoirs alors que tu t'étais jamais entrainé")
            print("parfois la gentillesse mène à sa perte")
            print("LOOOOOOOOOSSSSSEEEEEERRRR")
            dragon_ball()
        elif choix == "non" :
            print("Tu as tué tout les dieux et tu apprends que c'était le dernier Humain en vie")
            print("Tu as réussi ta mission !!!!")
            print("VICTOIIIIIIIIIIIRE !!!")
            
    elif choix == "non" :
        print("tu n'es pas discret et tu te fais tuer")
        print("la prochaine fois reste sans rien faire !")
        print("LOOOOOOOOOSSSSSEEEEEERRRR")
        dragon_ball()
            


        
        
# Début de l'aventure
inventaire = []
vie = 100

print("Ta mère t'as acheté 1 jeu !!")
print("Allume la console et insère le disque")
dragon_ball()

    