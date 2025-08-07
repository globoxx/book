import sys
pv=100
santémentale=5
inventaire=[]
def début():
    global pv
    global santémentale

    def pasaraignée ():
        global pv
        global santémentale
        print("Vous longez un sombre couloir,n'aillant pas de source de lumière avec vous, vous perdez 1 point de santé mentale.")
        santémentale = santémentale - 1
        if santémentale <= 0:
            print("vous sombrez dans la folie et vous perdez dans l'obscurité du labyrinthe")
            print("GAME OVER")
            sys.exit()
        reponse = input("Vous regardez autour de vous et voyer une porte à votre droite, voulez vous aller à droite ou à gauche ?")
        if reponse == "droite":
            print("Vous tournez à droite et tenter d'ouvir la porte, par chance, celle-ci s'ouvre ! Vous passez la porte mais l'endroit vous semble familier...")
            début()
        elif reponse == "gauche":
            print("Vous allez à gauche et regardez devant vous, il semble y avoir une lumière en face de vous, malheureusement, vous voyez également un trou qui vous sépare de la sortie. Vous voyez une petite bordure qui pourrait vous permettre d’accéder à l’autre côté sûrement.")
            reponse = input("Sauter ou longer la bordure ?")
            if reponse == "sauter":
                print(
                    "Vous sautez et par miracle, vous réussissez à passer de l'autre côté sain et sauf ! Vous courez vers la lumière.")
                print("Vous avez trouvé la sortie, bravo !")
            elif reponse == ("longer la bordure"):
                print(
                    "Vous longez la bordure avec prudence mais soudainement, la bordure s'effondre et vous tombez dans le trou.")
                pv =pv-100
                print("GAME OVER")
    def araignée ():
        global pv
        global santémentale
        print ("Une araignée apparaît devant vous, afin de se défendre, elle vous mords avec ses crochets, vous faisant perdre 50pv. ELle vous a pas manqué !")
        pv =pv -50
        if pv <= 0:
            print("GAME OVER")
            sys.exit()
        print("En plus de son venin, l'araignée vous a tant effrayée que votre santé mentale en a pris un coup, vous perdez un point de santé mentale.")
        santémentale = santémentale - 1
        if santémentale <= 0:
            print("vous sombrez dans la folie et vous perdez dans l'obscurité du labyrinthe")
            print("GAME OVER")
            sys.exit()
        print("vous revenez sur vos pas sans lâcher l'araignée des yeux.")
        pasaraignée()

    def gauche ():
        global pv
        global santémentale
        print("Vous allez à gauche et soudainement, vous entreyovez quelque chose dans un coin.")
        reponse = input("Regardez de plus près?")
        if reponse =="oui":
            araignée()
        if reponse =="non":
            pasaraignée()



    print("Vous êtes dans un labyrinthe. Prenez garde, plus vous passez de temps dans l'obscurité du labyrinthe, plus vous perdez de la santé mentale. Trouver la sortie.")
    reponse = input("Deux directions s'offre à vous, gauche ou droite ?")
    if reponse == "droite":
        print("Vous prenez à droite et vous enfoncé dans l'obsucrité du labyrithe...")
        reponse = input("Continuer tout droit ou tourner à gauche ?")
        while reponse == "gauche":
            print("Vous êtes dans une impasse, vous perdez un point de santé mentale.")
            santémentale =santémentale-1
            if santémentale <= 0:
                print("Vous avez perdu toute votre santé mentale, l'obscurité")
                print("GAME OVER")
                sys.exit()
            print("Vous revenez sur vos pas.")
            reponse = input("Continuer tout droit ou trouner à gauche ?")
        if reponse == "tout droit":
            print("Vous allez tout droit.")
            reponse=input("Voulez-vous continuer tout droit ou tourner à droite ?")
            while reponse == "droite":
                print("Vous vous trouvez dans une impasse, vous perdez deux points de santé mentale.")
                santémentale = santémentale-2
                if santémentale <= 0:
                    print("Vous avez perdu toute votre santé mentale, l'obscurité")
                    print("GAME OVER")
                    sys.exit()
                print("Vous revenez sur vos pas.")
                reponse=input("Voulez-vous continuer tout droit ou tourner à droite ?")
            if reponse == "tout droit":
                print("Vous continuez tout droit, décidement vous n'avez pas beaucoup d'originialité...")
                reponse=input("Aller à gauche ou à droite ?")
                if reponse=="droite":
                    print ("Vous tombez sur une pièce avec une bougie, vous gangez 2 points de santé mentale ")
                    santémentale = santémentale+ 2
                    print("Aucune autre sortie de semble se présenter, vous décidez de retrouner sur vos pas et de prendre l'autre direction.")
                    gauche()
                elif reponse=="gauche":
                    gauche()
                    if reponse =="oui":
                        araignée()
                    elif reponse == "non":
                        pasaraignée()
    elif reponse == "gauche":
        inventaire = []
        print ("Vous prenez à gauche et marcher durant quelques seconde...")
        reponse = input ("Deux nouveaux choix s'offre à vous, reprendre à gauche ou aller à droite ?")
        while reponse =="droite":
            print("Vous arrivez devant un tableau effrayant. Vous perdez un point de santé mentale pour la frayeur qu'il vous à causé.")
            santémentale = santémentale - 1
            if santémentale <= 0:
                print("Vous avez perdu toute votre santé mentale, l'obscurité")
                print("GAME OVER")
                sys.exit()
            print("Vous décidez de revenir sur vos pas en essayer d'oublier cet horrible tableau.")
            reponse = input("Deux nouveaux choix s'offre à vous, reprendre à gauche ou aller à droite ?")
        if reponse == "gauche":
                print("Vous prenez à gauche et arriver en face d'un mur, avant de distinguer deux nouvelles directions")
                reponse = input("Gauche ou droite?")
                if reponse == "droite":
                    print("Vous allez à droite et vous retrouvez dans une impasse, mais du coin de l'oeil, vous trouvez un morceau de viande et une épée. Vous les prenez avec vous avant de retourner en arrière.")
                    print("Vous arrivez en face d'un monstre, il vous a également vu.")
                    reponse = input("Utiliser le morceau de viande ou l'épée?")
                    if reponse == "Morceau de viande":
                        print("Vous jetez votre morceau de viande Le monstre n’a portée aucune attention à celui-ci. Il vous tue.")
                        print("GAME OVER")
                        sys.exit()
                    elif reponse == "épée":
                        print("Vous décidez de combattre le monstre avec votre épée. Vous ratez votre première attaque et le monstre se moque de vous. Vous essayez une nouvelle fois et par miracle, vous gagnez ! Le monstre disparaît et laisse tomber une clé.")
                        reponse = input("Prendre la clé?")
                        if reponse == "oui":
                            print("Vous continuez votre chemin dans l’obscurité totale, vous perdez 1 points de santé mentale. Avant de vous perdre dans l’obscurité totale, vous distinguez une porte avec un verrou.")
                            inventaire.append("clé")
                            if "clé" in inventaire:
                                inventaire.append("clé")
                                print("Vous vous dirigez vers la porte, et l'ouvrez avec votre clé. L'autre côté semble sombre, vous y mettez un pied et...")
                                print("Vous avez trouvé la sortie ! Bravo !")
                                sys.exit()
                        else:
                            print("Vous continuez votre chemin dans l’obscurité totale, vous perdez 1 points de santé mentale. Avant de vous perdre dans l’obscurité totale, vous distinguez une porte avec un verrou.")
                            print("Malheureusment vous n'avez pas de clé.")
                            print("vous continuez alors votre chemin dans un long couloir sombre, vous perdez deux points de santé mentale. Mais, avant de sombrer, vous distignez de la lumière, vous utilisez ce qui vous reste pour courir en direction de celle-ci. Mais vous ne l'atteindrez jamais.")
                            print("GAME OVER")
                            sys.exit()
                elif reponse == "gauche":
                    print("Vous arrivez en face d'un monstre, il vous a également vu.")
                    print ("Le monstre vous tue immédiatement, en même temps, comment voudriez-vous vous défendre ?")
                    print ("GAME OVER")
                    sys.exit()
début()