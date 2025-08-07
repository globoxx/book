


def grotte_et_fin():
    print("vous arrivez devant une grotte")
    reponse = input("souhaitez vous y entrer?")
    if reponse == "non":
        print("vous arrivez dans une forêts très dense")
        print("la forêt était en fait une jungle")
        print("vous arrivez devant un temple")
        reponse = input("voulez vous y entrer?")
        if reponse == "oui":
            print("un creeper vous attendais, et vous explose. Vous êtes mort.")
        elif reponse == "non":
            print("vous contournez le temple, mais 5 zombies vous agressent. Vous êtes mort. ")
    elif reponse == "oui":
        print("vous trouvez du minerais de fer et craftez une nouvelle épée, un casque et une pioche")
        inventaire.append("épée")
        inventaire.append("casque")
        inventaire.append("pioche_en_fer")
        print("vous trouvez un portail dans le quel vous sautez par curiosité.")
        print("vous êtes dans l'End, une dimension de laquelle vous ne pouvez vous êchapper qu'en tuant le draqon.")

        reponse = input("voulez vous tuer le dragon?")
        if reponse == "oui":

            print("Après un combat difficile vous venez à bout du dragon.")
            reponse = input("maintenant souhaitez vous explorer les autres parties de cette dimension?")
            if reponse == "oui":
                print("vous glissez sur un cailloux et tombez dans le vide. Vous est donc mort.")
                if spawn == "true":
                    print("vous vous réveillez dans le village où vous étiez précédemment.")
                    village()
                elif spawn == "false":
                    print("game over")
            elif reponse == "non":
                print("vous rentrez donc dans votre dimension, bien joué, vous êtes arrivé à la fin de notre jeu.")


        elif reponse == "non":
            print("vous tombez dans le vide, et mourrez.")
            if spawn == "true":
                print("vous vous réveillez dans le village où vous étiez précédemment.")
                village()
            elif spawn == "false":
                print("game over")


def village():
    global spawn
    print("vous trouvez un village")
    if "hache" in inventaire:
        print("vous aurez plus de faciliter à couper des arbres")


    reponse = input("vous l'éviter ou vous le fouiller ?")
    if reponse == "éviter":
        print("vous décidez de l'éviter et la nuit tombe vite.")
        print("votre stuff est trop mauvais et vous vous faites attaquer")

        grotte_et_fin()

    elif reponse == "fouiller":
        print("vous décidez de le fouillez et vous trouvez des ressources tels qu'un plastron en fer et des pommes")
        print("Au passage voulez vous initialisez votre point de spawn dans un des lits du village")

        spawn = "true"

    inventaire.append("plastron en fer")
    inventaire.append("pommes")

    reponse = input("vous croisez un villageois qui vous propose 5 émeraudes en échange de votre armure.Vous acceptez, oui ou non ?")

    if reponse == "oui":
        inventaire.append("5 émeraudes")
        inventaire.remove("plastron en fer")

    print("la nuit tombe vite et des monstres appaîssent vous n'avez plus rien pour vous défendre vous mourrez ")

    reponse = input("souhaitez-vous respawn ?")

    if reponse == "non":
        print("game over")

    elif reponse == "oui":
        print("Vous vous éveillez dans le lit que vous avez utilisé auparavant")
        village()





inventaire = []
nombre_de_buche = 0
spawn = "false"


print("vous venez de spawn")

reponse = input("vous allez couper des arbres ou explorer ?")
if reponse == "explorer":
    village()


elif reponse == "couper des arbres":
    print("vous récolter 10 bûches")

    nombre_de_buche += 10

    print("vous construisez une table de craft.")
    reponse = input("craftez vous une pioche ou une hache")

    if reponse == "hache":
        village()

    elif reponse == "pioche":
        grotte_et_fin()
