print("Vous êtes au finfond d'une bibliothèque infinie. Vous voyez 2 livres.")
inventaire = ["bracelet celtique"]  # inventaire initial
fraise = 1
grain = 2
amis = 0


def argente_gauche():
    global fraise, grain


    print("Vous entrez dans le royaume des fées en passant sous une cascade. Vous rencontrez des fées qui vous aident dans vos recherches, cela vous permet de trouver 6 fraises")
    fraise += 6

    reponse = input("Souhaitez-vous aller dans la ferme céleste ou rendre visite aux fées floraliennes?")
    while reponse not in ["dans la ferme céleste", "rendre visite aux fées floraliennes"]:
        reponse = input("Vous devez choisir entre la ferme céleste ou rendre visite aux fées floraliennes?")

    if reponse == "rendre visite aux fées floraliennes":
        print("Vous faites la connaissance de Fiora, une fée sylvestre aux cheveux faits de liane et de feuille d'or. Elle vous offre un sac à pollen d'étoiles. Vous avez 2 grains et dès qu'un grain brille, le pollen s'active pour accéder à un souvenir lointain.")
        print("Un grain brille!")
        reponse = input("Désirez-vous pénétrer dans un souvenir?")
        while reponse not in ["oui", "non"]:
            reponse = input("Désirez-vous pénétrer dans un souvenir?")

        if reponse == "oui":
            grain -= 1
            print("Vous vous retrouvez dans le souvenir de la famine.")
            reponse = input("Voulez-vous manger l'une de vos fraises ?")
            while reponse not in ["oui", "non"]:
                reponse = input("Voulez-vous manger l'une de vos fraises?")


            if reponse == "oui":
                fraise -= 1
                print("Vous manger l'une de vos fraises à contrecœur.")

            else:
                reponse = input("Voulez-vous utiliser votre dernier grain pour partir d'ici?")
                while reponse not in ["oui", "non"]:
                    reponse = input("Voulez-vous utiliser votre dernier grain pour fuir?")
                if reponse == "oui":
                    grain -= 1
                    print("Vous arrivez dans un souvenir de créatures géantes.")
                    print("Des hirondelles gloutonnes et des racoones géants dévorent toutes vos fraises.")
                    fraise = 0
                else:
                    print("Vous mourrez de faim et n'avez plus assez de de fraises pour faire votre tarte aux fraises pour faire plaisir à vos amis")

        else:
            print("Vous trouvez parterre une clé")
            inventaire.append("clé")
            reponse = input("Voler une potion magique à un magicien?")
            while reponse not in ["oui", "non"]:
                reponse = input("Voler une potion magique à un magicien?")

            if reponse == "oui":
                print("Le magicien vous transforme en grenouille")
                if "clé" in inventaire:
                    print("Heureusement, la clé vous permet de fuir")
            else:
                if "clé" in inventaire:
                    print("Vous entrez dans un monde où chacun est libre des ses choix et où tout le monde est bienveillant et il n'y a pas de conflits, votre but ultime est à présent de répandre le bonheur.")
                    inventaire.append("bonheur")
                if "bonheur" in inventaire:
                    print("Vous ne vous souciez plus de l'avis des autres, vous avez appris à vous aimer, vous osez, vous créez, vous apprenez, et vous décidez de vous consacrer à fond dans ce que vous aimez ! La confection de tarte aux fraises pour répandre le bonheur autour de vous!")

    elif reponse == "dans la ferme céleste":
        print("Vous croisez un chat féérique qui peut voler")
        reponse = input("Souhaitez-vous devenir son ami?")
        while reponse not in ["oui", "non"]:
            reponse = input("Souhaitez-vous devenir son ami?")

        if reponse == "oui":
            print("Vous gagnez un ami qui vous guide dans votre chasse en vous emmenant dans le jardin des fées agricultrices. Cela vous permet de trouver 10 fraises.")
            fraise += 10
            inventaire.append("ami")
        else:
            print("Vous tombez sur Zéphir, une biquette volante. Elle préfère croquer vos fraises, vous en perdez alors 3")
            fraise -= 3


