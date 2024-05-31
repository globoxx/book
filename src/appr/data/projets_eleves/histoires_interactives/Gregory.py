import math 

#variable de mort
death = False
#stats
life = 5
heal_point = 5
attack = 2
defense = 1
initiative = 10

#inventory
inventory = []

#item
    #weapon
long_sword = ["épée longue",0 ,0 ,0 ,3 , 0 ]
    #armor
chain_mail = ["côte de maille",0 ,5 , 0, 0]
plate_armor = ["armure de plaque",0 ,0 ,10 , 0, 0]
    #artifact
amulet_of_health = ["amulette_de_santée", 0, 10, 0, 0, 0]
amulet_of_eternity = ["amulette_de_l'éternité",math.inf , 0, 0, 0, 0]


#ajouts des stats de l'item à l'attaque
    #life
def getPlayerlife():
    totalPlayerlife = life
    for itemIndex in range(len(inventory)):
        totalPlayerlife += inventory[itemIndex][1]

        return totalPlayerlife

    #health_point
def getPlayerhealt_point():
    totalPlayerhealth_point = heal_point
    for itemIndex in range(len(inventory)):
        totalPlayerhealth_point += inventory[itemIndex][2]

        return totalPlayerhealth_point

    #attack
def getPlayerAttack():
    totalPlayerAttack = attack
    for itemIndex in range(len(inventory)):
        totalPlayerAttack += inventory[itemIndex][4]

    return totalPlayerAttack

    #defense
def getPlayerDefense():
    totalPlayerDefense = defense
    for itemIndex in range(len(inventory)):
        totalPlayerDefense += inventory[itemIndex][3]

    return totalPlayerDefense



