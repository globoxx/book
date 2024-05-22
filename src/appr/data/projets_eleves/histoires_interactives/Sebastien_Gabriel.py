#https://www.w3schools.com/python/python_classes.asp // https://docs.python.org/3/tutorial/classes.html documentation pour les classes
#autrement les bases vues au cours suffisaient pour faire tout ça

from operator import index
from random import randint
import time
import sys

class joueur:
    vie = 100
    maxVie = 100
    inventaire = []
    degat = 25
    sort = [] #pareil que pour les dégats physique et magique de l'enemie
    degatSort = []
    nombrePotion = 0
    idActuelle = 1
    autelApparition = False 
    
class enemie:
    def __init__(self, nom, vie, maxVie,  resistanceEstoc, resistanceCoupe, resistanceFrappe, resistanceMagique, attaquePhysique, degatAttaquePhysique, attaqueMagique, degatAttaqueMagique):
        self.nom = nom
        self.vie = vie
        self.maxVie = maxVie
        self.resistanceEstoc = resistanceEstoc
        self.resistanceCoupe = resistanceCoupe
        self.resistanceFrappe = resistanceFrappe
        self.resistanceMagique = resistanceMagique
        self.attaquePhysique = attaquePhysique #les degats de l'attaque physique est à la même position que son attaque dans la liste
        self.degatAttaquePhysique = degatAttaquePhysique
        self.attaqueMagique = attaqueMagique
        self.degatAttaqueMagique = degatAttaqueMagique      
        
def gameover():
    x = ""
    checking = False
    print("vous êtes mort au combat, mais vous pouvez revenir à la vie grâce à la guerriseuse")
    time.sleep(1)
    print("voulez vous le faire?")
    while not(checking):
        x = input()
        if x == "oui":
            checking = True
            end47.affichageEndroit()
        elif x == "non":
            checking = True
            print("dommage, vous n'étiez pas en mesure de finir avec si peu de determination")  
            sys.exit()
        else:
            print("Réponse séléctionnée incompatible. Veuillez recommencer")   
            
#explication du système de combat

#tour du joueur: choix entre attaque, sort, soin et parade
#selon l'attaque ou le sort, plus ou moins de dégats sont fait à l'enemie (determiné par les dégats et la resistance)
#soin met la vie au max
#parade demande quoi faire comme parade(magique, physique)

#tour de l'enemie
#attaque aléatoirement mais chaque attaque utilisée ne peut pas être utilisée avant 2 tours
#si il y a eu parade est qu'il s'agissait de la bonne par rapport à l'attaque: inflige de gros dégat à l'enemie, si raté, à nous
#sinon les dégats sont infligés comme le ferait le joueur
        
