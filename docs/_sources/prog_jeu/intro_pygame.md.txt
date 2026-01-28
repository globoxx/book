(prog_jeu.intro_pygame)=

# 2. Introduction à Pygame

Cette activité consiste à prendre en main les notions de base de Pygame Zero en jouant avec ses fonctionalités.

{download}`Téléchargement des ressources nécessaires<../data/prog_2d/intro_pygame.zip>`.

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

```{image} ../media/pygame_fenetre.png
```

## 1. Fond et formes
Ajoutons un fond bleu et quelques formes géométriques à l'écran. 

```{admonition} Important
:class: warning
Pour cela, nous allons utiliser la fonction `draw()` qui est appelée automatiquement par Pygame Zero à chaque frame (tour) du jeu pour **mettre à jour l'affichage du jeu**.
```

```python
...

def draw():
    screen.clear() # Efface l'écran avant de dessiner
    screen.fill("blue") # Remplit le fond en bleu
    screen.draw.circle((250, 250), 50, "white") # Cercle blanc de centre (250, 250) et de rayon 50
    screen.draw.filled_circle((250, 100), 50, "red") # Cercle rouge rempli de centre (250, 100) et de rayon 50
    screen.draw.rect(Rect((400, 200), (150, 100)), "green") # Rectangle vert avec le coin supérieur gauche en (400, 200) et de taille (150, 100)
    screen.draw.line((150, 20), (150, 450), "purple") # Ligne verticale violette de (150, 20) à (150, 450)
    screen.draw.text("Bonjour Pygame Zero!", (400, 50), color="yellow", fontsize=40) # Texte jaune à la position (400, 50)

pgzrun.go()
```

### Exercice 1
Changez le fond en mettant une image de votre choix. Vous en trouverez dans le dossier `images` ou trouvez-en une sur Internet et déposez-la dans le dossier `images`. Changez la ligne `screen.fill(...)` par 

```python
screen.blit('nom_de_votre_image', (0, 0))
```

Le `(0, 0)` indique que l'image doit être dessinée à partir du coin supérieur gauche de la fenêtre.

Attention, l'image devrait idéalement être de la même taille que la fenêtre (800x600 pixels) pour qu'elle s'affiche correctement.

## 2. Faire bouger les formes
Nous allons faire bouger des objets. 

```{admonition} Important
:class: warning
Pour cela, nous allons utiliser la fonction `update()` qui est appelée automatiquement par Pygame Zero à chaque frame (tour) du jeu. Cette fonction est utilisée pour **mettre à jour l'état du jeu**, comme la position des objets.
```

Nous allons faire bouger un carré rouge horizontalement.

```python
...

box = Rect((20, 20), (50, 50)) # Crée un rectangle de position (20, 20) et de taille (50, 50)

def draw():
    screen.clear()
    # Vous pouvez garder le fond d'écran si vous le souhaitez mais retirez les autres formes
    screen.draw.filled_rect(box, "red") # Dessine le rectangle et le remplit en rouge

def update():
    box.x += 2 # Déplace le rectangle de 2 pixels vers la droite
    if box.x > WIDTH: # Si le rectangle dépasse la largeur de la fenêtre
        box.x = 0 # Remet le rectangle à gauche
```

### Exercice 2
Faites bouger le carré plus rapidement.

````{dropdown} J'ai besoin d'aide !
Tout objet en Pygame Zero a une position définie par des coordonnées `x` (horizontale) et `y` (verticale). `box` est un rectangle, et `box.x` représente sa position horizontale. En augmentant `box.x`, on déplace le rectangle vers la droite.

La ligne 
```python
box.x += 2
```
ajoute `2` à la position `x` du rectangle à chaque frame, ce qui le fait bouger vers la droite.
Vous pouvez augmenter la valeur `2` pour le faire bouger plus rapidement, par exemple en la changeant en `5` ou `10`.
````

### Exercice 3
Faites bouger le carré en diagonale.

```{dropdown} J'ai besoin d'aide !
Pour faire bouger le carré en diagonale, vous devez modifier à la fois sa position horizontale (`box.x`) et sa position verticale (`box.y`).

Ajoutez une ligne dans la fonction `update()` pour augmenter `box.y` de la même manière que vous avez augmenté `box.x`.
```

### Exercice 4
Ajoutez un deuxième rectangle d'une autre couleur qui se déplace également (de la manière que vous voulez).

```{dropdown} J'ai besoin d'aide !
Vous pouvez créer un deuxième rectangle en utilisant une autre variable, par exemple `box2`. Définissez-le de la même manière que `box`, mais avec une position et une taille différentes.

Ensuite, dans la fonction `draw()`, dessinez ce deuxième rectangle en utilisant `screen.draw.filled_rect(box2, "couleur")`.
```

## 3. Ajouter des acteurs (avec des images)

Pour ajouter des acteurs, nous allons utiliser la classe `Actor` de Pygame Zero. Voyez `Actor` comme un nouveau type de variable qui représente un acteur dans votre jeu, avec des propriétés/attributs comme une position (x, y) et une image.

