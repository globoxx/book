(prog1.algo)=

# 7. Les algorithmes

<a href="https://perso.limsi.fr/pointal/_media/python:cours:mementopython3.pdf" target="_blank">Mémento Python</a>  
<a href="https://support.apple.com/fr-ch/HT201236" target="_blank">Raccourcis clavier</a>

Dans ce chapitre, nous allons découvrir quelques algorithmes à appliquer sur des listes. Nous allons surtout nous pencher sur le tri qui est une fonctionnalité fondamentale dans l’informatique. Le succès énorme de Google est basé sur un tri efficace de l’information, car dans une liste triée on peut trouver un élément beaucoup plus vite.  
Nous allons voir que :

- la fonction `min(liste)` retourne le minimum,
- la fonction `max(liste)` retourne le maximum,
- la fontion `sorted(liste)` trie une liste dans l'ordre croissant.

Pour visualiser les listes de nombres, nous allons utiliser le module `turtle` pour dessiner des points representant chaque nombre.  
**La hauteur du point représente sa valeur**.

```{codeplay}
from turtle import *
from random import *

def create(size):
    getscreen().bgcolor('skyblue')
    d = 600/size
    x0 = 300 - d//2
    y0 = 200 - d//2
    turtles = [Turtle() for _ in range(size)]
    for i, t in enumerate(turtles):
        t.speed(50)
        t.penup()
        t.goto(-x0 + i*d, randint(-y0, y0))
        t.pendown()
        t.color('blue')
        t.shape('circle')
        #t.shapesize(d/20, d/20, 1)
    return turtles
===
longueur_liste = 20
liste = create(longueur_liste)  # La fonction create (cachée) permet de créer une liste aléatoire de points
done()
```

## Fonctions min et max

Les fonctions `min()` et `max()` retournent le minimum et le maximum d'une liste à l'aide d'un algorithme.  
Mais comment fonctionne cet algorithme ?

```{codeplay}
liste = [3, 4, 1, 2, 6, 5]

print(min(liste))
print(max(liste))
```

Ces fonctions sont très utiles mais nous allons voir comment les écrire nous-mêmes !
Pour trouver le minimum dans une liste il faut :

- prendre la première valeur comme minimum courant,
- parcourir le reste de la liste,
- mettre à jour le minimum à chaque fois que l'on trouve un nombre plus petit.

```{codeplay}
def calcule_min(liste):
    minimum = liste[0]
    for valeur in liste[1:]:
        if valeur < minimum:
            minimum = valeur
    return minimum

liste = [3, 4, 1, 2, 6, 5]
minimum = calcule_min(liste)  
print(minimum)
```

Le maximum peut être trouvé de manière similaire, en mettant à jour le plus grand nombre trouvé.  
Voici une visualisation des algorithmes `min()` et `max()` où les points rouges représentent les plus petites et plus grandes valeurs trouvées dans la liste:

```{codeplay}
from turtle import *
from random import *

def create(size):
    getscreen().bgcolor('skyblue')
    d = 600/size
    x0 = 300 - d//2
    y0 = 200 - d//2
    turtles = [Turtle() for _ in range(size)]
    for i, t in enumerate(turtles):
        t.speed(50)
        t.penup()
        t.goto(-x0 + i*d, randint(-y0, y0))
        t.pendown()
        t.color('blue')
        t.shape('circle')
        #t.shapesize(d/20, d/20, 1)
    return turtles

def dessine_min_max(points):
    t_min = Turtle()
    t_max = Turtle()
    t_min.hideturtle()
    t_max.hideturtle()
    t_min.up()
    t_max.up()
    t_min.color('red')
    t_max.color('red')
    d = 600/len(points)
    for i in range(len(points)):
        if i == 0:
            min = points[i].ycor()
            max = points[i].ycor()
        else:
            t_min.down()
            t_max.down()
            if points[i].ycor() < min:
                min = points[i].ycor()
            if points[i].ycor() > max:
                max = points[i].ycor()
        t_min.goto(points[i].xcor(), min)
        t_min.dot(d/2)
        t_max.goto(points[i].xcor(), max)
        t_max.dot(d/2)
===
longueur_liste = 20
liste = create(longueur_liste)

dessine_min_max(liste)

done()
```

