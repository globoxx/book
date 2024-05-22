# Source: https://usaco.guide/general/io

import time

# variables de base
sac_a_dos = []
condition = 50
experience = 0
start = -2

# jeu
def jeu():
    print("Vous faites partie des rares élus à avoir été choisi pour les premiers tests dans le domaine de la téléportation en 2056.")
    print("Vous allez normalement ressurgir à deux moments dans le passé puis revenir à aujourd'hui.")
    print("À vous maintenant de jouer pour que vous réussissez à suivre à cette péripétie.")
    print("\n")
    print("Vous êtes en 90'056'983 avant J.C entouré de dinosaures.")
    print("Vous vous baladez en cherchant de quoi survivre. Il y a face à vous 2 chemins.")
    dinosaure()
    print("L'aventure est finie. Nous espérons qu'elle vous ait plu. :)")


# definir des fonctions utiles tout au long du programme/jeu
def poser_question(question, choix_possibles):
    reponse = input(question + " " + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + " " + str(choix_possibles))
    return reponse

# dead end
def game_over():
    print("G A M E  O V E R !")

# winning end
def victoire():
    print("V I C T O I R E !!!!")
    print("Bravo à vous, beau jeu :)")


# essayer de réparer le portail seul chez les aliens
def portail_seul():
    global sac_a_dos
    global condition
    global experience
    global start

    print("Vous allez donc devoir essayer de réparer le portail par vos propres moyens.")

    if "clé de 10" in sac_a_dos:
        print("Vous essayez de réparer le portail seul à l'aide de la clé de 10 précedemment récupérée.")
        print("Malheureusement le temps passe et avec lui vos chances de survie diminuent.")

        # le timer doit être pris en compte
        timer = time.time()- start
        if int(timer) > 300:
            print("Le temps est écoulé.")
            print("Vous ne pouvez plus revenir sur Terre et mourrez donc.")
            game_over()
        else:
            print("Vous avez trouvé une façon de réparer le portail dans le temps imparti.")
            print("Vous réussissez donc à retourner sur Terre.")
            victoire()

    else:
        print("Vous n'avez pas de quoi réparer le portail tout seul.")
        reponse = poser_question("Vous acceptez votre mort prochaine ou dans un excès de colère vous souhaitez tuer tous les aliens ?", ["acceptance", "colère"])

        # acceptance
        if reponse == "acceptance":
            print("Vous allez mourir prochainement.")
            game_over()

        # colère
        if reponse == "colère":
            print("Vous décidez donc de passer à l'action.")

            # grenade?
            if "grenade" not in sac_a_dos:
                print("Vous n'avez finalement pas de quoi vous venger.")
                print("Vous mourrez donc seul et en colère.")
                game_over()
            else:
                print("Vous faites sauter avec votre grenade tous les aliens MAIS vous parvenez bizarrement à survivre.")
                print("Vous utilisez le vaisseau des aliens dans l'espoir de revenir sur Terre.")
                print("Vous avez des problèmes pour entrer dans l'atmosphère. Cette dernière manoeuvre requiert beaucoup d'expérience.")

                # assez d'expérience?
                if experience >= 100:
                    print("Vous parvenez tout de même à revenir sur Terre grâce à vos incroyables talents.")
                    victoire()
                else:
                    print("Vous n'arrivez pas faire les derniers kms qui vous séparent de votre fille.")
                    print("Vous mourrez donc seul dans l'espace.")
                    game_over()


