(prog_jeu.hit_the_fly)=

# 6. Comment faire pour ..?

Nous avons vu plusieurs tutoriels de jeux pygame, mais il y a tellement de possibilités que nous n'avons pas pu tout couvrir. Voici quelques pistes pour aller plus loin et faire des choses plus avancées dans vos jeux. Sachez néanmoins que le plus simple est souvent de parcourir la <a href="https://pygame-zero.readthedocs.io/en/stable/introduction.html" target="_blank">documentation officielle</a>.

### Afficher du texte à l'écran ?
Il existe une fonction `screen.draw.text` qui permet d'afficher du texte à l'écran. Par exemple, `screen.draw.text('Score: 10', (10, 10), fontsize=30, color='white')` affichera le texte "Score: 10" en blanc avec une taille de police de 30 aux coordonnées (10, 10) de la fenêtre.

Si vous voulez afficher une variable dans du texte, vous pouvez utiliser les f-strings de Python. Par exemple, si vous avez une variable `score`, vous pouvez l'afficher avec le texte en écrivant `screen.draw.text(f'Score: {score}', (10, 10), fontsize=30, color='white')`.

Exemple:
```python
player.score = 0

def update():
    # Code pour augmenter le score
    player.score += 1

def draw():
    screen.draw.text(f'Score: {player.score}', (10, 10), fontsize=30, color='white')
```

### Tirer un nom d'image aléatoire ?
Vous pouvez utiliser le module `random` de Python pour tirer un nom d'image aléatoire. Par exemple, si vous avez plusieurs images d'astéroïdes nommées `asteroid1.png`, `asteroid2.png`, etc., vous pouvez choisir une image aléatoire avec `random.choice(['asteroid1', 'asteroid2', 'asteroid3'])`.

Exemple:
```python
import random
asteroid = Actor('asteroid1') # On crée un acteur avec une image par défaut
asteroid.image = random.choice(['asteroid1', 'asteroid2', 'asteroid3'])
```

### Détecter un clic de souris ?
Pygame Zero offre une fonction spéciale `on_mouse_down(pos)` qui est appelée automatiquement à chaque fois que l'utilisateur clique avec la souris. La variable `pos` correspond aux coordonnées du clic de souris. Vous pouvez donc ajouter cette fonction à votre code et y mettre le code que vous voulez exécuter à chaque clic de souris.

Exemple:
```python
def on_mouse_down(pos):
    print(f'Vous avez cliqué aux coordonnées {pos}')    
```

## Détecter un déplacement de souris ?
Pygame Zero offre également une fonction spéciale `on_mouse_move(pos)` qui est appelée automatiquement à chaque fois que l'utilisateur déplace la souris. La variable `pos` correspond aux coordonnées de la souris.

Exemple:
```python
def on_mouse_move(pos):
    print(f'La souris est aux coordonnées {pos}')    
```

### Ajouter un bouton ?
Pgzhelper vous fournit une classe `Button` qui permet de créer facilement des boutons cliquables. Vous pouvez créer un bouton avec `button = Button('mon_texte', (x, y), (largeur, hauteur))` et ensuite vérifier s'il a été cliqué dans la fonction `on_mouse_down(pos)` avec `if button.collidepoint(pos):`. Important: n'oubliez pas d'appeler la méthode `button.draw()` dans la fonction `draw` pour que le bouton soit visible à l'écran.

Exemple:
```python
button = Button('Cliquez-moi', (100, 100), (200, 50))
def on_mouse_down(pos):
    if button.collidepoint(pos):
        print('Le bouton a été cliqué !')

def draw():
    button.draw() # Affiche le bouton
```

### Déplacer un acteur dans une direction donnée ?
Si vous voulez déplacer un acteur dans une direction donnée, vous pouvez lui donner un attribut `direction` qui correspond à un angle en degrés (0 = vers la droite, 90 = vers le bas, 180 = vers la gauche, 270 = vers le haut). Ensuite, dans la fonction `update`, vous pouvez simplement appeler `acteur.move_in_direction(speed)` qui déplacera l'acteur à la vitesse `speed` dans la direction indiquée par son attribut `direction`. Cela remplace donc `acteur.x += ...` et `acteur.y += ...`.

Exemple:
```python
player.direction = 90 # Le joueur va vers le bas
player.speed = 5 # Le joueur se déplace à une vitesse de 5 pixels par tour de jeu

def update():
    if keyboard.up:
        player.direction = 270 # vers le haut
    elif keyboard.down:
        player.direction = 90 # vers le bas
    elif keyboard.left:
        player.direction = 180 # vers la gauche
    elif keyboard.right:
        player.direction = 0 # vers la droite

    player.move_in_direction(player.speed) # Le joueur se déplace à une vitesse de 5 pixels par tour de jeu
```

### Calculer l'angle / la direction entre 2 acteurs ?
Vous pouvez utiliser la fonction `angle_to` d'un acteur pour calculer l'angle entre lui et un autre acteur. Par exemple, `player.angle_to(ennemi)` vous donnera l'angle en degrés entre le joueur et un ennemi. Ces calculs peuvent être utiles pour faire un ennemi qui poursuit le joueur ou pour faire des tirs qui partent dans la direction d'un ennemi.

Exemple:
```python
def update():
    angle = player.angle_to(ennemi)
    print(f'L\'angle entre le joueur et l\'ennemi est de {angle} degrés')

    player.direction = angle # Le joueur se dirige vers l'ennemi
    player.move_in_direction(player.speed) # Le joueur se déplace à une vitesse de
```

## Déplacer un acteur avec la souris ?
Vous pouvez faire en sorte qu'un acteur suive la souris en utilisant la fonction `on_mouse_down(pos)` qui est appelée à chaque fois que la souris est cliquée. La variable `pos` correspond aux coordonnées de la souris. Vous pouvez donc faire en sorte que le player se déplace vers cette position avec des calculs d'angles.

Exemple:
```python
def on_mouse_down(pos):
    direction = player.angle_to(pos) # Calcul de l'angle entre le joueur et la position de la souris
    player.direction = direction
    player.angle = direction # Si vous voulez que l'image du joueur soit orientée dans la direction du mouvement
    player.move_in_direction(player.speed) # Le joueur se déplace à une vitesse de player.speed
```

### Mesurer le temps écoulé depuis un évènement ?
La fonction `update` de Pygame Zero reçoit un paramètre optionnel `dt` qui correspond au temps écoulé en secondes depuis le dernier tour de jeu. Cela peut être très utile pour faire des actions qui ne peuvent pas être faites à chaque tour de jeu, comme tirer un laser ou faire une animation. Par exemple, si vous voulez que le joueur puisse tirer un laser toutes les 0.5 secondes, vous pouvez créer une variable `timer` qui s'incrémente à chaque tour de jeu avec le temps écoulé `dt`, et vérifier si cette variable est supérieure ou égale à 0.5 avant de permettre un tir.

Exemple:
```python
player.timer = 0 # Initialisation du timer à 0

def update(dt):
    if keyboard.space and player.timer >= 0.5:
        # Code pour tirer un laser
        player.timer = 0 # Réinitialisation du timer après le tir

    player.timer += dt # on incrémente le timer avec le temps écoulé depuis le dernier tour de jeu
```