inventaire = []

def retour_lieu_publique():
    reponse = input("Où vous rendez-vous? (parc / musée) ")
    if reponse == "parc":
        print("Vous êtes parti direction le parc. Le ciel est gris. Sur le chemin vous voyez des passants plus malheureux les uns que les autres.")
        print("Une fois arrivé, vous voyez une fontaine sur laquelle se dresse une statue d'un chevalier avec une épée rare.")
                
        reponse = input("Prenez-vous l'épée? ")
        if reponse == "oui":
            inventaire.append("épée")
            print("Cet objet pourrait avoir la même utilitée que la dague.")
            print(inventaire)
                    
            reponse = input("Souhaitez-vous visiter le musée? ")
            if reponse == "oui":
                print("Lorsque vous entrez dans le musée de la ville vous ne voyez personne à par un historien déprimé.")
                print("Vous visitez le musée et vous voyez une dague derrière une vitrine. Vous tentez de la volée mais l'historien vous voie. Il accepte de vous la vendre contre une épée rare.")
                
                
                
                if "épée" in inventaire:
                    inventaire.remove("épée")
                    print("L'historien accepte d'échanger la dague avec l'épée.")
                    inventaire.append("dague")
                    print("Vous avez désormais la dague dans votre inventaire.")
                    print(inventaire)
                    requete()
                
                else:
                    print("L'historien vous ordonne de sortir du musée.")
                
            elif reponse == "non":
                print("Retournez au lieu de départ.")
                requete()
                        
        elif reponse == "non":
            print("Vous decidez d'aller au musée.")
            musee()
                
    elif reponse == "musée":
                    musee()
                    
                    

        

def musee():
    print("Lorsque vous entrez dans le musée de la ville vous ne voyez personne à par un historien déprimé.")
    print("Vous visitez le musée et vous voyez une dague derrière une vitrine. Vous tentez de la volée mais l'historien vous voie. Il accepte de vous la vendre contre une épée rare.")
                
    if "épée" in inventaire:
        inventaire.remove("épée")
        print("L'historien accepte d'échanger la dague avec l'épée.")
        inventaire.append("dague")
        print("Vous avez désormais la dague dans votre inventaire.")
        print(inventaire)
        print("Vous retournez vers l'homme étrange.")
        requete()
        
    elif "bague" in inventaire:
        inventaire.remove("bague")
        print("L'historien accepte d'échanger la dague avec la bague.")
        inventaire.append("dague")
        print("Vous avez désormais la dague dans votre inventaire.")
        print(inventaire)
        print("Vous retournez vers l'homme étrange.")
        requete()
                
    else:
        print("L'historien vous ordonne de sortir du musée.")
        requete()
    

