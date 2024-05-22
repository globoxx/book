inventaire = []
gold = 0

def poser_question(question, choix_possibles):
    reponse = input(question + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + str(choix_possibles))
    return reponse

def porte_chambre():
    print("Vous rentrez dans votre chambre et vous reposez de cette aventure.")
    print("Victoire!")
    exit("Vitoire")

def porte_grise():
    if "clé chambre" in inventaire:
        print("Il n'y a plus rien à faire ici.")
        print("Vous rentrez dans la salle des portes.")
    else:
        print("Vous entrez dans un  brouillard qui vous entoure.")
        choix = poser_question("mettre les lunettes ?",["oui","non"])
        if choix == "oui":
            print("Vous vous enfoncez dans le brouillard et grâce aux lunettes vous pouvez discerner des formes.")
            print("Vous êtes à côté d'un pommier, mais les pommes sont trop hautes.")
            choix = poser_question("Tirer une flèche pour avoir une pomme?",["oui","non"])
            if choix == "oui":
                print("Vous tirez sur une pomme, mais vous la ratez et faites tomber la clé de votre chambre.")
                inventaire.append("clé chambre")
                print(inventaire)
                print("Vous rentrez dans la salle des portes.")
            elif choix == "non":
                print("Vous rentrez dans la salle des portes.")     
        elif choix == "non":
            print("Vous vous perdez et tombez dans un ravin.")
            print("Game Over")
            exit("Game Over")
        
def porte_rouge(money):
    if "lunette" in inventaire:
        print("Il n'y a plus rien à faire ici.")
        print("Vous rentrez dans la salle des portes.")
    
    else:
        print("Vous entrez dans un monde de feu, il y a des cascades de lave partout. Au milieu se trouve une elfe rouge.")
        choix = poser_question("Lui donner la bague?",["oui","non"])
        if choix == "oui":
            inventaire.remove("bague")
            print("Elle vous remercie et vous donne ses lunettes infrarouge et un billet.")
            inventaire.append("lunette")
            print(inventaire)
            money += 50
            print("gold =", money)
        
        elif choix == "non":
            print("Vous rentrez dans la salle des portes.")
    return money

def porte_verte():
    print("Vous entrez dans un village elfique caché dans la forêt.")
    print("Il y a un forgeron et un soldat.")
    forgeron_ou_soldat(gold)
    
def forgeron_ou_soldat(gold):
    choix = poser_question("Parler au forgeron ou au soldat?",["forgeron","soldat"])
    if choix == "forgeron":
        print("gold =", gold)
        if "clé grise" in inventaire:
            print("Il n'y a plus rien à faire avec le forgeron.")
            print("Vous rentrez dans la salle des portes.")
            
        elif gold == 0:
            print("*snif snif* Votre odeur n'est guère attirante. Ouste! Vous faites partir les clients!")
            print("Un peu d'argent et nous pourrons parler...")
            print("gold =", gold)
            forgeron_ou_soldat(gold)
        else:
            if gold == 50:
                print("Entrez vite! Entrez vite! Votre commande est arrivée. Maintenant je vous prends les 50 et vous cette clé d'argent. Au revoir!")
                gold -= 50
                print("gold =", gold)
                inventaire.append("clé grise")
                print(inventaire)
                print("Vous rentrez dans la salle des portes.")
                    
    elif choix == "soldat":
        if "arc" in inventaire:
            print("Il n'y a plus rien à faire avec le soldat.")
            print("Vous rentrez dans la salle des portes.")

        else:
            print("IL vous dit que sa femme est dans le royaume de lave, mais il n'a pas le courage de lui parler.")
            print("Il vous confie sa clé rouge et vopus demande de donner la bague qu'il vous passe à sa bien-aimée et en comptant sur vous il vous donne son arc.")
            inventaire.append("clé rouge")
            inventaire.append("bague")
            inventaire.append("arc")
            print(inventaire)
            print("Vous le remeriez et partez.")
            
def porte_bleue():
    if "clé verte" in inventaire:
        print("Il n'y a plus rien à faire ici.")
        print("Vous rentrez dans la salle des portes.")

    else:
        print("Vous entrez dans un dôme qui est sous l'eau.")
        print("Devant vous il y a trois fioles d'eau.")
        choix = poser_question("Voulez-vous boire?",["boire","laisser"])
        if choix == "boire":
            choix = poser_question("Boire celle de gauche, droite ou du milieu?",["gauche","milieu","droite"])
            if choix == "gauche" or "droite" or "milieu":
                print("Vous avez bu.")
                inventaire.append ("eau")
                print(inventaire)
                gens_d_eau()
        else:
            choix == "laisser"
            gens_d_eau()
            
def gens_d_eau():
    print("Des gens d'eau entrent dans la salle.")
    if "eau" in inventaire:
        print("Les fioles étaient les souverains de la cité et les êtres d'eau vous tuent.")
        print("game over")
        exit("Game Over")
        
    else:
        print("Ils vous remercient d'avoir surveillé leurs rois et vous offre une clé verte.")
        inventaire.append("clé verte")
        print(inventaire)
        print("Vous rentrez dans la salle des portes.")

def sortie_de_la_chambre():
    print("Vous sortez de votre chambre et arrivez dans une salle remplie de pièces et  la porte de votre chambre se claque derrière vous.")
    print("Il y a cinq portes.")
    
def centre_portes():
    global gold
    choix = poser_question("Ouvrir la porte bleue, grise, rouge, verte ou celle de votre chambre?",["bleue","grise","rouge","verte","chambre"])
    if choix == "bleue":
        porte_bleue()
        
    elif choix == "verte":
        if "clé verte" in inventaire:
            porte_verte()
            
        else:
            print("Vous n'avez pas la clé verte.")
            print("Vous rentrez dans la salle des portes.")
            
    elif choix == "rouge":
        if "clé rouge" in inventaire:
            gold = porte_rouge(gold)
            
        else:
            print("Vous n'avez pas la clé rouge.")
            print("Vous rentrez dans la salle des portes.")
            
    elif choix == "grise":
        if "clé grise" in inventaire:
            porte_grise()
            
        else:
            print("Vous n'avez pas la clé grise.")
            print("Vous rentrez dans la salle des portes.")          
    else:
        choix == "chambre"
        if "clé chambre" in inventaire:
            porte_chambre()
            
        else:
            print("Vous n'avez pas la clé de votre chambre, il va visiblement falloir explorer la zone.")
            print("Vous rentrez dans la salle des portes.")
    centre_portes()    
    
sortie_de_la_chambre()
centre_portes()