(divers.aventure)=

# Aventure textuelle

Dans cette activité, vous allez programmer une **histoire interactive**.
C'est-à-dire une **histoire durant laquelle le lecteur peut faire des choix**.

Pour cela, vous allez principalement utiliser les éléments suivants:

- `print()` pour afficher le texte de l'histoire
- `input()` pour récupérer les choix du lecteur
- `if`, `elif` et `else` pour créer les embranchements de l'histoire
- `while` si vous voulez créer des boucles dans l'histoire
- éventuellement une `liste` pour stocker un inventaire

Voici un exemple pour vous aider:

```{codeplay}
# Vous pouvez utiliser cette fonction pour poser une question avec des choix possibles à l'utilisateur
def poser_question(question, choix_possibles):
    choix = input(f'{question} ({"/".join(choix_possibles)}): ')
    while choix not in choix_possibles:
        choix = input(f'{question} ({"/".join(choix_possibles)}): ')
    return choix

inventaire = []
perdu = False

print("Vous venez d'inventer une machine à voyager dans le temps.")
choix = poser_question("En quelle année voulez-vous aller ?", ["-100'000'000", "-2580", "-50", "1789", "2100"])
if choix == "-100'000'000":
    print("A peine arrivé, vous êtes bouffé par un dinosaure !")
    perdu = True
elif choix == "-2580":
    print("Vous êtes vénéré comme un dieu en Egypte antique.")
    print("Le phraraon Khéops vous offre son sceptre en or.")
    inventaire.append("Sceptre")
elif choix == "-50":
    print("Vous faites la rencontre de Jules César.")
    choix = poser_question("Voulez-vous rejoindre sa garde personnelle ?", ["oui", "non"])
    if choix == "oui":
        print("Vous recevez une armure de romain.")
        inventaire.append("Armure")
    elif choix == "non":
        print("Vous refusez poliment.")
elif choix == "1789":
    print("Vous vous faites couper la tête lors de la révolution française !")
    perdu = True
elif choix == "2100":
    print("Dans le futur, un sérum d'immortalité est vendu en pharmacie. Vous en piquez un peu.")
    inventaire.append("Sérum")

if not perdu:
    print("Vous revenez dans le présent.")
    if "Sceptre" in inventaire:
        print("Votre aventure vous a rendu super riche !")
    elif "Armure" in inventaire:
        print("Plus personne ne vous cherchera d'ennuis avec l'armure que vous avez ramenée !")
    elif "Sérum" in inventaire:
        print("Vous commercialisez votre sérum et rendez toute l'humanité immortelle (oups) !")

print("Fin de l'aventure")
```

## A vous de jouer 🎮

Créez votre propre histoire interactive et déposez le fichier `.py` sur Moodle !

```{codeplay}
:file: mon_aventure.py
# Vous pouvez utiliser cette fonction pour poser une question avec des choix possibles à l'utilisateur
def poser_question(question, choix_possibles):
    choix = input(f'{question} ({"/".join(choix_possibles)}): ')
    while choix not in choix_possibles:
        choix = input(f'{question} ({"/".join(choix_possibles)}): ')
    return choix

inventaire = []

print("Début de votre histoire...")
```

`````{admonition} Exemple plus complexe
:class: hint
````{dropdown} <span style="color:grey">Clique ici</span>
Voici le logigramme représentant une aventure plus complexe:

```{image} ../media/aventure.png
:width: 800px
```
Et son code:

```{codeplay}
# Vous pouvez utiliser cette fonction pour poser une question avec des choix possibles à l'utilisateur
def poser_question(question, choix_possibles):
    choix = input(f'{question} ({"/".join(choix_possibles)}): ')
    while choix not in choix_possibles:
        choix = input(f'{question} ({"/".join(choix_possibles)}): ')
    return choix