def combat(joueur, enemie):
    utilisationSort = 2
    attaqueUtilisee = []
    print("Un enemie vous attaque. Il s'agit d'un " + enemie.nom)
    time.sleep(1)
    while joueur.vie > 0 and enemie.vie > 0: 
        x = "" #tour du joueur
        y = ""
        print("vous avez " + str(joueur.vie) + " vie et votre ennemie a " + str(enemie.vie) + " vie")
        print("c'est votre tour")
        checking = False
        print("que voulez vous faire?")
        print("attaque, sort, parade ou soin")
        while not(checking): #checking est là pour la gestion des erreurs
            x = input()
            if x == "attaque":
                print("quel type d'attaque voulez-vous effectuez?")
                print("estoc, coupe ou frappe")
                while not(checking):
                    y = input()
                    if y == "estoc":
                        print("vous infligez " + str(joueur.degat * enemie.resistanceEstoc / 100) + " dégat")
                        enemie.vie -= joueur.degat * enemie.resistanceEstoc / 100
                        checking = True
                    elif y == "coupe":
                        print("vous infligez " + str(joueur.degat * enemie.resistanceCoupe / 100) + " dégat")
                        enemie.vie -= joueur.degat * enemie.resistanceCoupe / 100
                        checking = True
                    elif y == "frappe":
                        print("vous infligez " + str(joueur.degat * enemie.resistanceFrappe / 100) + " dégat")
                        enemie.vie -= joueur.degat * enemie.resistanceFrappe / 100
                        checking = True
                    else:
                        print("Réponse séléctionnée incompatible. Veuillez recommencer")
            elif x == "sort":
                if len(joueur.sort) > 0 and utilisationSort > 0:
                    print("quel sort voulez-vous lancer")
                    print(joueur.sort)
                    while not(checking):
                        y = input()
                        if y in joueur.sort:
                            i = joueur.sort.index(y)
                            print("vous infligez " + str(joueur.degatSort[i] * enemie.resistanceMagique / 100) + " dégat grâce à ce sort")
                            enemie.vie -= joueur.degatSort[i] * enemie.resistanceMagique / 100
                            utilisationSort -= 1
                            checking = True
                        else:
                            print("Réponse séléctionnée incompatible. Veuillez recommencer")
                else:
                    print("Plus de mana ou pas de sort")
            elif x == "parade":
                print("quelle type de parade")
                print("magique ou physique")
                while not(checking):
                    y = input()
                    if y not in ["magique", "physique"]:
                        print("Réponse séléctionnée incompatible. Veuillez recommencer")
                    else: 
                        checking = True
            elif x == "soin":
                if joueur.nombrePotion > 0:
                    joueur.vie = joueur.maxVie
                    joueur.nombrePotion -= 1
                    checking = True
                else:
                    print("vous n'avez plus de potions")
                    checking = True
            else:
                print("Réponse séléctionnée incompatible. Veuillez recommencer")
        if enemie.vie > 0:
            attaque = enemie.attaquePhysique + enemie.attaqueMagique #tour de l'enemie
            if len(attaqueUtilisee) == 2:
                for i in range(2):
                    attaque.remove(attaqueUtilisee[i-1])
                    attaquePossible = attaque
            elif len(attaqueUtilisee) == 1:
                attaque.remove(attaqueUtilisee[0])
                attaquePossible = attaque
            else:
                attaquePossible = attaque
            attaqueChoisie = attaquePossible[randint(0, len(attaquePossible)-1)]
            if attaqueChoisie in enemie.attaquePhysique: #systeme de parade
                if y == "physique":
                    print("vous avez réussi votre parade, dégat critique")
                    enemie.vie = enemie.vie / 2 - 5
                elif y == "magique":
                    print("vous avez raté votre parade, votre vie diminue drastiquement")
                    joueur.vie = 5 * joueur.vie/8 - enemie.degatAttaquePhysique[enemie.attaquePhysique.index(attaqueChoisie)]
                else:
                    print("l'enemie vous attaque avec " + attaqueChoisie)
                    joueur.vie -= enemie.degatAttaquePhysique[enemie.attaquePhysique.index(attaqueChoisie)]
            elif attaqueChoisie in enemie.attaqueMagique:
                if y == "magique":
                    print("vous avez réussi votre parade, dégat critique")
                    enemie.vie = enemie.vie / 2 - 5
                elif y == "physique":
                    print("vous avez raté votre parade, votre vie diminue drastiquement")
                    joueur.vie = 5 * joueur.vie/8 - enemie.degatAttaqueMagique[enemie.attaqueMagique.index(attaqueChoisie)]
                else:
                    print("l'enemie vous attaque avec " + attaqueChoisie)
                    joueur.vie -= enemie.degatAttaqueMagique[enemie.attaqueMagique.index(attaqueChoisie)]
            if len(attaqueUtilisee) == 2:
                attaqueUtilisee.remove(attaqueUtilisee[0])
            attaqueUtilisee.append(attaqueChoisie)
            time.sleep(1)
    if enemie.vie <= 0: #fin du combat
        print("vous avez gagné, vos statistique augmente")
        joueur.maxvie = round(joueur.maxVie * 1.1)
        joueur.degat = round(joueur.degat * 1.1)
        joueur.nombrePotion += 1
        enemie.vie = enemie.maxVie
        changerEndroit(joueur.idActuelle, 0)
    if joueur.vie <= 0:
        enemie.vie = enemie.maxVie
        joueur.vie = joueur.maxVie
        gameover()
                                    
                             
class endroit:
    def __init__(self, texte, possibilité, IDPossibilité, probaCombat):
        self.texte = texte
        self.possibilité = possibilité
        self.IDPossibilité = IDPossibilité #est fait en sorte que idPossibilité[x] l'id de possibilité[x]
        self.probaCombat = probaCombat
        
    def affichageEndroit(objet):  #permet de changer la position du joueur
        time.sleep(1)
        checking = False
        print(objet.texte)
        if len(objet.possibilité) > 0: #pour faire une salle sans choix(uniquement du texte) il suffit de ne rien mettre dans possibilité et l'ID d'après dans IDpossibilité
            print(objet.possibilité)
            while not(checking):
                x = input()
                for i in range(len(objet.possibilité)):
                    if objet.possibilité[i-1] == x:
                        checking = True
                        changerEndroit(objet.IDPossibilité[i-1], objet.probaCombat)
                print("Réponse séléctionnée incompatible. Veuillez recommencer")
        else:
            changerEndroit(objet.IDPossibilité[0], objet.probaCombat)
            
