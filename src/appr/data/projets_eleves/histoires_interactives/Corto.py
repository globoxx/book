# Ecrit ton programme ici ;-)
def poser_question(question, choix_possibles):
    reponse = input(question + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + str(choix_possibles))
    return reponse

inventaire = []
x = 1

def point_de_vie():
    if x == 0 :
        print ("vous êtes mort")
    return x

def arene_romaine():
    print ("vous êtes un gladiateur dans une arène romaine, vous avez 1 point de vie")
    print ("une armure est posée devant vous.")
    choix = poser_question ("prendre l'armure ?",[ "oui","non"])
    if choix == "oui":
        print ("vous avez pris l'armure, point de vie +1")
        x = 2
        inventaire.append ("armure")
    elif choix == "non":
        print ("vous ne prenez pas l'armure")
    print ("une épée et une lance gisent devant vous")
    choix = poser_question ("prendre l'épée ou la lance ?", ["épée","lance"])
    if choix == "épée":
        print ("vous prenez l'épée")
        inventaire.append ("épée")
    elif choix == "lance":
        print ("vous prenez la lance")
        inventaire.append ("lance")
    print ("vous voyez votre adversaire équiper avec une épée et un bouclier. une trompette sonne le début du combat")
    
    
def combat_debut():            
    print ("votre adversaire lance une attaque")
    choix = poser_question ("parer ou esquiver ?", ["parer","esquiver"])
    if choix == "parer":
        if 'épée' in inventaire :
            print ("vous parez le coup")
            combat_suite()
        else :
            print ("vous perdez votre lance")
            inventaire.remove ("lance")
            choix = poser_question ("fuir ?", ["oui","non"])
            if choix == "oui":
                print ("un archer vous abat avant que vous ayez pu vous sauvez. vous êtes mort")
                x = 0
            elif choix == "non":
                choix = poser_question ("votre adversaire s'avance vers vous, attaquer ?", ["oui","non"])
                if choix == "oui":
                    print ("votre adversaire rigole avant de vous achevez, vous êtes mort")
                    x = 0
                elif choix == "non":
                    print ("vous ramassez l'épée que vous avez laissé au début")
                    combat_debut()
    elif choix == "esquiver":
        if "armure" in inventaire :
            print ("vous trébuchez à cause du poids de votre armure et votre adversaire vous touche aces son arme. point de vie -1")
            x = 1
            combat_suite()
        else :
            print ("vous esquivez le coup de votre adversaire")
            combat_suite()
            
def combat_suite():
    print ("vous décidez de contre-attaquer")
    choix = poser_question ("attaquer verticalement ou en estoc ?", ["verticalement","estoc"])
    if choix == "verticalement" :
        if "épée" in inventaire :
            print ("vous portez une attaque puissante à votrre adversaire qui, blessé, se rend. vous avez gagné !")
        else :
            print ("attaquer verticalement avec une lance ? pas très efficace. point de vie -1")
            x == x-1
    elif choix == "estoc" :
        if "lance" in inventaire :
            print ("vous planter votre lance dans le ventre de votre adversaire, le blessant mortellement")
            print ("vous avez gagné !")
        else :
            print ("votre adversaire dévie votre attaque et vous blesse mortellement. vous êtes mort")
         
point_de_vie()
arene_romaine()
combat_debut()