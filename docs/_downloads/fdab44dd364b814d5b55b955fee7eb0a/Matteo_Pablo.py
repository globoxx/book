import time

hp = 100
def poids_lourds():
    global hp
    prenom=input("Bonjour jeune combatant, quel est votre prénom ?")
    reponse = input("parfait, "+prenom+" j'ai pu te t'arranger un combat contre Francis Ngannou (100 points de vie), t'es partant ?")
    
    if reponse  =="non":
        poids_lourds()
    elif reponse =="oui":    
        reponse = input("quelques mois plus tard...        ok "+prenom+" c'est l'heure du combat, quelle attaque choisis-tu en premier ? takedown, highkick ou crochet? (Tu as "+str(hp)+" points de vie)")
        while reponse not in ["takedown", "highkick", "crochet"] :
            print("J'ai pas compris")
        if reponse == "takedown":
            start = time.time()
            reponse = input("Il te contre et t'attaque avec une soumission guillotine que fais-tu ? abandonner, enlever son bras, lui mettre un coup de coude ? Tu as 10 secondes pour choisir")
            end = time.time()
            temps_repondu = end - start
            
            if temps_repondu > 10:
                print("Trop tard tu t'es évanoui")
                exit()
            
            elif reponse == ("abandonner"):
                print("GAME OVER")
                exit()
            
            elif reponse == ("enlever son bras"):
                print("tu réussis à t'échapper mais tu perds 20 pv")
                hp = hp - 20
                print("Vous avez", hp, "points de vie")
            
            if reponse == "coup de coude":
                print("GAME OVER, tu te fais disqualifié, les coups de coudes sont interdits!!")
                exit()
        
        elif reponse == "highkick":
            print("Bien joué tu lui enlèves 40pv !")
        elif reponse =="crochet":
            print("pas mal, tu lui enlèves 20pv")
        reponse = input("ATTENTION ! il te lance un uppercut, que fais-tu ? esquive ou contre?")
        
        if reponse == "contre": 
            print("VICTOIRE!!! Tu le contre et le met KO avec un superbe crochet")
        
        elif reponse =="esquive":
            reponse = input(" belle esquive ! maintenant il faut attaquer, que fais-tu? Coup de genou ou highkick? ")
            if reponse == "highkick":
                print("GAME OVER, il esquive ton coup et te met KO")
                exit()
            elif reponse == "coup de genou":
                print("VICTOIRE!!! Tu le mets KO avec un superbe coup de genou")
poids_lourds()

    

