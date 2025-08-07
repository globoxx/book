
import pygame
import sys
pygame.init()
import time




def main():
    def poser_question(question, choix_possibles):
        reponse = input(question + str(choix_possibles))
        while reponse not in choix_possibles:
            reponse = input(question + str(choix_possibles))
        return reponse

    vieduslim = 30
    vie = 20
    inventaire = []
    burger= 10
    banane=5
    jusdorange=2
    vie_de_la_moule=60


    def intro(texte, delai=0.08):
        for lettre in texte:
            sys.stdout.write(lettre)
            sys.stdout.flush()
            time.sleep(delai)
        time.sleep(1)
        print()

    intro("Il y a fort longtemps les humains et les monstres vivèrent en harmonie")
    intro("Mais un jour ils entrèrent en guerre et les humains sortèrent victorieux.")
    intro("Après ça ils scellèrent les monstres dans la montagne ")
    intro("La légende dis que ceux qui s'aventureraient trop loin dans la montagne n'en reviennent jamais.")
    print()
    print('Vous tombez dans un trou trè profonde.')
    time.sleep(2)
    print('Vous vous réveiller sur un tas de fleur jaune.')
    time.sleep(2)
    print('Une fleur qui se baladais dans le coin vous trouve. ')
    time.sleep(3)
    prenom = input("Quel est ton prénom jeune humain ?")
    print("salut",prenom)
    print("Je m'appel Flowey.")
    choix = poser_question("Veux-tu un bonbon pour soigner t'es blessure?",["oui","non"])



    if choix == 'oui':
        print('Tu sens une sensation bizarre dans ta gorge, tu  suffoques et tu meurs')
        print ("FIN")
    elif choix == 'non':
        print("Tu l'a échappé belle")
        choix = poser_question("Tu veux me suivre ? Je t'emmerais à la basse ville",["oui","non"])

    # Embranchement de droite
        if choix =='oui':
            print("Parfait, tu vas voir on ne s'ennuye jamais avec moi !")
            time.sleep(2)
            print("Voilà on est arriver tu va voir c'est super sypmpa ici!")
            time.sleep(1)
            print("Ce village est entièrement enneigé.")
            time.sleep(1)
            print("Bizarre pour une grotte.")
            argent = 0
            print("Tu voies un magasin et dicides d'y entrée.")
            time.sleep(1)
            print("Un chien vous vend de la nourriture")
            if argent == 0 :
                time.sleep(2)
                print ("Tu as",argent,"pièce")
                time.sleep(2)
                print ("Vous ne pouvez rien achtez.")
                time.sleep(2)
                print("Vous quittez le magasin")
                time.sleep(2)

            elif argent > 0 :

                print ("Tu as ",argent, "pièces")
                choix = poser_question("Il y a un burgere(choix1), une banane(choix2) et du jus d'orange(choix3) que prends-tu ?",["1","2","3"])
                if choix == "1":
                    print()
                    argent -= 10
                    inventaire.append(burger)
                    print("Très bien ce burger te rends 10 point de vie dans un combat")
                    time.sleep(1)
                if choix == "2":
                    print()
                    argent -= 3
                    inventaire.append(banane)
                    print("Magnifique, cette banane te donnes +10 de vitesse d'attaque!")
                if choix == "3" :
                    print()
                    argent -= 5
                    inventaire.append(jusdorange)
                    print("Super! Ce jus d'orange te donnera 5 point de dégât en plus pour cette attaque")
            time.sleep(1)
            print("Vous avez", inventaire, "dans votre sac")
            time.sleep(1)
            print("Tu continues ta route")
            time.sleep(1)
            print("Cette ville semble si paisible.")
            time.sleep(1)
            print("La neige est d'un blanc immaculé")
            time.sleep(1)
            choix=poser_question("Veux-tu aller à gauche dans la zone de lave(1) ou aller à droit dans la grotte d'azur(2)?",["1","2"])



            #entrée zone de lave(embranchement de droite)


            if choix == "1":
                print("Plus tu avances plus il fait chaud.")
                time.sleep(2)
                print("La chaleur est insoutenable.")
                time.sleep(2)
                print("Tu n'avais jamais vue de la lave d'autant près.")
                time.sleep(2)
                print("Ce rouge vife détaillé de jaune te donne presque envie de t'envlopper dans ce draps.")
                choix=poser_question("Veux-tu te jetter dans la lave?",["oui","non"])
                if choix== "oui":
                    print("Vous mourrez reposé et en paix")
                    intro("FIN")
                    time.sleep(4)
                    intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")
                    sys.exit()
                elif choix == "non" :
                    print("C'est un choix judicieux.")
                    time.sleep(2)
                    print("Tout d'un coup vous faites face à un petit slim de feu")
                    time.sleep(2)
                    print("Il semble determiné à vous barrer la route, vous êtes obligés de le combattre")
                while vie > 0 and vieduslim > 0:
                    choix=poser_question("Veux-tu attaquer(1), rien faire(2)ou sortir un objet de ton sac (3)? ",["1","2","3"])
                    if choix == "1":
                        vieduslim -= 10
                        print("Vous lui avez infligé 10 points de dégât")
                        time.sleep(2)
                        print("Le monstre à", vieduslim, "")
                    elif choix == "2":
                        vie -= 2
                        print("Le monstre vous a infligé 2 points de dégât")
                        time.sleep(2)
                        print("Vous avez", vie, "points de vie")
                    elif choix in ["3"]:
                        if burger in inventaire:
                            print("Tu sors un burger de ton sac")
                            vie += 10
                            print("Vous mangez un burger qui vous rend 10 points de vie. Vous avez", vie, "points de vie")
                            inventaire.remove(burger)
                        elif banane in inventaire:
                            print("Tu sors une banane de ton sac")
                            time.sleep(2)
                            vie += 5
                            print("Vous mangez une banane qui vous rend 5 points de vie. Vous avez", vie, "points de vie")
                            inventaire.remove(banane)
                        elif jusdorange in inventaire:
                            print("Tu sorts un jus d'orange de ton sac")
                            vie += 2
                            time.sleep(2)
                            print("Vous buvez votre jus d'orange qui vous rend 2 points de vie. Vous avez", vie,
                                  "points de vie")
                            inventaire.remove(jusdorange)

                if vie <= 0:
                    print("Tu es mort")
                elif vieduslim <= 0:
                    print("Bravo, tu as vaincu le monstre !")
                    time.sleep(2)
                    print("Un portail se forme devant toi")
                    time.sleep(2)
                    choix=poser_question("Veux-tu le prendre oui(1) ou non(2)",["1","2"])
                    if choix== "1":
                        print("Tu ressens un sensation bizarre et tu t'évanouis")
                        time.sleep(2)
                        print("À ton réveil, tu te retrouves devant l'intersection devant les deux chemins.")
                        time.sleep(2)



                        # premier portaille,à droit


                        choix=poser_question("Veux-tu aller à droit(1)ou à gauche(2)",["1,""2"])
                        if choix=="1":
                            print("Plus tu avances plus il fait chaud.")
                            time.sleep(2)
                            print("La chaleur est insoutenable.")
                            time.sleep(2)
                            print("Tu repasse devvant cette lave.")
                            time.sleep(2)
                            print(
                            "Ce rouge vife détaillé de jaune te donne toujours envie de t'envlopper dans ce draps.")
                            choix=poser_question("Veux-tu finalement te jetter dans la lave?",["oui","non"])
                            if choix == "oui":
                                print("Vous mourrez reposé et en paix")
                                intro("FIN")
                                time.sleep(4)
                                intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")
                                sys.exit()
                            elif choix == "non":
                                vieduslim=30
                                time.sleep(2)
                                print("Tout d'un coup vous faites face à un petit slim de feu")
                                time.sleep(2)
                                print("Il semble determiné à vous barrer la route, vous êtes obligés de le combattre")
                                while vie > 0 and vieduslim > 0:
                                    choix=poser_question("Veux-tu attaquer(1), rien faire(2)ou sortir un objet de ton sac (3)? ",["1","2","3"])
                                    if choix == "1":
                                        vieduslim -= 10
                                        print("Vous lui avez infligé 10 points de dégât")
                                        time.sleep(2)
                                        print("Le monstre à", vieduslim, "")
                                    elif choix == "2":
                                        vie -= 2
                                        print("Le monstre vous a infligé 2 points de dégât")
                                        time.sleep(2)
                                        print("Vous avez", vie, "points de vie")
                                    elif choix in ["3"]:
                                        if burger in inventaire:
                                            print("Tu sors un burger de ton sac")
                                            vie += 10
                                            print("Vous mangez un burger qui vous rend 10 points de vie. Vous avez",vie, "points de vie")
                                            inventaire.remove(burger)
                                        elif banane in inventaire:
                                            print("Tu sors une banane de ton sac")
                                            time.sleep(2)
                                            vie += 5
                                            print("Vous mangez une banane qui vous rend 5 points de vie. Vous avez",vie, "points de vie")
                                            inventaire.remove(banane)
                                        elif jusdorange in inventaire:
                                            print("Tu sorts un jus d'orange de ton sac")
                                            vie += 2
                                            time.sleep(2)
                                            print("Vous buvez votre jus d'orange qui vous rend 2 points de vie. Vous avez",vie,"points de vie")
                                            inventaire.remove(jusdorange)

                            if vie <= 0:
                                print("Tu es mort")
                                intro("FIN")
                                time.sleep(4)
                                intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")
                            elif vieduslim <= 0:
                                print("Bravo, tu as vaincu le monstre !")
                                time.sleep(2)
                                print("Tu vois la sortie.")
                                time.sleep(2)
                                print("Devant toi le plus beau couché de soleil de ta vie")
                                time.sleep(2)
                                print("Devant ça ton coeur s'emplit de détermination")
                                time.sleep(2)
                                intro("FIN")
                                time.sleep(4)
                                intro("Merci d'avoir joué à ce jeux et j'espère que vous l'avez aprrécier")


                                #premier portail à gauche(embranchen^ment de droit)


                        elif choix=="2":

                            print("Tu t'avances de plus en plus")
                            time.sleep(2)
                            print("L'air est frais et tu te sens reposé.")
                            time.sleep(2)
                            print("De l'eau est sur les deux côtés du chemin.")
                            time.sleep(2)
                            print("Elle est d'un bleu turquoise illuminée et scintillant.")
                            time.sleep(2)
                            print("Une moule géante vous empêche de passer. Vous êtes obligé de la combattre.")
                            while vie > 0 and vie_de_la_moule > 0:
                                choix=poser_question("Veux-tu attaquer(1), rien faire(2)ou sortir un objet de ton sac (3)? ",["1","2","3"])

                                if choix == "1":
                                    vie_de_la_moule -= 10
                                    print("Vous lui avez infligé 10 points de dégât")
                                    time.sleep(2)
                                    print("Le monstre à", vie_de_la_moule, "")
                                elif choix == "2":
                                    vie -= 10
                                    print("Le monstre vous a infligé 10 points de dégât")
                                    time.sleep(2)
                                    print("Vous avez", vie, "points de vie")
                                elif choix in ["3"]:
                                    if burger in inventaire:
                                        print("Tu sors un burger de ton sac")
                                        vie += 10
                                        print("Vous mangez un burger qui vous rend 10 points de vie. Vous avez", vie,
                                              "points de vie")
                                        inventaire.remove(burger)
                                    elif banane in inventaire:
                                        print("Tu sors une banane de ton sac")
                                        time.sleep(2)
                                        vie += 5
                                        print("Vous mangez une banane qui vous rend 5 points de vie. Vous avez", vie,
                                              "points de vie")
                                        inventaire.remove(banane)
                                    elif jusdorange in inventaire:
                                        print("Tu sorts un jus d'orange de ton sac")
                                        vie += 2
                                        time.sleep(2)
                                        print("Vous buvez votre jus d'orange qui vous rend 2 points de vie. Vous avez",
                                              vie,
                                              "points de vie")
                                        inventaire.remove(jusdorange)

                            if vie <= 0:
                                print("Tu es mort")
                                intro("FIN")
                                time.sleep(4)
                                intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")
                            elif vie_de_la_moule <= 0:
                                print("Bravo, tu as vaincu le monstre !")
                                time.sleep(2)
                                print("Tu vois la sortie.")
                                time.sleep(2)
                                print("Devant toi le plus beau couché de soleil de ta vie")
                                time.sleep(2)
                                print("Devant ça ton coeur s'emplit de détermination")
                                time.sleep(2)
                                intro("FIN")
                                time.sleep(4)
                                intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")

                    elif choix== "2":
                        print("Tu vois la sortie")
                        time.sleep(2)
                        print("Aprèes cette longue péripétie tu te dis qu'il faudra fair plus attention à où tu mets les pied")
                        time.sleep(2)
                        intro("FIN")
                        time.sleep(4)
                        intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")








          #entrée dans la grotte d'azure(embrenchement de droite)


            elif choix=="2":
                print("Tu t'avances de plus en plus")
                time.sleep(2)
                print("L'air est frais et tu te sens reposé.")
                time.sleep(2)
                print("De l'eau est sur les deux côtés du chemin.")
                time.sleep(2)
                print("Elle est d'un bleu turquoise illuminée et scintillant.")
                time.sleep(2)
                print("Une moule géante vous empêche de passer. Vous êtes obligé de la combattre.")


                #combat de la moule(embrenchement de droite)


                while vie > 0 and vie_de_la_moule > 0:
                    choix=poser_question("Veux-tu attaquer(1), rien faire(2)ou sortir un objet de ton sac (3)? ",["1","2","3"])

                    if choix == "1":
                        vie_de_la_moule -= 10
                        print("Vous lui avez infligé 10 points de dégât")
                        time.sleep(2)
                        print("Le monstre à", vie_de_la_moule, "")
                    elif choix == "2":
                        vie -= 10
                        print("Le monstre vous a infligé 10 points de dégât")
                        time.sleep(2)
                        print("Vous avez", vie, "points de vie")
                    elif choix in ["3"]:
                        if burger in inventaire:
                            print("Tu sors un burger de ton sac")
                            vie += 10
                            print("Vous mangez un burger qui vous rend 10 points de vie. Vous avez", vie, "points de vie")
                            inventaire.remove(burger)
                        elif banane in inventaire:
                            print("Tu sors une banane de ton sac")
                            time.sleep(2)
                            vie += 5
                            print("Vous mangez une banane qui vous rend 5 points de vie. Vous avez", vie, "points de vie")
                            inventaire.remove(banane)
                        elif jusdorange in inventaire:
                            print("Tu sorts un jus d'orange de ton sac")
                            vie += 2
                            time.sleep(2)
                            print("Vous buvez votre jus d'orange qui vous rend 2 points de vie. Vous avez", vie,
                                  "points de vie")
                            inventaire.remove(jusdorange)

                if vie <= 0:
                    print("Tu es mort")
                    intro("FIN")
                    time.sleep(4)
                    intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")
                elif vie_de_la_moule <= 0:
                    print("Bravo, tu as vaincu le monstre !")
                    print("Un portail se forme devant toi")
                    time.sleep(2)
                    choix=poser_question("Veux-tu le prendre oui(1) ou non(2)",["1","2"])
                    if choix == "1":
                        print("Tu ressens un sensation bizarre et tu t'évanouis")
                        time.sleep(2)
                        print("À ton réveil, tu te retrouves devant l'intersection devant les deux chemins.")
                        time.sleep(2)

                        # deuxième portaille,à droit

                        choix=poser_question("Veux-tu aller à droit(1)ou à gauche(2)",["1","2"])
                        if choix == "1":
                            print("Plus tu avances plus il fait chaud.")
                            time.sleep(2)
                            print("La chaleur est insoutenable.")
                            time.sleep(2)
                            print("Tu repasse devant ce lac de lave.")
                            time.sleep(2)
                            print(
                                "Ce rouge vife détaillé de jaune te donne toujours envie de t'envlopper dans ce draps.")
                            choix=poser_question("Veux-tu enfin te jetter dans la lave?",["oui","non"])
                            if choix == "oui":
                                print("Vous mourrez reposé et en paix")
                            elif choix == "non":
                                vieduslim=30
                                print("C'est un choix judicieux.")
                                time.sleep(2)
                                print("Tout d'un coup vous faites face à un petit slim de feu")
                                time.sleep(2)
                                print("Il semble determiné à vous barrer la route, vous êtes obligés de le combattre")
                            while vie > 0 and vieduslim > 0:
                                choix=poser_question("Veux-tu attaquer(1), rien faire(2)ou sortir un objet de ton sac (3)? ",["1","2","3"])
                                if choix == "1":
                                    vieduslim -= 10
                                    print("Vous lui avez infligé 10 points de dégât")
                                    time.sleep(2)
                                    print("Le monstre à", vieduslim, "")
                                elif choix == "2":
                                    vie -= 2
                                    print("Le monstre vous a infligé 2 points de dégât")
                                    time.sleep(2)
                                    print("Vous avez", vie, "points de vie")
                                elif choix in ["3"]:
                                    if burger in inventaire:
                                        print("Tu sors un burger de ton sac")
                                        vie += 10
                                        print("Vous mangez un burger qui vous rend 10 points de vie. Vous avez", vie,
                                              "points de vie")
                                        inventaire.remove(burger)
                                    elif banane in inventaire:
                                        print("Tu sors une banane de ton sac")
                                        time.sleep(2)
                                        vie += 5
                                        print("Vous mangez une banane qui vous rend 5 points de vie. Vous avez", vie,
                                              "points de vie")
                                        inventaire.remove(banane)
                                    elif jusdorange in inventaire:
                                        print("Tu sorts un jus d'orange de ton sac")
                                        vie += 2
                                        time.sleep(2)
                                        print("Vous buvez votre jus d'orange qui vous rend 2 points de vie. Vous avez",
                                              vie, "points de vie")
                                        inventaire.remove(jusdorange)

                            if vie <= 0:
                                print("Tu es mort")
                                intro("FIN")
                                time.sleep(4)
                                intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")
                            elif vieduslim <= 0:
                                print("Bravo, tu as vaincu le monstre !")
                                time.sleep(2)
                                print("Tu vois la sortie.")
                                time.sleep(2)
                                print("Devant toi le plus beau couché de soleil de ta vie")
                                time.sleep(2)
                                print("Devant ça ton coeur s'emplit de détermination")
                                time.sleep(2)
                                intro("FIN")
                                time.sleep(4)
                                intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")

                                # deuxième portaille à gauche


                        elif choix == "2":
                            vie_de_la_moule=60
                            print("Tu t'avances de plus en plus")
                            time.sleep(1)
                            print("L'air est frais et tu te sens reposé.")
                            time.sleep(2)
                            print("De l'eau est sur les deux côtés du chemin.")
                            time.sleep(2)
                            print("Elle est d'un bleu turquoise illuminée et scintillant.")
                            time.sleep(2)
                            print("Une moule géante vous empêche de passer. Vous êtes obligé de la combattre.")
                            while vie > 0 and vie_de_la_moule > 0:
                                choix=poser_question("Veux-tu attaquer(1), rien faire(2)ou sortir un objet de ton sac (3)? ",["1","2","3"])

                                if choix == "1":
                                    vie_de_la_moule -= 10
                                    print("Vous lui avez infligé 10 points de dégât")
                                    time.sleep(2)
                                    print("Le monstre à", vie_de_la_moule, "")
                                elif choix == "2":
                                    vie -= 10
                                    print("Le monstre vous a infligé 10 points de dégât")
                                    time.sleep(2)
                                    print("Vous avez", vie, "points de vie")
                                elif choix in ["3"]:
                                    if burger in inventaire:
                                        print("Tu sors un burger de ton sac")
                                        vie += 10
                                        print("Vous mangez un burger qui vous rend 10 points de vie. Vous avez", vie,
                                              "points de vie")
                                        inventaire.remove(burger)
                                    elif banane in inventaire:
                                        print("Tu sors une banane de ton sac")
                                        time.sleep(2)
                                        vie += 5
                                        print("Vous mangez une banane qui vous rend 5 points de vie. Vous avez", vie,
                                              "points de vie")
                                        inventaire.remove(banane)
                                    elif jusdorange in inventaire:
                                        print("Tu sorts un jus d'orange de ton sac")
                                        vie += 2
                                        time.sleep(2)
                                        print("Vous buvez votre jus d'orange qui vous rend 2 points de vie. Vous avez",
                                              vie,
                                              "points de vie")
                                        inventaire.remove(jusdorange)

                            if vie <= 0:
                                print("Tu es mort")
                                intro("FIN")
                                time.sleep(4)
                                intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")
                            elif vie_de_la_moule <= 0:
                                print("Bravo, tu as vaincu le monstre !")
                                time.sleep(2)
                                print("Tu vois la sortie.")
                                time.sleep(2)
                                print("Devant toi le plus beau couché de soleil de ta vie")
                                time.sleep(2)
                                print("Devant ça ton coeur s'emplit de détermination")
                                time.sleep(2)
                                intro("FIN")
                                time.sleep(4)
                                intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")

                    elif choix == "2":
                        print("Tu vois la sortie")
                        time.sleep(2)
                        print(
                            "Aprèes cette longue péripétie tu te dis qu'il faudra fair plus attention à où tu mets les pied")
                        time.sleep(2)
                        intro("FIN")
                        time.sleep(4)
                        intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")














            #embranchement de gauche

        elif choix =="non" :
            print("Tu continues ton chemin seule.")
            print("Tu trouves des pièces par terre et tu décides de les garder.")
            time.sleep(3)
            argent=20
            print("Tu as",argent,"pièces")
            time.sleep(1)
            print("Tu trouves un village.")
            time.sleep(1)
            print("Bizarre pour une grotte.")
            time.sleep(1)
            print("Ce village est entièrement enneigé.")
            time.sleep(2)
            print("Bizarre pour une grotte.")
            time.sleep(2)
            print("TU voies un magasin et dicides d'y entrée.")
            time.sleep(1)
            print("Un chien vous vend de la nourriture")
            if argent == 0:
                print("Tu as",argent,"pièce")
                print("Vous ne pouvez rien achetez.")
            elif argent > 0 :
                print("Tu as", argent,"pièces")
                print("Il y a un burgere(choix1), une banane(choix2) et du jus d'orange(choix3) que prenez vous ?")
                choix = poser_question ("Le burger vaut 10,la banane 3 et le jus d'orange 5 ",["1","2","3"])
            if choix == "1":
                print()
                argent -= 10
                inventaire.append(burger)
                print("Très bien ce burger te rends 10 point de vie dans un combat")
                time.sleep(1)

            if choix == "2" :
                print()
                argent -= 3
                inventaire.append(banane)
                print("Magnifique, cette banane te donnes +10 de vitesse d'attaque!")
            if choix == "3":
                print()
                argent -= 5
                inventaire.append(jusdorange)
                print("Super! Ce jus d'orange te donnera 5 point de dégât en plus pour cette attaque")

            time.sleep(1)
            print("Tu continues ta route.")
            time.sleep(1)
            print("Cette ville semble si paisible.")
            time.sleep(1)
            print("La neige est d'un blanc immaculé")
            time.sleep(1)
            print("Bizarre pour une grotte")
            time.sleep(1)
            choix=poser_question("Veux-tu aller à gauche dans la zone de lave(1) ou aller à droit dans la grotte d'azur(2)?",["1","2"])


            #entrée de la zone de lave (embranchement de gauche)



            if choix == "1":
                print("Plus tu avances plus il fait chaud.")
                time.sleep(1)
                print("La chaleur est insoutenable.")
                time.sleep(1)
                print("Tu n'avais jamais vue de la lave d'autant près.")
                time.sleep(1)
                print("Ce rouge vife détaillé de jaune te donne presque envie de t'envlopper dans ce draps.")
                choix=poser_question("Veux-tu te jetter dans la lave?",["oui","non"])
                if choix == "oui":
                    print("Vous mourrez reposé et en paix")
                elif choix == "non":
                    print("C'est un choix judicieux.")
                    time.sleep(1)
                    print("Tout d'un coup vous faites face à un petit slim de feu")
                    time.sleep(1)
                    print("Il semble determiné à vous barrer la route, vous êtes obligés de le combattre")


                    #combat du slim(embranchement de gauche)


                    while vie > 0 and vieduslim > 0:
                        choix=poser_question("Veux-tu attaquer(1), rien faire(2)ou sortir un objet de ton sac (3)? ",["1","2","3"])

                        if choix == "1":
                            vieduslim -= 10
                            print("Vous lui avez infligé 10 points de dégât")
                            time.sleep(2)
                            print("Le monstre à", vieduslim, "")
                        elif choix == "2":
                            vie -= 2
                            print("Le monstre vous a infligé 2 points de dégât")
                            time.sleep(2)
                            print("Vous avez", vie, "points de vie")
                        elif choix in ["3"]:
                            if burger in inventaire:
                                print("Tu sors un burger de ton sac")
                                vie += 10
                                print("Vous mangez un burger qui vous rend 10 points de vie. Vous avez", vie,
                                      "points de vie")
                                inventaire.remove(burger)
                            elif banane in inventaire:
                                print("Tu sors une banane de ton sac")
                                time.sleep(2)
                                vie += 5
                                print("Vous mangez une banane qui vous rend 5 points de vie. Vous avez", vie,
                                      "points de vie")
                                inventaire.remove(banane)
                            elif jusdorange in inventaire:
                                print("Tu sorts un jus d'orange de ton sac")
                                vie += 2
                                time.sleep(2)
                                print("Vous buvez votre jus d'orange qui vous rend 2 points de vie. Vous avez", vie,
                                      "points de vie")
                                inventaire.remove(jusdorange)

                    if vie <= 0:
                        print("Tu es mort")
                        intro("FIN")
                        time.sleep(4)
                        intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")
                    elif vieduslim <= 0:
                        print("Bravo, tu as vaincu le monstre !")
                        print("Un portail se forme devant toi")
                        time.sleep(2)
                        choix=poser_question("Veux-tu le prendre oui(1) ou non(2)",["1","2"])
                        if choix == "1":
                            print("Tu ressens un sensation bizarre et tu t'évanouis")
                            time.sleep(2)
                            print("À ton réveil, tu te retrouves devant l'intersection devant les deux chemins.")
                            time.sleep(2)

                            # deuxièm portaille,après combat du slim(embranchement de gauch)

                            choix=poser_question("Veux-tu aller à droit(1)ou à gauche(2)",["1","2"])
                            if choix == "1":
                                print("Plus tu avances plus il fait chaud.")
                                time.sleep(1)
                                print("La chaleur est insoutenable.")
                                time.sleep(1)
                                print("Tu n'avais jamais vue de la lave d'autant près.")
                                time.sleep(1)
                                print(
                                    "Ce rouge vife détaillé de jaune te donne presque envie de t'envlopper dans ce draps.")
                                choix=poser_question("Veux-tu te jetter dans la lave?",["oui","non"])
                                if choix == "oui":
                                    print("Vous mourrez reposé et en paix")
                                elif choix == "non":
                                    print("C'est un choix judicieux.")
                                    time.sleep(1)
                                    print("Tout d'un coup vous faites face à un petit slim de feu")
                                    time.sleep(1)
                                    print(
                                        "Il semble determiné à vous barrer la route, vous êtes obligés de le combattre")
                                while vie > 0 and vieduslim > 0:
                                    choix=poser_question(
                                        "Veux-tu attaquer(1), rien faire(2)ou sortir un objet de ton sac (3)? ",["1","2","3"])
                                    if choix == "1":
                                        vieduslim -= 10
                                        print("Vous lui avez infligé 10 points de dégât")
                                        time.sleep(2)
                                        print("Le monstre à", vieduslim, "")
                                    elif choix == "2":
                                        vie -= 2
                                        print("Le monstre vous a infligé 2 points de dégât")
                                        time.sleep(2)
                                        print("Vous avez", vie, "points de vie")
                                    elif choix in ["3"]:
                                        if burger in inventaire:
                                            print("Tu sors un burger de ton sac")
                                            vie += 10
                                            print("Vous mangez un burger qui vous rend 10 points de vie. Vous avez",
                                                  vie, "points de vie")
                                            inventaire.remove(burger)
                                        elif banane in inventaire:
                                            print("Tu sors une banane de ton sac")
                                            time.sleep(2)
                                            vie += 5
                                            print("Vous mangez une banane qui vous rend 5 points de vie. Vous avez",
                                                  vie, "points de vie")
                                            inventaire.remove(banane)
                                        elif jusdorange in inventaire:
                                            print("Tu sorts un jus d'orange de ton sac")
                                            vie += 2
                                            time.sleep(2)
                                            print(
                                                "Vous buvez votre jus d'orange qui vous rend 2 points de vie. Vous avez",
                                                vie, "points de vie")
                                            inventaire.remove(jusdorange)

                                if vie <= 0:
                                    print("Tu es mort")
                                    intro("FIN")
                                    time.sleep(4)
                                    intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")
                                elif vieduslim <= 0:
                                    print("Bravo, tu as vaincu le monstre !")
                                    time.sleep(2)
                                    print("Tu vois la sortie.")
                                    time.sleep(1)
                                    print("Devant toi le plus beau couché de soleil de ta vie")
                                    time.sleep(2)
                                    print("Devant ça ton coeur s'emplit de détermination")
                                    time.sleep(2)
                                    intro("FIN")
                                    time.sleep(4)
                                    intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")

                                    # combat de la moule après protail du slim(embranchement de gauch)


                            elif choix == "2":
                                print("Tu t'avances de plus en plus")
                                time.sleep(1)
                                print("L'air est frais et tu te sens reposé.")
                                time.sleep(1)
                                print("De l'eau est sur les deux côtés du chemin.")
                                time.sleep(1)
                                print("Elle est d'un bleu turquoise illuminée et scintillant.")
                                time.sleep(1)
                                print("Une moule géante vous empêche de passer. Vous êtes obligé de la combattre.")
                                while vie > 0 and vie_de_la_moule > 0:
                                    choix=poser_question(
                                        "Veux-tu attaquer(1), rien faire(2)ou sortir un objet de ton sac (3)? ",["1","2","3"])

                                    if choix == "1":
                                        vie_de_la_moule -= 10
                                        print("Vous lui avez infligé 10 points de dégât")
                                        time.sleep(2)
                                        print("Le monstre à", vie_de_la_moule, "")
                                    elif choix == "2":
                                        vie -= 10
                                        print("Le monstre vous a infligé 10 points de dégât")
                                        time.sleep(2)
                                        print("Vous avez", vie, "points de vie")
                                    elif choix in ["3"]:
                                        if burger in inventaire:
                                            print("Tu sors un burger de ton sac")
                                            vie += 10
                                            print("Vous mangez un burger qui vous rend 10 points de vie. Vous avez",
                                                  vie,
                                                  "points de vie")
                                            inventaire.remove(burger)
                                        elif banane in inventaire:
                                            print("Tu sors une banane de ton sac")
                                            time.sleep(2)
                                            vie += 5
                                            print("Vous mangez une banane qui vous rend 5 points de vie. Vous avez",
                                                  vie,
                                                  "points de vie")
                                            inventaire.remove(banane)
                                        elif jusdorange in inventaire:
                                            print("Tu sorts un jus d'orange de ton sac")
                                            vie += 2
                                            time.sleep(2)
                                            print(
                                                "Vous buvez votre jus d'orange qui vous rend 2 points de vie. Vous avez",
                                                vie,
                                                "points de vie")
                                            inventaire.remove(jusdorange)

                                if vie <= 0:
                                    print("Tu es mort")
                                    intro("FIN")
                                    time.sleep(4)
                                    intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")
                                elif vie_de_la_moule <= 0:
                                    print("Bravo, tu as vaincu le monstre !")
                                    time.sleep(2)
                                    print("Tu vois la sortie.")
                                    time.sleep(1)
                                    print("Devant toi le plus beau couché de soleil de ta vie")
                                    time.sleep(2)
                                    print("Devant ça ton coeur s'emplit de détermination")
                                    time.sleep(2)
                                    intro("FIN")
                                    time.sleep(4)
                                    intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")

                        elif choix == "2":
                            print("Tu vois la sortie")
                            time.sleep(2)
                            print(
                                "Aprèes cette longue péripétie tu te dis qu'il faudra fair plus attention à où tu mets les pied")
                            time.sleep(2)
                            intro("FIN")
                            time.sleep(4)
                            intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")

                        # entrée grotte d'azure(enbranchement de gauche)


            elif choix == "2":
                print("Tu t'avances de plus en plus")
                time.sleep(1)
                print("L'air est frais et tu te sens reposé.")
                time.sleep(1)
                print("De l'eau est sur les deux côtés du chemin.")
                time.sleep(1)
                print("Elle est d'un bleu turquoise illuminée et scintillant.")
                time.sleep(1)
                print("Une moule géante vous empêche de passer. Vous êtes obligé de la combattre.")

                    #combat de la moule (embranchement de gauche)

                while vie > 0 and vie_de_la_moule > 0:
                    choix=poser_question("Veux-tu attaquer(1), rien faire(2)ou sortir un objet de ton sac (3)? ",["1","2","3"])

                    if choix == "1":
                        vie_de_la_moule -= 10
                        print("Vous lui avez infligé 10 points de dégât")
                        time.sleep(2)
                        print("Le monstre à", vie_de_la_moule, "")
                    elif choix == "2":
                        vie -= 10
                        print("Le monstre vous a infligé 10 points de dégât")
                        time.sleep(2)
                        print("Vous avez", vie, "points de vie")
                    elif choix in ["3"]:
                        if burger in inventaire:
                            print("Tu sors un burger de ton sac")
                            vie += 10
                            print("Vous mangez un burger qui vous rend 10 points de vie. Vous avez", vie,
                                    "points de vie")
                            inventaire.remove(burger)
                        elif banane in inventaire:
                            print("Tu sors une banane de ton sac")
                            time.sleep(2)
                            vie += 5
                            print("Vous mangez une banane qui vous rend 5 points de vie. Vous avez", vie,
                                      "points de vie")
                            inventaire.remove(banane)
                        elif jusdorange in inventaire:
                            print("Tu sorts un jus d'orange de ton sac")
                            vie += 2
                            time.sleep(2)
                            print("Vous buvez votre jus d'orange qui vous rend 2 points de vie. Vous avez", vie,
                                      "points de vie")
                            inventaire.remove(jusdorange)

                if vie <= 0:
                    print("Tu es mort")
                    intro("FIN")
                    time.sleep(4)
                    intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")
                elif vie_de_la_moule <= 0:
                    print("Bravo, tu as vaincu le monstre !")
                    print("Un portail se forme devant toi")
                    time.sleep(2)
                    choix=poser_question("Veux-tu le prendre oui(1) ou non(2)",["1","2"])
                    if choix == "1":
                        print("Tu ressens un sensation bizarre et tu t'évanouis")
                        time.sleep(2)
                        print("À ton réveil, tu te retrouves devant l'intersection devant les deux chemins.")
                        time.sleep(2)

                            # deuxiem portail après combat de la moule(embranchement de gauch)

                        choix=poser_question("Veux-tu aller à droit(1)ou à gauche(2)",["1","2"])
                        if choix == "1":
                            print("Plus tu avances plus il fait chaud.")
                            time.sleep(1)
                            print("La chaleur est insoutenable.")
                            time.sleep(1)
                            print("Tu n'avais jamais vue de la lave d'autant près.")
                            time.sleep(1)
                            print("Ce rouge vife détaillé de jaune te donne presque envie de t'envlopper dans ce draps.")
                            choix=poser_question("Veux-tu te jetter dans la lave?",["oui","non"])
                            if choix == "oui":
                                print("Vous mourrez reposé et en paix")
                            elif choix == "non":
                                print("C'est un choix judicieux.")
                                time.sleep(1)
                                print("Tout d'un coup vous faites face à un petit slim de feu")
                                time.sleep(1)
                                print("Il semble determiné à vous barrer la route, vous êtes obligés de le combattre")
                                while vie > 0 and vieduslim > 0:
                                    choix=poser_question("Veux-tu attaquer(1), rien faire(2)ou sortir un objet de ton sac (3)? ",["1","2","3"])
                                    if choix == "1":
                                        vieduslim -= 10
                                        print("Vous lui avez infligé 10 points de dégât")
                                        time.sleep(2)
                                        print("Le monstre à", vieduslim, "")
                                    elif choix == "2":
                                        vie -= 2
                                        print("Le monstre vous a infligé 2 points de dégât")
                                        time.sleep(2)
                                        print("Vous avez", vie, "points de vie")
                                    elif choix in ["3"]:
                                        if burger in inventaire:
                                            print("Tu sors un burger de ton sac")
                                            vie += 10
                                            print("Vous mangez un burger qui vous rend 10 points de vie. Vous avez",
                                                  vie, "points de vie")
                                            inventaire.remove(burger)
                                        elif banane in inventaire:
                                            print("Tu sors une banane de ton sac")
                                            time.sleep(2)
                                            vie += 5
                                            print("Vous mangez une banane qui vous rend 5 points de vie. Vous avez",
                                                  vie, "points de vie")
                                            inventaire.remove(banane)
                                        elif jusdorange in inventaire:
                                            print("Tu sorts un jus d'orange de ton sac")
                                            vie += 2
                                            time.sleep(2)
                                            print(
                                                "Vous buvez votre jus d'orange qui vous rend 2 points de vie. Vous avez",
                                                vie, "points de vie")
                                            inventaire.remove(jusdorange)

                                if vie <= 0:
                                    print("Tu es mort")
                                    intro("FIN")
                                    time.sleep(4)
                                    intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")
                                elif vieduslim <= 0:
                                    print("Bravo, tu as vaincu le monstre !")
                                    time.sleep(2)
                                    print("Tu vois la sortie.")
                                    time.sleep(1)
                                    print("Devant toi le plus beau couché de soleil de ta vie")
                                    time.sleep(2)
                                    print("Devant ça ton coeur s'emplit de détermination")
                                    time.sleep(2)
                                    intro("FIN")
                                    time.sleep(4)
                                    intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")

                                    #  combat de la moule après avoir pris le portaille de la moule(embranchement de gauche)


                        elif choix == "2":
                            print("Tu t'avances de plus en plus")
                            time.sleep(1)
                            print("L'air est frais et tu te sens reposé.")
                            time.sleep(1)
                            print("De l'eau est sur les deux côtés du chemin.")
                            time.sleep(1)
                            print("Elle est d'un bleu turquoise illuminée et scintillant.")
                            time.sleep(1)
                            print("Une moule géante vous empêche de passer. Vous êtes obligé de la combattre.")
                            while vie > 0 and vie_de_la_moule > 0:
                                choix=poser_question(
                                    "Veux-tu attaquer(1), rien faire(2)ou sortir un objet de ton sac (3)? ",["1","2","3"])

                                if choix == "1":
                                    vie_de_la_moule -= 10
                                    print("Vous lui avez infligé 10 points de dégât")
                                    time.sleep(2)
                                    print("Le monstre à", vie_de_la_moule, "")
                                elif choix == "2":
                                    vie -= 10
                                    print("Le monstre vous a infligé 10 points de dégât")
                                    time.sleep(2)
                                    print("Vous avez", vie, "points de vie")
                                elif choix in ["3"]:
                                    if burger in inventaire:
                                        print("Tu sors un burger de ton sac")
                                        vie += 10
                                        print("Vous mangez un burger qui vous rend 10 points de vie. Vous avez",
                                                  vie,
                                                  "points de vie")
                                        inventaire.remove(burger)
                                    elif banane in inventaire:
                                        print("Tu sors une banane de ton sac")
                                        time.sleep(2)
                                        vie += 5
                                        print("Vous mangez une banane qui vous rend 5 points de vie. Vous avez",
                                                  vie,
                                                  "points de vie")
                                        inventaire.remove(banane)
                                    elif jusdorange in inventaire:
                                        print("Tu sorts un jus d'orange de ton sac")
                                        vie += 2
                                        time.sleep(2)
                                        print(
                                                "Vous buvez votre jus d'orange qui vous rend 2 points de vie. Vous avez",
                                                vie,
                                                "points de vie")
                                        inventaire.remove(jusdorange)

                            if vie <= 0:
                                print("Tu es mort")
                                intro("FIN")
                                time.sleep(4)
                                intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")
                            elif vie_de_la_moule <= 0:
                                print("Bravo, tu as vaincu le monstre !")
                                time.sleep(2)
                                print("Tu vois la sortie.")
                                time.sleep(1)
                                print("Devant toi le plus beau couché de soleil de ta vie")
                                time.sleep(2)
                                print("Devant ça ton coeur s'emplit de détermination")
                                time.sleep(2)
                                intro("FIN")
                                time.sleep(4)
                                intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")

                    elif choix == "2":
                        print("Tu vois la sortie")
                        time.sleep(2)
                        print(
                                "Aprèes cette longue péripétie tu te dis qu'il faudra fair plus attention à où tu mets les pied")
                        time.sleep(2)
                        intro("FIN")
                        time.sleep(4)
                        intro("Merci d'avoir joué à ce jeux et j'espère que vous avez aprrécier")

main()