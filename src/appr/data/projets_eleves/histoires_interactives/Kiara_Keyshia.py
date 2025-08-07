print("Tu as pour mission de sauver la princesse Fiona. Cependant, des épreuves t'attendent! Tu as à ta disposition 5h.")
temps = 5
inventaire = []
def histoire():
    global temps
    def debut():
        global temps
        reponse = input("Accepte-tu la mission? oui ou non?")
        if reponse == "oui":
            print("Quelle courage! Tu te retrouves dans le village lointain-lointain. Tu ramènes avec toi une epée et de la nourriture. ")
            reponse = input("Tu veux te deplacer à pied ou à cheval?")
            if reponse == "à pied":
                print("Tu arrives 1h après devant une grotte.")
                temps = temps - 1
            elif reponse == "à cheval":
                print("tu arrives en 30min devant la grotte. Quelle vitesse!")
                temps = temps - 0.5
            else:
                print("Pourquoi tu reponds autre chose, tu recommences!")
                debut()
        else:
            print("Tu n'as pas assez de courage. Quelle honte!!!! Reessaye!")
            debut()


    debut()

    def village_lointain_lointain():
        reponse = input("Tu trouves une lampe-torche par terre, veux-tu la ramasser?")
        if reponse == "oui":
            print("Bon choix! Tu continue ta recherche de la princesse Fiona.")
            inventaire.append("lampe-torche")
        elif reponse == "non":
            print("Moi à ta place je l'aurais pris, mais tu continue à marcher...")
        else:
            village_lointain_lointain()

    village_lointain_lointain()

    print("Tu retournes devant l'entrée de la grotte. Malheureusement, il fait noir dans la grotte, tu as besoin d'une lampe-torche.")
    if "lampe-torche" in inventaire:
        print("Vu que t'es intelligent, tu l'avais pris donc tu peux continuer facilement ton chemin.")
        temps = temps - 1
    else:
        print("Tu prends plus de temps car tu ne vois plus rien.")
        temps = temps - 1.5

    def foret():
        print("Tu es enfin sorti de cette grotte. Tu te retrouves dans une foret.")
        reponse = input("Veux-tu récolter du bois ?")
        if reponse == "oui":
            print("Tu n'es pas bête. Maintenant tu possèdes du bois.")
            inventaire.append("bois")
        else:
            print("Tant pis pour toi.")

    foret()

    print("Tu traverses la forêt et t'arrives devant deux chemins: une rivière et un champs.")
    def chemins():
        global temps
        reponse = input("rivière ou champs ?")
        if reponse == "rivière":
            if "bois" in inventaire:
                print("Vu que tu es quelqu'un de prudent tu as pris du bois et tu te fabriques un bâteau")
                temps = temps - 1.5
            else:
                print("Tu ne peux pas car tu n'as pas les matériaux.")
                chemins()
        elif reponse == "champs":
            print ("Tu prends beaucoup trop de temps à traverser.")
            temps = temps - 2.5

    chemins()

    print("Tu es enfin arriver et t'arrives devant la tour à Fiona. Devant la tour se trouve un dragon que tu dois combattre. ")
    reponse = input("Veux-tu le combattre ?")
    if reponse == "oui":
        if temps > 0:
            print("Tu l'as combattu grâce à ton temps et ton courage. Vous vécûtes heureux et eûtes beaucoup d'enfants.YOUPI 🥳")

        else:
            print("Tu ne peux plus. Tu n'as plus de temps tu as échouer. C'est la vie !😔")
    else:
        print("Tu n'as pas assez de courage donc tu as échouer!!!!")

histoire()