def argente_droite():
    global fraise
    print("Vous entrez dans une clairière où le soleil vous éclaire pour tenter de mieux trouver vos fraises. Grâce à la luminosité vous trouvez 4 fraises.")
    fraise += 4

    reponse = input("Souhaitez-vous explorer les buissons?")
    while reponse not in ["oui", "non"]:
        reponse = input("Souhaitez-vous explorer les buissons?")

    if reponse == "oui":
        print("Vous trouvez 20 fraises magiques qui vous rendent joyeux.")
        fraise = fraise + 20
        inventaire.append("bonheur")
    else:
        print("Vous percutez un ogre champêtre sur votre chemin et il vous agresse. Ce qui vous fait perdre 2 fraises")
        fraise -= 2
        print("Vous trouvez parterre un sifflet de guerre, qui produit un son puissant et strident permettant d'éloigner l'ennemi.")
        inventaire.append("sifflet_de_guerre")
        if "sifflet_de_guerre" in inventaire:
            print("L'ogre vous laisse tranquille")


def mondes():
    global amis
    reponse = input("Vous choisisez le livre doré ou argenté?")
    while reponse not in ["doré", "argenté"]:
        reponse = input("Vous choisissez le livre doré ou argenté?")

    if reponse == "doré":
        print("Le livre vous a transporté dans un autre monde. Vous êtes dans une plaine venteuse. Vous êtes  Ascane, une chasseresse étheré craint de tous. vous avez 0 amis vous allez donc essayer de vous en faire.vous voyez quelque chose qui brille à votre gauche et un château à votre droite.")
        reponse = input("voulez-vous entrer dans le château ou aller voir la chose qui brille ?")
        while reponse not in ["entrer dans le château", "aller voir la chose qui brille"]:
            reponse = input("Voulez-vous entrer dans le château ou aller voir la chose qui brille ?")

        if reponse == "aller voir la chose qui brille":
            print("vous découvrez un petit dragon doré qui brille au soleil et un énorme dragon noir comme la nuit")
            reponse = input("vous parlez aux dragons ou vous fuyez ?")
            while reponse not in ["parler aux dragons", "fuir"]:
                reponse = input("Vous parlez aux dragons ou vous fuiez ?")

            if reponse == "parler aux dragons":
                reponse = input("dire aux dragons qui vous êtes où leur mentir ?")
                while reponse not in ["leur dire qui je suis", "leur mentir"]:
                    reponse = input("dire aux dragons qui vous êtes ou leur mentir ?")

                if reponse == "leur dire qui je suis":
                    print("vous leur dites la vérité, en gage de confiance ils vous offre un corset fait d'écailles de dragons qui vous protègeras.")
                    print("Vous devenez leur cavalière et êtes amis.")
                    print("vous avez 2 amis en plus")
                    amis = amis + 2
                    inventaire.append("corset protecteur en écaille de dragons")

                elif reponse == "leur mentir":
                    print("vous mourrez sous leurs griffes acéré ")
                    print("vous ne pouvez plus avoir d'amis étant donné que vous êtes mort.")
                    mondes()

            elif reponse == "fuir":
                print("vous partez vous réfugier sous un arbre plus loin")
                reponse = input("vous tombez nez à nez avec un jeune homme de votre âge, vous parlez avec la personne ou vous partez ?")
                while reponse not in ["parler avec la personne", "partir"]:
                    reponse = input("Vous tombez nez à nez avec un jeune homme de votre âge, vous parlez avec la personne ou vous partez ?")

                if reponse == "parler avec la personne":
                    print("vous apprenez qu'il s'appelle Xaden. Vous lui racontez ce qu'il vous est arrivé")
                    print("pour que vous puissiez vous protegez, il vous offre une vieille dague qui se prénomme : fend-le -coeur, en gage de son amitié.")
                    print("vous découvrez que la dague est télépathe. Elle devient un de vos précieux allié.")
                    print("vous avez 1 ami en plus")
                    amis = amis + 1
                    inventaire.append("dague télépathe")

                elif reponse == "partir":
                    print("vous vous éloignez sans prêter attention au jeune homme qui vous suit du regard et retournez vers la plaine avec un sentiment de honte du au fait que vous n'avez pas osé lui parler.")
                    amis = amis + 0

        elif reponse == "entrer dans le château":
            print("vous entrez dans le château et bousculez deux personnes d'à peu près votre âge. ")
            reponse = input("vous vous arrêtez pour vous excusez ou vous continuez votre chemin comme de rien ?")
            while reponse not in ["s'arrêter pour s'excuser", "continuer son chemin"]:
                reponse = input("Vous vous arrêtez pour vous excusez ou vous continuez votre chemin comme de rien ?")

            if reponse == "s'arrêter pour s'excuser":
                print("vous vous excusez, faites plus ample connaissance et devenez amis")
                print("vous avez 2 amis de plus")
                amis = amis + 2

            elif reponse == "continuer son chemin":
                print("vous tournez dans un couloir le plus vite possible et vous vous apprêtez à continuer votre chemin quand soudain un groupe de 4 personnes vous arrête")
                reponse = input("vous vous en allez ou vous rester ?")
                while reponse not in ["s'en aller", "rester"]:
                    reponse = input("Vous vous en allez ou vous restez ?")

                if reponse == "s'en aller":
                    print("vous vous empresser de sortir du château et regagnez l'endroit d'où vous venez.")

                elif reponse == "rester":
                    print("le groupe de jeunes vous fait sortir du château de force, vous menacent et s'assurent que vous ne reveniez jamais.")
                    print("vous perdez tous les amis que vous vous êtes fait")
                    mondes()

        print("en rebroussant chemin pour retourner d'où vous venez, un groupe de personnes masquées vous attaquent")
        reponse = input("amis >= 1 ?")
        while reponse not in ["oui", "non"]:
            reponse = input ("amis >= 1 ?")

        if reponse == "oui":
            if "bracelet celtique" in inventaire :
                print ("la chasseresse appelle ses amis avec le bracelet celtique qui la relie avec eux et les informent si l'un d'entre eux est en danger")
                print("il faut que vous vous protegez du danger le temps que vos amis arrivent")

            if "corset protecteur en écaille de dragons" in inventaire:
                print("vous réussissez à n'avoir que quelles égratinures grâce au corset et tous vos amis sont arrivés pour vous aidez")
                print("vous gagnez vous et vos amis la bataille")
                print("Vous n'êtes plus seule, vous restez avec vos amis et vivez encore pleins d'aventures et découvrez le monde avec eux")

            elif "dague télépathe" in inventaire:
                print("vous avez blessé vos agresseurs et n'avez aucune blessure grâce à la dague qui vous avertissait du danger et bessait les attaquants qui se rapprochaient trop de vous")
                print("vos amis arrivent et vous aident à mettre fin à cette bataille")
                print("Vous n'êtes plus seule, vous restez avec vos amis et vivez encore pleins d'aventures et découvrez le monde avec eux")

            elif "bracelet celtique" in inventaire :
                print("Vous êtes blessé et épuisé lorsque vos amis arrivent mais gagnez le combat.")
                print("Vous n'êtes plus seule, vous restez avec vos amis et vivez encore pleins d'aventures et découvrez le monde avec eux")

        elif reponse == "non":
            print("vous arrivez à échapper à vos assaillants de justesse")
            print("vous rentrez chez vous avec vous-même pour seule compagnie.")


    elif reponse == "argenté":
        print("Le livre vous a transporté dans un autre monde. Vous êtes à présent dans la forêt. Vous vous appelez Élara, une nymphe partie à la chasse aux fraises pour faire une tarte aux fraises en vue de régaler vos amis. Vous avez pour l'instant 1 fraise.")
        reponse = input("Voulez-vous aller à gauche ou à droite ?")
        while reponse not in ["gauche", "droite"]:
            reponse = input("Vous devez choisir entre gauche ou droite ?")
        if reponse == "gauche":
            argente_gauche()
        elif reponse == "droite":
            argente_droite()

        if fraise > 10:
            print("Vous pouvez faire votre tarte aux fraises et régaler vos amis.")
        else:
            print("Vous ne pouvez pas faire votre tarte aux fraises et ne régalerez pas vos amis")
        if "bonheur" in inventaire:
            print("🥳Vous avez trouvez le bonheur ! Vous avez gagné le jeu !")


mondes()  # début
