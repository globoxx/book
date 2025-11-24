(prog_dessin.repeter)=

# 3. Répéter

Dans ce chapitre, nous allons découvrir comment utiliser une boucle `for` pour **répéter un bloc d'instructions** un certain nombre de fois. Nous allons voir que :

- la boucle `for` permet de répéter des instructions,
- la structure `for i in range(n):` permet de répéter un bloc `n` fois,
- le deux-points `:` est toujours suivi d'un bloc en indentation.

```{question}
Une boucle informatique est

{f}`une instruction`  
{f}`un passage ondulé`  
{v}`une section de code répétée`  
{f}`une protection thermique`
```

## La répétition

Revenons vers un exemple simple : dessiner un carré.

Si nous regardons le code de près, nous pouvons voir que nous répétons 4 fois les mêmes deux instructions `forward()` et `left()`.

```{codeplay}
:file: for1.py
from turtle import *
d = 100

forward(d)
left(90)
forward(d)
left(90)
forward(d)
left(90)
forward(d)
left(90)
```

Ne serait-ce pas pratique de pouvoir répéter ces deux instructions 4 fois ?
C'est possible avec une boucle `for`.

`````{exercise}
La ligne `for i in range(4):` va répéter `4` fois le bloc en indentation qui suit afin de dessiner un rectangle.  
Transformez le rectangle en triangle.

```{codeplay}
:file: for2.py
from turtle import *
d = 100

for i in range(4):
    forward(d)
    left(90)
```

````{dropdown} Solution
```python
from turtle import *
d = 100

for i in range(3):
    forward(d)
    left(120)
```
````
`````

## Variable d'itération `i`

Que représente `i` dans l'expression `for i in range(n)` ?  
C'est ce qu'on appelle une **variable d'itération**. Cette variable commence à 0 et augmente de 1 à chaque répétition jusqu'à `n-1`. Pour visualiser cette valeur nous pouvons l'afficher dans le dessin avec l'instruction `write(i)`.

```{codeplay}
:file: for2.py
from turtle import *
d = 100

for i in range(4):
    write(i)
    forward(d)
    left(90)
```

## Polygone régulier

Avec une boucle `for`, nous pouvons simplifier le dessin des formes symétriques.

`````{exercise}
Observez bien la double indentation dans le code suivant :

- la première pour `def`
- la deuxième pour `for`

Dans les deux cas un `:` est suivi d'un bloc en indentation. En Python vous pouvez avoir plusieurs niveaux d'indentation.

Définissez la fonction `hexagone()` pour dessiner un hexagone, et appelez cette fonction.

```{codeplay}
:file: for3.py
from turtle import *

def triangle():
    for i in range(3):      # indentation 1 (bloc pour def)
        forward(100)        # indentation 2 (bloc pour for)
        left(120)

def carre():
    for i in range(4):
        forward(100)
        left(90)

def pentagone():
    for i in range(5):
        forward(100)
        left(72)

triangle()
carre()
pentagone()
```

````{dropdown} Solution
```python
...

def hexagone():
    for i in range(6):
        forward(100)
        left(60)

triangle()
carre()
pentagone()
hexagone()
```
````
`````

## Escalier

Pour dessiner un escalier, il faut simplement répéter dans une boucle le dessin pour une seule marche. Nous utilisons la variable `i` pour numéroter les marches.

```{codeplay}
:file: for4.py
from turtle import *

for i in range(5):
    write(i)
    forward(20)
    left(90)
    forward(20)
    right(90)

forward(100)
```

## Éventail

Que se passe-t-il si nous dessinons une ligne droite et tournons chaque fois d'un petit angle ?
C'est un peu comme un éventail qui s'ouvre. Les lignes de l'éventail sont numérotées en utilisant la variable `i`.

````{exercise}
Doublez l'angle de rotation dans `left()`.

```{codeplay}
:file: for6.py
from turtle import *
d = 100

for i in range(18):
    forward(d)
    write(i)
    backward(d)
    left(10)
```
````

Que se passe-t-il si nous avançons plus que nous reculons ?
Une toute petite modification du programme peut faire une chouette différence.

````{exercise}
Modifiez les valeurs dans `forward()` et `backward()`.

```{codeplay}
:file: for7.py
from turtle import *

for i in range(18):
    forward(100)
    write(i)
    backward(90)
    left(20)
```
````

## Étoile

Voici une autre façon de toujours avancer, mais en tournant chaque fois d'un angle un peu plus petit que 180°.
Essayons !

```{codeplay}
:file: for8.py
from turtle import *

for i in range(9):
    write(i)
    forward(200)
    left(160)
```

## Losange

Si nous déformons les angles droits d'un carré, nous obtenons un losange.

```{codeplay}
:file: for9.py
from turtle import *
d = 100

def carre():
    for i in range(4):
        right(90)
        forward(d)

def losange():
    for i in range(2):
        forward(d)
        left(120)
        forward(d)
        left(60)
        
carre()
right(90)
losange()
left(120)
losange()
```

Si nous dessinons un losange 6 fois, nous obtenons une fleur.

````{exercise}
Tournez d'un angle plus petit que 60° entre chaque losange.

