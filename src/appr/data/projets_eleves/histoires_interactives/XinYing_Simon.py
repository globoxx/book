import time
from random import*

# Fonction principale pour gérer les PV et redémarrer le jeu si nécessaire
def gestion_pv(pv):
    if pv <= 0:
        print("Game Over! Le voyageur a succombé à ses blessures.")
        time.sleep(2)
        print("Redémarrage du jeu...")
        time.sleep(2)
        return False
    return True
def text(texte):
    for lettre in texte:
        print(lettre, end="")
        time.sleep(0.0)
    print()
def text1(texte):
    for lettre in texte:
        print(lettre, end="")
        time.sleep(0.0)
    print()

# Fonction pour l'histoire à Fontaine
def Fontaine():
    pv=100
    inventaire = []

    text("Vous vous réveillez à Fontaine, la cité de l'eau et de la justice.")
    text("Après quelques temps d'exploration, un jour vous arrivez devant une satue imance d'une déesse.")

    text("La déesse étais Furina, la déesse hydro et de la justice")

    text("En s'approchant de la statue, une lumière bleue sorti de la statue et entra dans votre corp")

    text("vous senti soudain quelques choses de different dans votre corp, vous levez la main au ciel ")

    text("et soudian une tube l'eau sorti de votre main et projète jusqu'au ciel")

    text("Vous avez reçu le control de l'élément hydro.")

    text("ce qui auparavant,était uniquement destiné aux possesseurs d'une vison hydro")

    text("Les gardes de Fontaine, les Argents, vous arrêtent immédiatement.")

    text("Ils vous accusent d'avoir perturbé l'ordre public.")


    # Premier choix : se révolter ou non
    while True :
        choix = input("Que faites-vous ? (1: Se révolter / 2: Ne pas se révolter) : ")
        if choix == "1":
            text("Vous décidez de vous révolter contre les gardes.")

            text("Les gardes ripostent avec force. Vous perdez 20 PV.")
            pv -= 20
            if not gestion_pv(pv):
                return
            break
        elif choix == "2":
            text("Vous décidez de ne pas résister et de suivre les gardes.")

            text("Vous êtes emmené devant Neuvillette, le juge suprême de Fontaine.")
            time.sleep(2)
            break
        else :
            print("choix invalide,veuillez réessayer")


    text1("++++++++++++++++++++++++++++++++++++++++++++++++++")
    # Deuxième choix : protester ou non devant Neuvillette
    text("Vous êtes maintenant dans l'Opéra Epiclèse, face à Neuvillette et Furina la déesse hydro")

    text("Furina regarde le procès comme une pièce d'opéra")

    text("Neuvillette vous accuse de crimes graves et vous demande de plaider votre cas.")

    while True:
        choix = input("Que faites-vous ? (1: Protester / 2: Ne pas protester) : ")

        if choix == "1":
            text("Vous décidez de protester contre l'accusation.")

            text("Neuvillette ordonne à Clorinde, la championne de duel, de vous affronter.")

            text("Le combat est acharné, mais vous perdez 80 PV.")
            pv -= 80
            if not gestion_pv(pv):
                return pv
            text("Vous êtes condamné à 2 ans de prison.")
            time.sleep(2)
        elif choix == "2":
            text("Vous décidez de ne pas protester et d'accepter votre sort.")

            text("Neuvillette, impressionné par votre humilité, réduit votre peine.")

            text("Vous êtes condamné à 3 mois de prison.")

            break
        else:
            text("Choix invalide. Veuillez réessayer.")


    text1("++++++++++++++++++++++++++++++++++++++++++++++++++")
    text("\nVous arrivez à la forteresse de Méropide, une prison sous-marine mystérieuse.")

    text("Dans un coin sombre, vous entendez une voix mélodieuse chanter des chansons sur les mythes de Fontaine.")


    # Choix : s'approcher du poète ou non
    while True:
        choix = input("Que faites-vous ? (1: S'approcher du poète / 2: Ignorer le poète) : ")

        if choix == "1":
            text("\nVous vous approchez du poète, un homme venu de Mondstadt ,le pays du vent et de la liberté.")

            text("Il chante une chanson étrange :")

            text("'Tous les Fontainiens vont se fondre dans l'eau, laissant la déesse pleurer seule dans son royaume.'")

            text("Le poète vous explique que cette chanson raconte un ancien mythe de Fontaine.")

            text("Il vous confie ensuite que quelqu'un a volé sa lyre magique, un objet précieux pour lui.")


            # Choix : aider le poète ou non
            while True:
                choix = input("Souhaitez-vous l'aider à retrouver sa lyre ? (1: Oui / 2: Non) : ")

                if choix == "1":
                    text("\nVous acceptez d'aider le poète à retrouver sa lyre magique.")

                    text("Vous commencez votre enquête dans la prison et trouvez trois suspects :")

                    text("1. Sigewinne, l'infirmière de la prison.")
                    text("2. Jimmy, un prisonnier mystérieux.")
                    text("3. Son, un prtit garçon")


                    # Choix : qui interroger ?
                    while True:
                        choix = input("Qui décidez-vous d'interroger en premier ? (1: Sigewinne / 2: Jimmy / 3: Son) : ")

                        if choix == "1":
                            text("\nVous interrogez Sigewinne, l'infirmière de la prison.")

                            text("Elle vous assure qu'elle n'a pas volé la lyre, mais elle propose de vous aider à trouver le vrai coupable.")

                            text("Pendant votre enquête, Sigewinne vous offre une boisson faite maison.")
                            # Choix : boire la boisson ou non
                            while True:
                                choix = input("Voulez-vous boire la boisson ? (1: Oui / 2: Non) : ")

                                if choix == "1":
                                    text("\nVous buvez la boisson et vous sentez revigoré ! Vous gagnez 50 PV.")
                                    pv += 50
                                    text(f"Vous avez maintenant {pv} PV.")
                                    break
                                elif choix=="2":
                                    text("\Vous refusez poliment la boisson.")
                                    break
                                else:
                                    text("choix invalide,veuillez reéssayer")

                            text("Avec l'aide de Sigewinne, vous finissez par découvrir que Jimmy est le vrai voleur.")

                            text("Vous retrouvez la lyre magique et la rapportez au poète.")
                            break



                        elif choix == "2":
                            text("\nVous interrogez Jimmy, un prisonnier mystérieux.")

                            text("Il avoue immédiatement être le voleur et vous rend la lyre magique.")

                            text("Vous rapportez la lyre au poète.")
                            break

                        elif choix == "3":
                            text("\nVous interrogez Son, un autre prisonnier.")

                            text("Il vous assure qu'il n'a rien à voir avec le vol, mais vous perdez du temps à le croire.")

                            text("Vous finissez par découvrir que Jimmy est le vrai voleur, mais vous perdez 10 PV à cause du temps perdu.")
                            pv -= 10
                            if not gestion_pv(pv):
                                return
                            text(f"Vous avez maintenant {pv} PV.")

                            text("Vous rapportez la lyre au poète.")
                            break
                        else:
                            text("choix invalide,veuillez reéssayer")


                    # Choix : rendre la lyre ou la garder
                    while True:
                        choix = input("Souhaitez-vous rendre la lyre au poète ? (1: Oui / 2: Non) : ")

                        if choix == "1":
                            text("\nVous rendez la lyre au poète, qui est extrêmement reconnaissant.")

                            text("En remerciement, il vous donne une 'bouteille de vent venu de Barbatos, le dieu Anemo'.")

                            text("Vous buvez la bouteille et gagnez 80 PV !")
                            pv += 80
                            text(f"Vous avez maintenant {pv} PV.")
                            break
                        elif choix=="2":
                            text("\nVous décidez de garder la lyre magique pour vous.")
                            inventaire.append("Lyre magique")
                            text("La lyre magique a été ajoutée à votre inventaire.")
                            break
                        else:
                            text("choix invalide,veuillez reéssayer")
                    break

                elif choix=="2":
                    text("\nVous décidez de ne pas aider le poète et continuez votre chemin.")

                    break
                else:
                    text("choix invalide,veuillez reéssayez")
            break


        elif choix =="2":
            text("\nVous ignorez le poète et continuez votre chemin dans la prison.")
            break
        else:
            text("choix invalide,veuillez reéssayer")


    # Rencontre avec Wriothesley
    text("\nVous faites la rencontre de Wriothesley, le chef de la forteresse de Méropide.")




    text("\nWriothesley vous observe avec un regard sérieux.")
    text("Wriothesley : 'Je suis impressionné par vos capacités à maîtriser les éléments sans Vision.'")

    text("Wriothesley : 'Nous avons besoin de votre aide pour empêcher une catastrophe. L'eau Primordial menace de s'échapper.'")

    text("Wriothesley : 'Si elle entre en contact avec les Fontainiens, elle les fera fondre. Nous devons agir vite.'")

    text("Wriothesley : 'En échange de votre aide, je vous libérerai 3 mois plus tôt.'")


    # Choix : aider Wriothesley ou non
    while True:
        choix = input("Acceptez-vous d'aider Wriothesley ? (1: Oui / 2: Non) : ")

        if choix == "1":
            text("\nVous acceptez d'aider Wriothesley à empêcher la catastrophe.")

            text("Vous vous rendez avec Wriothesley et Clorinde à la soupape qui contient l'eau Primordial.")

            text("La pression à l'intérieur de la soupape est beaucoup trop élevée.")

            text("Soudain, la soupape explose, libérant l'eau Primordial !")

            text("L'eau jaillit de partout, et vous voyez des Fontainiens fondre au contact de cette eau.")

            text("Heureusement, l'eau Primordial semble ne pas avoir d'effet sur vous.")

            text("Cependant, l'explosion vous a blessé. Vous perdez 20 PV.")
            pv -= 20
            if not gestion_pv(pv):
                return
            text(f"Vous avez maintenant {pv} PV.")

            text("Nevillette arrive juste à temps et utilise ses pouvoirs pour contrôler l'eau Primordial.")

            text("Il parvient à la repousser dans la soupape et à sceller la brèche.")

            text("Nevillette : 'Nous avons évité le pire, grâce à vous.'")

            text("Wriothesley : 'Vous avez tenu votre promesse. Vous serez libéré 3 mois plus tôt.'")

            text("Vous avez sauvé Fontaine de la catastrophe !")
            break


        elif choix=="2":
            text("\nVous décidez de ne pas aider Wriothesley.")
            time.sleep(2)


            text("Soudain, vous assistez à une scène de chaos : l'eau Primordial s'est échappée !")

            text("Vous voyez des Fontainiens fondre au contact de cette eau, mais elle n'a aucun effet sur vous.")

            text("L'explosion de la soupape vous blesse tout de même. Vous perdez 20 PV.")
            pv -= 20
            if not gestion_pv(pv):
                return
            text(f"Vous avez maintenant {pv} PV.")

            text("Nevillette arrive juste à temps et utilise ses pouvoirs pour contrôler l'eau Primordial.")

            text("Il parvient à la repousser dans la soupape et à sceller la brèche.")

            text("Nevillette : 'Nous avons évité le pire, mais beaucoup ont souffert.'")

            text("Vous réalisez que votre aide aurait pu sauver plus de vies.")
            break
        else:
            text("choix invalide,Veuillez réessayer")


    text(f"Vos PV actuels : {pv}")
    text(f"Votre inventaire : {inventaire}")

    text1("++++++++++++++++++++++++++++++++++++++++++++++++++")
    text("\nquelques temps plutard, le jour de votre libération arrive enfin.")

    text("Vous sortez de la forteresse de Méropide, mais quelqu'un vous attend déjà.")

    text("C'est Arlecchino, la 4ème chef des Fatui, connue pour son calme et sa détermination.")

    text(" 'Les Fatui font partie des forces de la Déesse Cryo, et nous avons un objectif clair.'")

    text("Arlecchino : 'Je suis impressionnée par votre réputation, voyageur.'")
    text("Arlecchino : 'Nous recherchons les Gnosis, des artefacts divins qui permettent aux dieux d'exercer leur pouvoir.'")

    text("Arlecchino : 'La Gnosis Hydro est celle que nous convoitons ici à Fontaine.'")

    text("Arlecchino : 'Chaque dieu contrôle une règle de Teyvat. La Déesse Hydro contrôle la loi et la justice.'")

    text("Arlecchino : 'Mais je soupçonne Furina, la prétendue Déesse Hydro, d'être une impostrice.'")

    text("Arlecchino : 'Lors d'une soirée, je l'ai attaquée. Elle était faible, apeurée, et m'a suppliée de ne pas la tuer.'")

    text("Arlecchino : 'Une vraie déesse n'aurait jamais agi ainsi. Elle doit être jugée.'")

    text("Vous: Mais si Furina n'est pas la déesse, qui pourrait être la vrai déesse?")

    text("Arlecchino:Je pense que c'est le grand juge Neuvillette.")

    text("Arlecchino:Je l'ai dêja vu utilier ses pouvoirs,il a un control absolu sur l'eau")

    text("Son calme et sa tranquiltité fait qu'il ressemble beaucoup plus à un dieu que Furina")

    text("Arlecchino : Aidez-moi à porter plainte auprès de Neuvillette.")

    text("Arlecchino:Ne t'inquiete pas ,il ne pourra pas refuser.")
    text("Arlecchino:Avec les preuves que j'ai recolté,elle ne pourra pas gagner")
    # Choix : aider Arlecchino ou non
    while True:
        choix = input("Acceptez-vous d'aider Arlecchino ? (1: Oui / 2: Non) : ")
        if choix == "1":
            text("\nVous acceptez d'aider Arlecchino à démasquer Furina.")

            text1("++++++++++++++++++++++++++++++++++++++++++++++++++")

            text("Vous ètes arrivé au Palais de Mermonia, là où travail Neuvillete")

            text("Vous lui expliquez votre doute envers Furina")

            text("Neuvillette:...")

            text("Neuvillette:Je connais la mythe aussi")

            text("Neuvillette:J'ai essayé de demander à la déesse une solution")

            text("Neuvillette:Mais elle m'évite")

            text("Neuvillette:Je veux vous inviter à chercher une solution dans la place des secrets")

            while True:
                choix=input("Voulez vous aider Neuvillette? (1:oui /2:non)")
                if choix=="1":
                    text1("++++++++++++++++++++++++++++++++++++++++++++++++++")
                    text("Vous ètes dans la place des secrets")
                    text("L'atmosphère est étrange, comme si le temps y était suspendu.")
                    text("Soudain, une petite fée lumineuse apparaît devant vous.")
                    text("Fée : 'Oh ! Un visiteur ! Suivez-moi, je dois vous montrer quelque chose !'")

                    choix_fee = input("Suivez-vous la fée ? (1: Oui / 2: Non) : ")
                    while True:
                        if choix_fee == "1":
                            text("\nVous suivez la fée à travers des couloirs invisibles.")
                            text(
                                "Elle s’arrête devant une fontaine ancienne et se transforme en une silhouette majestueuse.")
                            text("Egeria : 'Je suis Egeria, la première Déesse Hydro. Fontaine est en danger.'")
                            text("Egeria : 'Prenez ce dé magique. Il vous aidera à rétablir la vérité.'")
                            inventaire.append("Dé magique d'Egeria")
                            text("Le *Dé magique d'Egeria* a été ajouté à votre inventaire.")
                            break
                        elif choix_fee== "2":
                            text("vous choisissez de ne pas suivre la fée")
                            break
                        else:
                            text("choix invalide,veuillez reéssayer")
                    text("\nPlus loin, vous remarquez une pierre mystérieuse gravée de symboles anciens.")
                    text("Inscription sur la pierre : *'Tout va se terminer dans un grand procès contre la Déesse de Justice.'*")
                    text1("++++++++++++++++++++++++++++++++++++++++++++++++++")
                    text("Vous retournez voir Neuvillette au Palais de Justice pour lui rapporter vos découvertes.")
                    text("Neuvillette : 'Alors... Furina devra enfin répondre de ses actes.'")
                    text("Neuvillette : 'Préparez-vous. Le plus grand procès de l'histoire de Fontaine va commencer.'")
                    text1("++++++++++++++++++++++++++++++++++++++++++++++++++")
                    text("Vous ètes à l'Opéra Epiclèse")

                    text("La salle est comble. Neuvillette préside le procès le plus important de l'histoire de Fontaine.")
                    text("Vous vous levez pour accuser Furina :")
                    text("Vous : 'Furina a trompé Fontaine en prétendant être la Déesse Hydro depuis 500 ans !'")

                    text("\nFurina, visiblement nerveuse, se lève pour se défendre :")
                    text("Furina : 'C'est absurde ! Comment une simple humaine pourrait-elle vivre 500 ans ?'")
                    text("La foule murmure, impressionnée par cet argument.")


                    text("Comment contrer son argument ?")
                    if "Dé magique d'Egeria" in inventaire:
                        text("1 : Utiliser l'eau Primordial ")
                        text("2 : Présenter le Dé magique d'Egeria ")
                        while True:
                            choix = input("Votre choix (1/2) : ")

                            if choix == "1":
                                text("\nVous demandez qu'on apporte un récipient d'eau Primordial.")
                                text("Vous : 'Si tu es vraiment la Déesse Hydro, cette eau ne te fera rien.'")
                                text("Vous tendez le récipient à Furina sous les regards horrifiés de l'assemblée.")

                                text("\nFurina hésite pendant de longues secondes, sa main tremble visiblement...")
                                text("Finalement, elle plonge sa main dans l'eau Primordial.")
                                text("Contrairement aux Fontainiens normaux, elle ne fond pas...")
                                text("Mais Furina semble très afaiblie ")
                                text("ce qui est la reaction normal d'un fontainien en contact avec peu d'eau primordial")

                                text("\nLa foule explose : 'C'est un humain, elle n'est pas une déesse!!'")
                                text("Neuvillette frappe son marteau : 'La preuve est faite ! Furina est coupable'")
                                text("\n Soudain, l'Oratrice Mecanique d'Analyse Cardinale se met a fonctionner")
                                text("il a donné sa reponse, Furina est coupable")
                                text("Elle sera puni de la mort")
                                break

                            elif choix == "2" and "Dé magique d'Egeria" in inventaire:
                                text("\nVous brandissez le Dé magique d'Egeria :")
                                text("Vous : 'Egeria m'a confié ceci. Si tu es la vrai deésse tu pourrais alors faire briller cet dé'")
                                text("Furina pris la dé dans la main , rien ne se passe")

                                text("\n Soudain, l'Oratrice Mecanique d'Analyse Cardinale se met a fonctionner")
                                text("il a donné sa reponse, Furina est coupable")
                                text("Elle sera puni de la mort")
                                break
                            else:
                                text("choix invalide, veuillez reéssayer")
                    else:
                        text("\nVous demandez qu'on apporte un récipient d'eau Primordial.")
                        text("Vous : 'Si tu es vraiment la Déesse Hydro, cette eau ne te fera rien.'")
                        text("Vous tendez le récipient à Furina sous les regards horrifiés de l'assemblée.")

                        text("\nFurina hésite pendant de longues secondes, sa main tremble visiblement...")
                        text("Finalement, elle plonge sa main dans l'eau Primordial.")
                        text("Contrairement aux Fontainiens normaux, elle ne fond pas...")
                        text("Mais Furina semble très afaiblie ")
                        text("ce qui est la reaction normal d'un fontainien en contact avec peu d'eau primordial")

                        text("\nLa foule explose : 'C'est un humain, elle n'est pas une déesse!!'")
                        text("Neuvillette frappe son marteau : 'La preuve est faite ! Furina est coupable'")
                        text("\n Soudain, l'Oratrice Mecanique d'Analyse Cardinale se met a fonctionner")
                        text("il a donné sa reponse, Furina est coupable")
                        text("Elle sera puni de la mort")


                    text("Furina s'effondre en larmes :")
                    text(
                        "Furina : 'Je... je devais jouer ce rôle ! Sinon le vrai jugement serait arrivé trop tôt !'")
                    text("Soudain, la salle tremble. L'océan au-dehors commence à bouillonner anormalement.")
                    text1("Neuvillette : 'La prophétie... elle s'accomplit MAINTENANT ?!'")


                    text("La véritable crise de Fontaine commence. Préparez-vous pour le chapitre final !")




                    text("Soudain, le temps semble se figer autour de vous. Tout devient blanc...")
                    text("Vous et Neuvillette vous retrouvez sur une scène d'opéra déserte.")
                    text(
                        "Devant vous apparaît une silhouette ressemblant à Furina, mais irradiant une puissance divine.")

                    text("\nFocalors : 'Je suis Focalors, la véritable Déesse Hydro.'")
                    text("Neuvillette:Comment?")
                    text(
                        "Focalors : 'Il y a 500 ans, je me suis scindée en deux : Furina, mon humanité, et moi-même, la divinité.'")
                    text(
                        "Focalors : 'Pendant que Furina jouait mon rôle, je me cachais dans l'Oratrice Mécanique.'")
                    text(
                        "Focalors : 'J'ai accumulé assez d'énergie pour briser le Trône Hydro... et rendre son pouvoir à Neuvillette.'")


                    text(
                        "Focalors entame une danse gracieuse, son corps commence à se dissoudre en lumière bleutée.")
                    text("Focalors : 'Neuvillette... avec ce pouvoir... libérez notre peuple de la malédiction.'")
                    text("Dans un éblouissement, le Trône Hydro explose en milliards de bulles scintillantes.")
                    text("Et Focalors disparait dans cette lumière blanche")


                    text("Vous revenez brusquement à l'Opéra Epiclèse. Furina sanglote, inconsolable.")
                    text("Soudain, les murs tremblent - une BALEINE PRIMORDIALE géante perce le plafond !")
                    text("La créature ouvre sa gueule démesurée, attirant Furina vers elle comme un vortex !")

                    if "Lyre magique" in inventaire:

                        text(
                            "Soudain,dans votre inventaire,la Lyre magique commence à briller.")
                        text("Un vent puissant jaillit, contrebalançant l'attraction !")
                        text("Neuvillette : 'Barbatos ?!'. ")
                        text("Le vent forme un bouclier autour de Furina.")
                        text("La baleine rugit de frustration avant de disparaître dans un tourbillon d'écume.")
                        text("Furina s'effondre dans vos bras, sauvée de justesse.")
                        inventaire.remove("Lyre magique")
                    else:

                        text("Vous tendez désespérément la main... mais rien ne peut arrêter la baleine.")
                        text("Furina pousse un dernier cri avant d'être engloutie dans les abysses.")
                        text("Neuvillette hurle de rage impuissante.")
                        text("La balène disparait dans un tourbillon d'écume")

                    from random import randint



                    pv_baleine = 150
                    rounds = 0

                    text1("++++++++++++++++++++++++++++++++++++++++++++++++++")
                    text("Vous plongez dans le tourbillon avec Neuvillette. Tout autour, l'eau Primordial gronde.")
                    text("La Baleine Primordiale (150 PV) vous fait face dans une gigantesque bulle sous-marine!")

                    while pv_baleine > 0 and pv > 0 and rounds < 3:
                        rounds += 1
                        text(f"\n--- Round {rounds} ---")
                        text(f"Vos PV: {pv} | PV Baleine: {pv_baleine}")
                        while True:

                            if "Dé magique d'Egeria" in inventaire:
                                choix = input(
                                    "Choisissez votre action (1: Attaquer / 2: Défendre / 3: Utiliser le Dé magique): ")
                            else:
                                choix = input("Choisissez votre action (1: Attaquer / 2: Défendre): ")

                            # Actions du joueur
                            if choix == "1":  # Attaque
                                degats = 30
                                pv_baleine -= degats
                                text(f"Vous frappez la Baleine avec une attaque élémentaire! (-{degats} PV)")
                                break
                            elif choix == "2":  # Défense
                                text("Vous vous préparez à parer l'attaque...")
                                break
                            elif choix == "3" and "Dé magique d'Egeria" in inventaire:  # Dé magique
                                valeur_de = randint(1, 6)
                                degats = valeur_de * 10
                                pv_baleine -= degats
                                text(f"Vous lancez le Dé magique... il montre {valeur_de}! (-{degats} PV à la Baleine)")
                                break
                            else:
                                text("choix invalide, veuillez reéssayer")

                        # Attaque de la Baleine (sauf si défense)
                        if choix != "2" and pv_baleine > 0:
                            pv -= 30
                            text(f"La Baleine vous frappe violemment! (-30 PV) Il vous reste {pv}")
                            if not gestion_pv(pv):
                                return

                    # Attaque ultime au 4ème round
                    if pv > 0 and pv_baleine > 0:
                        text("\nLa Baleine rugit et prépare son attaque ultime!")
                        if choix == "2":  # Si défense au dernier tour
                            text("Grâce à votre position défensive, vous évitez le pire! (-100 PV au lieu de 200)")
                            pv -= 100

                        else:
                            text("La Baleine déchaîne un tsunami d'eau Primordial! (-200 PV)")
                            pv -= 200
                        if not gestion_pv(pv):
                            return

                    # Résultat du combat
                    if pv_baleine <= 0:
                        text("\n=== Victoire! ===")
                        text("La Baleine Primordiale se dissout dans l'eau")

                    else:
                        text("\n=== Défaite... ===")
                        text("La Baleine triomphe avant de disparaître dans les abysses.")
                        text("Game Over - Fontaine est submergée")
                        return







                    text("Avec la destruction du Trône Hydro, les eaux refluent progressivement.")
                    text("Neuvillette, désormais doté du plein pouvoir draconique, lève les bras :")
                    text("Neuvillette : 'Par ce jugement... que la malédiction des Fontainiens soit levée !'")
                    text("Une pluie curative s'abat sur Fontaine, guérissant les corps et les âmes.")

                    text("\nVotre aventure à Fontaine se termine ici...")
                    text(f"PV finaux : {pv}")
                    text(f"Inventaire final : {inventaire}")
                    text("Merci d'avoir joué à cette aventure Genshin Impact !")

                    break


                elif choix == "2":
                    text("\nVous décidez de ne pas aider Neuvillette.")

                    text("Neuvillette : 'Très bien. Je trouverai une autre manière d'accomplir ma mission.'")

                    text("Vous restez quelques jours à Fontaine, vous profitez de la liberté et du beau temps")

                    text("Finalement, vous quittez Fontaine pour continuer votre quête et chercher des pistes sur votre sœur.")
                    break

                else:
                    text("choix invalide,Veuillez réessayer")

            break
        elif choix=="2":
            text("\nVous décidez de ne pas aider Arlecchino.")

            text("Arlecchino : 'Très bien. Je trouverai une autre manière d'accomplir ma mission.'")

            text("Vous restez quelques jours à Fontaine, mais sans intervenir dans les affaires des Fatui.")

            text("Finalement, vous quittez Fontaine pour continuer votre quête et chercher des pistes sur votre sœur.")
            break



            text(f"Vos PV actuels : {pv}")
            text(f"Votre inventaire : {inventaire}")
            break

        else:
            text("choix invalide,Veuillez réessayer")

