# Alexian Bornand 1M02

print("Nous sommes au Moyen Âge. Tu es un chevalier armé au service du roi et tu es à la découverte dans trésor caché dans la forêt par des bandits")
vie = 3
inventaire = []
def main():
    global vie
    reponse= input("Ton druide te propose une fiole antipoison. Veux tu la prendre? oui ou non?")
    while reponse not in ["oui", "non"]:
        reponse = input("Ton druide te propose une fiole antipoison. Veux tu la prendre? oui ou non?")
    if reponse == "oui":
        print("Il te donne la fiole")
        inventaire.append("fiole antipoison")
    reponse = input("Il y deux chemins qui se propose à toi, le chemin éclairé et le chemin sombre. Lequels choisit tu ?")
    while reponse not in ["le chemin éclairé", "le chemin sombre"]:
        reponse = input("Il y deux chemins qui se propose à toi, le chemin éclairé et le chemin sombre. Lequels choisit tu ?")
    if reponse == "le chemin éclairé":
        reponse = input("Tu avances et trouves un blessé. Veux tu lui parler, oui ou non ? ")
        while reponse not in ["oui", "non"]:
            reponse = input("Tu avances et trouve un blessé. Veux tu lui parler, oui ou non ? ")
        if reponse == "oui":
            print("Il te donne un parchemin")
            inventaire.append("parchemin")
        print("Tu continues ton chemin")
        reponse = input("Tu tombes sur un ours déchainé, l'attaquer oui ou non ?")
        while reponse not in ["oui", "non"]:
            reponse = input("Tu tombes sur un ours déchainé, l'attaquer oui ou non ?")
        if reponse == "oui":
            print("Tu perds une vie")
            vie -= 1
            if vie == 0 :
                print("Tu n'as plus de vie")
                print("GAME OVER")
                return
            print("Tu continues ton chemin")
        elif reponse == "non":
            print("Tu continues ton chemin")
        reponse = input("Tu as soif et par chance tu trouves une fontaine. Tu bois oui ou non ?")
        while reponse not in ["oui", "non"]:
            reponse = input("Tu as soif et par chance tu trouves une fontaine. Tu bois oui ou non ?")
        if reponse == "oui":
            print("L'eau est empoisonnée. As tu une fiole antipoison ?")
            if "antipoison" in inventaire:
                print("Tu es guéri par la fiole")
            else:
                print("L'eau t'empoisonne. Tu meurs")
                print("GAME OVER")
                return
        elif reponse == "non":
            print("Tu continues")
        reponse = input("Il est tard. Décide tu de dormir à la belle étoile ?")
        while reponse not in ["dormir à la belle étoile", "ne pas dormir"]:
            reponse = input("Il est tard décide tu de dormir à la belle étoile ?")
        if reponse == "dormir à la belle étoile":
            print("Tu te fais tuer la nuit par des bandits")
            print("GAME OVER")
            return
        elif reponse == "ne pas dormir":
            print("Tu trouves une grotte et dors tranquillement")
            print("Tu te lèves le matin et repart à l'aventure")
        fin_de_l_histoire()

    elif reponse == "le chemin sombre":
        reponse = input("Tu rencontres un chevalier solitaire au loin. Lui courir après pour le rattraper? oui ou non?")
        while reponse not in ["oui", "non"]:
            reponse = input("Tu rencontres un chevalier solitaire au loin. Lui courir après pour le rattraper? oui ou non?")
        if reponse == "oui":
            print("Tu le rattrapes")
        elif reponse == "non":
            reponse = input("Tu tombes sur un vieux arbre illuminé par les rayons du soleil. Il a l'air creux. Veut tu l'explorer ou pas l'explorer?")
            while reponse not in ["l'explorer", "pas l'explorer"]:
                reponse = input("Tu tombes sur un vieux arbre illuminé par les rayons du soleil. Il a l'air creux. Veut tu l'explorer ou pas l'explorer?")
            if reponse == "l'explorer":
                print("Tu trouves un code permettant de déchifrer le coffre.")
                inventaire.append("code")
            elif reponse == "pas l'explorer":
                print("Il ne se passe rien")
            print("Tu continues ton chemin et pour finir tu rencontre quand meme le vieux chevailier")
        reponse = input("Veux tu lui parler, oui ou non?")
        while reponse not in ["oui", "non"]:
            reponse = input("Veux tu lui parler, oui ou non?")
        if reponse == "oui":
            print("Il t'explique que le pont de la riviere et cassé mais un peu à pres tu peu traverser par les arbres.")  # INVENTAIRE le savoir
            inventaire.append("savoir")
        print("Tu arrives a la riviere et le pont et cassé. As tu une information pour traverser?")
        if "savoir" in inventaire:
            print("Tu reussis à traverser la riviere et reprend ton chemin")
        else:
            print("Tu fais demi tour et retournes à la case départ")
            main()
        reponse = input("Tu vois un géant au loin. Veux tu aller le combattre ? oui ou non ?")
        while reponse not in ["oui", "non"]:
            reponse = input("Tu vois un géant au loin. Veux tu aller le combattre ? oui ou non ?")
        if reponse == "oui":
            print("Tu perds une vie")
            vie -= 1
            if vie == 0:
                print("Tu n'as plus de vie")
                print("GAME OVER")
                return
        fin_de_l_histoire()


def fin_de_l_histoire():
    reponse = input("Tu arrives enfin au campement des bandits. Ils ne sont pas tous présents. Voudrais tu attaquer ou attendre la nuit prochaine pour les prendrent par surprise ?")
    while reponse not in ["attendre", "attaquer"]:
        reponse = input("Tu arrives enfin au campement des bandits. Ils ne sont pas tous présents. Voudrais tu attaquer ou attendre la nuit prochaine pour les prendrent par surprise ?")
    if reponse == "attendre":
        print("Malheureusement tous les bantits sont de retour et il est impossible d'attaquer")
        print("Tu fait demi tour et retour à la case départ")
        main()
    elif reponse == "attaquer":
        print("Victoire tu les bats. Il te faut maintenant le parchemin et le code pour trouver l'emplacemenet du coffre ")
        if "parchemin" in inventaire and "code" in inventaire:
            print("Tu trouves le coffre et l'ouvre")
            print("Victoire !!!!!!!!!!")
            return
        else:
            print("Il te manques un ou plusieurs objects")
            print("Tu fais demi tour et retournes à la case départ")
            main()


main()