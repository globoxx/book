import time

inventaire = []
vie = 5
argent = 0

def poser_question(question, choix_possibles):
    reponse = input(question + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + str(choix_possibles))
    return reponse


def naviguer_non():
    time.sleep(1)
    print("les pirates  vous voyent ils vous suivent et vous entourent")
    time.sleep(1)
    print("vous  sautez dans l'océan pour essayer de vous échapper")
    time.sleep(1)
    print("malheureusement vous vous noyez dans votre tentative")
    print ("game over")
    
def carte():
    time.sleep(1)
    print("il y aussi une carte!")
    time.sleep(1)
    print("elle est sûrement utile pour pouvoir trouver votre chemin pour chez vous!")
    time.sleep(2)
    print("malheureusement elle est usagé et il faut l'a reparé")
    time.sleep(2)
    i = poser_question ("que faites vous?", ["de retour à l'île" , "trouver une nouvelle île"])

    if i == "de retour à l'île":
        time.sleep(1)
        print("vous vous êtes rappellé du cartographe du village et vous retournez pour l'île")
        time.sleep(1)
        print("De retour au village vous courrez à la maison du cartographe")
        time.sleep(2)
        print("son prix est 1000 argent pour reparé votre carte avec la reduction ")
        time.sleep(1)
        
        
        if argent >= 1000 and vie > 0:
            time.sleep(2)
            print("vous obtenez votre carte et vous avez réussi à enfin rentrer")
            time.sleep(1)
            print("bien joué!")
            print("FIN")
       
        else:
            time.sleep(1)
            print("malheureusement vous n'avez pas l'argent pour acheter la reparation")
            time.sleep(1)
            print("vous essayez de trouver une autre île mais sans succès malheureusement")
            print("game over")     
            
    if i == "trouver une nouvelle île":
        time.sleep(1)
        print("malheureusement vous ne trouvez pas de nouvelle île et vous finissez par vous perdre de nouveau!")
        time.sleep(2)
        print("game over") 

def naviguer_oui():
    global argent
    global vie
    if "épée" in inventaire:
        time.sleep(1)
        print("les pirates sortent leurs armes pour se defendre de votre attaque et vous entourent")
        time.sleep(1)
        print("vous vous défendez avec votre épée et vous les battez")
        time.sleep(1)
        print("vous volez toute leur fortune de 1000 d'argent mais vous avez été frapper par une des armes des pirates et vous avez perdu de la vie.")
        argent = 1000 
        vie = vie - 5
        if vie <= 0:
            print("game over")
        
        else :
            carte()
            
    else:
        time.sleep(1)
        naviguer_sans_épée()

def naviguer_sans_épée():
    time.sleep(1)
    print("les pirates sont plus nombreux que vous")
    time.sleep(1)
    print("Ils sortent leurs armes pour se defendre de votre attaque et vous entourent")
    time.sleep(1)
    print("vous  sautez dans l'océan pour essayer de vous échapper")
    time.sleep(1)
    print("malheureusement vous vous noyez dans votre tentative")
    print ("game over")
    
def naviguer():
    time.sleep(1)
    print("vous continuez votre chemin sur l'ocean et vous voyez un bateau pirate au loin")
    time.sleep(1)
    print("ils ont sûrement des ressources qui peuvent vous être utiles")
    time.sleep(1)
    print("Que faites vous?")
    a = poser_question('Est ce que vous attaquez leur bâteau?', ["oui", "non"])
    
    if a == "oui":
        naviguer_oui()
           
    if a == "non":
        naviguer_non()

def village_2():
    time.sleep(1)
    print("vous allez au village et un villageois vous approche")
    time.sleep(1)
    print("En panique,il vous demande de le suivre et l'aider")
    time.sleep(1)
    print("Sa maison est en flammes!")
    print("Que faites vous?")
    reponse = poser_question("Vous aidez le villageois?",["oui" , "non"])
    
    if reponse == "oui":
        global vie
        time.sleep(1)
        print("vous sauvez sa maison et pour vous remerciez il vous donne de quoi manger")
        vie = vie + 5
        print("votre vie augmente de 5 points vie total: 10/10")
        time.sleep(1)
        print("le villageois vous remercie encore pour votre aide dit qu'il est cartographe et qu'il répare les cartes usagés ")
        time.sleep(1)
        print(" il vous dit de ne pas hésiter à venir réparer une carte si vous en auriez besoin pour un prix réduit")
        time.sleep(3)
        print("Avec votre vie qui est au max (10/10) vous decider de partir explorer sur l'océan")
        time.sleep(1)
        naviguer()
        
    if reponse == "non":
        print("vous reparter alors sur l'océan")
        naviguer()

