(prog1.sequences)=

# 6. Les types séquentiels

<a href="https://perso.limsi.fr/pointal/_media/python:cours:mementopython3.pdf" target="_blank">Mémento Python</a>  
<a href="https://support.apple.com/fr-ch/HT201236" target="_blank">Raccourcis clavier</a>

Certains programmes nécessitent l'utilisation d'un grand nombres de valeurs. Il serait impraticable de les mettre chacune dans une variable différente. Comme d'autres langages de programmation, Python offre la possibilité de stocker des séquences de valeurs dans des variables de type séquentiel (ou itérable).

## Le type liste

Une liste est une variable de type séquentiel. C'est une séquence ordonnée d'objets quelconques (nombres, textes, fonctions, etc...).  
Pour définir une liste, on met simplement la liste des objets que contient la liste dans des crochets `[]` séparés par des virgules. Ensuite on peut accéder au contenu de la liste en indiquant entre crochets le numéro de l'élément que l'on souhaite. **Attention, le numérotation commence à 0 !**

Il est aussi possible d'accéder aux éléments en partant de la fin en commençant par l'index -1 pour le dernier élément, puis -2, -3, etc.

```{codeplay}
jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
visiteurs = [200, 120, 345, 256, 123, 765, 644]

# On accède aux données du 1er jour (index 0)
print(f"Le {jours[0]}, il y a eu {visiteurs[0]} visiteurs")
# ...
# On accède aux données du dernier jour (index 06)
print(f"Le {jours[6]}, il y a eu {visiteurs[6]} visiteurs") 

# Il est aussi possible d'accéder au dernier élément avec l'index -1
print(f"Le {jours[-1]}, il y a eu {visiteurs[-1]} visiteurs") 
```

```{question}
En informatique, une liste ...

{v}`est ordonnée`  
{f}`n'est jamais vide`  
{f}`ne contient que des éléments du même type`  
{f}`est un ensemble mathématique`
```

````{admonition} Exercice 21 - Listes de branches
:class: note
Créez une liste `branches` et une liste `moyennes` qui contiennent respectivement les noms de 3 branches du gymnase et les moyennes que vous y avez.  
Affichez ensuite la moyenne pour chaque branche.  

```{codeplay}
:file: ex_21.py
branches = ...
moyennes = ...

print(...)
print(...)
print(...)
```
````

<!-- `````{admonition} Solution
:class: hint
````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down
```{codeplay}
:file: au_revoir.py
branches = ['math', 'français', 'info']
moyennes = [5, 4, 6]

print(f'Moyenne de {branches[0]}: {moyennes[0]}')
print(f'Moyenne de {branches[1]}: {moyennes[1]}')
print(f'Moyenne de {branches[2]}: {moyennes[2]}')
```
````
````` -->

```{question}
Que se passe-t-il si vous essayez d'accéder à un index en dehors de la liste (par exemple à l'index 3 dans l'exercice précédent) ?

{f}`ça fonctionne sans problème`  
{v}`vous avez une erreur de type "index out of range"`  
{f}`vous avez une erreur de type "invalid literal"`  
{f}`la valeur accédée dans ce cas vaut toujours 0`
```

Pour modifier un élément d'une liste, il suffit d'utiliser le signe `=` pour mettre une nouvelle valeur à l'index voulu.  
Pour ajouter un élément à une liste, on utilise la **méthode** `append()` ("ajouter" en français) en donnant en argument la valeur à ajouter.  

```{codeplay}
nombres = [5, 2, 6, 3, 8]
print(nombres)
nombres[2] = -5  # On modifie le 3ème élément de la liste
print(nombres)
nombres.append(1000)  # On ajoute un élément à la liste
print(nombres)
```

````{admonition} Pour aller plus loin
:class: hint
```{dropdown} <span style="color:grey">Méthode vs fonction</span>
:animate: fade-in-slide-down
Une méthode (ex: `append()`) est différente d'une fonction dans le sens où elle ne peut être appelée qu'avec un `.` via l'intermédiaire d'un objet (ici une liste). Plus de détails là-dessus l'année prochaine avec la **programmation orientée objet** !

