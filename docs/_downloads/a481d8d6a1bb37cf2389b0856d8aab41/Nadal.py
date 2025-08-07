import time as ti
import random as rd
import keyboard
import threading
import os



# Initialisation des variables
position = [0, 0]  # Liste qui contient x et y
pos_x = position[0]
pos_y = position[1]
lieu_peche_1 = [5, 3]
lieu_vente = [1, 0]

pos_x_peche = lieu_peche_1[0]
pos_y_peche = lieu_peche_1[1]

pos_x_vente = lieu_vente[0]
pos_y_vente = lieu_vente[1]

rows = 10
cols = 10
inv = []
argent = rd.randint(100, 500)
pv = 100
attack = 10
nombre_de_poisson = 0

achatarme = True

class Armes:
    def __init__(self, nom, damage, pos_x_arme, pos_y_arme, prix):
        self.nom = nom
        self.damage = damage
        self.pos_x_arme = pos_x_arme
        self.pos_y_arme = pos_y_arme
        self.prix = prix
        
excalibure = Armes("excalibure", 100, 0, 1, 1000)

#crée la classe des poissons
class Poissons:
    def __init__(self, nom, heal, valeur):
        self.nom = nom
        self.heal = heal  #poit de santé donné une fois consommé
        self.valeur = valeur #prix dans le marché

    def heal(self, heal):      #vérifier que les pv ne dépasse pas 100
        if vie + heal <= 100:
            vie += heal
        else:
            vie = 100

#initialisation des poisons
truite = Poissons("truite", 10, 100)
saumon = Poissons("saumon", 20, 200)
carpe = Poissons("carpe", 15, 150)
dorade = Poissons("dorade", 5, 50)
poulpe = Poissons("poulpe", 30, 300)
requin = Poissons("requin", 50, 500)

class Monstre:
    def __init__(self, nom, vie, degats, prix, x_ske, y_ske):
        self.nom = nom
        self.vie = vie
        self.degats = degats
        self.prix = prix
        self.x_ske = x_ske
        self.y_ske = y_ske

boss_final = Monstre("xerse", 200, 15, "vous avez gagné", 0, 5)
boss = True


#permet de prendre la valeur des poissons selon le valeur en string car dans l'inventaire ils sont stockés en string.
def verifier_valeur_poissons(inp):
    if inp == "truite":
        valeur = truite.valeur
        return valeur
    elif inp == "saumon":
        valeur = saumon.valeur
        return valeur
    elif inp == "carpe":
        valeur = carpe.valeur
        return valeur
    elif inp == "dorade":
        valeur = dorade.valeur
        return valeur
    elif inp == "poulpe":
        valeur = poulpe.valeur
        return valeur
    elif inp == "requin":
        valeur = requin.valeur
        return valeur
    
def verifier_heal_poissons(inp):
    if inp == "truite":
        heal = truite.heal
        return heal
    elif inp == "saumon":
        heal = saumon.heal
        return heal
    elif inp == "carpe":
        heal = carpe.heal
        return heal
    elif inp == "dorade":
        heal = dorade.heal
        return heal
    elif inp == "poulpe":
        heal = poulpe.heal
        return heal
    elif inp == "requin":
        heal = requin.heal
        return heal
    
        

#affichage de la map
def afficher_map(rows, cols, x, y):
    print("votre position sur la map est affiché avec Le <P>")
    print("")
    for i in range(rows):
        for j in range(cols):
            if i == y and j == x:
                print("P", end="  ")
            elif i == pos_y_peche and j == pos_x_peche:
                print("~", end="  ") #end permet de ne pas revenir à la ligne
            elif i == pos_y_vente and j == pos_x_vente:
                print("💰", end=" ") #end permet de ne pas revenir à la ligne
            else:
                print(".", end="  ")
        print()

#affichage de l' inventaire
def afficher_inventaire(inv):
    print("")
    print("\t     ===========inventaire===========\n") #15 espace
    
    for index, item in enumerate(inv):
        print(f"{index + 1}){item:<12}", end=" ")   #prends 12 espacements
        lonheur = len(item)
        if(index + 1)%5 == 0:       #retour à la ligne tous les 5 objets
            print("\n")
    print("\n")
    print("\t\t ***===================***")

#affiche l'argent
def afficher_argent(argent, val):
    print("=" * 30)
    print(f"💰 Argent disponible : {argent} $")
    if val:
        print(f"❤️ Points de vie : {pv} pv")
    print("=" * 30)

def revenir_passé(rows, cols):
    global pos_x, pos_y
    pos_x = 0
    pos_y = 0
    afficher_map(rows, cols, pos_x, pos_y)

