inventaire = []  

PV = 100

def montrer_vie():
    print(f"Points de vie restants : {PV}")

def monde_magique():
    global PV
    PV = 100
    inventaire.clear()
    montrer_vie()
    print("")
    print("Vous vous téléportez dans un monde magique.")
    print("")
    reponse = input("suite ? (oui)")
    while reponse not in ["oui"]:
        reponse = input("suite (oui)")
    print("")
    forêt()

def forêt():
    montrer_vie()
    print("")
    print("Vous vous retrouvez dans la forêt.")
    print("")
    print("Il fait sombre et vous voyez une source de lumière.")
    print("")
    print("Vous décidez d'y aller et vous voyez deux chemins.")
    print("")
    print("À gauche se trouve une grotte sinistre.")
    print("")
    print("Et à droite se trouve une jungle.")
    print("")
    print("Deux choix s'offrent à vous.")
    print("")
    reponse = input("gauche ou droite ? ")
    while reponse not in ["gauche", "droite"]:
        reponse = input("gauche ou droite ? ")
        print("")

    if reponse == "gauche":
        print("")
        grotte_sinistre()

    elif reponse == "droite":
        print("")
        jungle()

def grotte_sinistre():
    montrer_vie()
    print("")
    print("Vous entrez dans la grotte sinistre.")
    print("")
    print("Vous voyez quelque chose briller par terre.")
    print("")

    reponse = input("Ramasser l'objet ? (oui/non) ")
    while reponse not in ["oui", "non"]:
        reponse = input("Ramasser l'objet ? (oui/non) ")
        print("")

    if reponse == "oui":
        print("")
        print("Vous avez trouvé une \033[92mépée magique\033[0m.")
        inventaire.append("épée magique")
        print("")
        print("Épée ajoutée à l'inventaire :", inventaire)
        print("")
        rivière()

    elif reponse == "non":
        print("")
        print("Vous continuez votre chemin.")
        print("")
        rivière()

def rivière():
    montrer_vie()
    print("")
    print("Vous apercevez une rivière au loin.")
    print("")
    reponse = input("Traverser la rivière ? (oui/non) ")
    while reponse not in ["oui", "non"]:
        reponse = input("Traverser la rivière ? (oui/non) ")
        print("")

    if reponse == "oui":
        print("")
        print("Vous arrivez maintenant face à un donjon.")
        print("")
        reponse = input("Voulez-vous entrer dans le donjon ? (oui/non)")
        while reponse not in ["oui", "non"]:
            reponse = input("Voulez-vous entrer dans le donjon ? (oui/non)")
            print("")

        if reponse == "oui":
            print("")
            donjon()

        elif reponse == "non":
            print("")
            print("Vous sortez de la grotte et vous revenez dans la forêt.")
            print("")
            forêt()

    elif reponse == "non":
        print("")
        print("Vous sortez de la grotte et vous revenez dans la forêt.")
        print("")
        forêt()