def changerEndroit(id, probaCombat):
    joueur.idActuelle = id
    if probaCombat >= randint(1, 20): #determine s'il y'aura un combat
        combat(joueur, listeEnemie[randint(0, len(listeEnemie)-1)])
    if id == 1: #grosse fonction qui affiche le bon endroit selon une id (voir logigramme) // certaine id ne sont pas sur le logigramme car il s'agit d'id de transition pour faire une disjonction de cas (ex. 33)
        end1.affichageEndroit()
    elif id == 2:
        end2.affichageEndroit()
    elif id == 3:
        end3.affichageEndroit()
    elif id == 4:
        end4.affichageEndroit()
    elif id == 7:
        end7.affichageEndroit()
    elif id == 8:
        if "grimoire" in joueur.inventaire: #dialogue du sorcier
            joueur.sort.append("frappe de feu")
            joueur.degatSort.append(30)
            joueur.inventaire.remove("grimoire")
            end9.affichageEndroit()
        elif joueur.nombrePotion == 0:
            joueur.nombrePotion = 1
            end10.affichageEndroit()
        else:
            end2.affichageEndroit()
    elif id == 6:
        if "ame du clerc" not in joueur.inventaire:
            changerEndroit(12, 0)
        else:
            changerEndroit(37, 0)
    elif id == 11:
        end11.affichageEndroit()
    elif id == 12:
        end12.affichageEndroit()
    elif id == 5:
        end5.affichageEndroit()
    elif id == 13:
        if "ame du clerc" not in joueur.inventaire:
            joueur.autelApparition = True
            end14.affichageEndroit()
        elif "ame du clerc" in joueur.inventaire and not(joueur.autelApparition):
            end14.affichageEndroit()
        elif "ame du clerc" in joueur.inventaire and joueur.autelApparition:
            joueur.inventaire.append("talisman")
            joueur.sort.append("halo de lumiere")
            joueur.degatSort.append(200)
            end15.affichageEndroit()
    elif id == 16:
        end16.affichageEndroit()
    elif id == 17:
        if "grimoire" not in joueur.inventaire and "frappe de feu" not in joueur.sort:
            joueur.inventaire.append("grimoire")
            print(joueur.inventaire)
            end18.affichageEndroit()
        else:
            end19.affichageEndroit()
    elif id == 20:
        end20.affichageEndroit()
    elif id == 21:
        end21.affichageEndroit()
    elif id == 22:
        end22.affichageEndroit()
    elif id == 23:
        end23.affichageEndroit()
    elif id == 24:
        end24.affichageEndroit()
    elif id == 25:
        if "ame du clerc" in joueur.inventaire:
            end27.affichageEndroit()
        else:
            end28.affichageEndroit()
    elif id == 26:
        end26.affichageEndroit()
    elif id == 29:
        end29.affichageEndroit()
    elif id == 30:
        joueur.idActuelle = 31
        combat(joueur, clercBestial)
    elif id == 31:
        joueur.inventaire.append("ame du clerc")
        end31.affichageEndroit()
    elif id == 32:
        end32.affichageEndroit()
    elif id == 33:
        if "ame du clerc" in joueur.inventaire and "frappe de feu" in joueur.sort:
            end34.affichageEndroit()
        else:
            end35.affichageEndroit()
    elif id == 36:
        end36.affichageEndroit()
    elif id == 37:
        end37.affichageEndroit()
    elif id == 38:
        end38.affichageEndroit()
    elif id == 39:
        joueur.idActuelle = 40
        combat(joueur, armureTenebreuse)
    elif id == 40:
        if "talisman" not in joueur.inventaire:
            print("vous avez battu l'armure, vous êtes maintenant coincé dans ce donjon prisonnier pendant que le mal s'abbat sur la contrée. Il en est fini pour vous")
            fin()
        else:
            end41.affichageEndroit()
    elif id == 42:
        end42.affichageEndroit()
    elif id == 43:
        joueur.idActuelle = 44
        combat(joueur, dieu)
    elif id == 44:
        end44.affichageEndroit()
    elif id == 45:
        print("Vous detruisez tous ce qui existe sur ce monde, l'âge des tenebres a commencé")
        fin()
    elif id == 46:
        print("Grâce à votre sacrifice le monde est meilleur et la paix règne et régnera pour l'éternité.")
        fin()
        
