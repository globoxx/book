(divers.crypto)=

# Challenge de cryptographie : Cassage de mot de passe

Le but de ce challenge est de retrouver des mots de passe en clair à partir de leur hash.

Pour rappel, **un hash est une chaîne de caractères obtenue en appliquant une fonction de hachage à un texte**. Cette fonction transforme le texte en une chaîne irréversible de longueur fixe.

Exemple: le mot de passe `chat` donnera toujours la chaîne `a24bf9ab` une fois haché (avec la fonction de hachage utilisée dans ce challenge).

## Code fourni

Vous trouverez ci-dessous du code python très utile. Il vous sera donné avec chaque challenge mais vous pouvez déjà y jeter un œil.

```python
import time # Librairie pour mesurer le temps d'exécution d'un programme

# Cette fonction permet de retourner le hash (FNV-1a) d'un texte
# Cette fonction n'est pas cryptographiquement sûre
def compute_hash(text):
    s = str(text)
    h = 2166136261
    for ch in s:
        h ^= ord(ch)
        h = (h * 16777619) & 0xFFFFFFFF  # modulo 2^32
    return f"{h:08x}"  # 8 caractères hexadécimaux
```

## Etoile 1

Une base de données a fuité. Elle contient des mots de passe hachés. **Vous devez retrouver le mot de passe en clair à partir de son hash**. Heureusement, vous savez que le mot de passe est un code à 4 chiffres.

```{codeplay}
import time

def compute_hash(text):
    s = str(text)
    h = 2166136261
    for ch in s:
        h ^= ord(ch)
        h = (h * 16777619) & 0xFFFFFFFF
    return f"{h:08x}"

mdp_hash = "ed1e2bc7"

# Votre code ici
```

```{dropdown} Force brute
Ce type d'attaque est appelé une attaque par force brute. Elle consiste à tester toutes les combinaisons possibles jusqu'à trouver la bonne. C'est une méthode simple et rarement efficace, sauf quand les internautes sont fénéants et choisissent des mots de passe très simples !
```

## Etoile 2

Retrouver un mot de passe à 4 chiffres se fait quasi instantanément. Vous vous demandez... à partir de combien de chiffres le cassage du code prend-il plus de 10 secondes ? A partir de là, **estimez après combien de chiffres le cassage du code prendra plus d'une année**.

```{codeplay}
import time

def compute_hash(text):
    s = str(text)
    h = 2166136261
    for ch in s:
        h ^= ord(ch)
        h = (h * 16777619) & 0xFFFFFFFF
    return f"{h:08x}"

start = time.time()

# Votre code ici

end = time.time()
print("Temps écoulé:", end - start, "secondes")
```

```{dropdown} Le temps c'est précieux !
Sachez que le code ci-dessus tourne dans le navigateur, ce qui le rend plus lent qu'un code exécuté directement sur un ordinateur.

En pratique, les fonctions de hachages sont conçues pour être lentes, afin de ralentir les attaques par force brute. Contre-intuitif dans un monde numérique où on essaie de tout accélérer ! Cela signifie que le temps nécessaire pour casser un mot de passe peut être considérablement plus long que dans cet exercice où nous utilisons une fonction de hachage très simple.
```

## Etoile 3

Cette fois, le mot de passe est un mot de la langue française. Heureusement, vous disposez d'un dictionnaire de mots ({download}`dico.txt<../data/dico.txt>`). Utilisez-le pour **retrouver le mot de passe en clair à partir de son hash**.

Généralement, on utilise une librairie pour importer les lignes d'un fichier texte en python. Cependant, vu que vous codez ici dans un navigateur, je vous fournis directement la liste de mots via la fonction `get_words()` ci-dessous.

