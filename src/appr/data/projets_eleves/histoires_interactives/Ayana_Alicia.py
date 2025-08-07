pigeon=0
inventaire = []
perdu = False
def poser_question(question, choix_possibles):
    reponse = input(question + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + str(choix_possibles))
    return reponse
def debut():
    global pigeon
    print("Vous trouvez un français mytérieux")
    print("Il vous défile a un jeu de pile ou face")
    choix = poser_question("pile ou face", {"pile", "face"})
    if choix == "pile":
        print("vous perdez")
        print("le français vous tabasse et vous vole vos pantalons")
        choix = poser_question("aller à une friperie ou appeler votre mère?",
                               {"aller à une friperie", "appeler votre mère"})
        if choix == "appeler votre mère":
            debut()

        elif choix == "aller à une friperie":
            friperie()
    elif choix == "face":
        print("vous perdez")
        print("le français s'enfuit en courant enn laissant un pigeon parisien derrière lui")
        pigeon += 1
        friperie()
def friperie():
    global pigeon
    print("vous arriver à une friperie")
    choix = poser_question("acheter une montre ou un pantalon?",{"montre", "pantalon"})
    if choix== "montre":
        print("les genevois vous ridiculise et vous êtes banni")
        print("game over")
    elif choix== "pantalon":
        print("tout le monde vous complimente et la présidente de l'UNESCO vous offre 4 piegons")
        pigeon += 4

print("vous êtes harold")
print("vous aviez toujours été passionné des pigeon")
print("vous décidez un jour de vous lancer dans une quête pour construire une armée de ces magnifique piaf")

choix=poser_question("voulez-vous aller à echallens ou genève?",{"echallens","genève"})
if choix== "echallens":
    print("une figure se rapproche.")
    print("Impossible! il s'agit d'un épouventail challensois!")
    choix=poser_question("il vous montre un chemin, voulez-vous le suivre?",["oui","non"])
    if choix== "non":
        print("il vous prend par le bras et vous force à le suivre")
    elif choix== "oui":
        print("vous le suivez gentiment (obéir à un épouventail? un peu nul)")
    print("vous discutez un peu avec l'épouventail, il vous révèle qu'il s'appelle jonathan et qu'il est en vérité genevois de naissance")
    print("il vous recommande de visiter la fameuse Cité des Nations un de ces jours!")
    print("il vous guide au musée du blé et du pain")
    choix=poser_question("monter à l'étage du haut? ou rester en bas?",["monter","rester"])
    if choix== "rester":
        print("wow! ils vendent toutes sortes de pains dans ce musée!")
        choix=poser_question("acheter une baguette?",["oui","non"])
        if choix== "oui":
            inventaire.append("baguette")
            print("vous récupérez la baguette")
        elif choix== "non":
            print("vous ne récupérez pas la baguette")
        print("oh non, les racailles d'echallens vous attaquent!! vous êtes en grand danger!")
        if "baguette" in inventaire:
            print("vous n'avez rien pour vous déendre mis à part votre baguette fraîchement sorti du four!")
            print("vous la lancer désesperement vers vos ennemis mais cela n'a fait aucun effet sur eux ")
            print("(bien qu'ils soient dégoûtés par votre énorme gachis de nourriture!)")
            print("mais vous voyez au loins vos oiseaux préférés voler vers vous, ils attaquent les racailles!")
            pigeon +=5
            print("vous gagnez 5 pigeons")
            print("les racaille se font bousiller par la quantité astronomique de pigeons")
        else:
            print("ils vous poussèrent jusqu'à vomissement")
            print("GAME OVER")

    elif choix== "monter":
        print("vous voyez une armure de chevalier(c'était pas un musée sur les pains?)")
        print("vous regardez à l'interieur de l'armure")
        print("vous trouvez un pigeon!")
        pigeon += 1
        print("vous décidez de prendre l'épée de l'armure avec à cause de vos problème de kleptomanie ")
        inventaire.append("épée")
        print("le boulanger vous découvre en plein vol et vous accuse")
        print("vous lui expliquez vos problèmes mentaux que vous avez eu depuis l'enfance et pour vous aider ils vous propose de travailler dans la boulangerie")
        choix=poser_question("venir travailler, oui ou non?",["oui","non"])
        if choix== "oui":
            print("vous couper du pain frais cela attire 4 pigeons (vous gagnez 4 pigeons)")
            pigeon+=4

        elif choix=="non":
            print("vous lui tranchez la gorge")
            print("GAME OVER")
elif choix=="genève":
    debut()
    friperie()
if pigeon >= 5:
    print ("victoire")
else:
    print("GAME OVER")



