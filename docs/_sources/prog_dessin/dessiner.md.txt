(prog_dessin.dessiner)=

# 1. Dessiner

Dans ce chapitre, nous allons explorer la programmation par le dessin. Dans ce contexte, **un programme est une séquence d’instructions** permettant de générer un image.  
Nous allons voir que:

- l’expression `from turtle import *` met à disposition les fonctions de dessin,
- les instructions `forward()`, `backward()` permettent de tracer une ligne,
- les instructions `left()`, `right()` permettent de changer de direction.

```{question}
Un programme informatique est

{f}`une instruction de séquences`  
{v}`une séquence d'instructions`  
{f}`un algorithme`  
{f}`une recette de cuisine`
===
Tout programme n'est qu'une séquence (une suite ordrée) d'instructions.  
Un algorithme par contre est la description générale des étapes de résolution d'un problème. Il **peut** être traduit en un programme informatique.
```

## Le module `turtle`

Dans le langage de programmation Python, le module `turtle` (tortue en anglais) présente une façon sympathique pour faire des dessins.

On s'imagine une tortue qui se déplace sur un canevas et laisse une trace sur son passage.

Ci-dessous, vous trouvez notre premier programme de trois lignes:

- dans la première ligne, nous importons toutes (`*`) les fonctions du module `turtle`,
- avec `shape('turtle')`, nous affichons une tortue (au lieu de la flèche),
- avec `forward(150)`, nous faisons avancer la tortue de 150 pixels.

````{exercise}
Ajoutez d'autres instructions telles que `backward()`, `left()` et `right()` pour faire un dessin et voir un peu comment cela fonctionne. Appuyez sur bouton bleu "Exécuter" pour lancer le programme.

```{codeplay}
:file: forward1.py
from turtle import *

shape('turtle')
forward(150)
```
````

```{question}
En Python, `turtle` est

{v}`un module`  
{f}`un éditeur de dessin`  
{f}`une tortue`  
{f}`une commande`
===
Le module `turtle` fait partie de la distribution standard de Python. Nous le trouvons donc inclus de base avec Python sur toutes les plateformes.
```

La tortue peut se déplacer et dessiner une trace avec les 4 fonctions suivantes:

- `forward(d)` pour avancer d'une distance `d` (en pixels)
- `backward(d)` pour reculer
- `left(a)` pour tourner à gauche d'un angle `a` (en degrés)
- `right(a)` pour tourner à droite

## Le canevas

Au départ, la tortue se trouve au centre d'une zone rectangulaire appelée **canevas**.  
Ce rectangle a les propriétés suivantes :

- l'origine (0, 0) se trouve au centre,
- l'axe horizontal x, s'étend de -300 à +300 (à droite),
- l'axe vertical y, s'étend de -200 à +200 (en haut).

`````{exercise}
Ajoutez une instruction dans le code ci-dessous pour mener la tortue tout en bas à droite du canevas. Ajoutez ensuite une diagonale passant par le centre (l'angle est de 33.7 degrés avec l'horizontale).

```{codeplay}
:file: forward2.py
from turtle import *

shape('turtle')
forward(300)
backward(600)
forward(300)

left(90)
forward(200)
```

````{dropdown} Solution
```python
...

backward(400)
left(90)
backward(300)
right(33.7)
forward(722)
```
````
`````

## Une séquence

Un programme est une **séquence d'instructions**. Le bloc de 8 instructions ci-dessous indique comment dessiner un carré. La tortue doit avancer, tourner, avancer, tourner, etc.

`````{exercise}
Modifiez ce code pour en faire un rectangle, au lieu d'un carré.

```{codeplay}
:file: forward3.py
from turtle import *

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
```

````{dropdown} Solution
```python
forward(200)
left(90)
forward(100)
left(90)
forward(200)
left(90)
forward(100)
left(90)
```
````
`````

```{question}
Une séquence d'instructions d'un bloc est exécutée

{f}`selon la priorité`  
{f}`simultanément`  
{v}`dans l'ordre de haut en bas`  
{f}`aléatoirement`   
```

## Épaisseur de ligne

La fonction `width(d)` (largeur en anglais) permet de définir l'épaisseur du trait.  

````{exercise}
Voici un triangle où chaque côté a une épaisseur différente.  
Explorez différentes épaisseurs de trait.

```{codeplay}
:file: forward5.py
from turtle import *

forward(200)
left(120)

width(5)
forward(200)
left(120)

width(10)
forward(200)
```
````

## Couleurs

La fonction `color(c)` permet de définir la couleur de trait `c`.
Entre les parenthèses de la fonction, vous devez écrire le nom d'une couleur en anglais, entouré d'apostrophes — par exemple `color('red')` pour dessiner un trait rouge.

La fonction `dot(d, c)` dessine un cercle de diamètre `d` et de couleur `c`. En mettant un diamètre très grand, on peut l'utiliser pour mettre une couleur de fond.

Voici un triangle avec 3 segments de couleurs différentes sur un fond jaune.

```{codeplay}
:file: color1.py
from turtle import *