def château():
    montrer_vie()
    print("")
    reponse = input("Voulez-vous aller au château ? (oui/non) ")
    while reponse not in ["oui", "non"]:
        reponse = input("Voulez-vous aller au château ? (oui/non) ")
        print("")

    if reponse == "oui":
        print("")
        print("Vous pénétrez dans le château.")
        print("")
        print("Vous apercevez une armure.")
        print("")
        reponse = input("Voulez-vous prendre l'armure ? (oui/non) ")
        while reponse not in ["oui", "non"]:
            reponse = input("Voulez-vous prendre l'armure ? (oui/non) ")
            print("")

        if reponse == "oui":
            print("")
            print("Vous avez pris l'\033[92marmure\033[0m.")
            inventaire.append("armure")
            print("")
            print("L'armure a été ajoutée à l'inventaire :", inventaire)
            print("")
            print("Vous rencontrez le gardien fou et il vous agresse")
            print("")
            reponse = input("Voulez-vous vous enfuir ? (oui/non) ")
            while reponse not in ["oui", "non"]:
                reponse = input("Voulez-vous vous enfuir ? (oui/non) ")
                print("")

            if reponse == "non":
                global PV
                PV -= 100
                print("")
                montrer_vie()
                print("")
                print("\033[91mVous restez sur place et le gardien fou vous tue\033[0m")
                print("")
                print("\033[91mGAME OVER\033[0m")
                print("")
                monde_magique()

            elif reponse == "oui":
                PV -= 100
                print("")
                montrer_vie()
                print("")
                print("\033[91mVous commencez à courir mais l'armure est trop lourde et il vous rattrape\033[0m")
                print("")
                print("\033[91mLe gardien fou vous tue\033[0m")
                print("")
                print("\033[91mGAME OVER\033[0m")
                print("")
                monde_magique()

        elif reponse == "non":
            print("")
            print("Vous rencontrez le gardien fou et il vous agresse")
            print("")
            reponse = input("Voulez-vous vous enfuir ? (oui/non) ")
            while reponse not in ["oui", "non"]:
                reponse = input("Voulez-vous vous enfuir ? (oui/non) ")
                print("")

            if reponse == "non":
                PV -= 100
                print("")
                montrer_vie()
                print("")
                print("\033[91mVous restez sur place et le gardien fou vous tue\033[0m")
                print("")
                print("\033[91mGAME OVER\033[0m")
                print("")
                monde_magique()

            elif reponse == "oui":
                print("")
                print("Grâce à votre agilité vous réussissez à le semer")
                print("")
                print("Vous avez réussi à sortir et vous voyez un portail et une échelle devant")
                print("")
                reponse = input("Choisissez-vous l'échelle ou le portail? (échelle/portail) ")
                while reponse not in ["échelle", "portail"]:
                    reponse = input("Choisissez-vous l'échelle ou le portail ? (portail/échelle")
                    print("")

                if reponse == "portail":
                    print("\033[35mVous avez réussi à vous échapper et vous revenez dans votre monde\033[0m")
                    print("\033[35mBravo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0m")
                    inventaire.clear()
                    print("")
                    monde_magique()

                elif reponse == "échelle":
                    print("")
                    print("Vous grimpez sur l'échelle et continuer votre route et arrivez près d'une ville")
                    print("")
                    print("Vous avez faim et vous voyez une ville au loin")
                    print("")
                    reponse = input("Voulez-vous aller en ville ? (oui/non)")
                    while reponse not in ["oui", "non"]:
                        reponse = input("Voulez-vous aller en ville ? (oui/non)")
                        print("")

                    if reponse == "oui":
                        print("")
                        print("\033[35mVous vous nourrissez et vous trouvez pas hasard un portail magique qui vous fait revenir dans votre monde\033[0m")
                        print("")
                        print("\033[35mBravo !!!!!!!!!!!!!\033[0m")
                        print("")
                        monde_magique()

                    elif reponse == "non":
                        PV -= 100
                        print("")
                        montrer_vie()
                        print("")
                        print("\033[91mUn groupe de brigands qui rôdait autour de la ville vous entoure\033[0m")
                        print("")
                        print("\033[91mGAME OVER\033[0m")


    elif reponse == "non":
        PV -= 100
        print("")
        montrer_vie()
        print("")
        print("\033[91mVous restez dans la forêt et un groupe de gobelin vous attaque\033[0m")
        print("")
        print("\033[91mVous essayez de vous battre mais en vain\033[0m")
        print("")
        print("\033[91mGAME OVER\033[0m")
        print("")
        monde_magique()


def jungle():
    montrer_vie()
    print("")
    print("Vous pénétrez dans la jungle.")
    print("")
    print("Vous voyez un château.")
    print("")
    château()