def lieu_depart():
    print("Vous entendez une étrange voix vous appeler depuis l'autel de la cathédrale.")
    reponse = input("Souhaitez-vous vous approcher de la voix et l'écouter? ")
    if reponse == "oui":
        print("Lorsque vous vous approchez de l'autel vous voyez une imposante statue qui vous murmure: 'Aide ton dieu qui est perdu ici depuis des années. Libère moi des ténèbres.'")
    
        reponse = input("Voulez-vous l'aider? ")
        if reponse == "oui":
            print("'Détruit la pierre jaune incrustée sur le front de la statue et apporte moi un corps que je pourrais posséder lorsque je serai libre'")
            print("La sincérité du dieu vous fait douter")
            
            reponse = input("Voulez-vous partir? ")
            if reponse == "non":
                print("Vous regardez une dernière fois la pierre en forme d'oeil posée dans vos mains avant de la détruire.")
                print("Vous pouvez sentir la présence menaçant du dieu auprès de vous.")
                
                reponse = input("Renoncez-vous à lui donner un corps? ")
                if reponse == "oui":
                    print("Le dieu s'agite, vous le sentez. Votre corps tremble, vous l'avez mis en colère.")
                    print("Vous ne pouvez rien faire. Le dieu prend posséssion de votre corps sans se soucier de votre souffrance.")
                    print("Vous venez de libèrer un dieu malfaisant rasponsable de la destruction du monde où vous vous trouvez.")
                    print("Votre vie s'éteint, le monde avec.")
                    print("GAME OVER")
                    protection()
                    
                elif reponse == "non":
                    print("Vous decidez de ne pas faire marche arrière, vous allez tuer quelqu'un.")
                    print("Votre regard se pose sur l'homme assis dans l'ombre sur un banc de la cathédrale.")
                    print("Vous passez discrètement derrière l'homme et vous le prenez par surprise. Par vous ne savez quel moyen vous avez réussi à tuer l'homme.")
                    print("Ce corps est désormais celui du dieu.")
                    print("Par votre faute le monde plongera dans le chaos. Et le dieu y régnera à jamais.")
                    
                    reponse = input("Vous vous sentez... ")
                    if reponse == "coupable" or "mal" or "responsable" or "perdu":
                        print("Plus jamais vous n'aurez l'occasion de rentrer chez vous. Votre vie sera malheureuse et ce jusqu'à votre mort.")
                        print("GAME OVER")
                        
                        if "bougie hibou" in inventaire:
                            print("Heureusement, le hibou vous a sauvé.")
                            lieu_depart()
                            inventaire.remove("bougie hibou")
                            inventaire.append("bougie")
                            print(inventaire)
                    
                    elif reponse == "insensible" or "impassible":
                        print("Vous avez compris que tout était perdu, votre ancienne vie comme ce monde. Vous ne voulez pas vivre malheureux, vous tuez le dieu pendant qu'il savoure le goût de sa victoire. Autant profiter de sa nouvelle vie en étant roi.")
                        print("Pour le restant de votre vie vous deviendrez le dieu qui inspira la peur et sèmera le chaos.")
                        print("Vous avez trouver votre propre fin.")
                        print("FIN")
                    
                    
                
            elif reponse == "oui":
                lieu_depart()
            
        elif reponse == "non":
            print("Retournez au lieu de départ.")
            lieu_depart()
    
    elif reponse =="non":
        print("Plus loin vous apercevez une silhouette assise sur un banc")
        print("Vous vous approchez de cet homme étrange")
        print("Vous demandez à l'homme à qui appartient la voix. L'homme vous répond que c'est un esprit qui est la source de tous les maux du monde.")
        print("L'homme vous demande gentillement si vous voulez accepter sa requête.")
    
        reponse = input("Acceptez-vous la requête? ")
        if reponse == "oui":
            print("Il me faudrait une dague, une pierre et une bougie.")
        
            reponse = input("Par quoi commencez-vous? ")
            if reponse == "dague":
                print("Pour trouver la dague, il faut chercher dans un lieu public.")
                print("Vous êtes désormais dehors.")
                retour_lieu_publique()
            
            elif reponse == "bougie":
                print("L'homme vous explique que la bougie est crucial pour le rituel. Sans elle le dieu pourrais se perdre dans les ténèbres après sa mort.")
                
                reponse = input("Vous pouvez choisir entre plusieurs endroits : un cimetière, une chapelle ou une maison abandonnée. ")
                if reponse == "cimetière":
                    print("Vous avez choisi d'aller dans un cimetière. Là bas, il y aura sûrement des bougies.")
                    print("Arrivé au cimetière, vous voyez une tombe avec deux bougies.")
                    print("Une bougie est gravée d'une colombe, l'autre d'un hibou.")
                    
                    reponse = input("Laquelle choisissez-vous? (colombe / hibou) ")
                    if reponse == "colombe":
                        print("Dans de nombreuses religions et lieux, la colombe est un symbole de paix.")
                        print("Reposez en paix.")
                        print("GAME OVER")
                        
                        if "bougie hibou" in inventaire:
                            print("Heureusement, le hibou vous a sauvé.")
                            inventaire.remove("bougie hibou")
                            inventaire.append("bougie")
                            print(inventaire)
                            lieu_depart()
                            
                    elif reponse == "hibou":
                        print("Le hibou est un symbole de mort ou de protection, cela dépend des croyances.")
                        print("Vous acquérez une bougie qui vous procurera une fois une protection si vous êtes sur le point de mourir.")
                        print("Vous avez trouver une bougie.")
                        print(inventaire)
                        objets_obtenus()
                    
                elif reponse == "chapelle":
                    print("Dans la cathédrale se trouve une petite chapelle.")
                    print("De nombreuse bougies sont posées pour les prières.")
                    print("Vous voyez une petite pancarte devant les bougies.")
                    
                    reponse = input("Lisez-vous la pancarte? ")
                    if reponse == "oui":
                        print("'Attention aux objets fragiles : merci de rester vigilant(e) en vous déplaçant.'")
                        print("En faisant attention à vos mouvements vous prenez une bougie.")
                        inventaire.append("bougie")
                        print(inventaire)
                        objets_obtenus()
                        
                    elif reponse == "non":
                        print("Vous ne lisez pas la pancarte. Tous ce dont vous avez besoin est d'une bougie.")
                        print("Dans ce petit espace vous bousculez une bougie. Rapidement la chapelle prend feu.")
                        print("Le feu vous consume.")
                        print("GAME OVER")
                        protection()
                        
                if reponse == "maison" or "maison abandonnée":
                    print(" Vous décidez de voir dans une maison. Vous voyez l'état dans lequel est le monde. Les maisons que vous voyez sont presque toutes abandonnées.")
                    print("Dans la maison, il doit surement se trouver des bougies.")
                    print("Quand vous entrez dans la maison, vous ne voyez pas tout de suite des bougies.")
                    print("Vous regardez la piece et voyez un escalier et une porte.")
                    
                    reponse = input("vous prenez l'escalier ou la chambre? ")
                    if reponse == "escalier":
                        print("L'escalier semble fragile mais vous réussissez quand même à accéder à l'étage.")
                        print("Vous trouvez une bougie et repartez sûrement.")
                        inventaire.append("bougie")
                        print(inventaire)
                        objets_obtenus()
                        
                    elif reponse == "chambre" or "porte":
                        print("En ouvrant la porte de la chambre le sol sous vos pied s'effondre.")
                        print("Vous ne survivez pas à la chute.")
                        print("GAME OVER")
                        protection()
                    
            
            elif reponse == "pierre":
                print("Il vous faut une pierre enchantée...")
                
                reponse = input("Vous partez directement la cherchée, car vous l'avez vue sur la statue de la cathédrale. (oui / non) ")
                if reponse == "oui":
                    print("Vous arrachez la pierre jaune située sur le front de la statue.")
                    print("Une lumière vous aveugle, vous venez de libérer un dieu de la mort scellé par une pierre enchantée. Vous mourez.")
                    print("GAME OVER")
                    protection()
                    
                elif reponse == "non":
                    print("Vous écoutez la suite des instuctions. Vous pouvez trouver une pierre normale, car l'homme étrange peut l'enchantée.")
                    
                    reponse = input("Vous préférez d'aller dans la cour / dans le jardin de la cathédrale. (cour / jardin) ")
                    if reponse == "cour":
                        print("Vous trouvez une très belle bague par terre. C'est un objet rare.")
                        print("Il y a un rubis sur cette bague. ")
                        
                        reponse = input("Prenez-vous la pierre? ")
                        if reponse == "oui":
                            print("Vous avez obtenu la pierre.")
                            inventaire.append("pierre")
                            inventaire()
                            print("Vous retournez à la cathédrale vers l'homme étrange.")
                            print("L'homme enchante la pierre.")
                            inventaire.remove("pierre")
                            inventaire.append("pierre enchantée")
                            print(inventaire)
                            objets_obtenus
                            
                        elif reponse == "non":
                            print("Vous gardez la bague, mais vous préférez continuer vos recherches et vous trouvez une jolie petite pierre.")
                            inventaire.append("bague")
                            inventaire.append("pierre")
                            print(inventaire)
                            print("Vous retournez à la cathédrale vers l'homme étrange.")
                            print("L'homme vous enchante la pierre")
                            inventaire.remove("pierre")
                            inventaire.append("pierre enchantée")
                            print(inventaire)
                            objets_obtenus()
                            
                    elif reponse == "jardin":
                        print("Vous visitez le magnifique jardin de la cathédrale.")
                        print("Vos yeux se posent sur le grand nuage de roses noires devant vous.")
                        
                        reponse = input("Souhaitez-vous toucher les roses? ")
                        if reponse == "oui":
                            print("Le saviez-vous que les rose noires symbolisaient la mort? ")
                            print("Votre curiosité vous a tué. ")
                            print("GAME OVER")
                            protection()
                            
                        elif reponse == "non":
                            print("Un grand nuage est toujours accompagné d'un orage. Une pluie d'abeille arrive sur vous et vous pique.")
                            print("Vous mourez.")
                            print("GAME OVER")
                            protection()
                        
                        
                    
                    
        elif reponse == "non":
            print("Retournez au lieu de départ.")
        
        
