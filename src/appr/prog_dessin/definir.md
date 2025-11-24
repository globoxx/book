(prog_dessin.definir)=

# 2. Définir

Dans ce chapitre, nous allons découvrir comment augmenter le vocabulaire de notre langage de programmation en définissant de nouvelles instructions, qu'on appelle aussi **fonctions**. Ceci permet de rendre le code plus compact, mais surtout plus lisible. Nous allons voir que :

- le mot-clé `def` permet de nommer (définir) une séquence d'instructions,
- le bloc qui suit doit être en **indentation** (décalé à droite),
- les fonctions `up()/down()` permettent de lever et baisser le stylo.

```{question}
Une fonction permet de

{v}`donner un nom à une séquence d'instructions`  
{f}`nous dire si ça fonctionne`  
{v}`augmenter le vocabulaire du langage de programmation`  
{v}`rendre un programme plus lisible`
```

## Nommer une séquence

Dessiner un rectangle est assez utile. C'est une forme qui se retrouve souvent dans les dessins. Mais à chaque rectangle dessiné, nous devons réécrire ces 8 lignes de code...

```python
forward(160)
left(90)
forward(100)
left(90)
forward(160)
left(90)
forward(100)
left(90)
```

Serait-il possible de nommer cette séquence d'instructions afin qu'on puisse la réutiliser autant que l'on veut ?

Oui ! Avec le mot-clé `def`, nous pouvons **définir** une nouvelle fonction que nous pouvons par exemple appeler `rectangle()`.
C'est une sorte de raccourci pour ne pas avoir à réécrire tout le temps des séquences identiques.
Le code à exécuter se trouve après l'expression `def rectangle():` et se trouve en **indentation** (décalé vers la droite).

```python
def rectangle():
    forward(160)
    left(90)
    forward(100)
    left(90)
    forward(160)
    left(90)
    forward(100)
    left(90)
```

Une fois que la fonction a été définie, il suffit d'écrire `rectangle()` pour dessiner un rectangle. On appelle ceci **appeler** une fonction.
Rappelez-vous ceci:

- on définit une fonction une seule fois,
- on appelle une fonction autant de fois que l'on veut,
- si on ne l'appelle pas, elle n'est pas exécutée et il ne se passe rien.

Définir une fonction nous permet de réduire le nombre de lignes de code nécessaires.
Chaque fois que nous utilisons `rectangle()`, au lieu d'écrire 8 lignes, nous écrivons seulement une ligne de code.

`````{exercise}
Dessinez encore d'autres rectangles en appelant la nouvelle fonction `rectangle()`.

```{codeplay}
:file: def1.py
from turtle import *

def rectangle():
    forward(160)
    left(90)
    forward(100)
    left(90)
    forward(160)
    left(90)
    forward(100)
    left(90)
        
rectangle() # 1er appel de la fonction rectangle
left(90)
rectangle() # 2ème appel de la fonction rectangle
```

````{dropdown} Solution
```python
...

rectangle() # 1er appel de la fonction rectangle
left(90)
rectangle() # 2ème appel de la fonction rectangle
left(45)
rectangle() # Encore un appel à la fonction
```
````
`````

```{question}
Une **indentation** de texte est 

{f}`un décalage vers la gauche`  
{v}`un décalage vers la droite`  
{f}`une mise en paragraphe`  
{f}`une mise en sous-section`  
```

## Donner du sens

Une fonction ne permet pas seulement d'économiser des lignes de code.
Elle permet aussi de **structurer** le code et de lui **donner un sens**. Considérez par exemple le code ci-dessous. Il est presque impossible de comprendre ce que fait le programme en regardant les 17 lignes de code.

```{codeplay}
:file: def2.py
from turtle import *