for i in range(life - 1):
    print("vous avez", life , "de vie")
    if life >= 1 :
        print("Bienvenue en enfer.")
        print("Vous vous réveillez dans un endroit qui ne vous est pas famillier. En effet hier soir vous étiez certain de vous être endormit dans votre lit.")
        respond = input("Au millieu de votre champ de vision, vous voyez une fenêtre d'un système avec écrit : vous avez une notification. Voulez vous l'ouvrir ? , (oui) ; (non)")
        while respond not in ["oui", "non"]:
            respond = input("Au millieu de votre champ de vision, vous voyez une fenêtre d'un système avec écrit : vous avez une notification. Voulez vous l'ouvrir ? , (oui) ; (non)")
        if respond == "oui" :
            print("Vous avez été téleporté dans l'enfer pour y résoudre un problème de grande envegure, pour cela il vous faudra explorer un donjon et le terminer.")
            respond = input("Acceptez-vous? (oui)(non)")
            if respond == "oui" :
                print("Vous êtes téleporté à l'entrée d'une ruine.")
                print("vous avez reçu une épée longue et une armure.")
                inventory.append(long_sword)
                inventory.append(chain_mail)
                print("Faites en bonne usage")
                print("Voici votre inventaire :")
                for itemIndex in range(len(inventory)):
                    print("Objet", inventory[itemIndex][0])
                    print("Vie", inventory[itemIndex][1])
                    print("Point de vie", inventory[itemIndex][2])
                    print("Attaque", inventory[itemIndex][3])
                    print("Défense", inventory[itemIndex][4])
            else:
                print("Le système commence à avoir de la neige et sans que vous compreniez quoi que soit vous vous sentez tombez.")
                print("Vous êtes mort")
                death = True
        elif respond == "non" : 
            print("La page s'ouvre malgré tout.")
            respond = input("Acceptez-vous? (oui)(non)")
            if respond == "oui" :
                print("Vous êtes téleporté à l'entrée d'une ruine.")
            else:
                print("Le système commence à avoir de la neige et sans que vous compreniez quoi que soit vous vous sentez tombez.")
                print("Vous êtes mort")
                death = True
            print("Vous avez été téleporté dans l'enfer pour y résoudre un problème de grande envegure, pour cela il vous faudra explorer un donjon et le terminer.")                
        if death == False :
            #retour
            respond = input("Entrez-vous dans le donjon ou décidez-vous de ne pas y entrer et de visiter les alentours? , (entrer) ; (visiter les alentours)")
            while respond not in ["entrer", "visiter les alentours"]:
                respond = input("Entrez-vous dans le donjon ou décidez-vous de ne pas y entrer et de visiter les alentours? , (entrer) ; (visiter les alentours)")
            if respond == "entrer":
                print("Vous entré dans la grotte")
                print("Un loup vous attaque")
                if defense <= 5 and attack <= 4 :
                    print("Vous mourrez.")
                    inventory.remove(long_sword)
                    inventory.remove(chain_mail)
                    death = True   
                else:
                    print("Vous arrivez a vaincre le loup.")
                    print("Vous avancer dans la grotte")
                    respond = input("Un embranchement s'ouvre à vous allez-vous à droite ou a gauche : (droite) ; (gauche)")
                    while respond not in ["droite","gauche"]:
                        respond = input("Un embranchement s'ouvre à vous allez-vous à droite ou a gauche : (droite) ; (gauche)")
                    if respond == "droite" :
                        respond = input("Vous voyez un coffre devant vous: l'ouvrez-vous? (oui) ; (non)")
                        if respond == "oui":
                            print("en ouvrant le coffre vous vous faites attrapper par celui-ci et vous mange. ")
                            inventory.remove(long_sword)
                            inventory.remove(chain_mail)
                            death = True
                        else :
                            print("Vous avancez dans le tunnel.")
                    elif respond == "gauche" :
                        respond = input("Vous voyez un coffre devant vous: l'ouvrez-vous? (oui) ; (non)")
                        if respond == "oui" :
                            print("Vous obtenez une armure de plaque.")
                            inventory.append(plate_armor)
                            inventory.append(chain_mail)
                        elif respond == "non" :
                            print("Vous retourner sur vos pas")
                            print("Vous allez dans le tunnel de droite")
                            respond = input("Vous voyez un coffre devant vous: l'ouvrez-vous? (oui) ; (non)")
                            if respond == "oui":
                                print("en ouvrant le coffre vous vous faites attrapper par celui-ci et vous mange. ")
                                inventory.remove(long_sword)
                                inventory.remove(chain_mail)
                                death = True
                            else :
                                print("Vous avancez dans le tunnel.")
                    print("Vous vous retrouvez de devant une fontaine.")
                    print("Le syteme s'affiche devant vous.")
                    print("Il est écrit que la fontaine est destinnée à une épreuves.")
                    respond = input("Voulez-vous y participer? (oui) ; (non)")
                    if respond == "oui" :
                        print("Vous allez être évalué sur 3 épreuves une de force la deuxieme sur votre capacité a encaisser puis si vous une grande force vitale. ")
                        print("Voici votre première épreuve")
                        print("Une statue apparait et vous demande de la taper.")
                        print("Vous frapper la statue.")
                        if attack <= 4 :
                            death = True
                        else : 
                            print("vous avez réussi la premiere épreuve.") 
                            print("Voici la seconde épreuve:")
                            print("Des pinces vous imobilise")
                            print("Une seconde statue apparait et vous frappe.")
                            if defense <= 10 :
                                print("Vous êtes mort.")
                            else:
                                print("le 2ème test est réussi.")
                                print("Voici le 3eme test.")
                                if heal_point <= 1 :
                                    print("Vous êtes mort.")
                                    death = True
                                else :
                                    print("Vous comprenez que pour sortir de se monde vous devez mourir autant de fois que vo avez de vie")
                                    print("Un item et suprimmer de votre inventaire")
                                    inventory.remove(amulet_of_eternity)
                                    inventory.remove(chain_mail)
                                    inventory.remove(long_sword)
                                    inventory.remove(plate_armor)
                                    print("Vous mourrez  sans comprendre pour quoi.")
                                    death = True
                    else :
                        print("Vous mourrez en voyant de la neige apparaitre devant votre vision.")
                        death = True
            elif respond == "visiter les alentours":
                respond = input("Vous voyez un groupe devant vous. Le rejoignez-vous ou est ce que vous revenez à la grotte? (rejoindre) ; (retourner)")
                if respond == "rejoindre":
                    print("Le groupe vous voyent et vous abordent:")
                    print("Hey vous!. Que faites vous ici.")
                    print("C'est une zone interdite au public.")
                    print("Ils engagent un combat")
                    inventory.append(amulet_of_eternity)
                    print("Vous êtes mort")
                    inventory.remove(long_sword)
                    inventory.remove(chain_mail)
                    death = True
                else:
                    #attention problème boucle dois revenir à la ligne 92
                    print("Vous retourner à la grotte") 
                    respond = input("Entrez-vous dans le donjon ou décidez-vous de ne pas y entrer et de visiter les alentours? , (entrer) ; (visiter les alentours)")
                    while respond not in ["entrer", "visiter les alentours"]:
                        respond = input("Entrez-vous dans le donjon ou décidez-vous de ne pas y entrer et de visiter les alentours? , (entrer) ; (visiter les alentours)")
                    if respond == "entrer":
                        print("Vous entré dans la grotte")
                        print("Un loup vous attaque")
                        if defense <= 5 and attack <= 4 :
                            print("Vous mourrez.")
                            inventory.remove(long_sword)
                            inventory.remove(chain_mail)
                            death = True   
                        else:
                            print("Vous arrivez a vaincre le loup.")
                            print("Vous avancer dans la grotte")
                            respond = input("Un embranchement s'ouvre à vous allez-vous à droite ou a gauche : (droite) ; (gauche)")
                            while respond not in ["droite","gauche"]:
                                respond = input("Un embranchement s'ouvre à vous allez-vous à droite ou a gauche : (droite) ; (gauche)")
                            if respond == "droite" :
                                respond = input("Vous voyez un coffre devant vous: l'ouvrez-vous? (oui) ; (non)")
                                if respond == "oui":
                                    print("en ouvrant le coffre vous vous faites attrapper par celui-ci et vous mange. ")
                                    inventory.remove(long_sword)
                                    inventory.remove(chain_mail)
                                    death = True
                                else :
                                    print("Vous avancez dans le tunnel.")
                            elif respond == "gauche" :
                                respond = input("Vous voyez un coffre devant vous: l'ouvrez-vous? (oui) ; (non)")
                                if respond == "oui" :
                                    print("Vous obtenez une armure de plaque.")
                                    inventory.append(plate_armor)
                                    inventory.append(chain_mail)
                                elif respond == "non" :
                                    print("Vous retourner sur vos pas")
                                    print("Vous allez dans le tunnel de droite")
                                    respond = input("Vous voyez un coffre devant vous: l'ouvrez-vous? (oui) ; (non)")
                                    if respond == "oui":
                                        print("en ouvrant le coffre vous vous faites attrapper par celui-ci et vous mange. ")
                                        inventory.remove(long_sword)
                                        inventory.remove(chain_mail)
                                        death = True
                                    else :
                                        print("Vous avancez dans le tunnel.")
                            print("Vous vous retrouvez de devant une fontaine.")
                            print("Le syteme s'affiche devant vous.")
                            print("Il est écrit que la fontaine est destinnée à une épreuves.")
                            respond = input("Voulez-vous y participer? (oui) ; (non)")
                            if respond == "oui" :
                                print("Vous allez être évalué sur 3 épreuves une de force la deuxieme sur votre capacité a encaisser puis si vous une grande force vitale. ")
                                print("Voici votre première épreuve")
                                print("Une statue apparait et vous demande de la taper.")
                                print("Vous frapper la statue.")
                                if attack <= 4 :
                                    death = True
                                else : 
                                    print("vous avez réussi la premiere épreuve.") 
                                    print("Voici la seconde épreuve:")
                                    print("Des pinces vous imobilise")
                                    print("Une seconde statue apparait et vous frappe.")
                                    if defense <= 10 :
                                        print("Vous êtes mort.")
                                    else:
                                        print("le 2ème test est réussi.")
                                        print("Voici le 3eme test.")
                                        if heal_point <= 1 :
                                            print("Vous êtes mort.")
                                            death = True
                                        else :
                                            print("Vous comprenez que pour sortir de se monde vous devez mourir autant de fois que vo avez de vie")
                                            print("Un item et suprimmer de votre inventaire")
                                            inventory.remove(amulet_of_eternity)
                                            inventory.remove(chain_mail)
                                            inventory.remove(long_sword)
                                            inventory.remove(plate_armor)
                                            print("Vous mourrez  sans comprendre pour quoi.")
                                            death = True
                            else :
                                print("Vous mourrez en voyant de la neige apparaitre devant votre vision.")
                                death = True
                    elif respond == "visiter les alentours":
                        respond = input("Vous voyez un groupe devant vous. Le rejoignez-vous ou est ce que vous revenez à la grotte? (rejoindre) ; (retourner)")
                        if respond == "rejoindre":
                            print("Le groupe vous voyent et vous abordent:")
                            print("Hey vous!. Que faites vous ici.")
                            print("C'est une zone interdite au public.")
                            print("Ils engagent un combat")
                            inventory.append(amulet_of_eternity)
                            print("Vous êtes mort")
                            inventory.remove(long_sword)
                            inventory.remove(chain_mail)
                            death = True 
    else:
        print("Vous vous réveillez dans votre lit comme si vous aviez passez un mauvais rêve. ")
        print("Fin")
