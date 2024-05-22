import time
import random


class Player:
    def __init__(self):  # on crée notre joueur avec les pv, la saturation, et l'inventaire
        self.pv = 10
        self.saturation = 10
        self.stuff = list()

    def display(self):  # cette méthode affiche les valeures vitales et si le joueur est mort elle retourne True
        if self.pv <= 0 or self.saturation <= 0:
            return True
        print("\n\npv : ", self.pv)
        print("saturation : ", self.saturation)
        for i in self.stuff:
            print(f"{i[0]} x {i[1]}")

    def stuff_finder(self, item, index):  # cette méthode permet de trouver le nombre de valeur pour un objet ou
        # l'index dans l'inventaier d'un objet
        if index:
            return self.stuff.index([w for w in self.stuff if item in w][0])
        if [w for w in self.stuff if item in w]:
            return [w for w in self.stuff if item in w][0]
        return None


while True:
    input("\n\n\n\nBienvenue dans minecraft\nEntrer pour créer un nouveau monde.\n")  # Cette première partie
    # indispensable, a pour but de faire renoncer les joueur trop peut motivés à jouer en les faisant attendre, mais
    # c'est aussi un moyen des plus complexe de gagner des points sur le travail pratique.
    time.sleep(random.randint(0, 1))
    print("Création du monde...")
    time.sleep(random.randint(1, 7))
    print("Génération du terrain...")
    time.sleep(random.randint(1, 7))
    print("Entrée dans le monde...")
    time.sleep(random.randint(1, 7))
    p = Player()
    input("Vous entrez dans un nouveau monde dans un biome marais. Pour sélectioner le premier choix proposé/non entrez"
          " une valeur vide, pour sélectionnez le second/oui entrer une valeur quelquonque. Entrer pour continuer\n")
    if p.display():  # à chaque question on affiche à l'utilisateur son inventaire etc...
        input("Vous êtes mort, entrer pour recommencer.")
        continue  # une fois mort l'utilisateur peur recommencer p sera écraser par un nouveau Player() (ligne 39)
    if input("Couper du bois ou explorer ?\n"):
        p.saturation -= 1  # je me suis permi d'enlever de la saturation de temps à autre
        if p.display():
            input("Vous êtes mort, entrer pour recommencer.")
            continue
        if not input("Vous sortez du marais et trouvez un village.\nPiller ou retourner dans le marais ?\n"):
            p.stuff.append([1, "hache"])  # je construit l'inventaire en liste, chaque élément de cette liste est lui
            # meme une liste ou je donne le nombre d'objet d'abord puis son nom.
            if p.display():
                input("Vous êtes mort, entrer pour recommencer.")
                continue
            input("Vous trouver une hache et retournez au marais pour allez récolter du bois.\n")
    if p.stuff_finder("hache", False):
        p.stuff.append([8, "bois"])
    else:
        p.stuff.append([6, "bois"])
        p.saturation -= 1
    if p.display():
        input("Vous êtes mort, entrer pour recommencer.")
        continue
    input(f"Vous avez récolté {p.stuff[p.stuff_finder('bois', True)][0]} bois. Vous allez explorer une grotte.\n")
    p.stuff[p.stuff_finder("bois", True)][0] -= 3
    p.stuff.append([1, "torche"])  # Ici on a de toute façon une torche, c'est juste pour gagner des points
    if p.display():
        input("Vous êtes mort, entrer pour recommencer.")
        continue
    if input("Vous utilisez 3 blocks de bois pour fabriquer une torche de quoi vous éclairer... vous rencontrez une "
             "horde de zombie. Utiliser deux blocs de bois pour fabriquer une épée ?\n"):
        p.stuff[p.stuff_finder("bois", True)][0] -= 3
        p.stuff.append([1, "épée"])
        p.pv -= 5
        if p.display():
            input("Vous êtes mort, entrer pour recommencer.")
            continue
        input("Pendant la fabrication les zombies vous ont déjà attaqué mais vous parvenez à tous les éliminer.\n")
    else:
        p.saturation -= 7
        if p.display():
            input("Vous êtes mort, entrer pour recommencer.")
            continue
        input("Vous parvenez à combattre les zombies mais sans épée, cela vous a beaucoup fatigué.\n")
    if p.display():
        input("Vous êtes mort, entrer pour recommencer.")
        continue
    input("Vous avez trouvé in filon de diamant !\n")
    if p.stuff_finder("bois", False)[0] >= 3:
        p.stuff[p.stuff_finder("bois", True)][0] -= 3
        p.stuff.append([5, "diamant"])
        p.stuff.append([1, "pioche"])
        if p.display():
            input("Vous êtes mort, entrer pour recommencer.")
            continue
        input("Vous fabriquer une pioche avec 3 blocks de bois et minez le diamant.\n")
    else:
        p.stuff.append([5, "diamant"])
        if p.display():
            input("Vous êtes mort, entrer pour recommencer.")
            continue
        input("Malheureusement vous n'avez pas assez de bois pour faire une pioche vous avez du récolter les diamants "
              "à la main ce qui vous a fatigué.\n")
    while True:  # ici je crée une boucle qui fait que tant que l'on choisi pas de sortir on ne gagne pas et on perd des
        # pv et des points de sturation
        if p.display():
            input("Vous êtes mort, entrer pour recommencer.")
            break
        if input("Rester dans la grotte ou remonter à la surface ?\n"):
            if p.display():
                input("Vous êtes mort, entrer pour recommencer.")
                break
            input("Après être remonté vous vender vos diamants et viver une vie de riche, vous gagnez. Entrer pour "
                  "quitter\n")
            exit()  # Ici on propose à l'utilisateur de quitter si il gagne au lieu de recommencer.
        if p.stuff_finder("épée", False):
            p.pv -= random.randint(0, 1)
            p.saturation -= random.randint(0, 1)
        else:
            p.pv -= 2
            p.saturation -= 2
        if p.display():
            input("Vous êtes mort, entrer pour recommencer.")
            break
        input("En restant dans la grotte vous fous fatiguer et rencontrer des monstres qui vous enlève des pv.\n")
