(prog_jeu.intro_pygame)=

# 2. Introduction à Pygame
Pygame est une bibliothèque Python permettant de créer des jeux vidéo en 2D. Elle fournit des fonctionnalités pour gérer les fenêtres, les événements, les images, les sons, et bien plus encore.

Vous trouverez ci-dessous le code minimal pour faire apparaître la fenêtre de votre jeu.

```python
import pgzrun
from pgzhelper import *

TITLE = 'Premier test !' # Titre de votre jeu

WIDTH = 800 # Largeur de la fenêtre
HEIGHT = 600 # Hauteur de la fenêtre

pgzrun.go() # Lance le jeu
```

## Fond et formes
Ajoutons un fond bleu et quelques formes géométriques à l'écran. Pour cela, nous allons utiliser la fonction `draw()` qui est appelée automatiquement par Pygame Zero à chaque frame (tour) du jeu.

```python
...

def draw():
    screen.clear() # Efface l'écran avant de dessiner
    screen.fill("blue") # Remplit le fond en bleu
    screen.draw.circle((250, 250), 50, "white") # Dessine un cercle blanc de centre (250, 250) et de rayon 50
    screen.draw.filled_circle((250, 100), 50, "red") # Dessine un cercle rouge rempli de centre (250, 100) et de rayon 50
    screen.draw.line((150, 20), (150, 450), "purple") # Dessine une ligne verticale violette de (150, 20) à (150, 450)
    screen.draw.line((150, 20), (350, 20), "purple") # Dessine une ligne horizontale violette de (150, 20) à (350, 20)

pgzrun.go()
```

### Exercice 1
Complétez la forme.

## Faire bouger les formes
Pour faire bouger les objets, nous allons utiliser la fonction `update()` qui est appelée automatiquement par Pygame Zero à chaque frame (tour) du jeu. Nous allons faire bouger un carré rouge horizontalement.

```python
...

box = Rect((20, 20), (50, 50)) # Crée un carré rouge de position (20, 20) et de taille (50, 50)

def draw():
    screen.clear()
    screen.draw.filled_rect(box, "red")

def update():
    box.x = box.x + 2
    if box.x > WIDTH:
        box.x = 0
```

### Exercice 2
Faites bouger le carré plus rapidement.

### Exercice 3
Faites bouger le carré en diagonale.

### Exercice 4
Ajoutez un deuxième carré d'une autre couleur qui se déplace également.

## Ajouter des acteurs (avec des images)

Pour ajouter des images, nous allons utiliser la classe `Actor` de Pygame Zero. Assurez-vous d'avoir une image nommée `ninja.png` dans le dossier `images` de votre projet.

```python
...

alien = Actor('alien')
alien.x = 0
alien.y = 50

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.x += 2
    if alien.x > WIDTH:
        alien.x = 0