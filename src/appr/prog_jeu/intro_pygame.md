(prog_jeu.intro_pygame)=

# 2. Introduction à Pygame
Pygame est une bibliothèque Python permettant de créer des jeux vidéo en 2D. Elle fournit des fonctionnalités pour gérer les fenêtres, les événements, les images, les sons, et bien plus encore.

Vous trouverez ci-dessous le code minimal pour faire apparaître la fenêtre de votre jeu.

```python
import pgzero
import pgzrun
from pgzhelper import *

TITLE = 'Premier test !' # Titre de votre jeu

WIDTH = 800 # Largeur de la fenêtre
HEIGHT = 600 # Hauteur de la fenêtre

pgzrun.go() # Lance le jeu
```

## 1. Fond et formes
Ajoutons un fond bleu et quelques formes géométriques à l'écran. Pour cela, nous allons utiliser la fonction `draw()` qui est appelée automatiquement par Pygame Zero à chaque frame (tour) du jeu pour dessiner les éléments à l'écran.

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

### Exercice 2
Changez le fond en mettant une image de votre choix. Trouvez-en une et déposez-la dans le dossier `images` de votre projet. Changez la ligne `screen.fill("blue")` par `screen.blit('nom_de_votre_image', (0, 0))`.

Attention, l'image devrait être de la même taille que la fenêtre (800x600 pixels) pour qu'elle s'affiche correctement.

## 2. Faire bouger les formes
Pour faire bouger les objets, nous allons utiliser la fonction `update()` qui est appelée automatiquement par Pygame Zero à chaque frame (tour) du jeu. Cette fonction est utilisée pour **mettre à jour la logique du jeu**, comme la position des objets.

Nous allons faire bouger un carré rouge horizontalement.

```python
...

box = Rect((20, 20), (50, 50)) # Crée un rectangle de position (20, 20) et de taille (50, 50)

def draw():
    screen.clear()
    screen.draw.filled_rect(box, "red") # Dessine le rectangle et le remplit en rouge

def update():
    box.x += 2 # Déplace le rectangle de 2 pixels vers la droite
    if box.x > WIDTH: # Si le rectangle dépasse la largeur de la fenêtre
        box.x = 0 # Remet le rectangle à gauche
```

### Exercice 2
Faites bouger le carré plus rapidement.

### Exercice 3
Faites bouger le carré en diagonale.

### Exercice 4
Ajoutez un deuxième rectangle d'une autre couleur qui se déplace également (de la manière que vous voulez).

## 3. Ajouter des acteurs (avec des images)

Pour ajouter des acteurs, nous allons utiliser la classe `Actor` de Pygame Zero. Assurez-vous d'avoir une image nommée `alien.png` dans le dossier `images` de votre projet.

Voyez `Actor` comme un nouveau type de variable qui représente un acteur dans votre jeu, avec des propriétés comme une position (x, y) et une image.

```python
...

player = Actor('alien') # Crée un acteur (nommé player) avec l'image 'alien.png'
player.x = 0 # Positionne l'acteur à x = 0
player.y = 50 # Positionne l'acteur à y = 50

def draw():
    screen.clear()
    player.draw() # Dessine l'acteur à sa position actuelle

def update():
    player.x += 2 # Déplace l'acteur de 2 pixels vers la droite
    if player.x > WIDTH: # Si l'acteur dépasse la largeur de la fenêtre
        player.x = 0 # Remet l'acteur à gauche
```