```{codeplay}
dictionary = [
    "chat",
    "chien",
    "loup",
    "lion",
    "tigre",
    "ours",
    "singe",
    "cheval",
    "vache",
    "mouton",
    "cochon",
    "poule",
    "canard",
    "oiseau",
    "poisson",
    "requin",
    "dauphin",
    "baleine",
    "serpent",
    "araignee",
    "soleil",
    "lune",
    "etoile",
    "ciel",
    "nuage",
    "pluie",
    "neige",
    "vent",
    "orage",
    "hiver",
    "ete",
    "printemps",
    "automne",
    "glace",
    "feu",
    "eau",
    "terre",
    "mer",
    "ocean",
    "montagne",
    "maison",
    "porte",
    "fenetre",
    "mur",
    "toit",
    "route",
    "pont",
    "ville",
    "village",
    "ecole",
    "classe",
    "table",
    "chaise",
    "livre",
    "stylo",
    "papier",
    "sac",
    "montre",
    "telephone",
    "cle",
    "voiture",
    "velo",
    "train",
    "bus",
    "avion",
    "bateau",
    "fusée",
    "moteur",
    "roue",
    "frein",
    "essence",
    "route",
    "garage",
    "voyage",
    "vacances",
    "pomme",
    "poire",
    "banane",
    "orange",
    "citron",
    "fraise",
    "cerise",
    "raisin",
    "pain",
    "fromage",
    "lait",
    "beurre",
    "sucre",
    "sel",
    "chocolat",
    "gateau",
    "pizza",
    "pates",
    "riz",
    "soupe",
    "rouge",
    "bleu",
    "vert",
    "jaune",
    "noir",
    "blanc",
    "gris",
    "rose",
    "violet",
    "orange",
    "clair",
    "sombre",
    "jour",
    "nuit",
    "matin",
    "soir",
    "minute",
    "heure",
    "seconde",
    "temps",
    "date",
    "annee",
    "ami",
    "amour",
    "famille",
    "parent",
    "enfant",
    "frere",
    "soeur",
    "voisin",
    "prof",
    "eleve",
    "classe",
    "groupe",
    "sport",
    "foot",
    "tennis",
    "basket",
    "velo",
    "course",
    "nage",
    "ski",
    "danse",
    "yoga",
    "secret",
    "code",
    "clef",
    "motdepasse",
    "login",
    "admin",
    "user",
    "guest",
    "systeme",
    "reseau",
    "internet",
    "ordinateur",
    "python",
    "crypto",
    "hash",
    "secure"
]
===
import time

def compute_hash(text):
    s = str(text)
    h = 2166136261
    for ch in s:
        h ^= ord(ch)
        h = (h * 16777619) & 0xFFFFFFFF
    return f"{h:08x}"

def get_words():
    return dictionary # Retourne la liste des mots de dico.txt (prête à l'emploi)

mdp_hash = "f96890c6"

# Votre code ici
```

```{dropdown} Attaque par dictionnaire
Cette attaque est plus efficace que la force brute car elle se base sur une liste de mots probables (le dictionnaire) plutôt que d'essayer toutes les combinaisons de caractères possibles. C'est une méthode couramment utilisée par les hackers alors évitez les mots courants dans vos mots de passe !
```

# Etoile 4

Notre cobaye a appris de ces erreurs et désormais son mot de passe est consistitué d'un mot de la langue française suivi de 2 chiffres. Exemple: chat21. Utilisez le dictionnaire précédent pour **retrouver le mot de passe en clair à partir de son hash**.

```{codeplay}
dictionary = [
    "chat",
    "chien",
    "loup",
    "lion",
    "tigre",
    "ours",
    "singe",
    "cheval",
    "vache",
    "mouton",
    "cochon",
    "poule",
    "canard",
    "oiseau",
    "poisson",
    "requin",
    "dauphin",
    "baleine",
    "serpent",
    "araignee",
    "soleil",
    "lune",
    "etoile",
    "ciel",
    "nuage",
    "pluie",
    "neige",
    "vent",
    "orage",
    "hiver",
    "ete",
    "printemps",
    "automne",
    "glace",
    "feu",
    "eau",
    "terre",
    "mer",
    "ocean",
    "montagne",
    "maison",
    "porte",
    "fenetre",
    "mur",
    "toit",
    "route",
    "pont",
    "ville",
    "village",
    "ecole",
    "classe",
    "table",
    "chaise",
    "livre",
    "stylo",
    "papier",
    "sac",
    "montre",
    "telephone",
    "cle",
    "voiture",
    "velo",
    "train",
    "bus",
    "avion",
    "bateau",
    "fusée",
    "moteur",
    "roue",
    "frein",
    "essence",
    "route",
    "garage",
    "voyage",
    "vacances",
    "pomme",
    "poire",
    "banane",
    "orange",
    "citron",
    "fraise",
    "cerise",
    "raisin",
    "pain",
    "fromage",
    "lait",
    "beurre",
    "sucre",
    "sel",
    "chocolat",
    "gateau",
    "pizza",
    "pates",
    "riz",
    "soupe",
    "rouge",
    "bleu",
    "vert",
    "jaune",
    "noir",
    "blanc",
    "gris",
    "rose",
    "violet",
    "orange",
    "clair",
    "sombre",
    "jour",
    "nuit",
    "matin",
    "soir",
    "minute",
    "heure",
    "seconde",
    "temps",
    "date",
    "annee",
    "ami",
    "amour",
    "famille",
    "parent",
    "enfant",
    "frere",
    "soeur",
    "voisin",
    "prof",
    "eleve",
    "classe",
    "groupe",
    "sport",
    "foot",
    "tennis",
    "basket",
    "velo",
    "course",
    "nage",
    "ski",
    "danse",
    "yoga",
    "secret",
    "code",
    "clef",
    "motdepasse",
    "login",
    "admin",
    "user",
    "guest",
    "systeme",
    "reseau",
    "internet",
    "ordinateur",
    "python",
    "crypto",
    "hash",
    "secure"
]
===
import time

def compute_hash(text):
    s = str(text)
    h = 2166136261
    for ch in s:
        h ^= ord(ch)
        h = (h * 16777619) & 0xFFFFFFFF
    return f"{h:08x}"

def get_words():
    return dictionary # Retourne la liste des mots de dico.txt (prête à l'emploi)

mdp_hash = "f0fa6b08"

# Votre code ici
```