# si chemin gauche chez dino
def dino_gauche():
    global sac_a_dos
    global condition
    global experience
    global start

    print("Vous continuez de marcher et arrivez dans un forêt tropicale.")
    print("Un petit dinosaure sort d'un buisson, c'est un Microceratus il est inoffensif.")
    reponse = poser_question("Vous essayez de le tué ou de l'apprivoiser ?" ,["vous le tué", "apprivoisé"])
    print("\n")

    # en premier traiter le cas si "vous le tué"
    if reponse == "vous le tué":
        print("Vous arrivez à le tuer après 2 heures à le courser.")
        condition = condition - 30
        experience = experience + 10
        sac_a_dos.append("trois_morceaux_de_viande_crue")
        print("Vous avez extrêmement faim.")
        reponse = poser_question("Vous mangez vos morceaux de viande crue ou pas ?", ["vous ne les mangez pas", "vous les mangez"])

        #en premier traiter le cas "vous ne les mangez pas"
        if reponse == "vous ne les mangez pas":
            print("Vous mourrez de faim.")
            game_over()
        
        #en deuxieme traiter le cas "vous les manger"
        elif reponse == "vous les mangez":
            print("Vous n'avez plus faim et vous êtes malade.")
            sac_a_dos.remove("trois_morceaux_de_viande_crue")
            print("Vous rencontrez un ami du petit dinosaure, c'est un gigantesque T-rex.")
            reponse = poser_question("Vous l'affrontez ou fuyez ?", ["vous l'affrontez", "vous fuyez"])
            print("\n")

            #en premier traiter le cas "Vous l'affrontez"
            if reponse == "vous l'affrontez":
                print("Vous n'êtes pas en condition de continuer, vous mourrez.")
                game_over()

            #en deuxième traiter le cas "Vous fuyer"
            elif reponse == "vous fuyez":
                print("Vous avez une nouvelle chance de poursuivre cette aventure.")
                dinosaure()       

    # en deuxième traiter le cas si "apprivoisé"
    elif reponse == "apprivoisé":
        print("Grâce à votre talent de chaman, vous réussissez à l'apprivoiser.")
        condition = condition - 5
        experience = experience + 15
        print("Vous commencez à avoir faim et soif.")
        print("Vous suivez votre dinosaure et il vous montre un point d'eau avec des fruits autour.")
        reponse = poser_question("Vous buvez et mangez ?", ["vous buvez l'eau", "vous mangez des fruits"])
        print("\n")

        #en premier traiter le cas si "vous buvez l'eau"
        if reponse == "vous buvez l'eau":
            print("Vous attrapez une maladie très grave, vous mourrez dans d'atroces souffrances.")
            game_over()

        #en deuxième traiter le cas si "vous mangez ces fruits"
        elif reponse == "vous mangez des fruits":
            print("Ils sont délicieux.")
            condition = condition + 10
            print("Vous trouvez des pépites d'or dans l'eau et une peau de dinosaure pare-balle.")
            sac_a_dos.append("pépites d'or")
            sac_a_dos.append("peau de dinosaure pare-balle")
            dino_droite()


# si chemin droite chez dino
def dino_droite():
    global sac_a_dos
    global condition
    global experience
    global start

    print("Vous continuez de marcher et arrivez dans une grotte.")
    print("Vous tombez sur un dinosaure femelle qui cherche son petit.")
    reponse = poser_question("Elle vous attaque, vous fuyez ou la combattez ?", ["fuyez","combattez"])

    #en premier traiter le cas si "fuyez"
    if reponse == "fuyez":
        print("\n")
        print("Vous tombez sur un portail, vous entrez dedans.")
        ww2()

    #en deuxieme traiter le cas si "combattez"
    elif reponse == "combattez":
        if (condition >= 45) and (experience >= 10):
            print("Vous gagnez et recupérez une peau de dinosaure pare-balle.")
            sac_a_dos.append("peau de dinosaure pare-balle")
            print("Vous tombez sur un portail, vous entrez dedans.")
            ww2()
        else:
            print("\n")
            print("Vous n'est pas assez puissant pour gagner ce combat, vous mourrez.")
            game_over()


# première partie du jeu: chez les dinosaures
def dinosaure():
    reponse = poser_question("Vous choisissez quel chemin ?" ,["gauche", "droite"])
    print("\n")

    # en premier traiter le cas si "gauche"
    if reponse == "gauche":
        dino_gauche()

    # en deuxième traiter le cas si "droite"
    elif reponse == "droite":
        dino_droite()

        

