inventaire = []
souris = 0

def poser_question(question, choix_possibles):
    reponse = input(question + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + str(choix_possibles))
    return reponse

def cendrillon():
    print("Cendrillon cherche le prince charmant")
    choix = poser_question("Est-ce que la belle-mère la laisse-t-elle aller au bal ?",["oui","non"])
    if choix == "oui" :
        print("Elle sort par la porte de gauche et tpmbe sur une citrouille, elle la prend avec elle")
        inventaire.append("citrouille")
    elif choix == "non" :
        print("Elle sort part la porte de droite. Elle croise une baguette magique et elle la prend avec elle.")
        inventaire.append("baguette_magique")
    choix_1()

def choix_1() :
    global souris
    print("Elle marche et croise Anastasia et Javotte qui l'embête.")
    choix = poser_question("Elle fuit ou elle s'arrête et les écoute ?", ["fuire", "écouter"])
    if choix == "fuire":
        print("Elle tombe sur un dragon affamé.")
        if "citrouille" in inventaire :
            print("Elle lui donne la citrouille.")
            choix_1()
        else :
            print("Le dragon la mange et elle meurt.")
            print("GAME OVER")
    elif choix == "écouter" :
        print("Les deux soeurs lui demande où elle va et une souris sort de la robe d'Anastasia.")
        souris = souris + 1
        choix = poser_question("Les soeur embêtent Cendrillon, ripoiste-t-ell ou les écoute-t-elle ?", ["écouter", "riposter"])
        if choix == "écouter" :
            print("Les deux soeurs lui interdisent d'aller au bal.")
            print("GAME OVER")
        elif choix == "riposter" :
            print("Les deux soeurs surprises ne disent rien et la laisse partir.")
            chemin()

def chemin() :
    global souris
    choix = poser_question("Elle arrive sur un petit chemin, elle va à droite ou à gauche ?", ["gauche","droite"])
    if choix == "gauche" :
        choix = poser_question("Le chemin se sépare en deux, elle va à gauche ou à droite ?", ["gauche", "droite"])
        if choix == "droite" :
            print("Elle continue sur le chemin.")
            château()
        elif choix == "gauche" :
            print("Elle trouve une deuxième souris qui s'était perdu et la prend.")
            souris = souris + 1
            château()
    elif choix == "droite" :
        print("Il y a un gros trou et elle ne peut pas faire demi tour.")
        if "baguette_magique" in inventaire :
            print("Elle construit un pont grâce à la baguette et elle continue sa route.")
            château()
        else :
            print("Elle reste bloquée.")
            print("GAME OVER")

def château() :
    global souris
    print("Elle arrive devant un grand château, la porte est fermée et elle a besoin de deux souris pour passer.")
    if souris >= 2 :
        print("Les souris lui permette d'entrer et elle trouve le PRINCE !!!!!!")
    else :
        print("Elle retourne au petit chemin.")
        chemin()

cendrillon()