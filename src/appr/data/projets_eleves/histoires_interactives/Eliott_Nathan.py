def poser_question(question, choix_possibles):
    reponse = input(question + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + str(choix_possibles))
    return reponse #exercice

def histoire():
    inventaire = []
    cheveux = 60
        
    print ("Vous, Cyllvèstre Pydouille êtes triste à cause de votre calvitie et décidez d'aller en Turquie. Vous préparez votre valise")

    print ("Choisissez un objet")
    choix = poser_question("Que prenez-vous ?", ["Perruque", "Chapeau"])
    if choix == "Perruque":
        inventaire.append ("Perruque")
        print("Vous avez récupérez la perruque")
        print("Votre inventaire actuel", inventaire)
        
    elif choix == "Chapeau":
        inventaire.append ("Chapeau")
        print("Vous avez récupérez le chapeau")
        print("Votre inventaire actuel", inventaire)
        
    print("Choisissez un autre objet")
    choix = poser_question("Que prenez-vous ?", ["Brosse à cheveux", "Rasoire"])
    if choix == "Brosse a cheveux":
        inventaire.append ("Brosse à cheveux")
        print("Vous prenez la brosse à cheveux")
        print("Votre inventaire actuel", inventaire)
        
    elif choix == "Rasoire":
        inventaire.append ("Rasoire")
        print("Vous prenez le rasoire")
        print("Votre inventaire actuel", inventaire)
        
    print("Quelques uns de vos cheveux sont tombés (10)")
    cheveux -= 10
    print ("Vos cheveux actuel", cheveux)
    print("Vous partez")
    choix = poser_question("Comment y allez-vous ?", ["Avion", "Voiture"])
    if choix == "Avion":
        print("Vous rentrez dans l'avion et arrivez en Turquie")
        print("Vous passez une nuit à l'hotel, vous avez perdu des cheveux (10)")
        cheveux -= 10
        print ("Vos cheveux actuel", cheveux)
        
        print("Le lendemain, vous allez au centre pour votre implant capilaire")
        print("Sur le chemin vous croisez un enfant")
        choix = poser_question("Voulez-vous jouer avec lui ?",["Oui", "Non"])
        if choix == "Oui":
            print("Il tire vos cheveux")
            if "Perruque" in inventaire:
                print ("Vous perdez votre perruque")
                inventaire.remove ("Perruque")
                print(inventaire)
                
            elif "Perruque" not in inventaire:
                print ("Vous perdez 30 cheveux")
                cheveux -= 30
                print("Vos cheveux actuel", cheveux)
                
        elif choix == "Non":
            print("Vous continuez votre route")
                
        print("Vous vous rendez au centre et vous voyez des gens en train de faire des travaux.")
        choix = poser_question("Allez-vous dans leurs direction ?",["Oui", "Non"])
        if choix == "Oui":
            print("Vous vous prenez de la poussières sur le visage et vous perdez 15 cheveux")
            cheveux -= 15
            print ("Vos cheveux actuel", cheveux)
            if cheveux <= 0:
                print ("Vous êtes mort car vous avez perdu tout vos cheveux")
                quit()
            
        elif choix == "Non":
            print ("Vous faites simplement le tour")
              
        print("Vous continuez votre route et arrivez devant une porte")
        
        while choix == "Non" or "Oui":
            choix = poser_question("Est-ce que vous toquez et entrez ?",["Oui", "Non"])
            if choix == "Oui":
                print ("Félicitation ! Le docteur a fait vos implants capillaires de rêves !")
                print ("Vous avez gagné !!!")
                quit()
            
            elif choix == "Non":
                print ("Dommage, c'était celle du docteur")
                
            print("Attention !!! Un liquide radioactif est en train de tombé sur votre tete!!")
            if "Chapeau" in inventaire:
                print ("Vous perdez votre chapeau mais heureusement qu'il vous a pas touché")
                inventaire.remove ("Chapeau")
                print("Votre inventaire actuel", inventaire)
                
            elif "Chapeau" not in inventaire:
                print("Votre crâne est endommagé, vous ne pouvez donc pas effectuer l'opération")
                print("Vous avez perdu")
                quit()
                break
                
    elif choix == "Voiture":
        print ("Vous montez à bord de votre Fiat Panda")
        choix = poser_question("Sur la route, vous avez deux choix possible: Soit une route courte mais périlleuse, soit une route longue mais sûre. Que choisissez-vous ?",["Route_courte", "Route_longue"])
        if choix == "Route_courte":
            print("Vous croisez un gang de chevelus qui a perdu ses brosses à cheveux")
            if "Brosse à cheveux" in inventaire:
                choix = poser_question("Voulez-vous donner votre brosse à cheveux ?")
                if choix == "Oui":
                    print("Ils vous prennent votre brosse à cheveux et vous laisse passer")
                    inventaire.remove ("Brosse à cheveux")
                    print("Votre inventaire actuel", inventaire)
                    
                elif choix == "Non":
                    print("Le gang vous arrache 25 cheveux et vous laisse partir")
                    cheveux -= 25
                    print("Vos cheveux actuel", cheveux)
                
            elif "Brosse à cheveux" not in inventaire:
                print("Le gang vous arrache 25 cheveux et vous laisse partir")
                cheveux -= 25
                print("Vos cheveux actuel", cheveux)
                
        elif choix == "Route_longue":
            print("Votre trajet se passe paisiblement, mais vous perdez 10 cheveux")
            cheveux -= 10
            print ("Vos cheveux actuel", cheveux)
            
        print("Vous êtes arrivé en Turquie")
        print("Vous passez la nuit dans un hotel, vous perdez 10 cheveux")
        cheveux -= 10
        print("Vos cheveux actuel", cheveux)
        print("Le lendemain, vous vous rendez chez le docteur. Après une longue marche, vous arrivez vers son cabinet, mais des chauves vous attaquent")
        if "Rasoire" in inventaire:
            choix = poser_question("Voulez-vous utiliser votre rasoire ?", ["Oui", "Non"])
            if choix == "Oui":
                print("Vous les dissuadez de vous attaquez et perdez votre rasoire")
                inventaire.remove("Rasoire")
                print("Votre inventaire actuel", inventaire)
                print("Vous arrivez chez le docteur et entrez dans son cabinet")
                print("Félicitation !!!!! Le docteur a fait cos implants capillaires de rêves !!!")
                quit()
           
            elif choix == "Non":
                print("Ils vous arrachent vos cheveux")
                print("Vous avez perdu")
                quit()
                cheveux -= cheveux
        
        elif "Rasoire" not in inventaire:
            print("Ils vous arrachent tous vos cheveux")
            print("Vous avez perdu")
            quit()
            cheveux -= cheveux
                
            
histoire()
        
    
        
        
                
