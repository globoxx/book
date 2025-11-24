(prog_dessin.parcourir)=

# 5. Parcourir

Dans ce chapitre, nous allons découvrir le concept très important de **liste**. Une liste est une séquence ordonnée d'objets, par exemple de couleurs, de distances ou d'angles. Nous pouvons parcourir les valeurs d'une liste une après l'autre avec une boucle `for`. Nous allons voir que :

- la liste `[10, 20, 30]` représente une séquence de valeurs,
- dans la boucle `for d in [10, 20, 30]:` la variable d'itération `d` parcourt des nombres,
- dans la boucle `for c in ['red', 'blue', 'green']:` la variable d'itération `c` parcourt des couleurs.

```{question}
En informatique, une liste est 

{v}`une séquence d'objets ordonnée`  
{f}`une séquence d'objets non ordonnée`  
{f}`un ensemble mathématique`  
{f}`une suite de nombres (et uniquement ça)`
```

Auparavant nous avons vu la boucle `for` comme une simple répétition. Dans ce chapitre, la boucle `for` est différente dans le sens où nous parcourons une séquence et nous utilisons une valeur différente pour chaque tour. En programmation, cette idée de **parcourir une séquence** et d'utiliser une **valeur successive** à chaque tour, est un concept fondamental.

## Variable d'itération

Dans des boucles d'itération, nous allons utiliser des variables d'une seule lettre. Ce n'est pas une règle de python, mais c'est une convention.

- `a` pour un angle
- `c` pour une couleur
- `d` pour une distance
- `i` pour un indice (entier)
- `r` pour un rayon

```{question}
La variable `i` désigne normalement

{f}`une longueur`  
{f}`un caractère`  
{v}`un entier`  
{f}`une coordonnée`
```

## Parcourir

Dans les exemples suivants nous allons parcourir différents types de listes.

### Des couleurs

Pour dessiner de multiples couleurs, nous pouvons définir une liste de couleurs à parcourir.
En Python, une liste est délimitée par des crochets `[]` et les éléments sont séparés par une virgule.

Dans l'expression `for c in [...]`, la variable `c` va prendre à tour de rôle les valeurs dans la séquence. Dans l'exemple ci-dessous, `c` prendra successivement les valeurs : `'yellow'`, `'cyan'`, `'orange'`, etc. Le bloc indenté qui suit la ligne `for` sera exécuté autant de fois que la séquence contient d'éléments.

La fonction `dot(80, c)` afficher un disque de diamètre 80 et de couleur `c`.  
La fonction `write(c)` affiche le nom de la couleur `c`.

````{exercise}
Modifiez la séquence des couleurs.

```{codeplay}
from turtle import *
up()

backward(200)
for c in ['yellow', 'cyan', 'orange', 'pink', 'lime']:
    dot(80, c)
    write(c)
    forward(80)
```
````

### Des diamètres

Nous pouvons également parcourir une séquence de nombres et ainsi, spécifier une liste de diamètres de disques.

La fonction `dot(d, 'pink')` affiche un disque de diamètre `d` de couleur rose.  
La fonction `write(d)` affiche la distance `d`.

````{exercise}
Modifiez la séquence des diamètres.

```{codeplay}
from turtle import *
up()

backward(220)
for d in [40, 60, 80, 60, 40]:
    dot(d, 'pink')
    write(d)
    forward(100)
```
````

### Des distances

Dans le chapitre [2. Définir](prog_dessin.definir) nous avons vu les fonctions `batiment()` et `porte()` avec 8 lignes chacune qui dessinent un rectangle.

À l'aide d'une liste qui contient ces 4 distances, nous pouvons écrire ces fonctions de manière bien plus compacte. Pour illustrer les distances parcourues, nous l'affichons à chaque itération avec `write(a)`.

````{exercise}
Modifiez la taille du bâtiment et de la porte.

```{codeplay}
from turtle import *

def batiment():
    for d in [200, 100, 200, 100]:
        forward(d/2)
        write(d)
        forward(d/2)
        left(90)