def entrer_foret():
    print("Vous arrivez dans une grande forêt lugubre.")
    print("Devant vous, vous pouvez voir deux chemins. Le chemin de gauche mène à une rivière et le chemin de droite mène à une grotte sombre.")
    choix = poser_question("Sur quel chemin voulez-vous aller ?", ["gauche", "droite"])
    if choix == "gauche":
        arriver_riviere()
    elif choix == "droite":
        entrer_grotte()

def arriver_riviere():
    print("Vous arrivez à la rivière.")
    print("Vous pouvez voir une canne à pêche sur la berge.")
    choix = poser_question("Voulez-vous ramasser la canne à pêche ?", ["oui", "non"])
    if choix == "oui":
        inventaire.append("canne à pêche")
        print("Vous avez ramassé la canne à pêche.")
    elif choix == "non":
        print("Vous avez décidé de ne pas prendre la canne à pêche.")
    print("Vous décidez de longer la rivière.")
    print("Après un certain temps, vous trouvez un pont en bois qui traverse la rivière.")
    choix = poser_question("Voulez-vous traverser le pont ?", ["oui", "non"])
    if choix == "oui":
        print("Vous traversez le pont et vous vous retrouvez sur l'autre rive de la rivière.")
        print("Vous tombez nez à nez avec un horrible ogre.")
        choix = poser_question("Voulez-vous l'affronter ?", ["oui", "non"])
        if choix == "oui":
            if 'épée' in inventaire:
                print("Grâce à votre épée, vous terrassez l'ogre en lui coupant la tête.")
                print("Vous reprenez la route et trouvez finalement votre maison.")
                print("Félicitations, vous avez terminé l'aventure!")
            else:
                print("Comme vous n'avez pas d'arme, l'ogre vous écrabouille.")
                print("Vous êtes mort.")
        elif choix == "non":
            print("Vous décidez de rebrousser chemin et retournez dans la forêt.")
            entrer_foret()
    elif choix == "non":
        print("Vous décidez de ne pas traverser le pont et retournez dans la forêt.")
        entrer_foret()

def entrer_grotte():
    print("Vous arrivez devant une grotte.")
    print("Vous voyez une torche éteinte près de l'entrée de la grotte.")
    choix = poser_question("Voulez-vous prendre la torche ?", ["oui", "non"])
    if choix == "oui":
        inventaire.append("torche")
        print("Vous avez pris la torche.")
    elif choix == "non":
        print("Vous décidez de ne pas prendre la torche et vous entrez dans la grotte sans lumière.")
    print("Vous avancez dans la grotte et vous rencontrez un dragon qui bloque votre chemin.")
    if "canne à pêche" in inventaire:
        print("Vous utilisez votre canne à pêche pour combattre le dragon et vous réussissez à le vaincre (incroyable).")
        entrer_salle_secrete()
    elif "torche" in inventaire:
        print("Vous utilisez votre torche pour effrayer le dragon et vous réussissez à passer sans être attaqué (incroyable).")
        entrer_salle_secrete()
    else:
        print("Vous n'avez pas d'arme pour combattre le dragon et vous êtes dévoré.")
        print("Vous êtes mort.")

def entrer_salle_secrete():
    print("Vous continuez votre chemin jusqu'à trouver une salle secrète.")
    print("Vous trouvez une magnifique épée sur un socle.")
    choix = poser_question("Voulez-vous ramasser l'épée ?", ["oui", "non"])
    if choix == 'oui':
        print("Vous parvenez à l'extraire du socle, vous être probablement l'élu.")
        inventaire.append("épée")
    elif choix == 'non':
        print("Vous décidez d'ignorer l'épée (mais pourquoi ???).")
    print("C'est un cul de sac, vous retournez dans la forêt.")
    entrer_foret()

# Début de l'aventure
inventaire = []

print("En vous balladant un peu trop loin de chez vous, vous avez fini par vous perdre.")
print("Retrouvez le chemin de la maison.")
entrer_foret()
```
