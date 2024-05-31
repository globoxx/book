def poser_question(question, choix_possibles):
    reponse = input(question + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + str(choix_possibles))
    return reponse



inventaire = []
pièces = 0



    
def grotte():
    print("Vous êtes dans une grotte")
    choix = poser_question("Prendre le chemin de droite ou le chemin de gauche?",["gauche", "droite"])
    if choix == "gauche":
        arriver_clairiere()
    elif choix == "droite":
        arriver_foret()
    
def arriver_clairiere():
    print("Vous arrivez dans une clairière.")
    choix = poser_question("Continuez votre chemin ou faire une sieste ?", ["continuer mon chemin", "faire une sieste"])
    if choix == "continuer mon chemin":
        grotte()
    elif choix == "faire une sieste":
        print("Vous mourrez écrasé par une météorite!!!!!!, GAME OVER")
    
def arriver_foret():
    global pièces
    print("Vous arrivez dans une fôret")
    print("Vous trouvez un coffre avec une épée rouilée")
    choix = poser_question("Prendre l'épée rouilée ?", ["oui", "non"])
    if choix == "oui":
        print("Vous vous êtes blessé avec l'épée et vous mourrez du tétanos, GAME OVER")
    elif choix == "non":
        print("Vous rencontrez un farfadet malicieux qui vous demande de l'aide")
        choix = poser_question("Voulez-vous l'aider", ["oui", "non"])
        if choix == "oui":
            print("Comme vous l'avez aidé il vous donne 5 pièces d'or!!! Pièces + 5 ")
            pièces = pièces + 5
        elif choix == "non":
            print("Vous passez votre chemin")
        print("Vous rencontrez un marchand d'armes")
        choix = poser_question("Voulez-vous acheter une épée à 5 pièces d'or ?", ["oui", "non"])
        if choix == "oui":
            if pièces == 5:
                inventaire.append("épée")
                print("Vos êtes maintenant l'heureux propriétaire d'une magnifique épée")
                arriver_ville()
            else:
                print("Le marchand vous éventre avec l'épée parce que vous avez essayé de l'arnaquer, GAME OVER")
        elif choix == "non":
            print("Vous passez votre chemin")
            arriver_ville()
            
def arriver_ville():
    print("Vous arrivez dans une ville")
    print("Vous vous faites attaquer par des bandits")
    if 'épée' not in inventaire:
        print("Vous vous faites dévaliser et vendre comme esclave au sultan du royaume, GAME OVER")
    elif 'épée' in inventaire:
        print("Vous tuez les brigands")
        print("Il reste un dernier survivant et il vous supplie de l'épargner")
        choix = poser_question("Voulez-vous l'épargner?", ["oui", "non"])
        if choix == "non":
            print("Vous êtes arrêté pour meurtre et condamné à mort par lapidation, GAME OVER")
        elif choix == "oui":
            print("Il vous propose de rejoindre sa bande de malfaiteur")
            choix = poser_question("Rejoindre sa bande de voleur ?", ["oui", "non"])
            if choix == "oui":
                print("Vous rejoignez sa bande et vous devenez riche!!!!!! VICTOIRE")
            elif choix == "non":
                print("Il n'accepte pas votre refus et vous tue GAME OVER")
  
grotte()
                        
                    
#pour faire ce travail je me suis inspiré du deuxième exemple de code

                
                
            
        
            
        
        
        
    