def porte():
    for d in [30, 50, 30, 50]:
        forward(d/2)
        write(d)
        forward(d/2)
        left(90)

batiment()
forward(40)
porte()
```
````

### Des angles

Nous allons reprendre notre fonction `maison()` et, à l'aide d'une séquence, nous allons l'écrire de manière bien plus compacte. Cette fois-ci, la séquence représente des angles, donc nous nommons notre variable `angle` pour nous en rappeler.
Pour illustrer le parcours des angles, nous les affichons à chaque itération avec `write(angle)`.

```{codeplay}
from turtle import *

def maison(d):
    dot()
    forward(1.41*d)
    for a in [90, 45, 90, 45]:
        write(a)
        left(a)
        forward(d)
    left(90)

backward(200)        
maison(50)
forward(150)
maison(80)
```

## Range

Vous vous rappelez de `for i in range(n)` ?  
La fonction `range(start, stop, step)` permet de produire une séquence linéaire d’entiers. Les entiers se trouvent dans l’intervalle semi-fermé `[start, stop[` avec un incrément de `step`.

Le sens des paramètres :

- `start` est la valeur de départ,
- `stop` est la valeur finale, mais sans l'inclure,
- `step` est l'incrément (la distance entre 2 valeurs successives).

Par défaut, `start = 0`, `step = 1` et seule la valeur de `stop` est obligatoire. C'est pourquoi quand nous écrivions `for i in range(n)`, `n` variait de `0` à `n-1`.

```{admonition} Pour résumer
:class: hint
Ecrire `range(10)` est donc similaire à écrire `[0, 1, 2, ..., 8, 9]`. L'unique différence réside dans le fait que la fonction `range()` ne retourne pas à proprement parler une liste, mais un <a href="https://gayerie.dev/docs/python/python3/iterateur_generateur.html#les-generateurs">générateur</a>.
```

`````{exercise}
Affichez les entiers entre -50 et 200 avec un incrément de 25.

```{codeplay}
:file: range3.py
from turtle import *
up()

start = -250
stop = 250
step = 50

for x in range(start, stop, step):
    goto(x, 0)
    write(x)
```

````{dropdown} Solution
```python
start = -50
stop = 201
step = 25
```
````
`````

## Dessiner une spirale

Si nous dessinons un polygone, mais augmentons la longueur de chaque segment successif en utilisant la variable d'itération `i`, nous obtenons une spirale.

```{codeplay}
:file: range8.py
from turtle import *

for i in range(100):
    write(i)
    forward(i)
    left(30)
```

## Maisons en couleurs

Revenons à nos listes et parcourons une séquence d'angles avec une variable d'itération `a` pour dessiner une maison.

Ensuite, nous allons parcourir une séquence de couleurs avec une variable `c` pour dessiner des maisons de différentes couleurs.

```{codeplay}
:file: tuple5.py
from turtle import *

def maison(d, c):
    fillcolor(c)
    begin_fill()     
    forward (1.41*d)
    for a in [90, 45, 90, 45]:
        left(a)
        forward(d)
    left(90)
    end_fill()

backward(250)
for c in ['red', 'yellow', 'pink', 'lightblue', 'lightgreen']:
    maison(50, c)
    forward(100)
```

## Fleur

Ci-dessous nous dessinons 6 fois un losange pour obtenir une fleur.
Avec une boucle `for` nous parcourons une séquence de 6 couleurs alternantes.

````{exercise}
Il manque un pétale, corrigez le programme.

```{codeplay}
:file: tuple6.py
from turtle import *
getscreen().bgcolor('lightgreen')

def losange(d, c):
    fillcolor(c)
    begin_fill()
    for a in [60, 120, 60, 120]:
        forward(d)
        left(a)
    end_fill()

for c in ['pink', 'red', 'pink', 'red', 'pink']:
    losange(100, c)
    left(60)
```

```{dropdown} Solution
Il n'y a que 5 couleurs dans la listes ce qui ne créera que 5 losanges. Il suffit d'ajouter une couleur à la liste à parcourir.
```
````

## Smiley

Dans cet exemple nous allons parcourir différents diamètres de la bouche à l'aide d'une variable que nous appelons `d`. Voici quatre smileys avec différentes formes de bouche.

````{exercise}
Faites varier un autre paramètre, par exemple la distance des yeux, ou la taille d'un œil.

```{codeplay}
:file: tuple8.py
from turtle import *

getscreen().bgcolor('skyblue') # Permet de modifier la couleur de fond
up()

backward(200)
for d in [10, 20, 30, 40]:
    dot(100, 'yellow')

    left(45)
    forward(20)
    dot(15)

    right(45)
    backward(30)
    dot(15)

    right(60)
    forward(35)
    dot(d)
    left(60)
    
    forward(120)
    left(5)
```
````

## Cube 3D

Avec trois losanges, nous pouvons dessiner un cube en 3D.

```{codeplay}
from turtle import *

def losange(d):
    for a in [120, 60, 120, 60]:
        forward(d)
        left(a)
        
for i in range(3):
    losange(100)
    left(120)
```

## Cube en couleur

Avec l'utilisation de trois couleurs, l'effet 3D est accentué.
Nous choisissons des couleurs claires pour les surfaces du haut, et des couleurs sombres pour les surfaces vers le bas.

```{codeplay}
from turtle import *

def losange(d, c):
    fillcolor(c)
    begin_fill()
    for a in [120, 60, 120, 60]:
        forward(100)
        left(a)
    end_fill()

def cube():      
    for c in ['pink', 'violet', 'darkviolet']:
        losange(100, c)
        left(120)

cube()
```

## Pavage du plan

Un pavage du plan est un ensemble de portions du plan, par exemple des polygones, dont l'union est le plan tout entier, sans recouvrement.

```{codeplay}
from turtle import *

def losange(d, c):
    fillcolor(c)
    begin_fill()
    for a in [120, 60, 120, 60]:
        forward(100)
        left(a)
    end_fill()
        
def cube():
    for c in ['pink', 'violet', 'darkviolet']:
        losange(100, c)
        left(120)

for i in range(3):
    backward(100)
    cube()
    forward(100)
    left(120)
```

## Exercice récapitulatif

````{exercise}

Voici une fonction `star(c, d)` qui dessine une étoile de couleur `c` et de diamètre `d`.  
Utilisez des boucles `for` pour dessiner des étoiles de différentes couleurs et tailles, afin de créer une jolie composition.

Il n'est pas nécessaire d'utiliser de l'aléatoire, vous pouvez définir vous-même des listes de couleurs et de diamètres à parcourir.

```{codeplay}
:file: ex5.py
from turtle import *
from random import *

def star(c, d):
    color(c)
    for i in range(5):
        forward(d) 
        right(144)

dot(1000, 'black') # Fond noir
up()
goto(randint(-300, 300), randint(-200, 200)) # Position aléatoire
down()
star('yellow', 50)

# Votre code ici...
```

Téléchargez le fichier `.py` et déposez le fichier sur Moodle à l'endroit prévu.
````

## Et à part le dessin ?

Les listes sont souvent un moyen de grouper des valeurs ensemble. Par exemple, le gymnase regroupe les notes d'un élève dans une branche pour en calculer la moyenne.

```{admonition} Rappel
:class: hint
- La fonction `print()` permet d'afficher du texte.
- `a = 0` est une instruction permettant de créer une variable `a` et lui donner la valeur `0`.
- `a = a + 3` permet d'ajouter 3 à la variable `a`.
```

`````{exercise}
Ecrivez une fonction qui prend une liste de notes en paramètre et affiche la moyenne.

La fonction prend donc un paramètre `notes` qui est une liste de nombres. La fonction `len(liste)` permet de calculer la longueur d'une liste.

```{codeplay}
# Votre code ici...
```

````{dropdown} Solution
```python
def calcul_moyenne(notes):
    somme = 0
    for n in notes:
        somme = somme + n
    moyenne = somme / len(notes)
    return moyenne

moyenne = calcul_moyenne([4.5, 5, 5.5, 4, 6])
print(moyenne)
```
````
`````