````{admonition} Exercice 25 - Max (facile)
:class: note
Ecrivez la fonction `calcule_max(liste)` qui retourne la valeur maximum d'une liste.

```{codeplay}
:file: ex_25.py
def calcule_min(liste):
    minimum = liste[0]
    for valeur in liste[1:]:
        if valeur < minimum:
            minimum = valeur
    return minimum

def calcule_max(liste):
    ...

liste = [3, 4, 1, 2, 6, 5]
minimum = calcule_min(liste)  
print(f'Le minimum est {minimum}')
maximum = ...
print(f'Le maximum est {maximum}')
```
````

## L'index du minimum/maximum

Souvent, on ne doit pas seulement trouver la valeur minimum, mais aussi sa position (son index) dans la liste.  
Contrairement au cas précédent, ici nous ne parcourons pas les valeurs, mais les index grâce à une `range`.

```{codeplay}
liste = [3, 4, 1, 2, 6, 5]

minimum = liste[0]
index_minimum = 0

n = len(liste)
for i in range(1, n):
    if liste[i] < minimum:
        minimum = liste[i]
        index_minimum = i
        
print(f"Le minimum est {minimum} et se trouve à l'index {index_minimum}")
```

````{admonition} Exercice 26 - Indice max (facile)
:class: note
Modifier l'exemple précédent pour **en plus** afficher le maximum et son index.

```{codeplay}
:file: ex_26.py
liste = [3, 4, 1, 2, 6, 5]

minimum = liste[0]
index_minimum = 0

n = len(liste)
for i in range(1, n):
    if liste[i] < minimum:
        minimum = liste[i]
        index_minimum = i
        
print(f"Le minimum est {minimum} et se trouve à l'index {index_minimum}")
print(f"Le maximum est {maximum} et se trouve à l'index {index_maximum}")
```
````

## Algorithmes de tri

La fonction `sorted(liste)` trie une liste dans l'ordre croissant. Cela fonctionne tant que la liste contient des éléments qui ont une relation d'ordre.  
Par exemple, une liste de textes (string) sera triée alphabétiquement.

```{codeplay}
liste = [3, 4, 1, 2, 6, 5]
liste_triee = sorted(liste)
print(liste_triee)

liste = ['banane', 'carotte', 'ananas', 'courgette', 'pomme']
liste_triee = sorted(liste)
print(liste_triee)
```

### Échanger deux éléments

Pour échanger deux éléments d'une liste, nous pouvons utiliser une variable temporaire pour stocker une valeur.  
Ici nous échangeons les deux premiers éléments, donc les éléments avec les index 0 et 1.

```{codeplay}
liste = [3, 4, 1, 2, 6, 5]
print(liste)

tmp = liste[0]  # On stocke la valeur de liste[0] car elle sera écrasée par liste[1] et donc perdue autrement
liste[0] = liste[1]
liste[1] = tmp

print(liste)
```

Le programme devient plus lisible si nous définissons une fonction `echange()` qui s'en occupe.

```{codeplay}
liste = [3, 4, 1, 2, 6, 5]
print(liste)

def echange(liste, i, j):
    tmp = liste[i]
    liste[i] = liste[j]
    liste[j] = tmp

echange(liste, 0, 2)
print(liste)
```

`````{admonition} Pour aller plus loin
:class: hint
````{dropdown} <span style="color:grey">Les affectations multiples</span>
:animate: fade-in-slide-down
Il est également possible d'échanger la valeur de 2 variables en utilisant une **affectation multiple**.
```python
def echange(liste, i, j):
    liste[i], liste[j] = liste[j], liste[i]
```
````
`````

