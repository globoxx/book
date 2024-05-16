
# Loris et Lila 1m07

def poser_question(question, choix_possibles):
    reponse = input(question + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + str(choix_possibles))
    return reponse

inventaire = []
argent = 10
argent = True

vie = 20
vie = False

perdu = False
perdu2 = False
perdu3 = False
perdu4 = False


def jeu():
    print("Vous vous réveillez dans une foret. En face de vous vous voyez un homme qui vous demande 10 sous.")
    choix = poser_question("Voulez vous lui les donnez ?", ["oui", "non"])
    if choix == "oui":
        print("Vous lui donnez 10 sous et il vous remercie")
        argent =-10
        argent = False
    elif choix == "non":
        print("Vous ne lui donnez pas 10 sous et il part")
        

    print("Vous vous retrouvez ensuite devant un panneau: Le panneau vous indique deux direction.")
    print("À gauche un ruisseau et à droite un village.")

    choix = poser_question("Vous devez choisir un chemin.", ["village", "ruisseau"])
    if choix == "ruisseau":
        print("Vous vous retrouvez au ruisseau.")
        print("Vous buvez de l'eau,trouvez de la nourriture et vous vous reposez")
        vie =+30
        vie = True
    elif choix == "village":
        print("Vous vous retrouvez dans un village, il semble n'y avoir personne.")
        print("Au loin vous distinguez deux ombres, une grande et une petite.")
        choix = poser_question("Vers la quelle voulez vous aller ?",["petite", "grande",])
        if choix == "petite":
            print("Vous vous retrouvez nez à nez avec un gobelin. Il vous tue sans hésiter.")
            jeu()
        elif choix == "grande":
            print("Vous vous retrouvez nez à nez avec l'homme du début.")
            if argent == False:
                print("En signe de gratitude il vous donne de l'eau, de la nourriture et une epée en or.")
                vie =+50
                vie = True 
                inventaire.append("épée en or")
            elif argent == True:
                print("Puisque vous n'avez pas voulu lui donner de l'argent, il vous frappe et part")
                vie =-10
                vie = False

    print("Après vous être reposé vous continuez votre route et vous tombez sur un chateau.")
    print("Vous y entrez et vous voyez un dragon.")
    choix = poser_question("Voulez vous le combattre ?", ["oui", "non"])
    if choix == "oui":
        if "épée en or" in inventaire:
            print(" Vous le tuez grâce à l'épée que l'homme vous a donné, elle était enfaite magique et vous devenez le nouveau roi de ce chateau.")
            perdu = False
        else:
            print("Vous vous combattez contre lui à main nu, faute de chance vous n'êtes qu'un humain lui un dragon.")
            print("Vous mourrez calcinez")
            perdu = True
            
    elif choix == "non":
        if vie == True:
            print("Vous vous enfuyez heureusement vous êtes extrêmement rapide.")
            print("Pas de chance que le dragon ait des ailes, il vous rattrape et vous tue.")
            perdu = True
        
        elif vie == False:
            print("Vous vous enfuyez, déjà que vous êtes peureux, vous êtes extrêmement lent.")
            print("Le dragon vous vois, vous rattrape et vous tue. Cest ciao")
            perdu = True
            
    if perdu == True:
        print("vous avez perdu")
        
    elif perdu == False:
        print("vous avez gagné")
        
        
jeu()
    
    

        

            
         