```{dropdown} Attaque par dictionnaire étendue
Cette attaque est une variante de l'attaque par dictionnaire. Elle combine des mots probables avec des variations courantes, comme l'ajout de chiffres à la fin, pour augmenter les chances de succès.
```

# Etoile 5

Voici le boss ultime ! Le mot de passe est constitué d'un mot, suivi de 1 chiffre, d'un autre mot, et finalement un caractère spécial parmi `!@#$%&*`. Exemple: chat8chien!. **Retrouvez le mot de passe en clair à partir de son hash**.

```{codeplay}
dictionary = [
    "chat",
    "chien",
    "loup",
    "lion",
    "tigre",
    "ours",
    "singe",
    "cheval",
    "vache",
    "mouton",
    "cochon",
    "poule",
    "canard",
    "oiseau",
    "poisson",
    "requin",
    "dauphin",
    "baleine",
    "serpent",
    "araignee",
    "soleil",
    "lune",
    "etoile",
    "ciel",
    "nuage",
    "pluie",
    "neige",
    "vent",
    "orage",
    "hiver",
    "ete",
    "printemps",
    "automne",
    "glace",
    "feu",
    "eau",
    "terre",
    "mer",
    "ocean",
    "montagne",
    "maison",
    "porte",
    "fenetre",
    "mur",
    "toit",
    "route",
    "pont",
    "ville",
    "village",
    "ecole",
    "classe",
    "table",
    "chaise",
    "livre",
    "stylo",
    "papier",
    "sac",
    "montre",
    "telephone",
    "cle",
    "voiture",
    "velo",
    "train",
    "bus",
    "avion",
    "bateau",
    "fusée",
    "moteur",
    "roue",
    "frein",
    "essence",
    "route",
    "garage",
    "voyage",
    "vacances",
    "pomme",
    "poire",
    "banane",
    "orange",
    "citron",
    "fraise",
    "cerise",
    "raisin",
    "pain",
    "fromage",
    "lait",
    "beurre",
    "sucre",
    "sel",
    "chocolat",
    "gateau",
    "pizza",
    "pates",
    "riz",
    "soupe",
    "rouge",
    "bleu",
    "vert",
    "jaune",
    "noir",
    "blanc",
    "gris",
    "rose",
    "violet",
    "orange",
    "clair",
    "sombre",
    "jour",
    "nuit",
    "matin",
    "soir",
    "minute",
    "heure",
    "seconde",
    "temps",
    "date",
    "annee",
    "ami",
    "amour",
    "famille",
    "parent",
    "enfant",
    "frere",
    "soeur",
    "voisin",
    "prof",
    "eleve",
    "classe",
    "groupe",
    "sport",
    "foot",
    "tennis",
    "basket",
    "velo",
    "course",
    "nage",
    "ski",
    "danse",
    "yoga",
    "secret",
    "code",
    "clef",
    "motdepasse",
    "login",
    "admin",
    "user",
    "guest",
    "systeme",
    "reseau",
    "internet",
    "ordinateur",
    "python",
    "crypto",
    "hash",
    "secure"
]
===
import time

def compute_hash(text):
    s = str(text)
    h = 2166136261
    for ch in s:
        h ^= ord(ch)
        h = (h * 16777619) & 0xFFFFFFFF
    return f"{h:08x}"

def get_words():
    return dictionary # Retourne la liste des mots de dico.txt (prête à l'emploi)

mdp_hash = "5bfcfc03"

# Votre code ici
```

```{dropdown} Ajouter du sel !
On peut se demander si un hacker n'aurait pas déjà créé une immense table de hachage pour toutes les combinaisons de caractères et qu'il suffirait de la lire pour retrouver n'importe quel mot de passe. La réponse est oui et cela s'appelle une attaque par table arc-en-ciel. Pour s'en protéger, on ajoute du "sel" (salt en anglais) au mot de passe avant de le hacher. Le sel est une chaîne de caractères aléatoire stockée avec le mot de passe haché. Ainsi, même si deux utilisateurs ont le même mot de passe, leurs hachages seront différents grâce au sel ajouté.
```