def requete():
    print("Il me faudrait une dague, une pierre et une bougie.")
        
    reponse = input("Par quoi commencez-vous? ")
    if reponse == "dague":
        print("Pour trouver la dague, il faut chercher dans un lieu publique.")
        print("Vous êtes désormais dehors.")
        retour_lieu_publique()
        
    elif reponse == "bougie":
        print("L'homme vous explique que la bougie est crucial pour le rituel. Sans elle le dieu pourrais se perdre dans les ténèbres après sa mort.")
                
        reponse = input("Vous pouvez choisir entre plusieurs endroits : un cimetière, une chapelle ou une maison abandonnée. ")
        if reponse == "cimetière":
            print("Vous avez choisi d'aller dans un cimetière. Là bas, il y aura sûrement des bougies.")
            print("Arrivé au cimetière, vous voyez une tombe avec deux bougies.")
            print("Une bougie est gravée d'une colombe, l'autre d'un hibou.")
                    
            reponse = input("Laquelle choisissez-vous? (colombe / hibou) ")
            if reponse == "colombe":
                print("Dans de nombreuses religions et lieux, la colombe est un symbole de paix.")
                print("Reposez en paix.")
                print("GAME OVER")
                        
                if "bougie hibou" in inventaire:
                    print("Heureusement, le hibou vous a sauvé.")
                    inventaire.remove("bougie hibou")
                    print(inventaire)
                    lieu_depart()
                            
            elif reponse == "hibou":
                print("Le hibou est un symbole de mort ou de protection, cela dépend des croyances.")
                print("Vous acquérez une bougie qui vous procurera une fois une protection si vous êtes sur le point de mourir.")
                print("Vous avez trouver une bougie.")
                inventaire.append("bougie hibou")
                inventaire.append("bougie")
                print(inventaire)
                objets_obtenus()
                    
        elif reponse == "chapelle":
            print("Dans la cathédrale se trouve une petite chapelle.")
            print("De nombreuse bougies sont posées pour les prières.")
            print("Vous voyez une petite pancarte devant les bougies.")
                    
            reponse = input("Lisez-vous la pancarte? ")
            if reponse == "oui":
                print("'Attention aux objets fragiles : merci de rester vigilant(e) en vous déplaçant.'")
                print("En faisant attention à vos mouvements vous prenez une bougie.")
                inventaire.append("bougie")
                print(inventaire)
                objets_obtenus()
                        
            elif reponse == "non":
                print("Vous ne lisez pas la pancarte. Tous ce dont vous avez besoin est d'une bougie.")
                print("Dans ce petit espace vous bousculez une bougie. Rapidement la chapelle prend feu.")
                print("Le feu vous consume.")
                print("GAME OVER")
                protection()
                        
        elif reponse == "maison" or "maison abandonnée":
            print(" Vous décidez de voir dans une maison. Vous voyez l'état dans lequel est le monde. Les maisons que vous voyez sont presque toutes abandonnées.")
            print("Dans la maison, il doit surement se trouver des bougies.")
            print("Quand vous entrez dans la maison, vous ne voyez pas tout de suite des bougies.")
            print("Vous regardez la piece et voyez un escalier et une porte.")
                    
            reponse = input("vous prenez l'escalier ou la chambre? ")
            if reponse == "escalier":
                print("L'escalier semble fragile mais vous réussissez quand même à accéder à l'étage.")
                print("Vous trouvez une bougie et repartez sûrement.")
                inventaire.append("bougie")
                print(inventaire)
                objets_obtenus()
                        
            elif reponse == "chambre" or "porte":
                print("En ouvrant la porte de la chambre le sol sous vos pied s'effondre.")
                print("Vous ne survivez pas à la chute.")
                print("GAME OVER")
                protection()
                        
    elif "pierre":
        print("Il vous faut une pierre enchantée...")
                
        reponse = input("Vous partez directement la cherchée, car vous l'avez vue sur la statue de la cathédrale. (oui / non) ")
        if reponse == "oui":
            print("Vous arrachez la pierre jaune située sur le front de la statue.")
            print("Une lumière vous aveugle, vous venez de libérer un dieu de la mort scellé par une pierre enchantée. Vous mourez.")
            print("GAME OVER")
            protection()
                    
        elif reponse == "non":
            print("Vous écoutez la suite des instuctions. Vous pouvez trouver une pierre normale, car l'homme étrange peut l'enchantée.")
                    
            reponse = input("Vous préférez d'aller dans la cour / dans le jardin de la cathédrale. (cour / jardin) ")
            if reponse == "cour":
                print("Vous trouvez une très belle bague par terre. C'est un objet rare.")
                print("Il y a un rubis sur cette bague. ")
                        
                reponse = input("Prenez-vous la pierre? ")
                if reponse == "oui":
                    print("Vous avez obtenu la pierre.")
                    inventaire.append("pierre")
                    print(inventaire)
                    print("Vous retournez à la cathédrale vers l'homme étrange.")
                    print("L'homme enchante la pierre.")
                    inventaire.remove("pierre")
                    inventaire.append("pierre enchantée")
                    print(inventaire)
                    objets_obtenus
                            
                elif reponse == "non":
                    print("Vous gardez la bague, mais vous préférez continuer vos recherches et vous trouvez une jolie petite pierre.")
                    inventaire.append("bague")
                    inventaire.append("pierre")
                    print(inventaire)
                    print("Vous retournez à la cathédrale vers l'homme étrange.")
                    print("L'homme vous enchante la pierre")
                    inventaire.remove("pierre")
                    inventaire.append("pierre enchantée")
                    print(inventaire)
                    objets_obtenus()
                            
            elif reponse == "jardin":
                print("Vous visitez le magnifique jardin de la cathédrale.")
                print("Vos yeux se posent sur le grand nuage de roses noires devant vous.")
                        
                reponse = input("Souhaitez-vous toucher les roses? ")
                if reponse == "oui":
                    print("Le saviez-vous que les rose noires symbolisaient la mort? ")
                    print("Votre curiosité vous a tué. ")
                    print("GAME OVER")
                    protection()
                            
                elif reponse == "non":
                    print("Un grand nuage est toujours accompagné d'un orage. Une pluie d'abeille arrive sur vous et vous pique.")
                    print("Vous mourez.")
                    print("GAME OVER")
                    protection()

        
        
    
        
def objets_obtenus():
    print("Avez-vous tous les objets demandé? ")
    if ["bougie", "pierre enchantée", "dague"] in inventaire:
        print("Vous retournez vers l'homme étrange et vous lui ramenez les trois objets. Une dague pour tuez le mal.Une pierre pour sceller la mort du dieu. Une bougie pour ne pas se perdre dans les ténèbres de la mort.")
        print("Vous réussissez à tuez le dieu qui faisait le mal.")
        print("Grâce à vous le monde retrouvera sa tranquillité.")
        print("Félicitation!!! Vous avez réussi le jeu.")
        print("Soudain vous voyez une lumière. Lorsque vous vous réveillez vous êtes enfin chez vous.")
        print("FIN")
                        
    else:
        requete()


def protection():
    if "bougie hibou" in inventaire:
        print("Heureusement, le hibou vous a sauvé.")
        inventaire.remove("bougie hibou")
        print(inventaire)
        lieu_depart()

                        
        


    
        
        
lieu_depart()

   


    
  

