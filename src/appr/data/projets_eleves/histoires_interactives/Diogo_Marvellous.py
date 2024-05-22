def poser_question(question, choix_possibles):
    reponse = input(question + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + str(choix_possibles))
    return reponse

def pont():
    print("Vous marchez quelques mètres et vous arrivez sur un pont et vous voyez un énorme volcan et de l'autre côté le début d'une prairie.")
    reponse = poser_question("Voulez vous aller à droite ou à gauche ?", ["droite", "gauche"])
    if reponse == "droite":
        volcan()
    elif reponse == "gauche":
        prairie()

def volcan():
    print("Vous arrivez au pied d'un volcan.")
    print("Depuis le bas du volcan, vous entendez le cri d'un dragon puis 2 armes aparaissent devant vous: une épée et une arbalète. Vous devez en choisir qu'une.")
    reponse = poser_question("Quelle arme choisissez vous de prendre ?",["l'épée", "l'arbalète"])
    if reponse == "l'épée":
        inventaire.append("épée")
        print("Vous avez ramassez l'épée.")
    elif reponse == "l'arbalète":
        inventaire.append("l'arbalète")
        print("Vous avez ramassez l'arbalète.")
    print("Vous entrez alors dans le volcan et à l'entrée il y a un petit coffre.")
    reponse = poser_question("Fouiller le coffre ?", ["oui", "non"])
    if reponse == "oui":
        print("En fouillant le coffre vous decouvrez la boule 4. Vous avez maitenant la boule 4 dans votre inventaire.")
        inventaire.append("boule 4")
    print("Vous continuez d'avancer dans le volcan et tomber nez à nez avec un dragon se qui vous oblige à vous battre.")
    if "épée" in inventaire:
        print("Vous auriez du prendre l'arbalète car avant même d'avoir pu approcher le dragon pour le tuer avec votre épée, il vous envoyé un coup de patte qui vous a tué. GAME OVER")
    elif "l'arbalète" in inventaire:
        print("Vous arrivez à tuer le dragon avec facilité car vous aviez juste à rester loin et lui tirer dessus. Bravo à vous.")
        reponse = poser_question("Voulez vous fouillez le corps du dragon ?", ["oui","non"])
        if reponse == "oui":
            print(" Vous trouvez la boule 5 dans l'estomac du dragon et vous avez maitenant la boule 5 dans votre inventaire.")
            inventaire.append("boule 5")
        print("Vous retournez en arrière et en sortant du volcan vous voyez un sentier qui monte jusqu'à tout en haut.")
        reponse = poser_question("Voulez vous aller explorer le sentier ou retrounez au pont ?", ["explorer le sentier","retourner au pont"])
        if reponse == "explorer le sentier":
            print("Vous montez tout en haut du volcan en suivant le sentier et tout en haut vous voyez la boule 6 qui est a deux doigts de tomber dans la lave du volcan.")
            reponse = poser_question("Que faites vous ?", ["je cours pour attraper la boule" ,"je ne prends pas le risque de la prendre c'est trop dangereux"])
            if reponse == "je ne prends pas le risque de la prendre c'est trop dangereux":
                print("La boule 6 tombe dans la lave et vous êtes condamné à mourir dans ce monde. GAME OVER")
            elif reponse == "je cours pour attraper la boule":
                print("Vous attrapez la balle juste à temps et vous récuperer donc la boule 6 dans votre inventaire. Après sa vous redescendez et revenez au pont")
                inventaire.append("boule 6")
                pont()
        elif reponse == "retourner au pont":
            pont()
        
    
    