La liste des méthodes accessibles aux listes est disponible <a href="https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists" target="_blank">ici</a>.
```
````

````{admonition} Exercice 22 - Modifications de listes
:class: note
Reprenez l'exercice précédent (l'exercice 21).
1. Modifier la moyenne de l'une de vos branches
2. Ajoutez une nouvelle branche avec sa moyenne.
3. Affichez les nouvelles données.

```{codeplay}
:file: ex_22.py
...  # Copiez l'exercice 21 ici

...  # Faites les modifications demandées

print(branches)
print(moyennes)
```
````

<!-- `````{admonition} Solution
:class: hint
````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down
```{codeplay}
:file: ex_25.py
branches = ['math', 'français', 'info']
moyennes = [5, 4, 6]

print(f'Moyenne de {branches[0]}: {moyennes[0]}')
print(f'Moyenne de {branches[1]}: {moyennes[1]}')
print(f'Moyenne de {branches[2]}: {moyennes[2]}')

moyennes[0] = 5.5  # Modification de ma moyenne de math
branches.append('histoire')  # Ajout de la branche histoire
moyennes.append(4.5)  # Ajout de ma moyenne d'histoire
print(branches)
print(moyennes)
```
````
````` -->

Les chaînes de caractères (`str`) peuvent aussi être indexées (chaque élément correspond alors à un caractère).

```{codeplay}
noms = ['Tim', 'Mia', 'Kim', 'Anna', 'Cindy', 'Léa']
print(noms[0][0])  # Accès à la première lettre de Tim
print(noms[2][1])  # Accès à la 2ème lettre de Kim
print(noms[-1][2])  # Accès à la 3ème lettre de Léa
```

La notation `[i:j]`, après le nom d'une variable qui contient une liste, permet d'extraire une sous-liste de la liste. Cette sous-liste, aussi appelée **tranche**, est une partie de la liste identifiée par les deux index `i` et `j`. La sous-liste contiendra donc les éléments se trouvant entre `i` et `j-1`.

```{codeplay}
noms = ['Tim', 'Mia', 'Kim', 'Anna', 'Cindy', 'Léa']

print(noms[:2])  # élément 0 et 1 (les 2 premiers éléments)
print(noms[2:4])  # élément 2 et 3
print(noms[4:])  # élément 4 et 5 (tous les éléments à partir de l'index 4)
```

```{question}
Quel est le résultat de l'expression `'python'[:2]` ?

{f}`thon`  
{f}`y`  
{f}`p`  
{v}`py`  
```

```{question}
Quel est le résultat de l'expression `'pikachu'[-3:]` ?

{f}`pik`  
{v}`chu`  
{f}`p`  
{f}`pika`  
```

Le mot-clé `in` permet de tester si une valeur se trouve dans une liste (ou n'importe quelle autre variable de type séquentiel).  
A l'inverse, `not in` permet de tester l'absence d'une valeur.

```{codeplay}
eleves_presents = ['Tiago', 'Marc', 'Simon', 'Julie', 'Maria', 'Inès']

if 'Marc' in eleves_presents:
    print('Marc est présent !')

if 'Hugo' not in eleves_presents:
    print('Hugo est absent !')
```

De la même manière, `in` permet de tester si un mot se trouve dans une phrase ou un texte.

```{codeplay}
poeme = """C'est un trou de verdure où chante une rivière
Accrochant follement aux herbes des haillons
D'argent ; où le soleil, de la montagne fière,
Luit : c'est un petit val qui mousse de rayons.

Un soldat jeune, bouche ouverte, tête nue,
Et la nuque baignant dans le frais cresson bleu,
Dort ; il est étendu dans l'herbe sous la nue,
Pâle dans son lit vert où la lumière pleut.

Les pieds dans les glaïeuls, il dort. Souriant comme
Sourirait un enfant malade, il fait un somme.
Nature, berce-le chaudement : il a froid.

Les parfums ne font pas frissonner sa narine ;
Il dort dans le soleil, la main sur sa poitrine
Tranquille. Il a deux trous rouges au côté droit."""

