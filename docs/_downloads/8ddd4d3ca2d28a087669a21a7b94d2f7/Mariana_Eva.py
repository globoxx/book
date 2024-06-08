# Ecrit ton programme ici ;-)
def début_histoire():
            inventaire=[]
            argent=0
            print("Après des semaines de reflexion, vous et votre ami Justin visitez un hôpital abandonné. À l'entrée se trouve un couteau et une lampe.")
            reponse = input("Vous prenez? (la lampe/le couteau)")
            while reponse not in ["la lampe", "le couteau"]:
                print("pas comrpis")
                reponse = input("Vous prenez? (la lampe/le couteau)")
            if reponse=="la lampe":
                print("La lampe est dans votre inventaire")
                inventaire.append("lampe")
                print(inventaire)
            elif reponse=="le couteau":
                print("Le couteau est dans votre inventaire")
                inventaire.append("couteau")
                print(inventaire)
            print("Vous entendez un bruit étrange venant d'une pièce")
            reponse = input("Vous rentrer?(chez vous/dans la pièce)")
            while reponse not in ["chez vous", "dans la pièce"]:
                print ("Pas compris.")
                reponse = input("Vous rentrer?(chez vous/dans la pièce)")
            if reponse=="chez vous":
                début_histoire()
                print("Vous prenez peur et rentrez chez vous avec Justin.")
            elif reponse=="dans la pièce":
                print("Vous rentrez dans la pièce et voyez un placard cadenassé.")
                reponse = input("Voulez vous essayer d'ouvrir le placard ou continuer d'explorer la pièce?(placard/pièce)")
                while reponse not in ["placard", "pièce"]:
                     print ("Pas compris.")
                     reponse = input("Voulez vous essayer d'ouvrir le placard ou continuer d'explorer la pièce?(placard/pièce)")
                if reponse=="pièce":
                    print("En explorant la pièce Justin s'est encoublé et s'est fracassé le crâne contre le coin de la table")
                    print("Votre ami est mort. GAME OVER")
                elif reponse=="placard":
                    print("Vous forcez le cadenas et trouvez un kit de survie et un porte monnaie.")
                    reponse = input("Prendre le kit de survie ou l'argent ?(kit de survie/argent)")
                    while reponse not in ["kit de survie", "argent"]:
                        print("Pas compris.")
                        reponse = input("Prendre le kit de survie ou l'argent ?(kit de survie/argent)")
                    if reponse == "kit de survie":
                        print("Vous mettez le kit dans votre sac.")
                        inventaire.append("kit de survie")
                    elif reponse == "argent":
                        print("Vous sortez une pièce de 5 francs et vous la mettez dans votre poche.")
                        argent= argent + 5
                        print("Vous avez",argent,"francs")
                    print("Vous rentrez dans une nouvelle pièce.")
                    print("Justin voit un distibuteur et vous demande de l'argent.")
                    if argent >=5:
                        print("Vous donnez les 5 francs à Justin et il se dirige vers le distibuteur.")
                        print("Soudainement vous tombez sur un individu suspect. Il essaie de vous attaquer. Vous essayez de répliquer.")
                        if "couteau" in inventaire:
                            print("Vous réussissez à mettre l'individu hors d'état de nuire grâce au couteau.")
                            print("Vous courrez dehors et appelez la police.")
                            print("Vous et Justin n'êtes pas mort.")
                            print("WIN")
                        else:
                            print("L'individu tranche Justin. Vous assistez à la scène la lampe en main.")
                            print("GAME OVER")
                    else:
                        print("Après votre réponse négative, Justin va tristement vers le distributeur et essaie de dérober objet. Malheuresement il se blesse le bras car il a essayé de casser la vitre.")
                        if"kit de survie" in inventaire:
                            print("Vous donnez le kit de survie à Justin")
                            print("En faisant son bandage, vous vous rendez compte qu'il est défectueux et la plaie s'infecte.")
                            print("GAME OVER")
                        else:
                            print("L'hemoragie est violente.")
                            print("GAME OVER")




début_histoire()
















