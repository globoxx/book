(prog_formel.intro)=

# 1. Introduction

<a href="https://perso.limsi.fr/pointal/_media/python:cours:mementopython3.pdf" target="_blank">Mémento Python</a>  
<a href="https://support.apple.com/fr-ch/HT201236" target="_blank">Raccourcis clavier</a>

## Votre tout premier programme 🤩

Voici un exemple d’un tout petit programme en Python qui ne contient qu’une seule instruction:

```{codeplay}
print("bonjour")
```

En anglais, "print" signifie “imprime". En Python, l’instruction `print` demande à l’ordinateur **d’afficher à l’écran le contenu de la parenthèse qui vient après**.

````{admonition} Exercice 1
:class: note
1. Changez le texte pour que l’ordinateur écrive autre chose, par exemple "au revoir !".  
2. Faites lui écrire un nombre (sans guillemets car ils ne sont utilisés que pour le texte)
3. Faites lui écrire le résultat d'une opération mathématique (sans guillemets)
```{codeplay}
:file: ex_1.py
print("bonjour")
```
````

`````{admonition} Solution
````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down
```{codeplay}
:file: ex_1.py
print('au revoir !')
print(42)
print(6 * 7 + 5)
``` 
Assurez-vous de bien maîtriser la sauvegarde de vos fichiers !  
Savoir sauvegarder et retrouver des fichiers dans les bons dossiers est primordial 😉
````
`````

## Les commentaires

Il est souvent utile de mettre des commentaires dans un programme, pour expliquer ce qu’il fait.
En Python, un commentaire est introduit par le caractère `#`.  
**Tout ce qui vient après et jusqu’à la fin de la ligne n’est pas lu par l’ordinateur**.  
Cela sert uniquement à l’humain qui va lire le programme 🤓

```{codeplay}
# un tout petit programme
print("bonjour")  # salutations
```

```{admonition} Exercice 2
:class: note
Enlevez les guillemets autour de "bonjour". Qu’est-ce qui se passe ?
```

`````{admonition} Solution
````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down
Le programme n’est plus compris par la machine car si "bonjour" était un texte pouvant être affiché sans problème, `bonjour` désigne une variable ayant pour nom bonjour.  
Cette variable n’existant pas au moment de son appel, l’ordinateur ne sait pas quoi afficher 🤔  
⚠️ Du texte s'écrit toujours entre guillemets ou apostrophes (`""` ou `''`). ⚠️
````
`````

## Exercices Turtle 🐢 (facultatif)

`turtle` est un module Python permettant de faire du **dessin en codant**. La tortue peut se déplacer et dessiner une trace avec les 4 fonctions:

1. `forward(d)` pour avancer d’une distance `d` (en pixels).
2. `backward(d)` pour reculer.
3. `left(a)` pour tourner à gauche d’un angle `a` (en degrés).
4. `right(a)` pour tourner à droite

Ce code permet de dessiner un carré, testez-le !

```{codeplay}
import turtle  # Importe le module

turtle.forward(100)  # Avance de 100 pixels
turtle.left(90)  # Tourne a gauche de 90 degres
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.done()  # Termine le dessin
```

Si vous êtes curieux, la plateforme <a href="https://apprendre.modulo-info.ch/prog1/dessiner.html" target="_blank">Modulo</a> propose beaucoup d’autres exemples et exercices dans son chapitre **Programmation**.

````{admonition} Exercice - Le triangle
:class: note
Ecrivez un programme qui dessine un triangle équilatéral avec chaque côté ayant une longueur de 100 pixels.  
(Rappel : chaque angle d’un triangle équilatéral fait 60 degrés).

```{codeplay}
:file: triangle.py
import turtle  # Importe le module

...

turtle.done()  # Termine le dessin
```
````

`````{admonition} Solution
````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down
```{codeplay}
:file: triangle.py
import turtle # Importe le module

turtle.forward(100) # Avance de 100 pixels
turtle.left(120) # Tourne a gauche de 120 degres (180-60)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)

turtle.done() # Termine le dessin
``` 
Assurez-vous de bien maîtriser la sauvegarde de vos fichiers !  
Savoir sauvegarder et retrouver des fichiers dans les bons dossiers est primordial 😉
````
`````