### Exercice 5
Changez l'image de l'acteur en utilisant une autre image de votre choix (assurez-vous de l'ajouter au dossier `images`).

## 4. Gestion du clavier

Il est temps de faire bouger notre acteur nous-mêmes ! Nous allons utiliser la variable spéciale `keyboard` fournie par Pygame Zero pour détecter les touches pressées.

```python
...

def update():
    if keyboard.right: # Si la touche flèche droite est pressée
        player.x += 5 # Déplace l'acteur de 5 pixels vers la droite
    elif keyboard.left: # Si la touche flèche gauche est pressée
        player.x -= 5 # Déplace l'acteur de 5 pixels vers la gauche
```

### Exercice 6
Permettez à l'acteur de se déplacer également vers le haut et vers le bas.

### Exercice 7
Empêchez l'acteur de sortir de l'écran (ou faites-le réapparaître de l'autre côté).

### Exercice 8
Si ce n'est pas déjà fait, permettez à l'acteur de se déplacer en diagonale en appuyant sur deux touches en même temps (par exemple, flèche droite + flèche haut).

## 5. Animation des acteurs
Pygame Zero permet également d'animer les acteurs en utilisant des images différentes pour représenter différentes poses ou états. Pour cela, vous devez avoir plusieurs images nommées de manière cohérente, par exemple `alien1.png`, `alien2.png`, etc.

```python

...
player = Actor('alien1') # Crée un acteur avec l'image 'alien1.png'
player.images = ['alien1', 'alien2', 'alien3'] # Liste des images pour l'animation

def update():
    ...
    player.animate(5) # Change l'image de l'acteur toutes les 5 frames (5 fps)

```

### Exercice 9
Modifiez la vitesse de l'animation en changeant le nombre passé à `player.animate()`.

### Exercice 10
Rendez-vous sur <a href="https://kenney.nl/assets" target="_blank">Kenny</a> pour télécharger un ensemble d'images d'animation gratuites. Ajoutez-les à votre projet (dans le dossier `images`) et utilisez-les pour animer votre acteur.

## 6. Ajouter un ennemi rebondissant
Ajoutons un ennemi qui se déplace diagonalement dans le jeu en rebondissant sur les coins. Il s'agira donc d'un nouvel `acteur`.

```python
...
enemy = Actor('alien2') # Crée un acteur ennemi avec l'image 'alien2.png'
enemy.x = 400
enemy.y = 300
enemy.vx = 3 # Vitesse horizontale
enemy.vy = 2 # Vitesse verticale

def draw():
    ...
    enemy.draw() # Dessine l'ennemi

def update():
    ...
    # Met à jour la position de l'ennemi
    enemy.x += enemy.vx

    # Vérifie les collisions avec les bords de la fenêtre
    if enemy.x < 0 or enemy.x > WIDTH:
        enemy.vx = -enemy.vx # Inverse la vitesse horizontale
```

#### Exercice 11
Complétez le code pour que l'ennemi se déplace diagonalement et rebondisse également sur les bords supérieur et inférieur de la fenêtre.

## 7. Des collisions entre acteurs
Pour détecter les collisions entre deux acteurs, vous pouvez utiliser la méthode `collides_with(actor)` qui vérifie si un acteur entre en collision avec un autre.

Le but est de détecter une collision entre le joueur et l'ennemi. Si une collision est détectée, le jeu se termine.

```python
...

def update():
    ...
    # Vérifie la collision entre le joueur et l'ennemi
    if player.collides_with(enemy):
        print("Collision détectée ! Jeu terminé.")
        exit() # Termine le jeu
```

### Exercice 12
Changez la difficulté du jeu en modifiant la vitesse de l'ennemi (ou celle du joueur).

## 8. Musique et sons
Pygame Zero permet également d'ajouter de la musique de fond et des effets sonores à votre jeu. Pour cela, vous devez avoir des fichiers audio dans le dossier `sounds` de votre projet.

```python
...

music.play('background_music') # Joue la musique de fond (fichier 'background_music.mp3' dans le dossier sounds)

def update():
    ...
    if player.collides_with(enemy):
        sounds.explosion.play() # Joue un son d'explosion (fichier 'explosion.wav' dans le dossier sounds)
        print("Collision détectée ! Jeu terminé.")
        exit()
```

### Exercice 13
Changez la musique de fond et les effets sonores en utilisant vos propres fichiers audio (assurez-vous de les ajouter au dossier `sounds`).

## Et quoi d'autre ?
Pygame Zero offre de nombreuses autres fonctionnalités. N'hésitez pas à explorer la [documentation officielle de Pygame Zero](https://pygame-zero.readthedocs.io/en/stable/) pour en savoir plus et continuer à développer vos compétences en programmation de jeux vidéo !

Voici une liste non exhaustive de ce que vous pouvez explorer ensuite :

### Afficher du texte à l'écran

Utilisez `screen.draw.text()` pour afficher du texte à l'écran, comme des scores ou des messages.

```python
def draw():
    screen.draw.text("Salut !", (10, 10), color="white", fontsize=30)
```

### Donner de la vie à vos acteurs
Utilisez des variables pour gérer la santé ou l'énergie de vos acteurs, et modifiez-les en fonction des événements du jeu.

```python
player = Actor('alien')
player.vie = 100 # Initialise la vie du joueur à 100

def update():
    if player.collides_with(enemy):
        player.vie -= 10 # Réduit la santé du joueur de 10 en cas de collision
        if player.vie <= 0:
            print("Le joueur est mort ! Jeu terminé.")
            exit()
```

### Gérer le temps qui s'écoule
Utilisez la variable spéciale `clock` pour gérer des événements basés sur le temps, comme des délais ou des minuteries.

```python
def update():
    if clock.get_time() % 5000 == 0: # Toutes les 5 secondes
        print("5 secondes se sont écoulées !")
```

Il est aussi possible de créer des minuteries personnalisées avec `clock.schedule()` et `clock.schedule_unique()`.
```python

def spawn_enemy():
    print("Un nouvel ennemi apparaît !")

def spawn_boss():
    print("Un boss apparaît !")

clock.schedule(spawn_enemy, 10.0) # Appelle spawn_enemy toutes les 10 secondes
clock.schedule_unique(spawn_boss, 15.0) # Appelle spawn_boss une seule fois après 15 secondes
```

### Gestion de la souris
Utilisez la fonction spéciale `on_mouse_down` pour décrire ce qui se passe lorsqu'un clic de souris est détecté à une position (`pos`) donnée.

```python
def on_mouse_down(pos):
    print(f"Souris cliquée en position {pos}")
```

### Gérer la rotation des acteurs
Vous pouvez faire pivoter les acteurs en modifiant leur propriété `angle`. Cela modifie uniquement l'image de l'acteur, pas sa direction de déplacement.

```python
player.angle += 5 # Fait pivoter l'acteur de 5 degrés à chaque frame
```

### Gérer des déplacements plus complexes
Parfois, il est nécessaire de déplacer un acteur dans une direction spécifique plutôt que simplement à gauche, à droite, en haut ou en bas.  

Utilisez la propriété `direction` pour définir la direction de déplacement d'un acteur en degrés (0° vers la droite, 90° vers le haut, etc.). Ensuite, utilisez la méthode `move_in_direction(speed)` pour déplacer l'acteur dans cette `direction` à une vitesse donnée.

```python
player.direction = 45 # Définit la direction de l'acteur à 45 degrés (diagonale haut-droite)
player.move_in_direction(5) # Déplace l'acteur de 5 pixels dans la direction définie
``` 

### Gérer des listes d'acteurs
Vous pouvez créer et gérer plusieurs acteurs en utilisant des listes Python. Cela est utile pour gérer des groupes d'ennemis, des projectiles, etc.

```python
enemies = [] # Liste pour stocker les ennemis
for i in range(5):
    enemy = Actor('alien2')
    enemy.x = random.randint(0, WIDTH)
    enemy.y = random.randint(0, HEIGHT)
    enemies.append(enemy) # Ajoute l'ennemi à la liste

def draw():
    for enemy in enemies:
        enemy.draw() # Dessine chaque ennemi dans la liste

def update():
    for enemy in enemies:
        enemy.x += 1 # Déplace chaque ennemi vers la droite
```