dot(1000, 'yellow')
width(20)

color('red')
forward(150)
left(120)

color('lime')
forward(150)
left(120)

color('blue')
forward(150)
left(120)
```

````{dropdown} Couleurs disponibles
```{image} ../media/colors.png
```
````

## Maison avec toit

Nous dessinons une maison et marquons le toit par une ligne plus épaisse.

`````{exercise}
Doublez l'épaisseur du toit. Ensuite, doublez la hauteur de la maison.

```{codeplay}
:file: forward6.py
from turtle import *

forward(100)
left(90)
forward(60)
left(45)
width(5)
color('brown')
forward(71)
left(90)
forward(71)
width(1)
color('black')
left(45)
forward(60)
left(90)
```

````{dropdown} Solution
```python
forward(100)
left(90)
forward(120)
left(45)
width(10)
forward(71)
left(90)
forward(71)
width(1)
left(45)
forward(120)
left(90)
```
````
`````

## Raquette de ping-pong

L'épaisseur de trait est très utile dans le dessin.

`````{exercise}
Transformez la raquette de ping-pong en haltères de musculation.

```{codeplay}
:file: forward7.py
from turtle import *

width(20)
forward(100)
width(80)
forward(20)
```

````{dropdown} Solution
```python
width(20)
forward(100)
width(80)
forward(20)
width(20)
backward(120)
width(80)
backward(20)
```
````
`````

## Lunettes de soleil

Voici encore un exemple permettant de faire facilement des lunettes de soleil en modifiant l'épaisseur du trait.

```{codeplay}
:file: forward8.py
from turtle import *

width(10)
backward(40)
right(135)
backward(60)
forward(60)
left(135)
forward(40)
width(50)
forward(20)
width(10)
forward(60)
width(50)
forward(20)
width(10)
forward(40)
left(45)
forward(60)
```

## Commentaire

Le symbole `#` indique un commentaire. Sur Mac, vous pouvez l'insérer avec **opt+3** ou **alt+3**.
Un commentaire permet d'ajouter une explication pour le lecteur humain. Il n'a aucune influence sur le programme. Python l'ignore tout simplement.

````{exercise}
Ajoutez un commentaire pour chaque ligne du programme suivant.

```{codeplay}
from turtle import *

width(10)       # met l'épaisseur du trait à 10
forward(20)     # avance de 20 pixels
left(90)
backward(60)
```
````

L'exercice précédent servait à expliciter pour un débutant en programmation la signification des commandes écrites en anglais.  
Normalement, on ne fait pas ça, car un programmeur est censé connaitre la signification des commandes.

Les commentaires servent à expliquer la signification d'une **partie** du programme.

## Équivalence

La tortue possède 4 fonctions de déplacement, mais à strictement parler, on pourrait s'en sortir avec seulement deux fonctions, `forward()` et `left()`, car:

- `backward(d)` est équivalent à `forward(-d)`
- `right(a)` est équivalent à `left(-a)`

Dans le programme ci-dessous, les 4 lignes du deuxième bloc sont équivalentes aux 4 instructions du premier bloc et donnent un résultat identique.

```{codeplay}
:file: forward4.py
from turtle import *

forward(160)
left(90)
forward(100)
left(90)

backward(-160)  # équivalent à forward(160)
right(-90)      # équivalent à left(90)
backward(-100)
right(-90)
```

```{question}
L'expression `left(90)` est équivalent à

{v}`right(-90)`  
{f}`right(180)`  
{f}`left(180)`  
{f}`left(-90)`  
```

## Exercice récapitulatif

````{exercise}
Dessinez une simple chaise en respectant les critères suivants:
- Utilisez au moins deux épaisseurs de trait différentes (ex: les pieds plus fins que l'assise)  
- Utilisez au moins deux couleurs différentes  

Le plus simple est de la dessiner de profil, mais si vous avez l'âme courageuse, vous pouvez tenter de la faire sous un autre angle !

```{codeplay}
:file: ex1.py
from turtle import *

# Votre code ici
```

Téléchargez le fichier `.py` et déposez-le sur Moodle à l'endroit prévu.
````

<!--
````{dropdown} Solution
Voici le code générant une chaise simpliste.
```python
from turtle import *

width(10)
left(90)
forward(60)
right(90)
width(20)
forward(60)
width(10)
right(90)
forward(60)
backward(150)
```
````
-->

## Et à part le dessin ?

Python ne sert évidemment pas qu'à faire du dessin, c'est juste une façon d'apprendre à l'utiliser.  
L'instruction la plus couramment utilisée est probablement `print()` ("imprime" en français) qui permet d'afficher du texte.

````{exercise}
Voici un exemple affichant "Hello world !".  
Modifiez le texte à afficher. Ensuite, ajoutez d'autres commandes `print` pour écrire du texte sur plusieurs lignes.

```{codeplay}
print("Hello world !")
```
````
