def poser_question(question, choix_possibles):
    reponse = input(question + " " + str(choix_possibles) + " ")
    while reponse.lower() not in choix_possibles:
        reponse = input(question + " " + str(choix_possibles) + " ")
    return reponse.lower()

print("Vous êtes dans votre canapé et vous regardez la TV")
time.sleep(1)  # Délai d'une seconde avant la question suivante
reponse = poser_question("Vous mettez la chaine 122 ou 44 ?", ["122", "44"])

if reponse == "122":
    print("Vous atterrissez dans une pièce sombre")
    print("Vous voyez une batte de baseball")
    time.sleep(1)  # Délai d'une seconde avant la question suivante
    reponse == poser_question("Voulez-vous prendre la batte de baseball ?", ["oui", "non"])
    if reponse == "oui":
        inventaire.append("batte de baseball")
        print("vous prenez la batte de baseball.")
    elif reponse == "non":
            print("Vous ne prenez pas la batte de baseball et vous sortez de la pièce sombre")
            print("Vous tombez sur un cambrioleur")
    if "batte de baseball" in inventaire:
            print("Vous vous battez avec le cambrioleur et vous gagnez le combat")
    else:
             print("Vous n'avez pas pris la batte de baseball pour vous défendre")
             print("Game over!!!")
    time.sleep(1)  # Délai d'une seconde avant la question suivante
    reponse == poser_question("Voulez-vous prendre le chat ?", ["oui", "non"])
    if reponse == "oui":
       print("Vous prenez votrer chat, vous rentrez chez vous.")
    elif reponse == "non":
            print("Vous ne voulez pas prendre votre chat.")
            print("Vous décidez de retourner dans votre canapé.")
            def poser_question()
            
elif reponse == "44":
    print("Vous atterrissez dans une jungle et tu as une carte dans les poches")
    inventaire = ["carte"]
    time.sleep(1)  # Délai d'une seconde avant la question suivante
    print("Vous sortez la carte de votre poche et vous voyez une croix")
    time.sleep(1)  # Délai d'une seconde avant la question suivante
    reponse = poser_question("Voulez-vous y aller ?", ["oui", "non"])
    if reponse == "non":
        print("Vous vous faites dévorer en vous reposant la nuit")
        print("Game over!!!")
    elif reponse == "oui":
        print("En vous baladant, vous trouvez un reste d'avion crashé.")
        print("Vous le fouillez et vous trouvez de la nourriture")
        time.sleep(1)  # Délai d'une seconde avant la question suivante
        reponse = poser_question("Voulez-vous la manger ?", ["oui", "non"])
        if reponse == "oui":
            print("La nourriture était toxique, Vous mourrez d'une intoxication")
            print("Game over!!!")
        print("Vous trouvez un pistolet derrière la nourriture")
        time.sleep(1)  # Délai d'une seconde avant la question suivante
        reponse = poser_question("Voulez-vous le prendre ?", ["oui", "non"])
        if reponse == "oui":
            inventaire.append("pistolet")
            print("Votre inventaire :", inventaire)
            print("Vous continuez votre chemin vers la croix ")
        elif reponse == "non":
            print("Vous continuez votre chemin vers la croix ")

print("Vous trouvez un ruisseau et en vous baissant pour boire, vous faites tomber la carte")
time.sleep(1)  # Délai d'une seconde avant la question suivante
reponse = poser_question("Voulez-vous la chercher", ["oui", "non"])
if reponse == "non":
    print("Tu te perds mais tu trouves une grotte remplie d'or")
    print("Tu adores tellement cet endroit que tu restes ici et que tu ne repartiras jamais")
    print("Fin du jeu pour toi")
elif reponse == "oui":
    print("La carte a changé de couleur et la Croix change de place sur ta position. Tu es dans l'antre d'une panthère")

print("Tu décides de te battre contre elle")
time.sleep(1)  # Délai d'une seconde avant la question suivante
if "pistolet" in inventaire:
    print("Tu as le pistolet! Tu survies!")
else:
    print("Tu n'as pas le pistolet! Tu meurs!")






Nous avons utlisées chatgpt pour le temps et nous nous sommes inspirées de votre modèle à des endroits ou nous avions des difficultés.