def fin():
    print("Merci d'avoir jouer à ce jeu jusqu'au bout.")
    time.sleep(10)
    print("il y a peut être plus à découvir")  
    sys.exit() #https://stackoverflow.com/questions/73663/how-do-i-terminate-a-script


#création des objets                                  
squelette = enemie("squelette", 50, 50, 25, 100, 250, 150, ["coup de poing", "coup d'épée", "desespoir"], [1, 15, 0], [], []) 
shamane = enemie("shamane", 75, 75, 200, 200, 300, 10, ["coup de bâton"], [5], ["boule de feu", "empoisonement", "electrocution"], [15, 20, 15])
chevalierTenebreux = enemie("chevalier tenebreux", 100, 100, 50, 100, 200, 30, ["coup d'épée", "coup de bouclier"], [20, 5], ["emprise tenebreuse"], [35])
ogre = enemie("ogre", 300, 300, 1000, 750, 500, 10000, ["coup de poing", "coup de pied"], [50, 30], ["avalement"], [30])
tankDebug = enemie("untitled", 1000000, 1000000, 100, 100, 100, 100, ["a", "b"], [0, 0], ["c", "d"], [0, 0])

listeEnemie = [squelette, shamane, chevalierTenebreux, ogre]

clercBestial = enemie("clerc bestial", 500, 500, 200, 250, 75, 0, ["griffure"], [20], ["halo de lumière", "serment doré", "lumière divine"], [30, 10, 75])
armureTenebreuse = enemie("armure tenebreuse", 250, 250, 50, 75, 200, 150, ["coup de hache", "pietinement"], [20, 30], ["emprise tenebreuse", "vortex noir"], [25,30])
dieu = enemie("princeps tenebris", 1000, 1000, 50, 500, 100, 175, ["lame perforante"], [99], ["emprise tenebreuse", "vortex noir", "avalement des abysses", "desespoir"], [30, 25, 15, 50]) 

