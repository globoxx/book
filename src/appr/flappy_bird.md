# Flappy Bird

Pygame Zero est un wrapper autour de Pygame, un moteur de jeu Python populaire. L'avantage de Pygame Zero est qu'il présente une interface très simple et rationalisée, ce qui signifie qu'il faut très peu de travail pour créer des jeux complets.

Dans ce tutoriel, nous allons créer un clone de Flappy Bird.

## Installation des ressources

...

## Mise en route

Appuyez sur le bouton Nouveau dans Mu pour ouvrir un nouveau fichier et saisissez les lignes suivantes:

```python
TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 708
```

Appuyez sur Enregistrer et enregistrez le fichier sous flappybird.py
Appuyez sur Play pour voir ce que fait ce code.

Vous devriez voir apparaître une nouvelle fenêtre vide.

## Dessiner un arrière-plan

Ajoutez ces lignes à la fin de votre programme.

```python
def draw():
    screen.blit('cascade', (0, 0))
```

Vous devez avoir une fonction de dessin si vous voulez que Pygame Zero dessine quoi que ce soit. La ligne qui commence par screen.blit est la seule instruction de cette fonction. Il dit à Pygame Zero de dessiner quelque chose sur l'écran.

## Ajouter l'oiseau

Ajoutez cette ligne à la fin de votre fichier.

```python
bird = Actor('bird1', (75, 350))
```

Cette ligne crée un acteur appelé bird.

Actor fait partie de Pygame Zero, mais bird est une nouvelle variable que vous créez en écrivant cette ligne. Vous pouvez l'appeler comme vous voulez. Si vous le vouliez, vous pourriez écrire:

```python
barry_the_bird = Actor('bird1', (75, 350))
```

Faisons ça en fait ! Je vais continuer avec barry_the_bird , mais si vous le souhaitez, vous pouvez choisir votre propre nom. N'oubliez pas de taper le nom que vous avez choisi au lieu de barry_the_bird chaque fois que nous utilisons la variable.

Si nous voulons vraiment voir Barry (ou quel que soit le nom de votre oiseau), nous devrons l'ajouter à la fonction de tirage.

Ajoutez la ligne suivante à votre fonction de dessin (n'oubliez pas d'utiliser le nom de votre oiseau):

```python
barry_the_bird.draw()
```

## Faire bouger l'oiseau

Faisons en sorte que notre oiseau réponde à l'entrée de la souris. Ajoutons une nouvelle fonction. Les fonctions peuvent être dans n'importe quel ordre dans le fichier, mais un bon endroit est juste avant la fonction de dessin.

Ajoutez le code suivant juste avant la fonction draw (n'oubliez pas d'utiliser le nom de votre oiseau):

```python
def on_mouse_down():
    print ('The mouse was clicked')
    barry_the_bird.y -= 50
```

La fonction on_mouse_down est appelée à chaque fois que vous cliquez sur la souris. Appeler une fonction signifie exécuter les instructions qu'elle contient. Si nous voulons que l'oiseau se déplace en douceur, nous devons le déplacer en petites quantités et le faire si souvent qu'il semble lisse.

Une fonction de mise à jour est une fonction qui est appelée encore et encore très rapidement. Normalement 60 fois par seconde.

Ajoutez cette fonction à votre fichier (n'oubliez pas d'utiliser le nom de votre oiseau):

```python
def update():
    barry_the_bird.y += 1
```