#éfface le terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#permet de définir un event.
stop_listener = threading.Event()

# Fonction pour vérifier les touches
def listen_obj_1(position, rows, cols, inv, argent):
    while not stop_listener.is_set():   #permet d'arrête le listener plus tard.
        #vérifie si la touche 1 est préssée
        if keyboard.is_pressed("1"):
            clear_terminal()
            afficher_map(rows, cols, pos_x, pos_y)
            ti.sleep(0.2)  # Petite pause pour éviter un spam trop rapide du message
            
        #vérifie si la touche 2 est préssée
        if keyboard.is_pressed("2"):
            clear_terminal()
            afficher_inventaire(inv)
            ti.sleep(0.1)
        #vérifie si la touche 3 est préssée
        if keyboard.is_pressed("3"):
            clear_terminal()
            afficher_argent(argent, True)
            ti.sleep(0.2)
        if keyboard.is_pressed("4"):
            clear_terminal()
            revenir_passé(rows, cols)
            ti.sleep(0.2)
           
def start_listener():
    global listener_thread, stop_listener
    if listener_thread and listener_thread.is_alive():
        return  # ne relance pas un thread s'il tourne déjà
    stop_listener = threading.Event()
    listener_thread = threading.Thread(target=listen_obj_1, args=(position, rows, cols, inv, argent), daemon=True)
    listener_thread.start()


# lancé en arrière fond pour vérifier les touches.
listener_thread = threading.Thread(target=listen_obj_1 , args=(position, rows, cols, inv, argent), daemon=True)
listener_thread.start()

# fonction de déplacement
def dep():
    global pos_x, pos_y
    
    def mouvement(x,y, position_max):
        choix = [] #liste de choix disponibles. 
        ajouter_a_choix = choix.append     #permet d'ajouter des objets à ma liste.
        #vérifie les déplacement possibles.
        if pos_x - 1 >= 0:
            ajouter_a_choix("gauche")
        if pos_x + 1 <= position_max:
            ajouter_a_choix("droite")
        if pos_y - 1 >=0:
            ajouter_a_choix("haut")
        if pos_y + 1 <= position_max:
            ajouter_a_choix("bas")
        return choix    #return la liste de choix
    #vérifie
    direction = mouvement(pos_x, pos_y, 9)
    options1 = "/".join(direction) #meilleurs affichage des options
    ch = input(f"dans quelle direction voulez-vous aller ({options1})?")
    #mise à jour des position en vérifiant qu'elles soient dans les possibilitées.
    if ch == "gauche" and "gauche" in direction:
        pos_x -= 1
    elif ch == "droite" and "droite" in direction:
        pos_x += 1
    elif ch == "haut" and "haut" in direction:
        pos_y -= 1
    elif ch == "bas" and "bas" in direction:
        pos_y += 1
    else:
        print("Direction invalide ou non possible.")

    #coèrence avec les position pour êttre en 1 1 en position initiale
    #print(pos_x , pos_y )
    afficher_map(rows, cols, pos_x, pos_y)
    ti.sleep(0.2)


def verifier_poi(inv):
    global nombre_de_poisson
    noms_poissons = [truite.nom, saumon.nom, carpe.nom, dorade.nom, poulpe.nom, requin.nom]
    nombre_de_poisson = sum(1 for i in inv if i in noms_poissons) #fait la somme des poissons dans l'inventaire.

            


# fonctionement de la pêche
def lieu_peche():
    global inv
    if pos_x == pos_x_peche and pos_y == pos_y_peche:   #vérifier l'emplacement
        verifier_poi(inv)   #fait la somme des poissons dans l'inventaire.
        if nombre_de_poisson < 5: #vérifie que la somme des poissons n'est pas plus grande que
                    
            peche_op = input("Vous êtes arrivé sur un lieu de pêche (pêcher/partir) : ").lower()
            while peche_op not in ["pêcher", "partir"]:
                    peche_op = input("Choix invalide. Tapez 'pêcher' ou 'partir' : ").lower()
            while peche_op == "pêcher":
                verifier_poi(inv)
                if nombre_de_poisson >= 5: #limitation de poisons possible.
                    print("limite de poissons fixé à 5")
                    break

                poi = rd.choice([truite.nom, saumon.nom, carpe.nom, dorade.nom, poulpe.nom, requin.nom])    #tirage au sort d'un poisson.
                    
                ti.sleep(3) # temps de pêche
                print(f"vous avez {poi}")
                inv.append(poi) #ajoute à l'inv le poissons
                afficher_inventaire(inv)
                peche_op = input("Voulez vous repêcher? (pêcher/partir) : ").lower()
        else:
            print("vous étes au max de poissons possibles") #message de prévention
    start_listener()
                       