def Mondstadt(pv):

    text("Tu te réveille à Mondstadt. La cité de la liberté. Le vent frais est comme entrain de te murmurer ses secrets. Tu commences avec 100hp. ")




    def dosdragon(pv):

        def grandfroid(pv):
            text("PLouf plouf *son de tes pv qui baissent")
            pv -= 10
            if not gestion_pv(pv):
                return


        def dosdragonseul(pv):


            def resolution(pv):
                text("Tu continues ton exploration de la montagne. ")
                if "Mika" in compagnon:
                    text("Mika connait un cité perdue.")
                    text("Vous tombez sur un gardien des ruines géants qui vous inflige 50 dégats")
                    pv -= 50
                    if not gestion_pv(pv):
                        return
                    text("Grace a votre talent, et un peu de chance, vous survivez. Mika t'emmene au quartier principal des chevalier de Favonius. Il t'offrent le Gnosis Anemo car ils sont impressionné par ton talent")
                    inventaire.append("Gnosis_Anemo")

                elif "Bennett" in compagnon:
                    text("On se la gèle ! Bennett allume un feu. Tu gagne 50 pv.")
                    text("Tu t'entends super bien avec Bennett, tu continues tes aventures avec lui.")
                    text("Un jour, en ouvrant un coffre, vous tombez par hasard sur un Gnosis Anemo")
                    inventaire.append("Gnosis_Anemo")

                elif "Sucrose" in compagnon:
                    text("Sucrose te montre son site de recherche. Tu apprends qu'elle fait de l'alchimie et te montre les bases. Avant de partir de la montagne enneigée, elle te propose deux de ses potions. La potion pourpre, qu'elle a confectionné quelque mois auparavant ainsi que la portion violette, qu'elle vient de préparer.")
                    while True :
                        choix = input("Quel potion choisis tu ? (1:La potion pourpre /2: La potion violette")
                        if choix == "1":
                            grandfroid(pv)
                            inventaire.append("potion_pourpre")
                            break
                        elif choix == "2":
                            grandfroid(pv)
                            inventaire.append("potion_violette")
                            break
                text("Après cette longue expédition, ton aventure à Dosdragon se termine là.")
                text("Xin Ying n'a pas eu le temps d'écrire une suite compliquée. Le gnosis Anemo tombe du ciel")
                inventaire.append("Gnosis_Anemo")




            def croisement():
                    choix = input("(1: Grotte sombre /2: Chemin déneigé /3: Sentier sinueux)")

                    if choix == "1":
                        grandfroid(pv)
                        text("Tu rencontre Bennett, un aventurier malchanceux. C'est super de te rencontrer !- Bennett")

                        while True:
                            choix = input("Explorer Dosdragon avec Bennett ?(1: oui / 2: non)")
                            if choix == "1":
                                grandfroid(pv)
                                compagnon.append("Bennett")
                                text("Tu explore la montagne avec Bennett.")
                                while True :
                                    choix = input("Revenir sur tes pas ?(1: oui / 2: non)")
                                    if choix == "1":
                                        grandfroid(pv)
                                        text("Te revoila au croisement, veux tu prendre les autres directions ?")
                                        while True :

                                            if choix == "1":
                                                grandfroid(pv)
                                                croisement()
                                    if choix == "2":
                                        resolution()
                                        break
                                break
                            elif choix == "2":
                                grandfroid(pv)
                                text("Bennett repart, déçu.")
                                break
                                while True :
                                    choix = input("Revenir sur tes pas ?(1: oui / 2: non)")
                                    if choix == "1":
                                        grandfroid(pv)
                                        text("Te revoila au croisement, veux tu prendre les autres directions ?")
                                        while True :

                                            if choix == "1":
                                                grandfroid(pv)
                                                croisement()

                                    elif choix == "2":
                                        grandfroid(pv)
                                        resolution()
                                        break




                    elif choix == "2":
                        grandfroid(pv)
                        text("Tu tombe sur Sucrose, une chercheuse passionée." )
                        while True:
                            choix = input("Explorer Dosdragon avec Sucrose?(1: oui / 2: non)")
                            if choix == "1":
                                grandfroid(pv)
                                compagnon.append("Sucrose")
                                text("Tu explore la montagne avec Sucrose.")
                                while True :
                                    choix = input("Revenir sur tes pas ?(1: oui / 2: non)")
                                    if choix == "1":
                                        grandfroid(pv)
                                        text("Te revoila au croisement, veux tu prendre les autres directions ?")
                                        while True :

                                            if choix == "1":
                                                grandfroid(pv)
                                                croisement()
                                    if choix == "2":
                                        resolution()
                                        break
                            elif choix == "2":
                                grandfroid(pv)
                                text("Sucrose repart, déçu.")
                                break
                                while True :
                                    choix = input("Revenir sur tes pas ?(1: oui / 2: non)")
                                    if choix == "1":
                                        grandfroid(pv)
                                        text("Te revoila au croisement, veux tu prendre les autres directions ?")
                                        while True :

                                            if choix == "1":
                                                grandfroid(pv)
                                                croisement()
                                                break

                                    elif choix == "2":
                                        grandfroid(pv)
                                        resolution()
                                        break


                    elif choix == "3":
                        grandfroid(pv)
                        text("Tu croise Mika, c'est un chevalier en reparage ")
                        while True:
                            choix = input("Explorer Dosdragon avec Mika ?(1: oui / 2: non)")
                            if choix == "1":
                                grandfroid(pv)
                                compagnon.append("Mika")
                                text("Tu explore la montagne avec Mika")
                                while True :
                                    choix = input("Revenir sur tes pas ?(1: oui / 2: non)")
                                    if choix == "1":
                                        grandfroid(pv)
                                        choix=input("Te revoila au croisement, veux tu prendre les autres directions ?(1:oui/2:non)")
                                        break
                                        while True :

                                            if choix == "1":
                                                grandfroid(pv)
                                                croisement()
                                                break
                                    if choix == "2":
                                        resolution(pv)
                                        break

                            if choix == "2":
                                grandfroid(pv)
                                text("Mika repart, déçu.")
                                break
                                while True :
                                    choix = input("Revenir sur tes pas ?(1: oui / 2: non)")
                                    if choix == "1":
                                        grandfroid(pv)
                                        choix=input("Te revoila au croisement, veux tu prendre les autres directions ?(1:oui/2:non")
                                        break
                                        while True:
                                            if choix == "1":
                                                grandfroid(pv)
                                                croisement()
                                                break

                                    elif choix == "2":
                                        grandfroid(pv)
                                        resolution()
                                        break
                    else:
                        croisement()

            compagnon = []
            text("Tu explore Dosdragon seul.")
            text("En t'enfoncant dans la montagne, tu arrive a un croisement. Dans quel direction vas tu ?")
            croisement()

        def dosdragonaventurier():
            grandfroid(pv)
            text(
                "Tu rencontre Joel, un enfant qui cherche son père aventurier. Il était parti en excursion, mais n'est toujours pas revenu depuis. ")
            while True:
                choix = input ("L'aider? (1: oui / 2: non) ")
                if choix == "1":
                        grandfroid(pv)
                        text("++++++++++")
                        text("A le demande de Joel, tu te rends au campement de son père.")
                        text("Il n'est pas la, en revanche, tu trouve deux notes intacts dans un coin.")
                        break
                        while True:
                            choix = input ("Lire quel note ? (1: la première note / 2: la deuxième note)")
                            if choix == "1":
                                grandfroid(pv)
                                text("'La tempête de neige a ensevelis tous mes provisions, je n'ai plus rien a manger'")
                                break
                            if choix =="2":
                                grandfroid(pv)
                                text("Les animaux de la montagne sont vraiment interéssant, je voudrai pouvoir les observer de plus pres. Peut etre que je pourrai mieux les voir depuis la Vallée du Dragon ronflant.")
                                break
                elif choix == "2":
                    grandfroid(pv)
                    dosdragonseul()
                    break










        #def grandfroid():
            #pv = 100
            #start = time.time()
            #duree = time.time() - start
            #if duree > 2:
                    #text("il fait froid ! tu perds 10 pv")
                    #pv -= 10
            #if not gestion_pv(pv):
                #return



        pv = 100
        text("Tu arrive à Dosdragon. L'air commence a se refroidir. Le paysage bleuté scintillait a chaque rayon de soleil.")
        time.sleep(1)
        text("Attention, il fait froid à Dosdragon, tu perds du pv à chaque décision!")
        time.sleep(1)
        text("Tu vois un regroupement d'aventurier. Peut etre qu'ils pourront te renseigner sur la montagne.")

        while True:
            choix = input( "Parler au aventurier ? (1: oui / 2: non)")
            if choix == "1":
                dosdragonaventurier()
                break

            elif choix == "2":
                grandfroid(pv)
                dosdragonseul(pv)
                break



        #while choix
    def ville():

        text("Une violente tempte frappe la ville,tu vas te refugier.")





    inventaire =[]
    #pygame.mixer.init()
    #pygame.mixer.music.load('')

    while True :
        choix = input("Dans quel direction marcher ? (1: Marcher en direction de la ville / 2: Marcher en direction de la montagne enneigé)")


        if choix =="1":
            ville()
            text("Oups, cette partie de l'histoire n'a pas pu etre écrite, tu vas directement etre teleporté a Dosdragon")
            dosdragon(pv)
            break

        elif choix == "2":
            dosdragon(pv)
            break

    #if "Gnosis_Anemo" in inventaire:






# Démarrage du jeu

text("vous ètes un voyageur qui voyage avec votre soeur")
text("Lors de votre voyage dans ce monde nommé Tayvat vous et votre soeur rencontrez beaucoup de problèmes.")
text("vous descidez de partir de ce monde.")
text("lorsque vous ètes arrivez à la frontière, une déesse arrète votre chemin.")
text("Elle se nommait Sustainer et vous empèche de partir de ce monde.")
text("Après une dure bataille vous avez perdu.")
text("votre soeur se fait capturer et vous vous endormez")


text("Le voyageur commence avec 100 PV et un inventaire vide.")
text("Faites des choix judicieux pour survivre à cette aventure !")



text("Où choisissez vous vous reveiller?")
while True:
    choix=input("1.Mondstadt 2.Fontaine :")
    if choix== "2":
        text1("++++++++++++++++++++++++++++++++++++++++++++++++++")
        Fontaine()
        Mondstadt(100)
        break

    elif choix=="1":
        text1("++++++++++++++++++++++++++++++++++++++++++++++++++")
        Mondstadt(100)
        Fontaine()

    else:
        text("choix invalide,veuillez réessayer")

