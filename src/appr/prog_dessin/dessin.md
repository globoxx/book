(prog_dessin.dessin)=

# 1. Dessin

Dans ce chapitre, nous allons explorer la programmation par le dessin. Dans ce contexte, un programme est une séquence d’instructions permettant de générer un image.  
Nous allons voir que:

- l’expression `from turtle import *` met à disposition les fonctions de dessin,
- les instructions `forward()`, `backward()` permettent de tracer une ligne,
- les instructions `left()`, `right()` permettent de changer de direction.

```{question}
Un programme informatique est

{f}`une instruction de séquence`  
{v}`une séquence d'instructions`  
{f}`un algorithme`  
{f}`une recette de cuisine`
===
Tout programme n'est qu'une séquence d'instructions.  
Un algorithme par contre est la description générale des étapes de résolution d'un problème. Il **peut** être traduit en un programme informatique.
```

## Le module `turtle`

Dans le langage de programmation Python, le module `turtle` (tortue en anglais) présente une façon sympathique pour faire des dessins. C'est pour cela que nous commençons notre aventure de programmation avec cet animal qui avance tout doucement à son propre rythme.

On s'imagine une tortue qui se déplace sur un canevas et laisse une trace.

Ci-dessous, vous trouvez notre premier programme de trois lignes:

- dans la première ligne, nous importons toutes (`*`) les fonctions du module `turtle`,
- avec `shape('turtle')`, nous affichons une tortue (au lieu de la flèche),
- avec `forward(150)`, nous faisons avancer la tortue de 150 pixels.

````{exercise}
Ajoutez d'autres instructions telles que `backward()`, `left()` et `right()` pour faire un dessin.

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

````{exercise}
Ajoutez une instruction dans le code ci-dessous pour mener la tortue tout en bas du canevas. Ensuite, ajoutez une diagonale.

```{codeplay}
:file: forward2.py
from turtle import *

shape('turtle')
forward(300)
backward(600)
forward(300)

left(90)
forward(200)
````

```{question}
La largeur de la zone de dessin de la tortue est de

{f}`200 pixels`   
{f}`400 pixels`  
{v}`600 pixels`  
{f}`800 pixels`  
```

## Une séquence

Un programme est une séquence d'instructions. Le bloc de 8 instructions ci-dessous indique comment dessiner un carré. La tortue doit avancer, tourner, avancer, tourner, etc.

````{exercise}
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
````

```{question}
Une séquence d'instructions d'un bloc est exécutée

{f}`selon la priorité`  
{f}`simultanément`  
{v}`dans l'ordre`  
{f}`aléatoirement`   
```

## Épaisseur de ligne

La fonction `width(d)` (épaisseur en anglais) permet de définir l'épaisseur de la ligne.  

````{exercise}
Voici un triangle où chaque côté a une épaisseur différente.  
Explorez différentes épaisseurs de ligne.

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