forward(200)
left(90)
forward(100)
left(90)
forward(200)
left(90)
forward(100)
left(90)
forward(30)
forward(30)
left(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
left(90)
```

Si nous observons la tortue, nous comprenons finalement qu'elle dessine deux fois un rectangle. Nous pouvons même interpréter cette image et donner le sens de bâtiment au premier rectangle, et de porte au second.

Essayons maintenant de découper le code en **sous-programmes** en utilisant deux fonctions `batiment()` et `porte()`.
En regardant ces 3 lignes de code, on comprend immédiatement le sens du programme.

``` python
batiment()
forward(30) # repositionner la tortue
porte()
```

La définition d'une fonction permet d'ajouter de nouveaux mots à un langage de programmation. Contrairement aux commandes natives de Python qui sont toutes en anglais, nous sommes libres de les choisir en français.

```{admonition} Attention
:class: attention
Ecrivez les fonctions sans accents, sans circonflexes et sans espaces: `batiment()`, `carre()`, `boite()`, `arc_en_ciel()`.
```

`````{exercise}
Ajoutez une deuxième porte au bâtiment.

```{codeplay}
:file: def3.py
from turtle import *

def batiment():
    forward(200)
    left(90)
    forward(100)
    left(90)
    forward(200)
    left(90)
    forward(100)
    left(90)

def porte():
    forward(30)
    left(90)
    forward(50)
    left(90)
    forward(30)
    left(90)
    forward(50)
    left(90)

batiment()
forward(30)
porte()
```

````{dropdown} Solution
```python
...

batiment()
forward(30)
porte()
forward(120)
porte()
```
````
`````

```{question}
À combien de lignes de code la fonction `porte()` est-elle équivalente ?

{f}`1 ligne`  
{f}`2 lignes`  
{v}`8 lignes`  
{f}`17 lignes`  
```

## Définir une fonction

Le fait de donner un nom à une séquence d'instructions est appelé **définir une fonction**. Une **définition de fonction** comporte :

1. le mot-clé `def` (définir),
2. le nom de la fonction (`batiment/porte/etc`),
3. les parenthèses `()`,
4. le deux-points `:`,
5. un bloc en indentation.

```{admonition} A retenir
:class: hint
Qu'est-ce qu'un bloc en indentation ?  
C'est un bloc de texte qui comporte des espaces vides à gauche. En Python, ces espaces apparaissent en multiples de 4.

L'indentation est très importante en Python. C'est l'indentation qui indique quelles sont les instructions qui font partie de la fonction.
```

```{question}
Parmi les 4 définitions de fonction ci-dessous, laquelle est correcte ?

{f}`def() rectangle:`  
{f}`def: rectangle`  
{v}`def rectangle():`  
{f}`def(rectangle):`  
```

## Indenter avec un raccourci

Comme l'indentation est tellement importante en Python, il en existe un raccourci.  
Il faut d'abord sélectionner les lignes de code dont vous voulez changer l'indentation.
Ensuite, vous appuyez sur:

- la touche **tab** pour augmenter l'indentation
- la touche **maj+tab** pour diminuer l'indentation

`````{exercise}
Essayez ces raccourcis dans le code ci-dessous. Transformez le code en deux fonctions `batiment()` et `porte()`, que vous appelez ensuite.

```{codeplay}
:file: def2.py
from turtle import *

forward(200)
left(90)
forward(100)
left(90)
forward(200)
left(90)
forward(100)
left(90)

forward(30)

forward(30)
left(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
left(90)
```

````{dropdown} Solution
```python
def batiment():
    forward(200)
    left(90)
    forward(100)
    left(90)
    forward(200)
    left(90)
    forward(100)
    left(90)

def porte():
    forward(30)
    left(90)
    forward(50)
    left(90)
    forward(30)
    left(90)
    forward(50)
    left(90)

batiment()
forward(30)
porte()
```
````
`````

## Maison avec porte

Une fois qu'une fonction est définie, elle peut être utilisée partout, même dans la définition d'une autre fonction.

Ici, nous avons une fonction `porte()`, qui est utilisée à l'intérieur d'une deuxième fonction `maison()`. Pour que ceci soit possible, la définition de porte doit être placée avant la définition de `maison()`.

`````{exercise}
Déplacez la porte vers le milieu de la maison, et dessinez une deuxième maison.

```{codeplay}
:file: def4.py
from turtle import *

def porte():
    forward(20)
    left(90)
    forward(40)
    left(90)
    forward(20)
    left(90)
    forward(40)
    left(90)

def maison():
    forward(100)
    left(90)
    forward(60)
    left(45)
    forward(71)
    left(90)
    forward(71)
    left(45)
    forward(60)
    left(90)
    porte()

maison()
```

````{dropdown} Solution
```python
...

def maison():
    forward(100)
    left(90)
    forward(60)
    left(45)
    forward(71)
    left(90)
    forward(71)
    left(45)
    forward(60)
    left(90)
    forward(40) # Décalage de la porte
    porte()

maison()
forward(100)
maison()
```
````
`````

## Variable globale

Une variable permet d'associer un **nom** à une valeur.

Avant de pouvoir utiliser une variable, elle doit être créée.
On appelle ce processus une **affectation** et on dit qu'on associe une valeur à une variable.
La forme générale est `var = valeur` ou `var` est le nom de la variable et `valeur` est sa valeur.

Attention, le `=` ici ne représente pas l'égalité au sens mathématique.

````{exercise}
Dans cet exemple, nous créons une variable `d` pour "distance" et lui affectons la valeur `80`. Python remplacera donc chaque `d` par `80` au cours du programme. La commande `forward(d)` va donc prendre le sens de `forward(80)` et faire avancer la tortue de `80` pas.  
Modifiez la valeur de la variable globale `d` et exécutez le programme.

```{codeplay}
from turtle import *

d = 80  # variable globale (d = distance)

def triangle():
    forward(d)
    left(120)
    forward(d)
    left(120)
    forward(d)

triangle()
triangle()
triangle()
```
````

Une variable globale apparait au début du programme et sert à configurer une propriété générale d'un programme. Ici nous choisissons une variable globale `d` pour indiquer une **distance** de base.
Cette distance est utilisée pour pouvoir dessiner des formes d'une hauteur standard.

```{admonition} Attention
:class: caution
Utilisez les variables globales avec beaucoup de modération ! Si vous en mettez trop, votre programme deviendra vite compliqué à comprendre.  
Nous verrons plus tard qu'il est plus judicieux d'utiliser des variables locales (au lieu de globales).
```

## Le point `dot()`

La fonction `dot()` dessine un point à la position actuelle de la tortue.

`````{exercise}
Ajoutez un point (`dot`) au sommet du triangle.

```{codeplay}
from turtle import *

d = 100 # variable globale (d = distance)

def triangle():
    dot()
    forward(d)
    left(120)
    dot()
    forward(d)
    left(120)
    forward(d)

triangle()
```

````{dropdown} Solution
```python
...

def triangle():
    dot()
    forward(d)
    left(120)
    dot()
    forward(d)
    left(120)
    dot()   # Ajout ici
    forward(d)

triangle()
```
````
`````

## Lever le stylo

Les deux commandes `up()` et `down()` permettent de lever et de baisser le stylo.

Ceci nous permet de dessiner des formes séparées, comme ici le petit i avec son point.

```{codeplay}
from turtle import *
d = 50

def i():
    down()      # poser le stylo
    left(90)
    forward(d)
    up()        # lever le stylo
    forward(10)
    dot()
    backward(d+10)
    right(90)
    forward(50)    # avancer à la prochaine lettre
    
i()
i()
i()
```

```{caution}
Contrairement aux fonctions `forward(d)` et `backward(d)` qui nécessitent un argument dans les parenthèses, les fonctions `up()` et `down()` ne nécessitent pas d'argument.
```

## Exercice récapitulatif

````{exercise}
Définissez une fonction `drapeau()` permettant de dessiner un drapeau suisse.  
Pour vous aider, définissez une fonction pour le carré et une autre pour la croix. Vous n'avez pas à vous préoccuper des couleurs pour le moment mais, si vous le souhaitez, cherchez les fonction `begin_fill()` et `end_fill()` sur Internet.

```{image} ../media/drapeau_suisse.png
```

Pour vous aider, la séquence d'instructions permettant de dessiner la croix vous est donnée.

```{codeplay}
:file: ex2.py
from turtle import *

up()
goto(-75, -25) # Permet d'aller à des coordonnées précises sur le canvas
down()

# Cette suite d'instructions dessine une croix, placez ces instructions dans une fonction "croix"
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)

