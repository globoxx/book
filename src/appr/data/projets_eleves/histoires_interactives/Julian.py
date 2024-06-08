def poser_question(question, choix_possibles):
    reponse = input(question + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + str(choix_possibles))
    return reponse

def entrer_foret():
    print("Vous vous trouvez à l'entrée de la forêt. Devant vous, le sentier s'enfonce dans les ténèbres. Votre cœur bat la chamade alors que vous vous apprêtez à pénétrer dans la forêt maudite. Vous avez devant vous trois choix")
    choix = poser_question("quel chemin empruntez vous ?",["le sentier de gauche","le sentier principal","le sentier de droite"])
    if choix == "le sentier de gauche":
        troll()
    if choix == "le sentier principal":
        cabane()
    if choix == "le sentier de droite":
        pont()
        
def troll():
    print("Vous suivez le sentier le long du ruisseau sombre. Soudain, vous entendez un grondement sourd. Une créature massive émerge des ombres. C'est un troll des bois, prêt à vous attaquer.")
    choix = poser_question("voulez vous combatre le troll ou essayer de l'amadouer avec de la nourriture pour pouvoir prendre la fuit ?",["le combatre","l'amadouer"])
    if choix == "le combatre":
        print("vous perdez vos deux points de vie et mourrez")
        entrer_foret()
    if choix == "l'amadouer":
        print("vous retroussez chemin et revenez au carrefour principal")
        entrer_foret()
        
def cabane():
    print("Vous avancez prudemment sur le sentier principal. Après quelques heures de marche, vous arrivez à un carrefour. Devant vous se dresse une vieille cabane abandonnée. Vous décidez d'entrer pour voir s'il y a quelque chose d'utile à l'intérieur.")
    print(" À l'intérieur, vous trouvez deux objets, une vieille carte au trésor et une fiole d'élixire de vie")
    choix = poser_question("lequel prenez vous?",["la carte","l'élixire de vie"])
    if choix == "la carte":
        inventaire.append("vieille carte")
        print("en sortant de la cabane vous ne trouvez aucun autre chemin et vous retournez au carrefour")
        aucun_autre_chemin()
    elif choix == "l'élixire de vie":
        inventaire.append("élixire de vie")
        print("en sortant de la cabane vous ne trouvez aucun autre chemin et vous retournez au carrefour")
        aucun_autre_chemin()
        
def pont():
    print("Vous serpentez à travers les arbres denses. Après un moment, vous arrivez à un pont suspendu au-dessus d'un ravin profond. Le pont semble fragile.")
    choix = poser_question("que décidez-vous de faire?",["traverser","chercher un autre chemin"])
    if choix == "traverser":
        print("En traversant, une planche se casse sous votre poid et vous fait perdre un point de vie.")
        vie = vie - 1
        coffre()
    elif choix == "chercher un autre chemin":
        papillon()
        
def coffre():
    print("En arrivant de l'autre côté, vous trouvez un coffre, il contient une épée enchantée et une boussole magique.")
    choix = poser_question("que prennez-vous?", ["épée anchantée","boussole"])
    if choix == "épée anchantée":
        grotte()
    elif choix == "boussole":
        grotte()
        
def papillon():
    print("En cherchant un autre chemin vous vous faîtes piquer par un papillon magique et vous fait perdre deux points de vie.")
    choix = poser_question("avez-vous pris l'élixir de vie?", ["oui","non"])
    if choix == "non":
        print("vous mourrez")
        entrer_foret()
    elif choix == "oui":
        choix = poser_question("l'utiliser?", ["oui","non"])
        if choix == "non":
            print("vous mourrez")
            entrer_foret()
        elif choix == "oui":
            if "élixir de vie" in inventaire:
                inventaire = [boussole]
                print("vous retournez au pont")
                pont()
                
def grotte():
    print("Vous appercevez une grotte et vous décidez de vous y aventurer. La grotte se sépart en deux chemins, à droite, sombre et dangeureux et celui de gauche qui est éclairé par une lueure faible.")
    choix = poser_question("quel chemin prennez-vous?", ["droite","gauche"])
    if choix == "droite":
        print("Vous vous perdez et retournez à l'entrée de la grotte")
        grotte()
    elif choix == "gauche":
        print("Après avoir avancé dans le chemin vous tombez sur une sortie très étroite avec des bors coupants. En la travesant vous perdez un point de vie.")
        vie = vie - 1
        elixir()
        print("En sortant de la grotte vous appercevez Eldoria. Malheureusement, un fort brouillard apparait et vous ne voyez plus où est la citée.")
        choix = poser_question("avez-vous la boussole magique?", ["oui","non"])
        if choix == "oui":
            print("Elle vous conduit à Eldoria et vous trouvez le coffre")
        elif choix == "non":
            print("vous vous perdez et retournez sur vos pas jusqu'à arriver à la forêt")
            entrer_foret()
        
def elixir():
    if "élixir de vie" in inventaire:
        vie = 2
        
        
            
        
        
        
def aucun_autre_chemin():
    entrer_foret()
    

    
    
inventaire = []
vie = 2
        
    
        
        
print("Vous êtes un aventurier intrépide à la recherche du légendaire trésor perdu de l'ancien royaume d'Eldoria. Vous avez entendu parler de ce trésor depuis votre enfance, mais personne n'a jamais réussi à le trouver. Guidé par une vieille carte trouvée dans une ancienne bibliothèque, vous vous lancez dans une aventure dangereuse à travers les profondeurs de la forêt maudite.Vous n'avez rien sur vous et vous avez deux points de vie.")
entrer_foret()
  