````{admonition} Exercice 27 - Echanges (moyen)
:class: note
Visualisons un peu ces échanges.
1. Utilisez une boucle `for` et la fonction `echange(liste, i, j)` pour echanger chaque point avec son voisin. Cela devrait faire remonter le 1er élément de la liste vers la fin de la liste.
2. Utilisez une boucle `for`et la fonction `echange(liste, i, j)` pour échanger 5 points aléatoirement.

```{codeplay}
:file: ex_27.py
from turtle import *
from random import *

def echange_elem(liste, i, j):
    liste[i], liste[j] = liste[j], liste[i]

def create(size):
    getscreen().bgcolor('skyblue')
    d = 600/size
    x0 = 300 - d//2
    y0 = 200 - d//2
    turtles = [Turtle() for _ in range(size)]
    for i, t in enumerate(turtles):
        t.speed(50)
        t.penup()
        t.goto(-x0 + i*d, randint(-y0, y0))
        t.pendown()
        t.color('blue')
        t.shape('circle')
        #t.shapesize(d/20, d/20, 1)
    return turtles

def move_simu(turtles, coordinates, nhops=10):
    deltas = []
    for t, coord in zip(turtles, coordinates):
        current_coord = (t.xcor(), t.ycor())
        diff = (coord[0]-current_coord[0], coord[1]-current_coord[1])
        delta = (diff[0] * (1.0/nhops), diff[1] * (1.0/nhops))
        deltas.append(delta)
    for _ in range(1, nhops+1):
        for t, delta in zip(turtles, deltas):
            t.goto(t.xcor() + delta[0], t.ycor() + delta[1])
    
def echange(turtles, i, j):
    turtles_to_move = [turtles[i], turtles[j]]
    coordinates = [(turtles[j].xcor(), turtles[i].ycor()), (turtles[i].xcor(), turtles[j].ycor())]
    turtles[i].color('green')
    turtles[j].color('green')
    move_simu(turtles_to_move, coordinates)
    turtles[i].color('black')
    turtles[j].color('black')
    echange_elem(turtles, i, j)
===
import random
longueur_liste = 20
liste = create(longueur_liste)

for ...

done()
```
````

### Tri à bulles

L’algorithme du **tri à bulles** compare les éléments voisins, deux par deux, et les met dans le bon ordre. Il recommence ensuite au début jusqu'à ce que toute la liste soit triée. Le mot 'bulles' fait référence aux bulles dans une boisson qui montent à la surface exactement comme les grands éléments remontent progressivement vers la fin de la liste.

```{codeplay}
def echange(liste, i, j):
    liste[i], liste[j] = liste[j], liste[i]
===
def bubble_sort(liste):
    N = len(liste)
    for iteration in range(N - 1):
        for i in range(N - 1):
            x = liste[i]
            voisin = liste[i + 1]
            if liste[i] > liste[i+1]:
                echange(liste, i, i+1)
                print(liste)
    return liste

liste = [3, 4, 1, 2, 6, 5]
print(liste)
liste = bubble_sort(liste)
print(liste)
```

Visualisons l'algorithme:

```{codeplay}
from turtle import *
from random import *

def echange_elem(liste, i, j):
    liste[i], liste[j] = liste[j], liste[i]

def create(size):
    getscreen().bgcolor('skyblue')
    d = 600/size
    x0 = 300 - d//2
    y0 = 200 - d//2
    turtles = [Turtle() for _ in range(size)]
    for i, t in enumerate(turtles):
        t.speed(50)
        t.penup()
        t.goto(-x0 + i*d, randint(-y0, y0))
        t.pendown()
        t.color('blue')
        t.shape('circle')
        #t.shapesize(d/20, d/20, 1)
    return turtles
    
def move_simu(turtles, coordinates, nhops=10):
    deltas = []
    for t, coord in zip(turtles, coordinates):
        current_coord = (t.xcor(), t.ycor())
        diff = (coord[0]-current_coord[0], coord[1]-current_coord[1])
        delta = (diff[0] * (1.0/nhops), diff[1] * (1.0/nhops))
        deltas.append(delta)
    for _ in range(1, nhops+1):
        for t, delta in zip(turtles, deltas):
            t.goto(t.xcor() + delta[0], t.ycor() + delta[1])
    
def echange(turtles, i, j):
    turtles_to_move = [turtles[i], turtles[j]]
    coordinates = [(turtles[j].xcor(), turtles[i].ycor()), (turtles[i].xcor(), turtles[j].ycor())]
    turtles[i].color('green')
    turtles[j].color('green')
    move_simu(turtles_to_move, coordinates)
    turtles[i].color('black')
    turtles[j].color('black')
    echange_elem(turtles, i, j)
===
def bubble_sort(liste):
    N = len(liste)
    for iteration in range(N - 1):
        for i in range(N - 1):
            if liste[i].ycor() > liste[i+1].ycor():  # ycor() est une méthode permettant de récupérer la hauteur du point (coordonnée y)
                echange(liste, i, i+1)
    return liste

longueur_liste = 20
liste = create(longueur_liste)

liste = bubble_sort(liste)

done()
```

### Tri par insertion

L’algorithme du **tri par insertion** est utilisé par la plupart des personnes pour trier des cartes à jouer.  
Il parcourt la liste d’éléments à trier du deuxième au dernier élément.
Pour chaque nouvel élément considéré, il l’insère à l’emplacement correct dans la liste déjà parcourue.

```{codeplay}
def echange(liste, i, j):
    liste[i], liste[j] = liste[j], liste[i]
===
def insertion_sort(liste):
    N = len(liste)
    for i in range(2, N):
        for j in range(i, 0, -1):
            if liste[j] < liste[j-1]:
                echange(liste, j, j-1)
                print(liste)
    return liste

liste = [3, 4, 1, 2, 6, 5]
print(liste)
liste = insertion_sort(liste)
print(liste)
```

```{codeplay}
from turtle import *
from random import *

def echange_elem(liste, i, j):
    liste[i], liste[j] = liste[j], liste[i]

def create(size):
    getscreen().bgcolor('skyblue')
    d = 600/size
    x0 = 300 - d//2
    y0 = 200 - d//2
    turtles = [Turtle() for _ in range(size)]
    for i, t in enumerate(turtles):
        t.speed(50)
        t.penup()
        t.goto(-x0 + i*d, randint(-y0, y0))
        t.pendown()
        t.color('blue')
        t.shape('circle')
        #t.shapesize(d/20, d/20, 1)
    return turtles
    
def move_simu(turtles, coordinates, nhops=10):
    deltas = []
    for t, coord in zip(turtles, coordinates):
        current_coord = (t.xcor(), t.ycor())
        diff = (coord[0]-current_coord[0], coord[1]-current_coord[1])
        delta = (diff[0] * (1.0/nhops), diff[1] * (1.0/nhops))
        deltas.append(delta)
    for _ in range(1, nhops+1):
        for t, delta in zip(turtles, deltas):
            t.goto(t.xcor() + delta[0], t.ycor() + delta[1])
    
def echange(turtles, i, j):
    turtles_to_move = [turtles[i], turtles[j]]
    coordinates = [(turtles[j].xcor(), turtles[i].ycor()), (turtles[i].xcor(), turtles[j].ycor())]
    turtles[i].color('green')
    turtles[j].color('green')
    move_simu(turtles_to_move, coordinates)
    turtles[i].color('black')
    turtles[j].color('black')
    echange_elem(turtles, i, j)
===
def insertion_sort(liste):
    N = len(liste)
    for i in range(2, N):
        for j in range(i, 0, -1):
            if liste[j].ycor() < liste[j-1].ycor():
                echange(liste, j, j-1)
    return liste

longueur_liste = 20
liste = create(longueur_liste)

liste = insertion_sort(liste)

done()
```

### Tri par sélection