# Suite de votre code

```

Téléchargez le fichier `.py` et déposez le fichier sur Moodle à l'endroit prévu.
````

<!--
````{dropdown} Solution
```python
from turtle import *

up()
goto(-125, -125)
down()

def croix():
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    
def carre():
    forward(250)
    left(90)
    forward(250)
    left(90)
    forward(250)
    left(90)
    forward(250)
    left(90)
    
def drapeau():
    carre()
    up()
    left(90)
    forward(100)
    right(90)
    forward(50)
    down()
    croix()
    
drapeau()
```
````
-->

## Et à part le dessin ?

Une fonction ne sert pas qu'à regrouper des instructions de dessin. Vous pouvez définir une fonction qui va afficher un texte en particulier.  

```{admonition} Rappel
:class: hint
La fonction `print()` permet d'afficher du texte.
```

`````{exercise}
Définissez une fonction `presentations()` qui affiche du texte vous présentant en plusieurs lignes (nom, age, hobbies, etc).  
Exécutez la fonction.

```{codeplay}
print("Salut je m'appelle Roger !")
...
```

````{dropdown} Solution
```python
def presentations():
    print("Salut, je m'appelle Roger")
    print("J'ai 58 ans")
    print("J'aime nourrir les canards")

presentations()
```
````
`````