#lieu de vente paramétrage
def lieu_vente():
    global argent, pv
    if pos_x == pos_x_vente and pos_y == pos_y_vente:       #vérifier la poistion.
        stop_listener.set()                                 #stop le listener pour que les touches 1 2 3 etc.. n'affiche pas la map ou autre.
        
        print("🍉🍉🍉🍉🍉🍉vous êtes au marché 🍉🍉🍉🍉🍉🍉🍉")
        afficher_inventaire(inv)

        sold = True
        while sold:
            try:
                choi_de_inventaire = input("chosissez l'emplacement que vous voulez vendre en comptant de gauche à droite et de haut en bas:\n 1 2 3 4 5\n 6 7 ...\n")
                afficher_inventaire(inv)
                
                valeur_choisi = int(choi_de_inventaire) #transforme en integer la valeur choisi pour l'emplacement
                
                if inv[valeur_choisi-1] != "excalibure":
                    poissons_choisit = inv[valeur_choisi-1] #sélctionne dans la liste de l'inventaire selon le choi.
                    vente = input(f"voulez vous vraiment vendre \033[1;38;2;255;255;0m{poissons_choisit}\033[0m qui coûte \033[1;92m${verifier_valeur_poissons(poissons_choisit)}\033[0m ? ")
                    if vente == "oui":
                        print("objet vendue")
                        print(f"{argent} + {verifier_valeur_poissons(poissons_choisit)}")
                        argent += verifier_valeur_poissons(poissons_choisit)        #mise à jour des données comme l'argent.
                        inv.remove(inv[valeur_choisi-1])
                        
                        afficher_argent(argent, False)
                        afficher_inventaire(inv)
                else:
                    print("excalibure est très dessus de vous, la foudre s'abat sur vous")
                    print("vous avez perdu")
                    pv = -100
                    sold = False
                
            except:
                
                exit_erreur = input("valeur d'entré invalide (partir) ?" )
                
                if exit_erreur == "partir":
                    print("vous avez quité le marché.")
                    sold = False
    start_listener()
    
    

def epee(nom_arme):
    global argent, inv, attack, achatarme
    
    if pos_x == nom_arme.pos_x_arme and pos_y == nom_arme.pos_y_arme and achatarme:
        stop_listener.set() 
        print(f"\nun passant vous propose de lui acheter son arme")
        stop_listener.set()
        prendre = input(f"voulez vous acheter son arme qui coûte ${nom_arme.prix}?")
        if prendre == "oui" and argent - nom_arme.prix > 0:
            print(f"vous avez acheté {nom_arme.nom} qui fait {nom_arme.damage} degats.")
            inv.append(nom_arme.nom)
            attack = nom_arme.damage
            argent -= nom_arme.prix
            print(f"vous avez ${argent}")
            achatarme = False
        elif prendre == "oui" and argent - nom_arme.prix <= 0:
            print("le passant vous recalle gentillment et vous dit que vous n'étes pas l'élu.")
        else:
            print("le passant vous dit au revoir.")
    start_listener()
            