mot = "soldat"
if mot in poeme:
    print(f"Le mot '{mot}' se trouve bien dans 'Le dormeur du Val' d'Arthur Rimbaud")
```

## La boucle for

L'instruction `for ... in ...` permet **d'itérer** sur une variable de type séquentiel (par exemple une liste) et de répéter un bloc d'instructions pour chaque valeur de la séquence.  
`for valeur in liste` peut être traduit en français par `pour chaque valeur de la liste` et permet donc **d'itérer** sur chaque valeur.

Dans l'exemple ci-dessous, la variable `name` prendra successivement les valeurs de la liste `presidents` et la fonction `print()` sera à chaque fois exécutée.

```{codeplay}
presidents = ["Bush", "Clinton", "Bush", "Obama", "Trump"]
for name in presidents:
    print(name)
```

L'exemple suivant montre comment **itérer** sur une liste de couleurs.

```{codeplay}
from turtle import *
up()

backward(200)
for couleur in ['yellow', 'cyan', 'orange', 'pink', 'lime']:
    dot(80, couleur)
    write(couleur, align='center')
    forward(80)
```

````{admonition} Exercice 23 - Calcul de moyenne
:class: note
Ecrivez une fonction `calcule_moyenne()` qui prend une liste de nombres en argument et qui retourne la moyenne de ces nombres.  
Indice: la fonction `len()` permet de calculer la longueur d'une liste.

```{codeplay}
:file: ex_23.py
def calcule_moyenne(liste):
    ...

