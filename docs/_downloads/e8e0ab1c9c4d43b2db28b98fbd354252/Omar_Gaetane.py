# Ecrit ton programme ici ;-)
inventaire = []

vie = 2

choix_possibles =("oui", "o", "non", "n", "Nord", "Sud", "s","gauche","g","droite","d")


print("""Dans un royaume lointain, niché au sommet des nuages, se trouve le légendaire Château dans le Ciel, Laputa. Les contes et légendes racontent que ce château renferme des trésors inestimables et des connaissances oubliées depuis longtemps. Dans un petit village en contrebas, vit un jeune homme nommé Kai. Depuis son plus jeune âge, il a été captivé par les histoires de Laputa, et il a toujours rêvé de voler vers ce mystérieux château pour découvrir ses secrets. Maintenant, debout au bord d'une falaise escarpée, Kai fixe le ciel étoilé avec détermination. Il a passé des années à se préparer pour ce moment, à étudier les anciennes cartes et à apprendre les rudiments de la navigation aérienne.
À côté de lui, son fidèle compagnon, un petit robot nommé Taro, s'agite avec excitation, prêt à suivre Kai dans cette aventure périlleuse. Les étoiles scintillent au-dessus d'eux, éclairant le chemin vers l'inconnu. Mais alors que Kai se prépare à décoller dans son aéronef bricolé, il se rappelle les avertissements des anciens : Laputa est un endroit dangereux, plein de pièges et de mystères insondables. Il sait qu'il doit être prudent et se préparer à tout ce qui l'attend.
Avec une profonde inspiration, Kai ajuste son équipement, vérifie une dernière fois les moteurs de son aéronef, et se lance dans l'obscurité du ciel nocturne, bien déterminé à percer les secrets de Laputa avant que le soleil ne se lève.""")
def aeronef():
    global vie
    reponse = input("Il décide d'aller a gauche ou a droite ?")
    while reponse not in choix_possibles:
        reponse = input("Il décide d'aller a gauche ou a droite ?")
    if reponse == "gauche" or reponse == "g":
            print(" il tombe dans une tempête  donc -1 vie ")
            vie = vie-1
            if vie == 0 :
                    print("GAME OVER")
                    exit()
            reponse = input ("il prend un autre chemin ? (oui/non)")
            while reponse not in choix_possibles:
                reponse = input("il prend un autre chemin ? (oui/non)")
            if reponse =="oui":
                aeronef()
            elif reponse == "non":
                    print("la tempête devient une tornade, et casse son vaisseau GAME OVER")
    elif reponse == "droite" or reponse == "d":
            print ("Au bouts de quelques minutes de voyage à travers les cieux, Kai observe bouche-bé les étoiles danser dans le ciel nocturne,Taro quant à lui continue d'analyser toutes les données aeriennes et pilote l'aeronef permetant a Kai de s'emerveillé par le spectacle devant lui, il ne voit pas s'approcher sur sa gauche le vaisseau pirate de la bande de Schaff. Lors de l'attaque des pirates, un de leur fusil tombe dans l'aeronef de Kai.")
            reponse = input("Kai rammase le fusil et se defend avec ? (oui/non)")
            while reponse not in choix_possibles:
               reponse =input("Kai rammase le fusil et se defend avec ? (oui/non)")
            if reponse =="oui":
                print("vous prenez le fusil")
                inventaire.append("fusil")
                print(inventaire)
            if "fusil" in inventaire:
                    print ("Kai et Taro parviennent à s'echapper et continue leurs voyage sous les myriades d'etoiles scintillantes et Kai sait que ce fusil lui sera indispensable pour se proteger à l'avenir.")
                    reponse = input ("Maintenant Où il va ? (Nord/Sud)")
                    while reponse not in choix_possibles:
                        reponse =input("Maintenant Où il va ? (Nord/Sud)")
            if reponse == "Nord" or reponse == "n":
                    print ("Après moultes peripeties à travers les cieux, Kai voit au loin un amas nuageux plus que suspicieux. il decide de l'investiguer en passant par le haut donc par l'oeil du dôme, il arrive alors juste au dessus de la cité perdue de laputa.")
                    reponse = input ("Kai survole la zone à la recherche d'un endroit où se poser, finalement il va se poser sur un de nombreux jardin qui semblait embellir la vielle cité. En explorant un peu la zone Kai tombe sur une pièce sceller et mysterieuse remplie de machine d'antan lorsque soudain une d'elles s'éveille et commence a marcher d'un pas lourd et mecanique en direction de Kai. Il est obliger d'utiliser le fusil afin de defendre, Kai ne parvients pas blesser le robots cependant il parvient à lui echhapper et peux explorer Laputa. VICTOIRE ")
            elif reponse == "Sud"  or reponse == "s":
                    print ("Kai tombe sur des ruines et en les explorant, il tombe sur une carte")
                    reponse = input ("Est ce que Kai la rammase ? (oui/non)")
                    while reponse not in choix_possibles:
                        reponse =input("Est ce que Kai la rammase ? (oui/non)")
                    if reponse == "oui" or reponse == "o":
                        print("vous prenez la carte ")
                        inventaire.append("carte")
                        print(inventaire)
                        if "carte" in inventaire:
                            print("INCROYABLE la carte raconte les secret de la navigations aeronautique pour eviter toutes les bourrasque extremement violente et permet de voler jusqu'à Laputa. VICTOIRE ")
                    elif reponse == "non" or reponse == "n":
                        print(" Malheureusement sans elle, il ne parviendra jamais jusqu'à Laputa. GAME OVER.")
            elif reponse =="non":
                print("Kai se démène et fait tout pour echapper au pirates, à bord de son aeronef il est extrement rapide et agile mais malheureusement pour lui les chasseurs pirates le sont encore plus et le rattrape, ils abattent l'aeronef de Kai et il s'écrase au sol.")
                vie = vie-1
                if vie==0 :
                    print("GAME OVER")
                    exit()
                reponse = input("Kai se pose en urgence après toute ces peripeties, est ce qu'il a vraiment envie de mettre sa vie en jeu pour trouver Laputa ? (oui/non)")
                while reponse not in choix_possibles:
                    reponse =input("Kai se pose en urgence après toute ces peripeties, est ce qu'il a vraiment envie de mettre sa vie en jeu pour trouver Laputa ? (oui/non)")
                if reponse == "oui" or reponse == "o":
                        print("Après une semaine de réparation intensive, l'aéronef peut enfin repartir, Kai peut a nouveau s'elancer dans les airs.")
                        aeronef()
                elif reponse == "non" or reponse == "n":
                        print("Kai se resigne et remet son voyage a une autre fois, Taro et Kai en profiteront pour se reposer et se remettre mais pour le moment c'est Game over. ")



aeronef()