def village ():
    global vie
    time.sleep(1)
    print("vous allez au village et un villageois vous approche")
    time.sleep(1)
    print("En panique,il vous demande de le suivre et l'aider")
    time.sleep(1)
    print("Sa maison est en flammes!")
    print("Que faites vous?")
    b = poser_question("Vous aidez le villageois?",["oui" , "non"])
    
    if b == "oui":
        time.sleep(1)
        print("vous sauvez sa maison et pour vous remerciez il vous donne de quoi manger")
        print("votre vie augmente de 5 points vie total: 10/10")
        vie = vie + 5
        time.sleep(1)
        print("le villageois vous remercie encore pour votre aide dit qu'il est cartographe et qu'il répare les cartes usagés ")
        time.sleep(1)
        print(" il vous dit de ne pas hésiter à venir réparer une carte si vous en auriez besoin pour un prix réduit")
        time.sleep(3)
        print("Avec votre vie qui est au max (10/10) vous decider de partir explorer mais où?")
        time.sleep(1)
        c = poser_question("vous explorer l'île ou l'océan?", ["île" , "océan"])
        
        if c == "île":
            explorer_île()
        
        if c == "océan":
            naviguer()
            
    if b == "non":
        time.sleep(1)
        print("le villageois part en panique et essaye de trouver quelqu'un pour l'aider")
        time.sleep(1)
        print("vous ne trouvez rien à manger et vous decidez de repartir sur l'océan ")
        time.sleep(1)
        print("votre vie diminue à 3/10 points")
        naviguer()
        
def explorer_île ():
    time.sleep(1)
    print("vous explorez alors cet île et sa petite forêt")
    time.sleep(1)
    print("vous trouvez une grotte dans cette forêt")
    time.sleep(1)
    d = poser_question("Que faites vous?", ["explorer la grotte" , "retourner au village"])
   
    if d == "explorer la grotte":
        time.sleep(1)
        print("vous entrez dans la grotte")
        time.sleep(1)
        print("cette grotte toute sombre ne semble rien avoir d'interessant")
        e = poser_question("Est ce que vous continuez à explorer la grotte?", ["continuer à explorer" , "retourner en arrière" ])
            
        if e == "continuer à explorer":
            time.sleep(1)
            print("vous continuez alors votre chemin jusqu'au fond de la grotte")
            time.sleep(1)
            print("à la fin de cette grotte vous trouvez alors une épée")
            inventaire.append("épée")
            time.sleep(1)
            print("vous retournez donc au village")
            village_2()
        
        if e == "retourner en arrière":
            village_2()
    
    if d == ("retourner au village"):
        village_2()

def île():
    time.sleep(1)
    print("vous arrivez sur la  plage de l'île  et vous voyez un village dans l'horizon")
    time.sleep(1)
    print("peut-être vous pourriez trouver de quoi manger en y allant.")
    time.sleep(1)
    f = poser_question("Que faites vous", ["aller au village" ,"explorer l'île"])

    if f == "aller au village":
        village()


    if f == "explorer l'île":
        explorer_île()




print("vous êtes sur un bateau perdu sur l'océan")
time.sleep(1)
print("vous voulez rentrez chez vous mais vous ne savez pas comment")
time.sleep(1)
print("vous n'avez pas d'argent à votre nom c'est un vrai problème!")
time.sleep(1)
print("vos points de vies sont à 5/10")
time.sleep(2)
print("vous voyez une île au loin et vous avez faim donc vous hésitez d'aller sur l'île si trouver de quoi manger pour recupéré des points de vie (5)")
choix = poser_question("Que faites vous?", ["continuer de naviguer", "aller sur l'île"])
    

if choix == "continuer de naviguer":
    naviguer()
    
        
if choix == "aller sur l'île":
    île()