def combat():
    global pv, boss, inv
    

    if pos_x == boss_final.x_ske and pos_y == boss_final.y_ske:
        stop_listener.set()      
        bataille_finale = input("voulez-vous vous battre avec le grand xerse ? (oui/non)")
        if bataille_finale == "oui":
            print("xerse joue à pile ou face pour savoir qui va commencer.(il choisit pile)")
            ti.sleep(2)
            pile_ou_face = rd.choice([True , False])
            if pile_ou_face:
                print("vous avez perdu.") #cas où vous perdez à pile ou face

                

                while pv >= 0:
                    print("xerse vous attaque.")
                    print(f"xerse vous inflige {boss_final.degats} degâts")
                    pv -= boss_final.degats
                    print(f"il vous reste {pv} pv")
                    if pv <= 0:
                        print("vous êtes mort.")
                        break
                    
                    ti.sleep(2)

                    #paramétrage des actions disponibles.
                    type_action = input("que voulez vous faire ?(attaquer/soigner/passer)")
                    if type_action == "attaquer":
                        print(f"vous infligez {attack} degâts à xerse")
                        boss_final.vie -= attack
                        print(f"xerse a {boss_final.vie} pv")
                    
                    elif type_action == "soigner":
                        print("vous vous soignez")
                        liste_speciale_poissons = [i for i in inv if i in ["truite", "saumon", "carpe", "dorade", "poulpe", "requin"]]
                        
                        if not liste_speciale_poissons:
                            print("vous n'avez pas de poisson pour vous soigner. Vous perdez un tour.")
                            continue

                        print("liste de poissons disponibles :")
                        for idx, poisson in enumerate(liste_speciale_poissons, start=1):
                            print(f"{idx}. {poisson} (soin: {verifier_heal_poissons(poisson)})")

                        heal_perso = input("Quelle position voulez-vous choisir ? ")
                        
                        try:
                            heal_perso_int = int(heal_perso)
                            poisson_choisi = liste_speciale_poissons[heal_perso_int - 1]

                            confirmation = input(f"Voulez-vous vraiment manger {poisson_choisi} qui soigne de {verifier_heal_poissons(poisson_choisi)} ? (oui/non) ")
                            if confirmation == "oui":
                                soin = verifier_heal_poissons(poisson_choisi)
                                pv = min(pv + soin, 100)
                                inv.remove(poisson_choisi)
                                print(f"Vous avez maintenant {pv} pv")
                            else:
                                print(f"Vous hésitez... mais vous attaquez finalement !")
                                boss_final.vie -= attack
                                print(f"Vous infligez {attack} dégâts à Xerse.")
                                print(f"Xerse a {boss_final.vie} pv")

                        except (IndexError, ValueError):
                            print("Choix invalide ! Vous attaquez par réflexe !")
                            boss_final.vie -= attack
                            print(f"Vous infligez {attack} dégâts à Xerse.")
                            print(f"Xerse a {boss_final.vie} pv")

                    #vérification des points de vie du boss
                    if boss_final.vie <=0:
                        print("vous avez tué le boss")
                        boss = False
                        break
                    ti.sleep(2)
                    
                         
            else:   #cas où vous gagnez à pile ou face
                print("vous avez gagné.")
                print("vous commencer")
                while pv >= 0:
                    type_action = input("que voulez vous faire ?(attaquer/soigner/passer)")
                    if type_action == "attaquer":
                        print(f"vous infligez {attack} degâts à xerse")
                        boss_final.vie -= attack
                        print(f"xerse a {boss_final.vie} pv")


                    elif type_action == "soigner":
                        print("vous vous soignez")
                        liste_speciale_poissons = [i for i in inv if i in ["truite", "saumon", "carpe", "dorade", "poulpe", "requin"]]
                        
                        if not liste_speciale_poissons:
                            print("vous n'avez pas de poisson pour vous soigner. Vous perdez un tour.")
                            continue

                        print("liste de poissons disponibles :")
                        for idx, poisson in enumerate(liste_speciale_poissons, start=1):
                            print(f"{idx}. {poisson} (soin: {verifier_heal_poissons(poisson)})")

                        heal_perso = input("Quelle position voulez-vous choisir ? ")
                        
                        try:
                            heal_perso_int = int(heal_perso)
                            poisson_choisi = liste_speciale_poissons[heal_perso_int - 1]

                            confirmation = input(f"Voulez-vous vraiment manger {poisson_choisi} qui soigne de {verifier_heal_poissons(poisson_choisi)} ? (oui/non) ")
                            if confirmation == "oui":
                                soin = verifier_heal_poissons(poisson_choisi)
                                pv = min(pv + soin, 100)
                                inv.remove(poisson_choisi)
                                print(f"Vous avez maintenant {pv} pv")
                            else:
                                print(f"Vous hésitez... mais vous attaquez finalement !")
                                boss_final.vie -= attack
                                print(f"Vous infligez {attack} dégâts à Xerse.")
                                print(f"Xerse a {boss_final.vie} pv")

                        except (IndexError, ValueError):
                            print("Choix invalide ! Vous attaquez par réflexe !")
                            boss_final.vie -= attack
                            print(f"Vous infligez {attack} dégâts à Xerse.")
                            print(f"Xerse a {boss_final.vie} pv")

                        
                    if boss_final.vie <=0:
                        print("vous avez tué le boss")
                        boss = False
                        break
                    ti.sleep(2)

                    print("xerse vous attaque.")
                    print(f"xerse vous inflige {boss_final.degats} degâts")
                    pv -= boss_final.degats
                    
                    print(f"il vous reste {pv} pv")
                    if pv <= 0:
                        print("vous êtes mort.")
                        break
                    ti.sleep(2)
                

        else:
            print("votre peur a pris le dessus sur vous. Vous rééssayerait une autre fois.")
        
def debut():
    print("Nadal Ibriz      version: 17/4/2025")
    
    input("bienvenue dans polyrpg. \ndans ce jeu les touches suivantes sont disponibles: \n 1 = ouvrir la map \n 2 = ouvrir l'inventaire \n 3 = voir l'argent \n 4 = revenir à la position initial\n")

debut()
while pv >= 0 and boss:
    dep()
    lieu_peche()
    lieu_vente()
    epee(excalibure)
    combat()
    
    
    
    
