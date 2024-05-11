
def poser_question(question, choix_possibles):
    reponse = input(question + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + str(choix_possibles))
    return reponse

sanity = 80
inventaire = [] 
perdu = False

def reve():
    print("Vous marchez tranquillement dans la rue...")
    print("Une petite ruelle apparaît sur votre gauche.")
    choix = poser_question("Voulez vous continuer votre chemin ou prendre la ruelle ?", ["ruelle", "chemin"])
    if choix == "ruelle":
        ruelle()
    elif choix == "chemin":
        chemin()
    
def ruelle():
    print("Vous voyez une fenêtre ouverte, le mal-aise s'installent plus vous regardez à travers")
    choix = poser_question("Voulez vous rentrer par la fenêtre ?", ["oui", "non"])
    if choix == "oui":
        entrer_par_la_fenetre()
    elif choix == "non":
        print(" ")
        print("Vous continuez à marcher jusqu'à ce que le vᶤɖ€ vous tombe dessus.")
        print("Vous avez perdu.")
        perdu = True
        
def chemin():
    print("Vous continuez votre chemin, en ayant l'impression que quelque chose vous suit.")
    global sanity # Comme ça, Python se réfère à la variable globale et non locale de la fonction.
    sanity = sanity - 15
    print(sanity)
    print("Votre niveau de Sanité est descendu...")
    choix = poser_question("Cette impression n'arrête pas d'augmenter, Vous penser à trois choses...", ["vous retourner", "continuer votre chemin", "partir en courant"])
    if choix == "vous retourner":
        ruelle()
    elif choix == "continuer votre chemin":
        banc()
    elif choix == "partir en courant":
        print(" ")
        print("Vous vous êtes faits chopés par « Lui ».")
        print("Vous avez perdu.")
        perdu = True
        
def banc():
    print("Vous voyez un banc") 
    choix = poser_question("Voulez-vous vous assoire ? ", ["oui", "non"])
    if choix == "oui":
        print("Vous vous sentez plus calme.")
        global sanity
        sanity = sanity + 25
        print(sanity)
        print("Votre niveau de Sanité a augmenté..!")
        choix = poser_question("Voulez-vous rester plus longtemps ? ", ["oui", "non"])
        if choix == "oui":
            print("Vous ne sentez plus rien et vos yeux se ferment...")
            if sanity >= 100:
                print(" ")
                reveil()
            else : 
                print(" ")
                print("Vous ne vous reveillerez  plus.")
                print("Le vᶤɖ€ vous a rattrapé.")
                print("Vous avez perdu.")
                perdu = True
                    
        elif choix == "non":
                print("Vous remarquez une boîte. Vous vous sentez angoissé.")
                print("Le vᶤɖ€ vous rattrape.")
                choix = poser_question("Voulez-vous vous la prendre ? ", ["oui", "non"])
                if choix == "oui":
                    print("Vous partez en courant avec la boite.")
                    inventaire.append("boîte de musique")
                    print("Malgré le stress, vous ne perdez pas votre sang froid et vous commencez à marcher.")
                    ruelle()
                elif choix == "non":
                    print("Vous partez en courant.")
                    print("Malgré le stress, vous ne perdez pas votre sang froid et vous commencez à marcher.")
                    ruelle()
    
    elif choix == "non":
        print(" ")
        print("Vous continuez à marcher jusqu'à ce que le vᶤɖ€ vous tombe dessus.")
        print("Vous avez perdu.")
        perdu = True 
    
def entrer_par_la_fenetre():  
    print("Le manque de son vous perturbe.")
    global sanity 
    sanity = sanity - 40
    print(sanity)
    print("Votre niveau de Sanité est descendu...")
    print("Avez-vous une boîte de musique ?")
    if 'boîte de musique' in inventaire:
        print("օʊɨ")
        print("Tout d'un coup, une musique commence à jouer. C'était la boîte de musique.")
        print("Vous vous sentez mieux et, du coin de l'œil, vous voyez un attrape-rêve sur une des tables.")
        choix = poser_question("Voulez vous le prendre ?", ["oui", "non"])
        if choix == "oui":
            print("Vous avez pris le attrape rêve, vous vous sentez mieux et vous décidez de sortir.")
            inventaire.append("attrape rêve")
            sanity = sanity + 35
            print(sanity)
            print("Votre niveau de Sanité a augmenté..!")
            banc()
        elif choix == "non":
            print("Vous le prenez pas et vous sortez de cet endroit gloque...")
            sanity = sanity + 35
            print(sanity)
            print("Votre niveau de Sanité a augmenté..!")
            banc()
        
    else:
        print(" ")
        print("Le silence vous fait perdre votre touche à la réalité.")
        print("Le vᶤɖ€ vous a rattrapé.")
        print("Vous avez perdu.")
        perdu = True
                    
def reveil():
    print("Vous vous réveiller sur votre lit, vous commencez à avoir la nausée")
    print(" ")
    print("Avez-vous un attrape rêve ?")
    global inventaire
    if 'attrape rêve' in inventaire:
        print("օʊɨ")
        print(" ")
        print("Vous reglez votre respiration et vous vous sentez beaucoup mieux.")
        print("Il est 6h 45 du matin et vous entendez votre coloc tocquer sur la porte.")
        choix = poser_question("Vous lui répondez « 5 minutes ! » ?", ["oui", "non"])
        if choix == "oui":
            print(" ")
            print("vous vous rendormez en regardant le vide dans ta chambre...")
            print(" ")
            print("Ɩɛ ɾê۷ɛ ɾɛƈơɱɱɛŋƈɛ.")
            sanity = 80 
            inventaire = [] 
            reve()
        elif choix == "non":
            print("Vous vous levez et vous allez rejoindre votre ami. Laissant le vide derrière vous.")
            print("Vous avez gagné. Ne pensez plus au vide.")
            print(" ")
            print("Fin du jeu.")
    else:
        print("ñ̶̢̘͙̗̹̪̫̤̤̘̆̑̄͘ȏ̶͔̭͕͙̒ń̶̗̯̬͎͈̲̘̮̱̈́̓̿͐͜͡") 
        print(" ")
        print("Vous tombez dans les pommes.")
        print(" ")
        ruelle()

#Début du jeux.


print("Votre Sanity est égal à 80...")
print(" ")

reve()