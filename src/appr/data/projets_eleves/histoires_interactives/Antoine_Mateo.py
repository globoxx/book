metal = 0
inventaire = []
inventaire_marchand = ["épée (25 pièces)", "potion de vie (100 pièces)", "corde (25 pièces)", "dynamite (100 pièces)", "parchemin antique (50 pièces)"]
vie = 3
gardien = True
mur = True
squelette = True
puit = False
mine = False
temple_ouvert = False
portail_allume = False
argent = 50
temple = False
attaque = 10
loup = True
cadeau = False
a_un_ami = False
from time import *
import sys
import random
print("Pour chaque réponses il suffit d'écrire un seul mot.")
sleep(2)
x = float(input("Choisissez la vitesse des dialogues.(<1 = rapide >1 = lent)"))
print("Vous vous réveillez dans une clairière.")
sleep(2*x)
print("vous ne savez pas ce que vous faites ici.")
sleep(1.5*x)
print("Vous avez 50 pièces dans votre porte monnaie.")
sleep(2*x)
print("Vous décidez de partir.")
sleep(2*x)
def clairiere():
    global attaque
    def question1():
        def village():
            print("Vous arrivez au village.")
            sleep(2*x)
            print("Dedans se trouvent une taverne, un magasin, une forge, des maisons et le chemin pour retourner à la clairière.")
            sleep(4*x)
            def question2():
                def taverne():
                    global a_un_ami
                    print("Vous entrez dans la taverne.")
                    sleep(1*x)
                    if a_un_ami == False:
                        if "cadeau" in inventaire:
                            print("Il n'y a personne dans la taverne, vous retournez donc au village.")
                            sleep(3*x)
                            village()
                    elif a_un_ami == True:
                        print("Il n'y a personne dans la taverne, vous retournez donc au village.")
                        sleep(3*x)
                        village()
                    print("Assis à une table, il y a des hommes musclés et intimidants qui boivent des bières.")
                    sleep(3*x)
                    def question3():
                        global a_un_ami
                        reponse=input("Voulez-vous leur parler?")
                        if reponse == "oui":
                            print("Vous allez vers eux.")
                            sleep(2*x)
                            print("-Hey! On a pas souvent de la visite par ici ahah!    dit un des hommes.")
                            sleep(3.5*x)
                            print("Vous discutez pendant une demie heure et vous vous nouez d'amitié avec les habitants. Finnalement, vous decidez de partir.")
                            sleep(5*x)
                            print("Avant de partir un des hommes vous propose de venir chez lui un de ces quatres.")
                            sleep(4*x)
                            a_un_ami=True
                            village()
                        elif reponse == "non":
                            print("Vous sortez de la taverne et retournez au village.")
                            sleep(2.5*x)
                            village()
                        else:
                            print("Orthagraphe mauvais.")
                            sleep(1*x)
                            question3()
                    question3()
                def magasin():
                    global argent
                    global attaque
                    print("-Que voulez-vous acheter? (dire 'village' pour sortir)")
                    sleep(2.5*x)
                    for item in inventaire_marchand:
                        print(item)
                    reponse=input()
                    if reponse == "corde":
                        if "corde (25 pièces)" in inventaire_marchand:
                            global argent
                            if argent >= 25:
                                inventaire_marchand.remove("corde (25 pièces)")
                                argent-= 25
                                inventaire.append("corde")
                                print("Vous achetez la corde pour 25 pièces")
                                sleep(2*x)
                                magasin()
                            else:
                                print("Vous n'avez pas assez d'argent!")
                                sleep(1.5*x)
                                magasin()
                        elif "corde (25 pièces)" not in inventaire_marchand:
                            print("-Je n'ai plus cet objet!")
                            magasin()
                    if reponse == "dynamite":
                        if "dynamite (100 pièces)" in inventaire_marchand:
                            if argent >= 100:
                                inventaire_marchand.remove("dynamite (100 pièces)")
                                argent-= 100
                                inventaire.append("dynamite")
                                print("Vous achetez la dynamite pour 100 pièces")
                                sleep(2*x)
                                magasin()
                            else:
                                print("Vous n'avez pas assez d'argent!")
                                sleep(1.5*x)
                                magasin()
                        elif "dynamite (100 pièces)" not in inventaire_marchand:
                            print("-Je n'ai plus cet objet!")
                            magasin()
                    if reponse == "potion":
                        if "potion de vie (100 pièces)" in inventaire_marchand:
                            global vie
                            if argent >= 100:
                                inventaire_marchand.remove("potion de vie (100 pièces)")
                                argent-= 100
                                print("Vous achetez la potion pour 100 pièces")
                                sleep(2*x)
                                print("La potion vous offre une vie supplémentaire!")
                                vie+=1
                                sleep(2*x)
                                magasin()
                            else:
                                print("Vous n'avez pas assez d'argent!")
                                sleep(1.5*x)
                                magasin()
                        elif "potion de vie (100 pièces)" not in inventaire_marchand:
                            print("-Je n'ai plus cet objet!")
                            magasin()
                    if reponse == "épée":
                        if "épée (25 pièces)" in inventaire_marchand:
                            if argent >= 25:
                                inventaire_marchand.remove("épée (25 pièces)")
                                argent-= 25
                                inventaire.append("épée")
                                print("Vous achetez l'épée pour 25 pièces")
                                attaque+=5
                                sleep(2*x)
                                print("Dégats augmentés de 5:")
                                sleep(2*x)
                                magasin()
                            else:
                                print("Vous n'avez pas assez d'argent!")
                                sleep(1.5*x)
                                magasin()
                        elif "épée (25 pièces)" not in inventaire_marchand:
                            print("-Je n'ai plus cet objet!")
                            magasin()
                    if reponse == "parchemin":
                        if "parchemin antique (50 pièces)" in inventaire_marchand:
                            if argent >= 50:
                                inventaire_marchand.remove("parchemin antique (50 pièces)")
                                argent-= 50
                                inventaire.append("parchemin")
                                print("Vous achetez le parchemin antique pour 50 pièces")
                                sleep(2*x)
                                magasin()
                            else:
                                print("Vous n'avez pas assez d'argent!")
                                sleep(1.5*x)
                                magasin()
                        elif "parchemin antique (50 pièces)" not in inventaire_marchand:
                            print("-Je n'ai plus cet objet!")
                            magasin()

                    if reponse == "village":
                        print("Vous sortez du magasin.")
                        sleep(1.5*x)
                        village()
                    else:
                        print("Orthographe mauvais.")
                        sleep(1*x)
                        magasin()


                def forge():
                        global metal
                        print("Vous arrivez à la forge.")
                        sleep(2*x)
                        print("-Hey, qu'est-ce que je peux faire pour vous?    dit le forgeron.")
                        sleep(2*x)
                        if metal > 0:
                            if metal == 3:
                                if "manche" in inventaire:
                                    global attaque
                                    print("-Avec les matériaux que vous avez recoltés je peux vous fabriquer une épée surpuissante.")
                                    sleep(3*x)
                                    print("Vous obtenez une épée de l'ombre!")
                                    sleep(2*x)
                                    attaque+=30
                                    print("Dégats augmentés de 10!")
                                    sleep(2*x)
                                    metal=0
                                    inventaire.remove("manche")
                                    print("Vous sortez de la forge.")
                                    village()
                                else:
                                    print("-Il vous manque un manche pour créer une épée.")
                                    sleep(2*x)
                                    print("Vous retournez au village.")
                                    village()
                            else:
                                print("-Je vois que vous avez du minerai d'ombre.")
                                sleep(2*x)
                                print("-Revenez quand vous en aurez trois et un manche.")
                                village()
                        else:
                            print("-Vous n'avez rien que je puisse utiliser sur vous.")
                            sleep(2*x)
                            print("Vous retournez donc au village")
                            village()
                def maison():
                    global a_un_ami
                    global attaque

                    print("Vous vous trouvez devant les maisons.")
                    sleep(2*x)
                    if a_un_ami == False:
                        print("Elles sont cotées.")
                        sleep(2*x)
                        print("Vous retournez donc au village.")
                        sleep(2*x)
                        village()
                    elif a_un_ami == True:
                        print("Vous voyez que toutes sont fermées sauf une.")
                        sleep(3*x)
                        print("Vous decidez d'y entrer.")
                        sleep(2*x)
                        print("à l'intérieur vous retrouvez votre ami.")
                        sleep(2*x)
                        print("Après une longue discussion, il vous donne un cadeau.")
                        sleep(2*x)
                        print("Vous recevez une épée tranchante!")
                        sleep(2*x)
                        print("Dégats augmentés de 10!")
                        attaque += 10
                        sleep(2*x)
                        print("Vous sortez de la maison et êtes de retour dans le village.")
                        a_un_ami = False
                        inventaire.append("cadeau")
                        village()

                reponse=input("Où voulez-vous aller?")
                if reponse == "maisons":
                    maison()
                elif reponse == "forge":
                    forge()
                elif reponse == "taverne":
                    taverne()
                elif reponse == "magasin":
                    print("Vous entrez dans le magasin.")
                    sleep(1.5 * x)
                    print("-Bonjour, bienvenu dans mon magasin!")
                    sleep(2 * x)
                    magasin()
                elif reponse == "clairière":
                    print("Vous retournez à la clairière.")
                    sleep(2*x)
                    clairiere()
                else:
                    print("Orthagraphe mauvais.")
                    sleep(1*x)
                    question2()

            question2()
        def foret():
            def cabane():
                print("Vous entrez dans la cabane.")
                sleep(2*x)
                print("-Bonjour!    dit le vieil homme.")
                sleep(2*x)
                if portail_allume == False:
                    print("-Il faut allumer le portail au plus vite. Pour cela, il vous faudra prononcer les mots scellés du temple devant le portail.  ")
                    sleep(5*x)
                    print("Vous sortez de la cabane")
                    question4()
                elif portail_allume == True:
                    print("-Bravo vous avez allué le portail! Foncez anéantir la menace de l'Umbral!")
                    sleep(3*x)
                    print("Vous quittez la cabane")
                    sleep(1.5*x)
                    question4()
            def question4():
                print("Vous êtes dans la forêt. Il y a le portail, la cabane et le chemin pour retourner à la clairière.")
                reponse=input("Où voulez-vous aller?")
                if reponse == "portail":
                    portail()
                elif reponse == "cabane":
                    cabane()
                elif reponse == "clairière":
                    clairiere()
                else:
                    print("Orthographe mauvais")
                    sleep(1*x)
                    question4()
            def mine():
                global vie
                global metal
                global mine
                if mine == True:
                    print("La mine est écroulée. Vous retournez au portail.")
                    question5()
                elif mine == False:
                    print("Vous entrez dans la mine.")
                    sleep(2*x)
                    print("Une forte odeur de métal se dégage des murs.")
                    sleep(2*x)
                    print("Vous avancez dans la mine quand tout à coup, un mineur corompu surgit de l'obscurité.")
                    sleep(2 * x)
                    if attaque >=15:
                        print("Le mineur n'était clairement pas de taille et vous le massacrez.")
                        sleep(2 * x)
                        print("Il vous donne 50 pièces et un minerais d'ombre!")
                    else:
                        print("Vous combattez avec courage mais le mineur est tout simplement trop fort.")
                        sleep(2 * x)
                        print("Vous vous faîtes piocher et perdez une vie.")
                        vie -= 1
                        if vie == 0:
                            print("Vous n'avez plus de vie!")
                            sleep(2)
                            print(
                                "Sans votre aide, Vincent le sanglant a réussi à sortir de l'Umbral et a pris le contrôle du monde!")
                            sleep(3)
                            print("GAME OVER")
                            sys.exit()
                        print("Vous vous reveillez au portail")
                        sleep(2 * x)
                        question5()
                    print("Vous avancez dans la mine quand tout à coup vous entendez une voix famillière.")
                    sleep(3 * x)
                    print("-Va au bastion sanglant et retrouve notre maître!")
                    sleep(3 * x)
                    print("C'était la voix du vieil homme.")
                    sleep(3 * x)
                    print("Il parlait avec un petit monstre infécté")
                    sleep(3 * x)
                    print("Il vous a trompé pour que vous alliez dans le temple pour ouvrir le portail et libérer les forces de l'Umbral!")
                    sleep(5 * x)
                    print("-Misérable humain! Bientôt vous serrez réduit à néant!   dit-il")
                    sleep(3 * x)
                    print("Vous répondez: -Sûrment pas! et le frappez avec une tel puissance que toute la mine se mit à s'écrouler!")
                    sleep(4*x)
                    print("Vous prenez le minerai d'ombre qu'avait l'homme et partez au plus vite.")
                    mine = True
                    metal = metal+2
                    if metal == 3:
                        print("Le forgeron vous attend.")
                    sleep(3 * x)
                    print("Vous arrivez juste à temps dehors. La mine s'est écroulée. Il y a le bastion sanglant, la mine et le portail.")
                    sleep(2.5 * x)
                    question5()
            def boss():
                print("Vous entrez dans le bastion sanglant.")
                sleep(2*x)
                print("Vous pouvez retournez au portail ou aller au sommet du bastion")
                sleep(2*x)
                reponse=input("Que voulez-vous faire?")
                if reponse == "portail":
                    print("Vous retournez au portail")
                    sleep(2*x)
                    print("Il y a la mine le portail et le bastion sanglant.")
                    question5()
                elif reponse == "sommet":
                    print("Vous montez les marches du bastion.")
                    sleep(2*x)
                    print("Sur les murs, des gouttes de sang s'écoulent.")
                    sleep(2*x)
                    print("Sur une stèle sont inscits les mots suivants:")
                    sleep(1*x)
                    print("Celui qui souhaite rompre la malédiction devra ouvrir un portail vers les cieux grâce à cette formule:")
                    print("'Que les divins m'ouvrent les portes'.")
                    sleep(6*x)
                    print("Vous êtes arrivé en haut des marches.")
                    sleep(2*x)
                    print("Vous voyez Vincent le sanglant, prêt à en découdre.")
                    sleep(2*x)
                    print("-J'ai déjà gagné! ça ne sert à rien d'essayer!   dit il")
                    sleep(3*x)
                    print("Le combat commence...")
                else:
                    print("Orthographe mauvais.")
                    sleep(2*x)
                    boss()
                if "EPEESOLEIL" in inventaire:
                    print("Grâce à votre épée divine, vous tuez Vincent le sanglant et rompez sa malédiction.")
                    sleep(2*x)
                    print("Félicitation, vous êtes le héro du monde!!")
                    print("Vous avez réussi à débloquer la bonne fin!")
                    print("J'éspère que mon jeu vous aura plu!")
                    sys.exit()
                elif attaque >= 50:
                    replique = ["Le combat est intense", "Vous rouez Vincent d'attaques.",
                                "Vincent vous lance une attaque surpuissante mais vous réussissez à ésquiver.",
                                "Vous canalisez toutes vos forces.",
                                "Vous recevez un coup mais continuez à vous battre.",
                                "L'avenir du monde repose sur vos épaules.",
                                "Vous êtes blessé mais continuez à vous battre."]
                    for i in range(3):
                        print(random.choice(replique))
                        sleep(3 * x)
                    print("Finnalement, vous réussissez à vaincre Vincent le sanglant.")
                    sleep(2*x)
                    print("-C'est inutile.")
                    sleep(2 * x)
                    print("-Tu as perdu.")
                    sleep(2 * x)
                    print("-Ma malédiction prendra le dessus sur ton corps.")
                    sleep(1)
                    print(".")
                    sleep(1)
                    print("..")
                    sleep(1)
                    print("...")
                    sleep(2*x)
                    print("Vincent ne respire plus.")
                    sleep(2 * x)
                    print("Vous sentez quelque chose au plus profond de vous.")
                    sleep(2 * x)
                    print("Votre vision devient trouble")
                    sleep(2 * x)
                    print("VOUS ÊTES DEVENU VINCENT.")
                    sleep(2 * x)
                    print("Merci d'avoir jouer!")
                    print("J'espère que cette histoire vous a plus!^^")
                    sys.exit()
                if "EPEESOLEIL" in inventaire:
                    print("Grâce à votre épée divine, vous tuez Vincent le sanglant et rompez sa malédiction.")
                    sleep(2*x)
                    print("Félicitation, vous êtes le héro du monde!!")
                    print("Vous avez réussi à débloquer la bonne fin!")
                    print("J'éspère que mon jeu vous aura plu!")
                    sys.exit()
                else:
                    replique = ["Le combat est intense", "Vous rouez Vincent d'attaques.",
                                "Vincent vous lance une attaque surpuissante mais vous réussissez à ésquiver.",
                                "Vous canalisez toutes vos forces.",
                                "Vous recevez un coup mais continuez à vous battre.",
                                "L'avenir du monde repose sur vos épaules.",
                                "Vous êtes blessé mais continuez à vous battre."]
                    for i in range(3):
                        print(random.choice(replique))
                        sleep(3 * x)
                    print("Finnalement, Vincent prend le dessus et vous tue.")
                    sleep(2*x)
                    print("Il part tout droit en direction du portail et finira par prendre le contrôle du monde entier.")
                    sleep(2*x)
                    print("GAME OVER")
                    sys.exit()

            def bastion_sanglant():
                global squelette
                global vie
                global mur
                global metal
                print("Vous vous dirigez vers le bastion sanglant.")
                sleep(2 * x)
                if squelette == True:
                    print("Un squelette vous barre la route")
                    if attaque >= 20:
                        sleep(2 * x)
                        print("Vous désossez le squelette sans soucis.")
                        sleep(2 * x)
                        print("Il vous donne 100 pièces et un minerai d'ombre!")
                        sleep(2*x)
                        if metal==3:
                            print("Le forgeron vous attend.")
                        sleep(3 * x)
                        print("Vous décidez de lui prendre un fémur.")
                        inventaire.append("manche")
                        squelette = False
                        metal=metal+1
                        bastion_sanglant()
                    else:
                        print("Le squelette vous arrache le cartilage et vous perdez une vie.")
                        vie = vie - 1
                        if vie == 0:
                            print("Vous n'avez plus de vie!")
                            sleep(2)
                            print("Sans votre intervention, Vincent le sanglant a réussi à sortir de l'Umbral et a pris le contrôle du monde!")
                            sleep(3)
                            print("GAME OVER")
                            sys.exit()
                        print("Vous vous reveillez au portail")
                        sleep(2*x)
                        question5()
                elif squelette == False:
                    if mur == True:
                        print("Une énorme muraille entoure le bastion.")
                        if "dynamite" in inventaire:
                            sleep(2*x)
                            print("Vous utilisez la dynamite pour exploser un passage dans le mur.")
                            mur = False
                            boss()
                        elif "dynamite" not in inventaire:
                            sleep(2*x)
                            print("La muraille est impossible à contourner et à grimper.")
                            sleep(2*x)
                            print("Vous ne pouvez pas la franchir et retournez donc au portail.")
                            question5()
                    elif mur == False:
                        boss()
            def question5():
                reponse=input("Où voulez-vous aller?")
                if reponse == "portail":
                    print("Vous entrez dans le portail")
                    sleep(2*x)
                    question4()
                elif reponse == "mine":
                    mine()
                elif reponse == "bastion":
                    bastion_sanglant()
                else:
                    print("Orthographe mauvais")
                    sleep(1 * x)
                    question5()

            def umbral():
                sleep(2*x)
                print("L'atmosphère est sinistre.")
                sleep(2*x)
                print("Il y a une mine, le portail et un chemin qui mène au bastion sanglant.")
                question5()
            def portail():
                global portail_allume
                global attaque
                if portail_allume == True:
                    print("Vous arrivez devant le portail et entrez dedans.")
                    sleep(2*x)
                    print("Vous arrivez dans l'Umbral.")
                    umbral()
                elif portail_allume == False:
                    print("Vous arrivez devant le portail")
                    sleep(2*x)
                    reponse=input("Que voulez-vous dire au portail?")
                    if reponse == "Umbral ouvre toi":
                        sleep(1*x)
                        print("Le portail s'ouvre.")
                        portail_allume = True
                        sleep(2*x)
                        print("Vous entrez dans le portail")
                        sleep(2*x)
                        print("Vous arrivez dans l'Umbral.")
                        umbral()
                    elif reponse == "Que les divins m'ouvrent la porte":
                        print("Le portail s'ouvre et vous y entrez.")
                        sleep(2 * x)
                        print("Vous êtes au paradis.")
                        sleep(2 * x)
                        print("Dans un coffre qui se trouve devant vous, vous trouvez une épée aussi légère qu'une plume et aussi brûlante que le soleil.")
                        inventaire.append("EPEESOLEIL")
                        sleep(2*x)
                        print("Vous gagnez 100 dégats.")
                        attaque+=100
                        sleep(2 * x)
                        print("Vous retournez dans le portail et vous vous retrouvez dans la forêt.")
                        sleep(2 * x)
                        print("Le portail s'est refermé.")
                        question4()
                    else:
                        print("Rien ne se passe, vous retournez dans la forêt.")
                        question4()
            global vie
            global argent
            global loup
            print("Vous pénétrez dans la forêt dense.")
            sleep(1.5*x)
            if loup == True:
                print("Sur votre chemin se dresse un loup enragé.")
                sleep(2*x)

                if attaque >= 5:
                    print("Vous arrivez à vous débarasser du loup avec aisance!")
                    sleep(2*x)
                    print("Sur lui se trouvaient 50 pièces d'or.")
                    argent+=50
                    sleep(2.5*x)
                    loup = False

                else:
                    print("Après un dur combat le loup fini par prendre le dessus.")
                    sleep(2*x)
                    print("Vous vous faîtes dévorer et perdez une vie.")
                    vie-=1
                    if vie == 0:
                        print("Vous n'avez plus de vie!")
                        sleep(2)
                        print("Sans votre aide, Vincent le sanglant a réussi à sortir de l'Umbral et a pris le contrôle du monde!")
                        sleep(3)
                        print("GAME OVER")
                        sys.exit()
                    sleep(2*x)
                    print("Vous vous reveillez au millieu de la clairière.")
                    sleep(2*x)
                    clairiere()
            elif loup == False:
                question4()
            print("Vous continuez votre chemin dans la forêt")
            sleep(2.5*x)
            print("Après quelques minutes de marche, vous entendez des cris.")
            sleep(3.5*x)
            print("Vous vous hâtez pour aller voir ce qui se passe")
            sleep(3.5*x)
            print("Vous appercevez une cabane au loin.")
            sleep(2.5*x)
            print("C'est de là bas que les cris proviennent!")
            sleep(3.5*x)
            print("En entrant dans la cabane, vous voyez un vieil homme et un monstre couvert d'une sorte d'infection")
            sleep(4*x)
            print("Vous arrivez finnalement à vous débarasser du monstre.")
            sleep(2.5*x)
            print("-Merci beaucoup! Sans votre aide j'y serais probablement resté.    dit le vieil homme.")
            sleep(3*x)
            print("Ce monstre vient d'un autre monde appelé l'Umbral.")
            sleep(2*x)
            print("Vous devez entrer dans ce monde et arrêter le chef des lieux: Vincent le sanglant.")
            sleep(3.5*x)
            print("Pour cela, entrez dans le portail là bas. Il vous faudra prononcer les mots scellés du temple devant le portail.")
            sleep(4*x)
            print("Avant de partir prenez ceci pour m'avoir sauvé la vie.")
            sleep(3*x)
            print("Vous recevez 100 pièces!")
            argent+=100
            sleep(1.5*x)
            print("Vous retournez dans la forêt.")
            sleep(2*x)
            question4()




        def temple():
            global temple_ouvert
            if temple_ouvert == False:
                if "clef_maudite" in inventaire:
                    print("La clef ouvre le temple.")
                    temple_ouvert = True
                    temple()
                else:
                    print("Vous arrivez devant le temple mais il est fermé.")
                    clairiere()
            if temple_ouvert == True:
                def au_fond():
                    global attaque
                    print("Vous continuez votre chemin dans le temple.")
                    sleep(2*x)
                    print("Vous trouvez un autel antique")
                    if "parchemin" in inventaire:
                        print("Vous poser le parchemin antique dessus et il disparait en brûlant.")
                        sleep(2*x)
                        print("Vous vous sentez plus fort.")
                        sleep(2*x)
                        print("dégats augmentés de 5!")
                        attaque+=5
                        sleep(2 * x)
                        print("Vous continuez")
                        sleep(2 * x)
                    else:
                        print("Vous ne pouvez rien faire ici et vous continuez votre chemin")
                        sleep(2 * x)
                    print("Vous arrivez au bout du temple")
                    sleep(2 * x)
                    print("Sur une grande tablette sont inscrits les mots scellés:")
                    sleep(1*x)
                    print("'Umbral ouvre toi'")
                    sleep(4*x)
                    if gardien == True:
                        print("Vous retournez à la clairière en esquivant le gardien.")
                    elif gardien == False:
                        print("Vous retournez à la clairière.")
                    clairiere()

                def ruse():
                    global vie
                    if "parchemin" in inventaire:
                        print("Vous faites mine d'être aussi un gardien grâce à votre parchemin antique et réussissez à passer derrière lui.")
                        sleep(3.5*x)
                        au_fond()
                    else:
                        print("Vous faites mine d'être aussi un gardien mais comme vous n'avez pas de preuve, il ne vous croit pas et vous tue.")
                        sleep(2*x)
                        print("Vous perdez une vie.")
                        sleep(1.5*x)
                        vie = vie-1
                        if vie == 0:
                            print("Vous n'avez plus de vie!")
                            sleep(2)
                            print("Sans votre aide, Vincent le sanglant a réussi à sortir de l'Umbral et a pris le contrôle du monde!")
                            sleep(3)
                            print("GAME OVER")
                            sys.exit()
                        print("Vous vous reveillez dans la clairière.")
                        clairiere()
                def bourin():
                    global gardien
                    global argent
                    if attaque >=20:
                        print("Vous sautez sur le gardien avec une force colossale. Il sucombe au choc.")
                        sleep(2*x)
                        print("Vous gagnez 50 pièces!")
                        argent+=50
                        gardien = False
                        au_fond()
                    else:
                        global vie
                        print("Vous foncez tête baissée sur le gardien. Il ne bouge pas et vous rend le coup.")
                        sleep(2*x)
                        print("Il vous écrabouille et vous perdez une vie")
                        vie-=1
                        if vie == 0:
                            print("Vous n'avez plus de vie!")
                            sleep(2)
                            print("Sans votre aide, Vincent le sanglant a réussi à sortir de l'Umbral et a pris le contrôle du monde!")
                            sleep(3)
                            print("GAME OVER")
                            sys.exit()
                        sleep(2*x)
                        print("Vous vous reveillez au millieu de la clairière.")
                        clairiere()
                def question6():
                    reponse=input("Que voulez-vous faire?  Le bourin, le rusé ou retourner à la clairière?")
                    if reponse == "bourin":
                        bourin()
                    elif reponse == "rusé":
                        ruse()
                    elif reponse == "clairière":
                        clairiere()
                    else:
                        print("Orthographe mauvais")
                        sleep(1 * x)
                        question6()
                print("Vous entrez dans le temple")
                sleep(2*x)
                global gardien
                if gardien == True:
                    print("Vous avancez à travers les pièces quand soudain, un gardien vous bloque la route.")
                    sleep(2.5 * x)
                    print("-Ces lieux sont interdits, personne ne passera.   dit le gardien.")
                    question6()
                else:
                    au_fond()
        def puit():
            global puit
            if puit == True:
                print("Il n'y a plus rien à faire au puit. Vous retournez dans la clairière.")
                sleep(2*x)
                clairiere()
            print("Vous arrivez devant un puit très profond.")
            sleep(2*x)
            if "corde" in inventaire:
                print("Vous voyez quelque chose briller au fond et decidez d'aller le chercher en utilisant la corde")
                sleep(2*x)
                inventaire.remove("corde")
                print("Au fond du puit se trouve une clef toute noire mais très brillante.")
                sleep(2*x)
                print("Vous remontez le puit et repartez dans la clairière.")
                sleep(2*x)
                inventaire.append("clef_maudite")
                puit = True
                clairiere()
            elif "corde" not in inventaire:
                print("Vous arrivez devant le puit. Quelque chose brille au fond mais le trou est trop profond pour sauter dedans.")
                sleep(3*x)
                print("Vous retournez dans la clairière.")
                sleep(2*x)
                clairiere()
        reponse = input("Où voulez-vous aller?")
        if reponse == "village":
            village()
        elif reponse == "puit":
            puit()
        elif reponse == "temple":
            temple()
        elif reponse == "forêt":
            foret()
        else:
            print("Orthagraphe mauvais.")
            sleep(1*x)
            question1()
    print("Il y a 4 chemins.")
    sleep(1*x)
    print("Un mène à un village.")
    sleep(1*x)
    print("Un mène à un puit.")
    sleep(1*x)
    print("Un mène à une forêt.")
    sleep(1*x)
    print("Le dernier mène à un temple.")
    sleep(1*x)
    question1()
clairiere()