L’algorithme du **tri par sélection** commence par rechercher le plus petit élément de la liste et l’échange avec le premier élément de la liste.  
Il recherche ensuite le plus petit élément de la liste restante. Il sélectionne ainsi le deuxième plus petit élément de la liste et l’échange avec le deuxième élément de la liste.  
Et ainsi de suite...

```{codeplay}
def echange(liste, i, j):
    liste[i], liste[j] = liste[j], liste[i]
===
def selection_sort(liste):
    N = len(liste)
    for i in range(N-1):
        index_minimum = i
        minimum = liste[i]
        for j in range(i+1, N):
            if liste[j] < minimum:
                index_minimum = j
                minimum = liste[j]
        echange(liste, i, index_minimum)
        print(liste)
    return liste

liste = [3, 4, 1, 2, 6, 5]
print(liste)
liste = selection_sort(liste)
print(liste)
```

```{codeplay}
from turtle import *
from random import *

def echange_elem(liste, i, j):
    liste[i], liste[j] = liste[j], liste[i]

def create(size):
    getscreen().bgcolor('skyblue')
    d = 600/size
    x0 = 300 - d//2
    y0 = 200 - d//2
    turtles = [Turtle() for _ in range(size)]
    for i, t in enumerate(turtles):
        t.speed(50)
        t.penup()
        t.goto(-x0 + i*d, randint(-y0, y0))
        t.pendown()
        t.color('blue')
        t.shape('circle')
        #t.shapesize(d/20, d/20, 1)
    return turtles
    
def move_simu(turtles, coordinates, nhops=10):
    deltas = []
    for t, coord in zip(turtles, coordinates):
        current_coord = (t.xcor(), t.ycor())
        diff = (coord[0]-current_coord[0], coord[1]-current_coord[1])
        delta = (diff[0] * (1.0/nhops), diff[1] * (1.0/nhops))
        deltas.append(delta)
    for _ in range(1, nhops+1):
        for t, delta in zip(turtles, deltas):
            t.goto(t.xcor() + delta[0], t.ycor() + delta[1])
    
def echange(turtles, i, j):
    turtles_to_move = [turtles[i], turtles[j]]
    coordinates = [(turtles[j].xcor(), turtles[i].ycor()), (turtles[i].xcor(), turtles[j].ycor())]
    turtles[i].color('green')
    turtles[j].color('green')
    move_simu(turtles_to_move, coordinates)
    turtles[i].color('black')
    turtles[j].color('black')
    echange_elem(turtles, i, j)
===
def selection_sort(liste):
    N = len(liste)
    for i in range(N-1):
        index_minimum = i
        minimum = liste[i].ycor()
        for j in range(i+1, N):
            if liste[j].ycor() < minimum:
                index_minimum = j
                minimum = liste[j].ycor()
        echange(liste, i, index_minimum)
    return liste

longueur_liste = 20
liste = create(longueur_liste)

liste = selection_sort(liste)

done()
```

````{admonition} Exercice 28 - Amélioration (difficile)
:class: note
L'algorithme du tri par sélection peut être simplifé à l'aide de la fonctions `min()` et de la méthode `index()`.  
La méthode `liste.index(x)` retourne l'index de l'élément `x` dans la liste.  

Tentez de simplifier l'écriture de l'algorithme de tri par sélection.  
Indice: toute la boucle interne ne sert qu'à une seule chose, trouver le minimum et son index. Elle peut donc être réécrite plus simplement avec `min()` et `liste.index()`.

```{codeplay}
def echange(liste, i, j):
    liste[i], liste[j] = liste[j], liste[i]
===
def selection_sort(liste):
    N = len(liste)
    for i in range(N-1):
        # Partie à modifier ------------
        index_minimum = i
        minimum = liste[i]
        for j in range(i+1, N):
            if liste[j] < minimum:
                index_minimum = j
                minimum = liste[j]
        # ------------------------------
        echange(liste, i, index_minimum)
        print(liste)
    return liste

liste = [3, 4, 1, 2, 6, 5]
print(liste)
liste = selection_sort(liste)
print(liste)
```
````
