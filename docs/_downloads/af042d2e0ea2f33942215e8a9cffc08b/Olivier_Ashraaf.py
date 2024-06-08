
def poser_question(question, choix_possibles):
    reponse = input(question + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + str(choix_possibles))
    return reponse

import random
inventaire = []

def chemindroite() :
    print("Vous avancez et tombez sur un ogre affamé. Vous essayez de le bruler avec votre torche mais il vous tue. GAME OVER")


def chateau():
    global attaque_corp
    attaque_loin = 0
    attaque_corp = 0
    print("Vous êtes dans un châteu et la pricesse vous demande d'aller chercher un anneua très spécial dans les montagnes")
    choix = poser_question ("Voulez vous aller a la recherche de cet anneau ?", ["oui", "non"])
    if choix == "non":
        choix = poser_question ("Voulez vous lui en donner un autre pour le remplacer", ["oui", "non"])
        if choix == "non":
            print("Elle meurt de chargin")
            print("GAME OVER")
        else:
            print("Ce n'est pas l'anneau qu'elle voulait, elle vous quitte")
            print("GAME OVER")
    else:
        print("Vous partez vous équiper")
        choix = poser_question ("Que décidez vous de prendre ?", ["arc et lance", "épée et bouclier"])
        inventaire.append (choix)
        if choix == "arc et lance":
            attaque_loin = 20
            attaque_corp = 5
        else:
            attaque_loin = 3
            attaque_corp = 30
        print("Vous sortez choisir une monture")
        choix = poser_question ("Quel monture choisissez vous de prendre? Un âne pour pouvoir transporter plus de matériel ou un cheval pour être plus rapide ?", ["un âne", "un cheval"])
        if choix == "un âne":
            liste_choix = ["corde", "lampe de poche", "briquet", "torche", "pioche"]
            choix = poser_question ("Quel objets voulez vous ?", liste_choix)
            liste_choix.remove(choix)
            inventaire.append (choix)
            choix = poser_question ("Choisissez un deuxième objet.", liste_choix)
            liste_choix.remove(choix)
            inventaire.append (choix)
            choix = poser_question ("Choisissez un dernière objet.", liste_choix)
            liste_choix.remove(choix)
            inventaire.append (choix)
            print("Vous atteignez une foret a la tombée de la nuit")
            choix = poser_question ("Voulez vous posez votre matériel et vous reposer ?", ["oui", "non"])
            if choix == "oui":
                print("Vous vous réveillez et vous voyez que tout votre matériel a été volé. Vous repartez au château à pied")
                chateau()
            else:
                print("Vous continuez votre chemin et vous trouvez une grotte.")
                choix = poser_question ("Voulez vous aller explorer la grotte ?", ["oui", "non"])
                if choix == "oui":
                    print("Vous entrer dans la grotte et une fléche vous passe devant les yeux et l'entrée se fait couvrir par un éboulement qui met la grotte dans l'obscurité complète. Vous comprenez que la grotte et piègée")
                    choix = poser_question
                    if "lampe de poche" in inventaire :
                        print("Malheureusement, votre lampe de poche n'a pas de piles. Elle ne vous sert donc a rien.") 
                    if "torche" and "briquet" in inventaire :
                        print("Vous pouvez vous éclairer grâce a la torche et au briquet et avancez dans la grotte. Vous voyez deux chemins.")
                        choix = poser_question ("Quel chemin voulez vous prendre ?", ["droite","gauche"])
                        if choix == "droite":
                            chemindroite()

                        else:
                            print("Vous avancez sur le chemin de droite et voyez une lumière au bout du chemin.")
                            choix = poser_question ("Voulez vous continuez vers la lumière ou retournez sur vos pas pour prendre l'autre chemin ?", ["continuer","prendre l'autre chemin"])
                            if choix == "continuer":
                                print("Vous arrivez au niveau de la lumière pour y voir que c'etait une pièrre précieuse. Vous la rammassez mais le tunnel s'effondre. GAME OVER")
                            else :
                                chemindroite()
                                
                                
                    else:
                        print ("Vous vous faites pièger dans la grotte et vous mourrez. GAME OVER")
                else:
                    print("Vous continuez dans la forêt et vous appercevez un groupe de sangliers affamés")
                    if attaque_loin == 20 :
                        print("Vous réussissez à affrontez les sangliers à distance et vous survivez. Après le combat vous appercevez une montagne")
                        choix = poser_question ("Voulez vous monter la montagne ?", ["oui", "non"])
                        if choix == "oui":
                            print("Vous commencez votre assencien mais vous tombez dans une crevasse. Heureusement elle n'est pas profonde et vous essayer de lancer une corde pour vous accrocher et remonter")
                            if "corde" in inventaire:
                                print("Vous réussissez à accrocher la corde et a vous sortir de cette crevasse, vous avancez et appercevez l'anneau et le récuperez.")
                                choix = poser_question ("Voulez vous faire le chemin retour pour amener l'anneau à la princesse ?", ["oui", "non"])
                                if choix == "oui":
                                    print ("Vous redescendez de la montagne pour reprendre votre âne et repartez en direction du château.Vous arrivez au château et épousez la princesse et lui offrez l'anneau. Félicitation, vous avez gagné !")
                                else:
                                    print ("Vous continuez sur la montagne et tombez sur un campement de bandits.")
                                    choix = poser_question ("Voulez vous les affronter ?", ["oui","non"])
                                    if choix == "oui":
                                        print("Vous vous battez mais ils sont trop nombreux et vouss tuent pour prendre votre matériel. GAME OVER")
                                    
                                    else:
                                        print ("Ils vous attaquent et vous tuent pour récuperer votre matériel. GAME OVER")
                                
                            else:
                                print("Vous ne pouvez pas sortir de la crevasse")
                                print("GAME OVER")
                        else:
                            print("Vous continuez votre chemin et appercevez un relais")
                            choix = poser_question("Voulez-vous vous arreter pour vous reposer ?", ["oui","non"])
                            if choix == "oui":
                                print("Vous êtes très bien accueilli, mais malheureusement, quand vous vous endormez, vois vous faites dépouiller. Vous essayez de continuer votre voyage mais vous n'avez olus de matériel. GAME OVER")

                            else:
                                print("Vous continuez votre route jusqu'à arriver à un énorme fleuve.")
                                choix = poser_question("Voulez vois le traverser a la nage ?", ["oui","non"])
                                if choix == "oui":
                                    print("Vous essayez de nager mais il y a trop de courant. Vous vous noyez. GAME OVER")
                                    
                                else:
                                    print("Vous retournez en arrière jusqu'au relais. Vous demandez pour vous reposer et vous pouvez le faire mais dans votre sommeil, vous vois faites dépouiller et ne pouvez pas continuer votre aventure. GAME OVER")
                            
                    else:
                        print("Vous essayez de vous déffendre avec votre épée et votre bouclier mais ils sont trop proches de vous et vous finnissez par être dévoré")
                        print("GAME OVER")

        else :
            print("Vous pouvez seulement prendre les choses choisi précédemment et rien de plus")
            print("Vous arrivez dans une fôret et vous voyez deux chemin")
            def chemin():
                if "épée et bouclier" in inventaire:
                    global attaque_loin
                    attaque_corp = 30
                    attaque_loin = 3
                else:
                    attaque_corp = 5
                    attaque_loin = 20
                choix = poser_question ("Vous prenez lequel ?", ["droite", "gauche"])
                if choix == "droite":
                    print("Vous rencontrez un pack de loups très agressifs")
                    choix = poser_question ("Vous voulez les battre ?", ["oui", "non"])
                    if choix == "non":
                        print("Vous avez peur et vous retournez au château")
                        chateau ()
                    else :
                        if attaque_corp == 30:
                            print("Vous les tuez très rapidement avec l'épée et le bouclier") 
                            tresor()


                        else :
                            print("Vous ne pouvez pas tuer les loups sans une épée et un bouclier")
                            print("GAME OVER")
                else :
                    print ("Tu rencontres un ours équipé avec des armes")
                    choix = poser_question ("Vous voulez lui confronter ?", ["oui", "non"])
                    if choix == "non" :
                        print("Vous revenez en arrière et vous redécidez le chemin que vous allez prendre")
                        chemin()
                    else : 
                        prob_die = 0.001
                        prob_live = 0.999
                        random_number = random.random()
                        if random_number <= prob_die :
                            print("Vous mourez. Bonne chance la prochaine fois.")
                            print("GAME OVER")
                        else :
                            print("Vous survivez")
                            print("Quelle chance que vous avez !")
                            tresor()
            chemin()