```{codeplay}
:file: for10.py
from turtle import *
d = 100

def losange():
    for i in range(2):
        forward(d)
        left(60)
        forward(d)
        left(120)

for i in range(6):
    losange()
    left(60)
```
````

## Paquebot

Une boucle `for` est utilisée dans l'exemple suivant pour dessiner les hublots d'un paquebot. Les hublots sont numérotés en utilisant la variable `i`.

```{codeplay}
from turtle import *

def paquebot():
    forward(200)
    left(80)
    forward(60)
    left(100)
    forward(220)
    left(100)
    forward(60)

    up()
    left(125)
    forward(40)
    right(45)

    for i in range(6):
        dot(20, 'lightgray')
        write(i)  
        forward(30)

paquebot()
```

```{admonition} Rappel
:class: note
La fonction `dot(d, c)` dessine un disque de diamètre `d` et de couleur `c`.
```

### Vitesse

Vous pouvez changer la vitesse de la tortue avec la fonction `speed(s)`.
Le paramètre vitesse `s` peut varier entre 1 (le plus lent) et 1000 (le plus rapide). Sa vitesse par défaut est de 3. Mettre la vitesse à 0 choisit automatiquement la vitesse maximum.

`````{exercise}
Augmentez graduellement la vitesse de la tortue, en utilisant la variable `i` comme argument de vitesse.

```{codeplay}
:file: for13.py
from turtle import *
speed(2)

for i in range(36):
    forward(280)
    left(170)
```

````{dropdown} Solution
```python
from turtle import *
speed(2)

for i in range(36):
    forward(280)
    left(170)
    speed(i+1) # +1 pour éviter de commencer à 0
```
````
`````

## Erreurs

Il est important de bien lire et comprendre les messages d'erreur.
Dans cette section, vous allez découvrir les différentes catégories d'erreur et comment les corriger.

### ImportError

Cette erreur survient lorsque vous essayez d'importer un module qui n'existe pas.

````{exercise}
Corrigez l'erreur d'importation.

```{codeplay}
from turtl import *

for i in range(3):
    forward(100)
    left(120)
```
````

### SyntaxError

Cette erreur survient lorsque vous écrivez mal un mot-clé, ou si vous oubliez une ponctuation. Dans ce cas, le mot-clé mal écrit n'est pas reconnu et il n'est pas colorié correctement dans votre code.

````{exercise}
Corrigez les trois erreurs de syntaxe.

```{codeplay}
fro turtle import *

fore i in range(3)
    forward(100)
    left(120)
```
````

### NameError

Cette erreur survient lorsque vous écrivez mal le nom d'une variable ou d'une fonction.

````{exercise}
Corrigez les trois erreurs de nom.

```{codeplay}
from turtle import *

for i in range(n):
    forwarde(100)
    lefft(120)
```
````

### TypeError

Cette erreur survient lorsque vous ne mettez pas le nombre d'arguments corrects pour une fonction.

````{exercise}
Corrigez les trois erreurs de type.

```{codeplay}
from turtle import *

for i in range():
    forward()
    left(100, 120)
```
````

## Exercice récapitulatif

````{exercise}
Dessinez une spirale dont chaque segment est plus long que le précédent. Cette spirale sera formée de segments rectilignes. À chaque tour, la longueur du segment augmentera, créant ainsi un effet de spirale.

![spirale](../media/spirale.png)

1. Commencez par un segment de longueur 10.
2. Pour chaque segment suivant, augmentez la longueur de 10 unités.
3. Tournez la tortue de 90 degrés après chaque segment.
4. Dessinez la spirale avec un total de 20 segments.

Vous devez utiliser une boucle `for`.

```{codeplay}
:file: ex3.py
from turtle import *

# Votre code ici...
```

Téléchargez le fichier `.py` et déposez le fichier sur Moodle à l'endroit prévu.
````
<!--
from turtle import *

longueur_segment = 10
augmentation = 10

for i in range(20):
    forward(longueur_segment)
    left(90)
    longueur_segment += augmentation
-->

## Et à part le dessin ?

Les boucles sont primordiales dans tout programme informatique. La boucle `for` n'est d'ailleurs qu'un type de boucle (l'autre étant la boucle `while`).

```{admonition} Rappel
:class: hint
- La fonction `print()` permet d'afficher du texte.
- `a = 0` est une instruction permettant de créer une variable `a` et lui donner la valeur `0`.
- `a = a + 3` permet d'ajouter 3 à la variable `a`.
```

`````{exercise}
Nous allons voir que les boucles peuvent être extrêmement utiles pour faire certains calculs.

1. Ecrivez un programme affichant tous les nombres entre 0 et 9.
2. Modifiez le programme pour afficher la somme des nombres de 0 à 9.
3. Modifiez le programme pour afficher la moyenne des nombres de 0 à 9.
```{codeplay}
# Votre code ici...
```

````{dropdown} Solution
```python
# Partie 1
for i in range(10):
    print(i)

# Partie 2
somme = 0

for i in range(10):
    somme = somme + i

print(somme)

# Partie 3
somme = 0

for i in range(10):
    somme = somme + i

moyenne = somme / 10
print(moyenne)
```
````
``````
