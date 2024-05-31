print("vous êtes devant un pont")

inventaire = []

reponse = input(" voulez-vous le traverser? (O, N)")
while reponse not in["O", "N"]:
    print("ERROR")
if reponse == "N":
    reponse = input("Un dragon est apparu que faites vous ? (faire un câlin, fuir en courant)")
    while reponse not in["faire un câlin", "fuir en courant"]:
        print("ERROR")
    if reponse == "faire un câlin":
        print("il vous a cramé, GAME OVER")
    elif reponse == "fuir en courant":
        print("il vous a cramé, GAME OVER")
elif reponse == "O":
    print("vous traversez le pont.")
    reponse = input("vous tombez face à un couteau à beurre, voulez vous le ramasser ? (O, N)")
    while reponse not in["O", "N"]:
        print("ERROR")
    if reponse == "O":
        print("ok")
        inventaire.append("couteau à beurre")
    elif reponse == "N":
        print("ok")
    print("vous passez votre chemin et rencontrez Papa Ramo, un riche.")
    reponse = input("voulez-vous le racketter? (O, N)")
    while reponse not in["O", "N"]:
        print("ERROR")
    if reponse == "O":
        print("vous gagnez 100 Doge Coins")
        inventaire.append("100 Doge Coins")
    elif reponse =="N":
        print("vous le saluez et passez votre chemin")
    print("vous arrivez devant un temple dans lequel sont disposées trois armes.")
    reponse = input("quelle arme voulez-vous prendre?(bombonne de gaz, pantoufle, fusil sniper)")
    while reponse not in["bombonne de gaz", "pantoufle", "fusil sniper"]:
        print("Tu le fais exprès?" or "Vas te faire voir!")
    if reponse == "bombonne de gaz":
        inventaire.append("bombonne de gaz")
    elif reponse == "pantoufle":
        inventaire.append("pantoufle")
    elif reponse == "fusil sniper":
        inventaire.append("fusil sniper")
    print("Un dragon camerounais israélien hong kongais vous demande si vous auriez l'amabilité de lui faire une tartine au beurre.")
    if "couteau à beurre" and "100 Doge Coins" in inventaire:
        print("étant donné que vous avez les ressources nécessaires àla confection de la tartine, c'est-à-dire un couteau à beurre et 100 Doge Coins, vous vous en sortez vivant. VICTOIRE!!!!!")
    elif "fusil sniper" in inventaire:
        print("vous lui mettez un 360° no scope. VICTOIRE !!!!!!!!")
    elif "bombonne de gaz" in inventaire:
        print("vous avez débloqué une fin somme toute secrète, lui gazez sa race et remportez le combat. VICTOIRE !!!!!!")
    elif "pantoufle" in inventaire:
        print ("Nous, les développeurs, vous accordons une deuxième chance de choisir une nouvelle arme parmis celles présentes dans le temple:")
        reponse = input("quelle arme voulez-vous? (bombonne de gaz, fusil sniper)")
        while reponse not in["bombonne de gaz", "fusil sniper"]:
            print("Tu le fais exprès?" or "Vas te faire voir!")
        if reponse == "bombonne de gaz":
            inventaire.append("bombonne de gaz")
        elif reponse == "fusil sniper":
            inventaire.append("fusil sniper")
        if "fusil sniper" in inventaire:
            print("vous lui mettez un 360° no scope. VICTOIRE !!!!!!!!")
        elif "bombonne de gaz" in inventaire:
            print("vous avez débloqué une fin somme toute secrète, lui gazez sa race et remportez le combat. VICTOIRE !!!!!!")