def montagne() :
    print("Vous apercevez la montage que vous cherchez pour l'anneau mais vous avez besoin quelque chose pour monter")
    if "corde" in inventaire :
        print("Vous utlisez la corde pour monter Vous montez la montagne et vous obtenez l'anneau pour la princesse. Vous lui l'as donnez et elle vous aime autant que jamais.")
        print("Mission passed + 100 respect")

    else : 
        print("Vous n'avez pas pu monter la montagne pour prendre l'anneau car vous n'avez pas de corde")
        print("GAME OVER")


def etang() :
        if "épée" in inventaire:
            attaque_corp = 50
        else :
            attaque_corp = 10
        print("Vous êtes devant un étang")
        choix = poser_question ("Vous pouvez soit traverser l'étang et continuez votre aventure, soit vous passez autour ce qui va prendre plus de temps.", ["à travers", "autour"])
        if choix == "à travers" :
            print("Un groupe de cocodiles vous attaque et vous devez vous défendre")
            if  attaque_corp == 50:
                print("Vous les tuez avec votre épée améliorée")
                montagne()
            else :
                print("Vous n'avez pas d'une épée améliorée donc vouus vous faîtes manger par un crocodile")
                print("GAME OVER")
                
        else :
            montagne()

def tresor():
    print("Vous avancez un momemt et puis vous retrouvez un trésor ")
    print("Dedans vous trouvez des choses pour améliorer une de vos armures et une corde. Mais vous avez seulement une choix")
    liste_choix = ["épée", "bouclier", "corde"]
    choix = poser_question ("Lequel vous prenez ?", liste_choix)
    inventaire.append (choix)
    etang()

chateau()


                        
                    
                     