end1 = endroit("Vous vous réveillez dans une contrée inconnue, dans un village calme bordé par une source d'eau nommé quietus . Vous apercevez un sorcier, une guérisseuse, un donjon et une forêt.", [], [2], 0)
end2 = endroit("Vous progressez et vous parvenez au centre du village. Où désirez-vous vous diriger ?", ["sorcier", "gueriseuse", "foret", "donjon"], [3, 4, 5, 6], 0)
end3 = endroit("vous allez vers le sorcier. Vous pouvez lui parler ou retourner en arrière", ["retour", "parler"], [2, 7], 0)
end7 = endroit("Il vous parle d un grimoire qu il a égaré dans la forêt.", [], [8], 0)
end9 = endroit("Vous lui donnez le grimoire et il vous apprend un sort rudimentaire en échange.", [], [2], 0)
end10 = endroit("Après avoir parlé Il vous donne une fiole de sang et vous dit qu'elle permet de vous soigner.", [], [2], 0)
end4= endroit("Vous approchez la guérisseuse. Voulez-lui parler ?", ["oui", "non"], [11, 2], 0)
end11 = endroit("Elle vous explique qu'il vous faut l'âme de l'ancien dieu dans le temple afin de rentrer dans le donjon. Elle vous dit aussi que chaque ennemie abbatu vous rendra plus fort.", [], [2], 0)
end12 = endroit("Le donjon est bloqué par une porte scellée", [], [2], 0)
end5 = endroit("Vous êtes dans la forêt. De grands arbres se dressent à vos cotés et il est difficile de se repérer. Voulez-vous aller en avant, à gauche ou à droite",["droite", "gauche", "avant", "arriere"], [13, 16, 20, 2], 0)
end14 = endroit("c est une impasse il faut retourner en arrière", ["arriere"], [5], 20)
end15 = endroit("Grâce à l'âme du clerc, un autel est apparu avec un talisman mis en évidence. Vous le prenez et retourner en arrière", [], [5], 0)
end16 = endroit("En marchant quelque mètre vous êtes à un pont. Mais il y a aussi une partie dans la forêt", ["traverser", "continuer", "arriere"], [17, 22, 5], 5)
end18 = endroit("À l’extrémité du pont se trouve un autel, à côté duquel repose un grimoire. Vous le prenez.", [], [16], 0)
end19 = endroit("Il n y a plus rien la-bàs", [], [16], 0)
end20 = endroit("Une statue d'une bête est visible où vous êtes. Il y a deux chemins.", ["premier", "deuxieme", "arriere"], [26, 21, 5], 10)
end21 = endroit("Une lueur est visible à travers les arbres.", ["continuer", "arriere"], [23, 20], 5)
end22 = endroit("à travers les arbres ont commence à voir une lueur de soleil.", ["continuer", "arriere"], [23, 16], 12)
end23 = endroit("vous vous apprpchez d'une montagne et vous montez une partie", ["continuer", "arriere"], [24, 21], 10)
end24 = endroit("sur la motagne il y a plusieurs chemin. L'un va dans une grotte et l'autre vers le sommet de cette montagne.", ["sommet", "grotte", "arriere"], [25, 32, 23], 0)
end26 = endroit("c est une impasse il faut retourner en arrière", ["arriere"], [20], 20)
end27 = endroit("Il n y a plus rien la-bàs", [], [24], 0)
end28 = endroit("En haut de cette montagne se trouve un petit temple dont des rugissement peuvent être entendus.", [], [29], 0)
end29 = endroit("en entrant dans le temple vous trouvez une immense bête sous un uniforme de clerc.", [], [30], 0)
end31 = endroit("vous obtenez l âme du clerc", [], [24], 0)
end32 = endroit("La grotte est peu éclairée mais il est possible de voir une porte.", ["continuer", "arriere"], [33, 24], 7)
end34 = endroit("vous pouvez ouvrir la porte grâce à votre feu et votre aura, voulez-vous le faire? (cela vous ramenera à un endroit précedent, l'inverse ne sera pas possible)", ["oui", "non"], [36, 32], 0)
end35 = endroit("Il faut du feu et l'aura d'un clerc pour ouvrir la porte.", [], [32], 0)
end36 = endroit("Vous ouvrez la porte. Le chemin derrière la porte vous amène à Quietus.", [], [2], 0)
end37 = endroit("Quand vous approchez la porte, elle s'ouvre grâce à l'âme du clerc", [], [38], 0)
end38 = endroit("vous trouvez à l'intérieur du donjon une armure qui se met à bouger. C'est le moment de se battre une dernière fois.", [], [39], 0)
end41 = endroit("Vous trouvez une ouverture sur l'armure où vous placer le talisman.", [], [42], 0)
end42 = endroit("vous êtes téléporté dans les abysses et face au dieu des ténèbres, la véritable dernière confrontation commence.", [], [43], 0)
end44 = endroit("Vous avez battu le dieu des tenebres. Souhaitez-vous prendre son pouvoir et semer le chaos ou les sceller à jamais dans ce donjon avec vous-même", ["chaos", "paix"], [45, 46], 0)
end47 = endroit("Vous réapparaissez à quietus vera la guériseuse", [], [2], 0)


#print("Hello, this is a snowflake: ❄") #pour je ne sais pas quelle raison avant de faire ce print trouvé ici: https://www.geeksforgeeks.org/how-to-print-unicode-character-in-python/ le programme se lançait avec une erreur 1: syntax error car j'avais des accents (cela n'était pas très amusant et je souffre de sérieux traumatismes maintenant. Si vous avez une raison merci de me la partager)
print("êtes-vous prêt à commencer cette aventure? (commencer pour commencer)")
x = ""
while x != "commencer":
    x = input()
    if x == "up, up, down, down, left, right, left, right, b, a, start": #petit easter egg
        print("vous avez gagné un sort faible")
        joueur.sort.append("get rekt")
        joueur.degatSort.append(10000000)
    elif x == "trodur":
        print("git gud (vous avez un million de point de vie maintenant)")
        joueur.maxVie = 10000000
        joueur.vie = joueur.maxVie
    elif x == "combat":
        combat(joueur, tankDebug) #utilisé pour le debug
    elif x == "ded":
        gameover() #utilisé pour le debug
    elif x == "test":
        joueur.inventaire.append("grimoire") #utilisé pour le debug
    else:
        if x != "commencer":
            print("Réponse séléctionnée incompatible. Veuillez recommencer")
end1.affichageEndroit()      

#merci pour nous avoir fait faire ce projet, c'était un exercice très sympa
        
        
                    