def prairie():
    print("Vous arrivez dans une prairie.")
    print("Vous voyez une bouteille d'eau.")
    reponse = poser_question("Ramassez la bouteille d'eau ?", ["oui", "non"])
    if reponse == "oui":
        inventaire.append("bouteille d'eau")
        print("Vous avez une bouteille d'eau dans votre inventaire")
    print("Au milieu de cette prairie, vous voyez un arbre gigantesque avec un escalier de branches qui l'entoure.")
    reponse = poser_question("Voulez vous fouiller le pied de l'arbre ou monter les escaliers ou vous reposez ?", ["fouiller le pied de l'arbre", "monter les escaliers", "me reposer"])
    if reponse == "me reposer":
        print("Vous vous endormez paisiblement mais manqque de chance un loup affamé passe dans les parages et vous mourrez engloutit.")
        print("GAME OVER")
    elif reponse == "fouiller le pied de l'arbre":
        print("Vous tournez tout autour de l'arbre et trouvez par chance, appuyer contre l'arbre et cacher par des hautes herbes, la boule 2.")
        inventaire.append("boule 2")
        print("Vous avez maitenant la boule 2 dans votre inventaire.")
        reponse = poser_question("Que voulez vous faire maitenant ?",["rebrousser chemin jusqu'au pont", "monter les escaliers", "dormir"])
        if reponse == "dormir":
            print("Vous vous allonger par terre, mais par mal adresse votre tête frappe violemment une pierre et vous mourrez.")
            print("GAME OVER")
        elif reponse == "monter les escaliers":
            monter_les_escaliers()
        if reponse == "rebrousser chemin jusqu'au pont":
            pont()

    elif reponse == "monter les escaliers":
        monter_les_escaliers()






def monter_les_escaliers():
    print("Vous montez les marches une par une et arrivez au somment essouffler.")
    if "bouteille d'eau" in inventaire:
        print("Vous buvez de l'eau et vous vous sentez mieux")
        print("La boule 3 est posée en haut des marches.")
        reponse = poser_question("Que faites vous ?", ["Je ramasse la boule et redescends", "Je redescends"])
        if reponse == "Je redescends":
            portail()
        elif reponse == "Je ramasse la boule et redescends":
            inventaire.append("boule 3")
            print("Vous avez obtenu la boule 3 et elle est maitenant dans votre inventaire")
            portail()
    elif "bouteille d'eau" not in inventaire:
        print("Vous vous evanouissez et faites une chute libre de 50m et vous mourrez")
        print("GAME OVER")
        
def portail():
    print("Vous voyez un petit sentier au loin avec une lumière violette qui y ressort.")
    reponse = poser_question("Voulez vous retournez au pont ou aller au petit sentier ?", ["aller au petit sentier", "retourner au pont"])
    if reponse == "retourner au pont":
        pont()
    elif reponse == "aller au petit sentier":
        print("Vous marchez alors sur ce petit santier et tomber sur un portail. Vous voyez écrit sur ce portail que pour l'activer il vous faut avoir les 6 boules de cristal.")
        if "boule 1" in inventaire:
            if "boule 2" in inventaire:
                if "boule 3" in inventaire:
                    if "boule 4" in inventaire:
                        if "boule 5" in inventaire:
                            if "boule 6" in inventaire:
                                print("Le portail s'active et vous rentrez dedans.")
                                print("Vous êtes sortis de ce monde et vous avez donc gagner, BRAVO.")
        elif "boule 1" "boule 2" "boule 3" "boule 4" "boule 5" "boule 6" not in inventaire:
            print("Vous devez retournez en arrière aller chercher les boules qui vous manque.")
            pont()

inventaire = []

print("À la recherche d'un parchemin dans un temple , vous tombez dans un portail vous amenant dans un monde parrallèle.")
print("Un veilliard vient vers vous et vous dit que pour sortir de ce monde il faut trouver 6 boules de cristal.")
print("Le vieillard vous donne une boule de cristal, la boule 1, et il vous dit que les 5 autres sont cachés dans ce monde. Il vous dit aussi que quand vous reviendrez au pont tout s'annulera à part les boules dans votre inventaire, elles resteront et si par hasard vous vous retrouvez à decouvrir la même boule deux fois ce n'est pas grave elles seront stockés seulement une fois dans votre inventaire.")
inventaire.append("boule 1")
pont()