def donjon():
    montrer_vie()
    print("")
    global PV 
    print("Inventaire :", inventaire)
    print("")
    print("À peine rentré dans la salle du donjon, les portes se referment violemment derrière vous.")
    print("")
    print("Et vous subissez l'embuscade d'un ogre.")

    survie = "survie" if "épée magique" in inventaire else "meurs"

    if survie == "meurs":
        print("")
        print("\033[91mN'ayant rien pour vous défendre, vous vous faites assommer par l'ogre\033[0m")
        print("")
        print("\033[91mGAME OVER\033[0m")
        print("")
        monde_magique()

    elif survie == "survie":
        print("")
        print("Grâce à votre épée magique, vous réussissez à infliger des dégâts à l'ogre.")
        print("")
        print("En combattant l'ogre, vous voyez une potion par terre.")
        print("")

        reponse = input("Ramasser la potion ? (oui/non) ")
        print("")

        while reponse not in ["oui", "non"]:
            reponse = input("Ramasser la potion ? (oui/non) ")
            print("")

        if reponse == "oui":
            print("")
            print("Vous avez ramassé une \033[92mpotion de vie\033[0m.")
            print("")
            inventaire.append("potion de vie")
            print("potion de vie ajoutée à l'inventaire :", inventaire)
            print("")
            print("En vous concentrant sur la potion, l'ogre vous met un coup de massue empoisonnée.")
            PV -= 50
            print("")
            print("Votre vie a été réduite de 50 points par le poison de la massue et vous perdez 5 PV par seconde !")
            print("")
            montrer_vie()
            print("")
            print("Vous essayez votre dernière option qui est de boire la potion")
            print("")
            reponse = input("Voulez-vous boire la potion ? (oui/non)")

            if reponse == "oui":
                inventaire.remove("potion de vie")
                PV = 100
                print("")
                montrer_vie()
                print("")
                print("Vous réussissez à vaincre l'ogre.")
                print("")
                print("Un coffre apparaît.")
                print("")
                reponse = input("Ouvrir le coffre ? (oui/non)")

                while reponse not in ["oui", "non"]:
                    reponse = input("Ouvrir le coffre ? (oui/non)")

                if reponse == "oui":
                    print("")
                    print("Vous avez ramassé une \033[92mpotion suspecte\033[0m.")
                    inventaire.append("potion suspecte")
                    print("")
                    print("potion suspecte ajoutée à l'inventaire :", inventaire)
                    print("")
                    reponse = input("Boire la potion ? (oui/non) ")
                    while reponse not in ["oui", "non"]:
                        reponse = input("Boire la potion suspect? (oui/non)")

                    if reponse == "oui":
                        print("")
                        print("Vous décidez de boire la potion suspect")
                        print("")
                        PV -= 100

                    if PV <= 0:
                        print("Vous buvez la potion suspecte ")
                        print("")
                        montrer_vie()
                        print("")
                        print("\033[91mVous vous empoisonnez avec la potion\033[0m")
                        print("")
                        print("\033[91mVous mourrez dans d'atroces souffrances\033[0m")
                        print("")
                        print("\033[91mGAME OVER\033[0m")
                        print("")
                        monde_magique()

                    elif reponse == "non":
                        print("")
                        print("Vous décidez de ne pas boire la potion suspect")
                        print("")
                        print("Le coffre vous aspire et vous ramène dans votre monde")
                        print("")
                        print("BRAVO !!!!")
                        print("")
                        monde_magique()

                elif reponse == "non":
                    print("")
                    forêt()

            elif reponse == "non":
                print("")
                print("Vous décidez de ne pas boire la potion.")
                print("")
                PV -= 50

                if PV <= 0:
                    print("Vous perdez 5 PV par seconde à cause du poison ! ")
                    print("")
                    montrer_vie()
                    print("")
                    print("\033[91mVous n'avez pas réussi à vous débarrasser du poison\033[0m")
                    print("")
                    print("\033[91mGAME OVER\033[0m")
                    print("")
                    monde_magique()

        elif reponse == "non":
            print("En vous concentrant sur la potion, l'ogre vous met un coup de massue empoisonnée.")
            print("")
            print("Vous perdez 5 PV par seconde à cause du poison ! ")
            print("")
            PV -=100
            montrer_vie()
            print("")
            print("\033[91mVous n'avez pas réussi à vous débarrasser du poison\033[0m")
            print("")
            print("\033[91mGAME OVER\033[0m")
            print("")
            monde_magique()



print("")
print("Inventaire :", inventaire)
print("")
monde_magique()