notes = [4.5, 3, 5, 2, 6, 5.5]
moyenne = calcule_moyenne(notes)
print(moyenne)
```
````

<!-- `````{admonition} Solution
:class: hint
````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down
```{codeplay}
:file: ex_23.py
def calcule_moyenne(liste):
    somme = 0
    for n in liste:
        somme = somme + n

    longueur_liste = len(liste)
    moyenne = somme / longueur_liste
    return moyenne

notes = [4.5, 3, 5, 2, 6, 5.5]
moyenne = calcule_moyenne(notes)
print(moyenne)
```
````
````` -->

## Le type range

Une `range` ("intervale" en français) est un autre exemple de variable de type séquentiel.  
Elles sont utilisées pour stocker des intervales de nombres entiers de manière plus efficace qu'une liste. Une variable de type `range` peut être créée avec la fonction `range(start, stop, step)` qui retourne un interval semi-fermé `[start, stop[` avec un incrément de `step`.

- `start` est la valeur de départ (vaut 0 si pas indiqué),
- `stop` est la valeur finale, mais sans l'inclure,
- `step` est l'incrément (vaut 1 si pas indiqué).

L'exemple suivant affiche le carré des nombres 1 à 9.

```{codeplay}
nombres = range(1, 10)  # Contient les nombres 1 jusqu'à 9
for nombre in nombres:
    print(f'{nombre}^2 = {nombre ** 2}')
```

L'exemple suivant dessine un polygone en utilisant une boucle `for` et une `range`.

```{codeplay}
from turtle import *

def polygone(a, n):
    for i in range(n):
        write(i)
        forward(a)
        left(360/n)

a = 50 # longueur des arrêtes
n = 5 # nombre de sommets
polygone(a, n)
```

En utilisant l'argument `step`, on peut visualiser l'intervale [-50, 250[ avec un incrément de 50.

```{codeplay}
from turtle import *
up()

start = -250
stop = 250
step = 50

for x in range(start, stop, step):
    goto(x, 0)
    write(x, align='center')
```

En imbriquant 2 boucles `for`, il est possible de construire toutes les tables de multiplications (jusqu'à 9 dans l'exemple).

```{codeplay}
for i in range(1, 10):
    print(f'Table de {i}')
    for j in range(1, 10):
        print(f'{i}*{j} = {i*j}')
    print()  # Ajout d'une ligne vide
```

````{admonition} Exercice 24 - Nombres premiers
:class: note
1. Ecrivez une fonction `est_premier()` qui contrôle si un nombre donné en argument est premier ou non et retourne la valeur logique associée.  
Pour rappel, un nombre est premier quand il n'est divisible par aucun autre nombre (à part 1 et lui-même).  
Les plus petits sont: 2, 3, 5, 7, 11, 13, etc...

2. Utilisez cette fonction pour afficher tous les nombres premiers plus petits que 1000.

```{codeplay}
---
hints: |
    Rappelle toi du modulo `%` pour contrôler si un nombre est divisible par un autre !
    ===
    Parcours les nombres un à un et vérifie qu'aucun ne soit diviseur du nombre à tester !
    ===
    Si tu trouves un diviseur, return False, sinon return True !
---
def est_premier(n):
    ...

...  # Affichage des nombres premiers plus petits que 1000
```
````

<!-- `````{admonition} Solution
:class: hint
````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down
```{codeplay}
:file: au_revoir.py
def est_premier(n):
    if n < 2:  # Nous savons que tout nombre plus petit que 2 ne peut pas être premier
        return False
    for i in range(2, n):  # On itère sur chaque nombre entre 2 et n-1
        if n % i == 0:  # Si notre argument est divisible par un nombre
            return False  # Alors il n'est pas premier
    return True  # S'il n'est divisible par aucun nombre entre 2 et n-1, alors il est premier

for n in range(1000):
    if est_premier(n):
        print(n)
```
````
````` -->

## Le jeu du pendu (optionnel)

Le jeu du pendu consiste à trouver un mot en devinant les lettres qui le composent. Le jeu se joue traditionnellement à deux, avec un papier et un crayon, avec le dessin d’une potence, dans lequel, pour chaque erreur, un trait du bonhomme allumette est ajouté.

```{codeplay}
:output_lines: 5
from turtle import *

a = 40
def potence():
    forward(100)
    backward(50)
    left(90)
    forward(180)
    right(90)
    forward(40)
    left(45)
    backward(56)
    forward(56)
    right(45)
    forward(50)
    right(90)
    forward(40)

def tete():
    dot(20)
    forward(20)

def bras1():
    right(45)
    forward(a)
    backward(a)

def bras2():
    left(90)
    forward(a)
    backward(a)

def torse():
    right(45)
    forward(a)

def jambe1():
    right(45)
    forward(a)
    backward(a)

def jambe2():
    left(90)
    forward(a)
    backward(a)
    hideturtle()

# On commence par dessiner la potence
potence()

# On définit la liste qui contient les fonctions de dessin à appeler dans l'ordre
dessins = [tete, bras1, bras2, torse, jambe1, jambe2]

mot_a_trouver = 'potiron'
lettres_trouvees = []  # Une liste vide qui contiendra les lettres trouvées par l'utilisateur

nb_erreurs = 0
while nb_erreurs < 6:
    mot_affiche = ''
    # On parcourt chaque lettre du mot à trouver et on l'affiche seulement si elle a été trouvée
    for lettre in mot_a_trouver:
        if lettre in lettres_trouvees:
            mot_affiche += lettre
        else:
            mot_affiche += '_'
        mot_affiche += ' '

    lettre_proposee = input(mot_affiche + '  lettre: ')
    if lettre_proposee in mot_a_trouver:
        lettres_trouvees.append(lettre_proposee)
    else:
        dessins[nb_erreurs]()
        nb_erreurs += 1  # Raccourci pour nb_erreurs = nb_erreurs + 1
```

```{admonition} Exercice du pendu
:class: note
Modifiez le programme du pendu pour que l'ordinateur choisisse aléatoirement un mot à trouver parmi une liste de mots de votre choix.  
Plusieurs pistes de solution:
1. Sélectionnez un mot de la liste à un index aléatoire avec la fonction `randint()` du module `random`.
2. Sélectionnez un mot de la liste aléatoirement avec la fonction `choice()` du module `random`.

Faites-en sorte que le programme s'arrête dès que vous avez trouvé le mot mystère.
```

Vous avez tout terminé ? Allez faire un tour sur <a href="https://apprendre.modulo-info.ch/prog1/grouper.html" target="_blank">Modulo</a> !