# deuxième partie: WW2
def ww2():
    global sac_a_dos
    global condition
    global experience
    global start

    print("\n")
    print("Après quelque secondes de vide et de silence, vous arrivez en France en 1940. Vous atterrissez au milieu d'un pays dévasté par la deuxième guerre mondiale. De quoi vous désorienter un bon moment.")
    reponse = poser_question("Qui voulez-vous suivre ?", ["le maréchal Pétain", "le général de Gaulle"])
    print("\n")

    # en premier traiter le cas avec Pétain
    if reponse == "le maréchal Pétain":
        print("Vous collaborez donc maintenant avec les Nazis. Le pays est en souffrance et l'entraide est promue. Comment pouvez-vous aidez votre patrie et ses alliés.")
        print("Comme tout bon Français, vous décidez de vous enrôler dans l'armée.")
        reponse = poser_question("Souhaitez-vous allés au front ?", ["oui", "non"])
        print("\n")

        # enrôlement non
        if reponse == "non":
            print("Vous êtes déshonorés et mépris.")
            print("Vous avez une nouvelle chance pour vous rachetez. Faites attention et la gaspiez pas.")
            print("\n")
            ww2()

        # enrôlement oui
        if reponse == "oui":
            print("Vous rejoignez donc le front. Mais d'un coup, vous subissez une attaque. Les Alliés vous tombent dessus.")
            if "peau de dinosaure pare-balle"  not in sac_a_dos:
                print("Vous n'avez malheureusement pas de quoi vous protéger dans votre sac à dos. Vous mourrez en héro sur le champ de bataille.")
                game_over()
            
            else:
                print("Grâce à votre équipement de qualité et l'expérience que vous aver accumulé tout au long des combats, vous survivez à la guerre.")
                print("En plus de gagner en expérience, vous trouvez et gardez une clé de 10.")
                experience += 50
                sac_a_dos.append("clé de 10")
                aliens()

    # en deuxième traiter le cas avec de Gaulle
    if reponse == "le général de Gaulle":
        print("\nVous choissiez donc de vous exiler auprès le général et ainsi rejoingez la France libre.")
        print("Vous souhaitez tout de même participer activement à la guerre.")
        reponse = poser_question("Vous avez le choix entre deux fronts, où vous rendez-vous ?", ["Paris", "Alsace"])

        # Paris
        if reponse == "Paris":
            print("\nVotre travail ici est plus passif mais vous participez tout de même à plusieurs enquêtes durant les 5 prochaines années de la guerre.")
            print("Durant l'une de vos enquêtes, vous trouvez une grenade. Toujours prévoyant, vous décidez de la garder et la placer dans votre sac à dos.")
            sac_a_dos.append("grenade")
            experience += 25
            aliens()
        
        # Alsace
        if reponse == "Alsace":
            print("Vous vous retrouvez très rapidement sur les champs de bataille.")
            if "peau de dinosaure pare-balle"  not in sac_a_dos:
                print("Vous êtes au dépourvu lors d'une bataille et n'avez pas de quoi vous défendre convenablement.")
                print("Vous mourrez donc, faute de protection.")
                game_over()
            else:
                print("Vous êtez malgré tout blessé. Mais vous survivez à la guerre!")
                print("De plus, vous avez trouvez une clé de 10 dans la boue et décidez de la glisser dans votre sac à dos.")
                sac_a_dos.append("clé de 10")
                aliens()
        
    

# troisième partie: chez les aliens
def aliens():
    global sac_a_dos
    global condition
    global experience
    global start

    print("\n")
    print("La machine à téléportation est en train de disjoncter. À la place de vous ramener au 21e siècle, le dernier portail vous a projecté dans le FUTUR!")
    print("Vous parvenez tout de même à intercepter un message qui vous fait froid au dos...")
    print("« grrr... vous avez... 5... bizzzz... minutes... pour restau... rer le portail... sinon..... »")
    print("Vous avez donc plus que 5 minutes pour rétablir la connection avec 2056 ou sinon vous serrez perdu à jamais et ne reverrez jamais votre fille.")
    start = time.time()
    reponse = poser_question("Que décidez-vous de faire: réparer le portail seul ou avec l'aide des aliens ?", ["seul", "aide"])

    # seul
    if reponse == "seul":
        portail_seul()

    # aide
    if reponse == "aide":
        print("Vous devez tout de même en premier devenir amis avec les aliens avant de réclamer leur aide.")

        if "pépites d'or" not in sac_a_dos:
            print("vous n'arrivez pas à les convaincre de votre supériorité, ils ne vous respectent donc pas et ne vous aident pas.")
            portail_seul()
        else:
            print("Convaincus de leur infériorité, ils décident de vous aider.")
            print("Les aliens réussissent à résoudre le problème en deux minutes.")
            start += 120
            
            # le timer doit être pris en compte
            timer = time.time()-start
            if int(timer) > 300:
                game_over()
            else:
                print("Vous survivez grâce à l'aide des aliens et revenez sur Terre.")
                victoire()



# début du jeu
jeu()