**Vous pouvez retirer le carré rouge dessiné précédemment pour ne garder que l'acteur.**

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

````{admonition} Remarque sur les acteurs
:class: tip
Il est important de noter que l'on peut ajouter toute sorte d'attributs à un acteur, comme par exemple une vitesse, une direction, une vie, etc. Ce sont des variables attachées à l'acteur qui permettent de stocker des informations supplémentaires le concernant.

Par exemple, on pourrait ajouter une vitesse à notre acteur `player` comme ceci :

```python
player.vitesse = 2 # Ajoute un attribut vitesse à l'acteur

def update():
    player.x += player.vitesse # Utilise l'attribut vitesse pour déplacer l'acteur
```

Si vous souhaitez en savoir plus (car cela ouvre en grand les portes de la programmation plus complexe), vous pouvez consulter <a href="https://courspython.com/classes-et-objets.html" target="_blank">cette ressource</a> sur la programmation orientée objet (POO).
````

### Exercice 5
Changez l'image de l'acteur en utilisant une autre image de votre choix (assurez-vous de l'ajouter au dossier `images` si vous la téléchargez sur Internet).

````{dropdown} J'ai besoin d'aide !
Pour changer l'image de l'acteur, modifiez la ligne où l'acteur est créé :
```python
player = Actor('nom_de_votre_image')
```
Assurez-vous que le nom de l'image correspond au nom du fichier image (sans l'extension) que vous avez ajouté dans le dossier `images` de votre projet.
````

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
Permettez à l'acteur de se déplacer également vers le haut et vers le bas avec les flèches haut et bas.

```{dropdown} J'ai besoin d'aide !
Ajoutez des conditions supplémentaires dans la fonction `update()` pour vérifier si les touches flèche haut (`up`) et flèche bas (`down`) sont pressées, et modifiez la position verticale (`player.y`) de l'acteur en conséquence.
```

### Exercice 7
Empêchez l'acteur de sortir de l'écran (ou faites-le réapparaître de l'autre côté).

````{dropdown} J'ai besoin d'aide !
Pour empêcher l'acteur de sortir de l'écran, vous pouvez ajouter des conditions après avoir mis à jour sa position pour vérifier si `player.x` ou `player.y` sont en dehors des limites de la fenêtre (0 à WIDTH pour x, 0 à HEIGHT pour y). Si cela se produit, vous pouvez par exemple le faire réapparaître de l'autre côté.

Par exemple, pour la position horizontale :
```python
if player.x > WIDTH: # Si l'acteur dépasse la largeur de la fenêtre
    player.x = 0 # Remet l'acteur à gauche
elif player.x < 0: # Si l'acteur dépasse le côté gauche
    player.x = WIDTH # Remet l'acteur à droite
```

Vous pouvez faire de même pour la position verticale (`player.y`).
````


## 5. Animation des acteurs
Pygame Zero permet également d'animer les acteurs en utilisant des images différentes pour représenter différentes poses ou états. Pour cela, vous devez avoir plusieurs images nommées de manière cohérente (ex: `alien_walk1.png`, `alien_walk2.png`, etc.) et les stocker dans l'attribut `images` de l'acteur.

```python

...
player = Actor('alien') # Crée un acteur avec l'image 'alien.png'
player.images = ['alien_walk1', 'alien_walk2'] # Liste des images pour l'animation

def update():
    ...
    player.animate(5) # Change l'image de l'acteur 5 fois par seconde (5 fps)

```

### Exercice 8
Modifiez la vitesse de l'animation en changeant le nombre passé à `player.animate()` et observez l'effet.

### Exercice 9
Changez les images d'animation de votre personnage. Piochez dans celles fournies dans le dossier `images` ou récupérez les votres sur Internet.  

La plateforme <a href="https://kenney.nl/assets" target="_blank">Kenny</a> propose une grande quantité d'ensembles d'images gratuites et libres de droit que vous pouvez utiliser pour vos jeux.

## 6. Ajouter un ennemi rebondissant
Ajoutons un ennemi qui se déplace diagonalement dans le jeu en rebondissant sur les bords de l'écran. Il s'agira donc d'un nouvel `acteur` que nous appelerons `enemy`.

```python
...
enemy = Actor('bird0') # Crée un acteur ennemi avec l'image 'bird0.png'
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

#### Exercice 10
Complétez le code pour que l'ennemi se déplace diagonalement et rebondisse également sur les bords supérieur et inférieur de la fenêtre.

````{dropdown} J'ai besoin d'aide !
Votre ennemi va tout droit ! Il faut commencer par ajouter la mise à jour de la position verticale de l'ennemi dans la fonction `update()`.

La ligne
```python
enemy.x += enemy.vx
```
permet de déplacer l'ennemi horizontalement. De la même manière, vous devez ajouter une ligne pour déplacer l'ennemi verticalement en utilisant `ennemy.y` et `ennemy.vy`.

Ensuite, vous devez ajouter une condition pour vérifier si l'ennemi touche le bord supérieur ou inférieur de la fenêtre. Si `enemy.y` est inférieur à `0` (bord supérieur) ou supérieur à `HEIGHT` (bord inférieur), vous devez inverser la vitesse verticale `enemy.vy` pour faire rebondir l'ennemi.
````


## 7. Des collisions entre acteurs
Pour détecter les collisions entre deux acteurs, vous pouvez utiliser la méthode `collides_with(actor)` qui vérifie si un acteur entre en collision avec un autre.

Le but est de détecter une collision entre le joueur et l'ennemi. Si une collision est détectée, le jeu se termine.

```python
...

def update():
    ...
    # Vérifie la collision entre le joueur et l'ennemi
    if player.collides_with(enemy):
        print("Collision détectée ! Terminé !")
        exit() # Termine le jeu
```

### Exercice 11
Changez la difficulté du jeu en modifiant la vitesse de l'ennemi (ou celle du joueur).

```{dropdown} J'ai besoin d'aide !
La vitesse de l'ennemi est définie par les variables `enemy.vx` (vitesse horizontale) et `enemy.vy` (vitesse verticale).
```

## 8. Musique et sons
Pygame Zero permet également d'ajouter de la musique et des effets sonores à votre jeu. Pour cela, vous devez avoir des fichiers audio dans les dossiers `music` et `sounds` de votre projet.

```python
...

music.play('adventure') # Joue la musique de fond (fichier 'adventure.mp3' dans le dossier music)

def update():
    ...
    if player.collides_with(enemy):
        sounds.die.play() # Joue un son de game over (fichier 'die.wav' dans le dossier sounds)
        print("Collision détectée ! Terminé !")
        exit()
```

### Exercice 12
Changez la musique de fond et les effets sonores en piochant dans ceux disponibles dans les dossiers `music` et `sounds` ou trouvez vos propres bruitages sur Internet.

Vous trouverez des sons `wav` sur <a href="https://mixkit.co/free-sound-effects/game/" target="_blank">Mixkit</a> et des musiques `mp3` libres de droits sur <a href="https://incompetech.com/music/royalty-free/music.html" target="_blank">Incompetech</a>.

## A rendre

```{Admonition} À rendre sur Moodle
:class: tip

Déposez sur Moodle le fichier `jeu.py` sur lequel vous avez travaillé, contenant toutes les fonctionnalités que vous avez implémentées.

Il n'est pas nécessaire de déposer les ressources (images, sons, musiques).
```

### Exercice 13 (optionnel)
Ajoutez un second joueur contrôlé par d'autres touches du clavier (par exemple, WASD) et faites en sorte que le jeu se termine si l'un des deux joueurs entre en collision avec l'ennemi. Le but étant de survivre plus longtemps que l'autre joueur !

### Exercie 14 (optionnel)
Ajoutez plus d'ennemis pour augmenter la difficulté du jeu.

### Exercice 15 (optionnel)
Ajoutez un système de score qui augmente avec le temps passé sans collision. Affichez le score à l'écran. (Cela devient un jeu coopératif de survie !)

## Et quoi d'autre ?
Pygame Zero offre de nombreuses autres fonctionnalités. N'hésitez pas à explorer la [documentation officielle de Pygame Zero](https://pygame-zero.readthedocs.io/en/stable/) pour en savoir plus et continuer à développer vos compétences en programmation de jeux vidéo !

Voici une liste non exhaustive de ce que vous pouvez explorer ensuite :

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

### Afficher la valeur d'une variable à l'écran

Utilisez `screen.draw.text()` pour afficher du texte à l'écran, comme des scores ou de la vie.

```python
def draw():
    screen.draw.text("Vie : " + str(player.vie), (10, 10), color="white", fontsize=30)
```

### Ajouter un bouton
Vous pouvez créer des boutons en utilisant la classe `Button` fournie par `pgzhelper`.

```python
start_button = Button("Start", (WIDTH//2, HEIGHT//2), (100, 50)) # Bouton centré de taille 100x50

def draw():
    start_button.draw() # Dessine le bouton

def update():
    start_button.update() # Met à jour l'état du bouton pour le hover

def on_mouse_down(pos):
    if start_button.collidepoint(pos):
        print("Bouton Start cliqué !")
```

### Gérer le temps qui s'écoule
Il est possible de vérifier le temps écoulé depuis le début du jeu avec `pygame.time.get_ticks()`, qui retourne le nombre de millisecondes écoulées.

```python
def update():
    temps_ecoule = pygame.time.get_ticks() / 1000 # Temps écoulé en secondes
    print(f"Temps écoulé depuis le début du jeu : {temps_ecoule} secondes")
```

Il est aussi possible de créer des événements programmés avec l'objet `clock`. Cela permet d'exécuter des fonctions à intervalles réguliers ou après un certain délai.

```python
def spawn_enemy():
    print("Un nouvel ennemi apparaît !")

def spawn_boss():
    print("Un boss apparaît !")

clock.schedule_interval(spawn_enemy, 10.0) # Appelle spawn_enemy toutes les 10 secondes
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
for i in range(5): # In crée 5 ennemis
    enemy = Actor('spider')
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

