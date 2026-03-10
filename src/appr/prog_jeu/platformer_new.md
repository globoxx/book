(prog_jeu.platformer)=

# 5. Jumper (platformer)

Dans ce tutoriel, nous allons développer un jeu de plateforme où le personnage peut se déplacer sur des blocs pour attraper des objets et combattre des ennemis. Nous allons également devoir mettre en place un système de gravité pour permettre au joueur de sauter et de tomber des blocs.

{download}`Téléchargement des ressources du jeu<../data/prog_2d/jumper.zip>`.

```{image} ../media/platformer.gif
```

## 1. Faire apparaître des blocs

Dans un jeu de plateforme, il faut des blocs (`tile` en anglais) ! Heureusement pour vous, je vous ai préparé un acteur qui va prendre ce rôle, l'acteur `Plateform`.  
Commençons par initialiser notre jeu et faire apparaître un bloc au centre de notre fenêtre.

```python
from pgzhelper import *

TITLE = 'Platformer'
WIDTH = 800
HEIGHT = 600

platform = Platform('grass_tile', (WIDTH/2, HEIGHT/2))

def draw():
    screen.fill('sky blue') # Ajout d'un background bleu pour faire le ciel
    platform.draw()

def update():
    pass # Notre acteur platform n'a pas de logique particulière pour le moment
```

```{image} ../media/platformer_bloc.png
```

````{dropdown} Voir le code à ce point
```python
import pgzero
import pgzrun
from pgzhelper import *

TITLE = 'Platformer'
WIDTH = 800
HEIGHT = 600

platform = Platform('grass_tile', (WIDTH/2, HEIGHT/2))

def draw():
    screen.fill('sky blue')
    platform.draw()

def update():
    pass

pgzrun.go()
```
````

## 2. Faire apparaître notre joueur

Faisons à présent apparaître notre personnage au-dessus de ce bloc. Comme dans les tutoriels `runner` et `star_wars`, nous allons utiliser directement la classe `Actor` fournie par Pygame Zero.

```python
player = Actor('alien_walk1')
player.x = WIDTH/2
player.y = HEIGHT/2 - 100
```

Il ne reste plus qu'à dessiner notre joueur dans la fonction principale `draw`.

```python
def draw():
    screen.fill('sky blue')
    platform.draw()
    player.draw()

def update():
    pass
```

```{image} ../media/platformer_bloc_joueur.png
```

````{dropdown} Voir le code à ce point
```python
import pgzero
import pgzrun
from pgzhelper import *

TITLE = 'Platformer'
WIDTH = 800
HEIGHT = 600

platform = Platform('grass_tile', (WIDTH/2, HEIGHT/2))

player = Actor('alien_walk1')
player.x = WIDTH/2
player.y = HEIGHT/2 - 100

def draw():
    screen.fill('sky blue')
    platform.draw()
    player.draw()

def update():
    pass

pgzrun.go()
```
````

## 3. Déplacer le joueur horizontalement

Commençons de manière simple par implémenter les déplacements horizontaux de notre personnage avec les touches `a` et `d`.  
Comme pour le jeu précédent, nous allons définir une vitesse pour notre personnage.

```python
player = Actor('alien_walk1')
player.x = WIDTH/2
player.y = HEIGHT/2 - 100
player.speed = 3
```

La logique du déplacement se code directement dans la fonction `update`. Il suffit de vérifier si la touche `a` ou `d` est enfoncée et, si c'est le cas, mettre à jour la position `x` du joueur en tenant compte de sa vitesse. On en profite également pour retourner l'image si le déplacement se fait vers la gauche.

```python
def update():
    if keyboard.a:
        player.x -= player.speed
        player.flip_x = True
    if keyboard.d:
        player.x += player.speed
        player.flip_x = False
```

Et voilà ! Vous devriez voir votre personnage flotter de gauche à droite de l'écran au-dessus du bloc.

````{dropdown} Voir le code à ce point
```python
import pgzero
import pgzrun
from pgzhelper import *

TITLE = 'Platformer'
WIDTH = 800
HEIGHT = 600

platform = Platform('grass_tile', (WIDTH/2, HEIGHT/2))

player = Actor('alien_walk1')
player.x = WIDTH/2
player.y = HEIGHT/2 - 100
player.speed = 3

def draw():
    screen.fill('sky blue')
    platform.draw()
    player.draw()

def update():
    if keyboard.a:
        player.x -= player.speed
        player.flip_x = True
    if keyboard.d:
        player.x += player.speed
        player.flip_x = False

pgzrun.go()
```
````

## 4. Ajouter la gravité

L'heure est grave, notre personnage flotte sans jamais tomber ! Repensons à notre ami Newton... la gravité est une accélération vers le bas. La vitesse verticale de notre personnage doit donc augmenter avec le temps.

La première chose à faire est de fixer notre constante de gravité à l'aide d'une variable. Elle vaut 9.81 m/s^2 sur Terre mais cela serait trop pour notre petit jeu. Fixons-la à `0.3` pour le moment. Il nous faut aussi déclarer une vitesse verticale `vy` pour notre personnage, qui est nulle par défaut.

```python
GRAVITY = 0.3 # Une constante s'écrit en majuscule par convention

player = Actor('alien_walk1')
player.x = WIDTH/2
player.y = HEIGHT/2 - 100
player.speed = 3
player.vy = 0 # Vitesse verticale du personnage
```

Bien, à présent il nous faut ajouter cette accélération à la vitesse verticale `vy` de notre personnage à chaque `tick` du jeu et faire évoluer sa position verticale `y`.

```python
def update():
    player.vy += GRAVITY # Augmente la vitesse verticale du joueur

    if keyboard.a:
        player.x -= player.speed
        player.flip_x = True
    elif keyboard.d:
        player.x += player.speed
        player.flip_x = False

    player.y += player.vy # Met à jour la position verticale du joueur
```

Vous devriez à présent pouvoir voir votre personnage chuter dès le début du jeu (et tomber à travers notre plateforme).

````{dropdown} Voir le code à ce point
```python
import pgzero
import pgzrun
from pgzhelper import *

TITLE = 'Platformer'
WIDTH = 800
HEIGHT = 600

GRAVITY = 0.3

platform = Platform('grass_tile', (WIDTH/2, HEIGHT/2))

player = Actor('alien_walk1')
player.x = WIDTH/2
player.y = HEIGHT/2 - 100
player.speed = 3
player.vy = 0

def draw():
    screen.fill('sky blue')
    platform.draw()
    player.draw()

def update():
    player.vy += GRAVITY

    if keyboard.a:
        player.x -= player.speed
        player.flip_x = True
    elif keyboard.d:
        player.x += player.speed
        player.flip_x = False

    player.y += player.vy

pgzrun.go()
```
````

## 5. Se poser sur une plateforme

Il faut maintenant s'occuper de faire tenir notre personnage sur le bloc afin de l'empêcher de passer au travers. En temps normal, c'est une implémentation difficile car il y a beaucoup de petits détails à prendre en compte mais je vous ai un peu facilité le travail. Notre acteur `Plateform` contient une méthode qui permet de gérer les collisions avec les autres acteurs: `check_collision_with_actor(actor)`.  
Il nous suffit de l'appeler dans la fonction `update`.

```python
def update():
    player.vy += GRAVITY

    if keyboard.a:
        player.x -= player.speed
        player.flip_x = True
    elif keyboard.d:
        player.x += player.speed
        player.flip_x = False

    platform.check_collision_with_actor(player) # S'occupe automatiquement de gérer la collision

    player.y += player.vy
```

Si vous êtes curieux de comprendre comment la collision est gérée, je vous invite à aller jeter un oeil à l'implémentation de cette méthode dans le fichier `pgzhelper.py`.

````{dropdown} Voir le code à ce point
```python
import pgzero
import pgzrun
from pgzhelper import *

TITLE = 'Platformer'
WIDTH = 800
HEIGHT = 600

GRAVITY = 0.3

platform = Platform('grass_tile', (WIDTH/2, HEIGHT/2))

player = Actor('alien_walk1')
player.x = WIDTH/2
player.y = HEIGHT/2 - 100
player.speed = 3
player.vy = 0

def draw():
    screen.fill('sky blue')
    platform.draw()
    player.draw()

def update():
    player.vy += GRAVITY

    if keyboard.a:
        player.x -= player.speed
        player.flip_x = True
    elif keyboard.d:
        player.x += player.speed
        player.flip_x = False

    platform.check_collision_with_actor(player)

    player.y += player.vy

pgzrun.go()
```
````

## 6. Permettre au personnage de sauter

Un jeu de plateforme n'en est pas un si notre personnage ne peut pas sauter ! Nous allons le faire avec la touche espace (`space`) du clavier.  
Quand on y pense, faire sauter notre personnage revient à modifier sa vitesse verticale. En la rendant négative, le personnage se déplace vers le haut jusqu'à ce que la gravité vienne compenser l'action du saut et le fasse tomber à nouveau.

Il suffit donc d'ajouter 2 lignes de code dans `update` où l'on vérifie si la touche `space` est enfoncée. Si c'est le cas, on modifie la vitesse verticale `vy` de notre personnage.

```{admonition} Pas de saut dans le vide !
:class: warning
Attention, il faut également que le personnage se trouve sur une plateforme pour pouvoir sauter ! Cela se vérifie si la vitesse verticale de notre personnage est nulle au moment du saut ! (`vy == 0`)
```

```python
def update():
    player.vy += GRAVITY

    if keyboard.a:
        player.x -= player.speed
        player.flip_x = True
    elif keyboard.d:
        player.x += player.speed
        player.flip_x = False

    platform.check_collision_with_actor(player)

    # Il est important que ce test se fasse après le contrôle de collision avec la plateforme
    if keyboard.space and player.vy == 0:
        player.vy = -10 # On met une vitesse verticale négative pour sauter

    player.y += player.vy
```

````{dropdown} Voir le code à ce point
```python
import pgzero
import pgzrun
from pgzhelper import *

TITLE = 'Platformer'
WIDTH = 800
HEIGHT = 600

GRAVITY = 0.3

platform = Platform('grass_tile', (WIDTH/2, HEIGHT/2))

player = Actor('alien_walk1')
player.x = WIDTH/2
player.y = HEIGHT/2 - 100
player.speed = 3
player.vy = 0

def draw():
    screen.fill('sky blue')
    platform.draw()
    player.draw()

def update():
    player.vy += GRAVITY

    if keyboard.a:
        player.x -= player.speed
        player.flip_x = True
    elif keyboard.d:
        player.x += player.speed
        player.flip_x = False

    platform.check_collision_with_actor(player)

    if keyboard.space and player.vy == 0:
        player.vy = -10

    player.y += player.vy

pgzrun.go()
```
````

## 7. Créer un niveau rempli de plateformes

Bon notre jeu est un peu triste avec une unique plateforme. Il est temps de créer un niveau entier.  
Il existe évidemment plein de manières de s'y prendre. Une solution courante et répandue est de représenter le niveau sous la forme d'un tableau en 2 dimensions où chaque élément du tableau spécifie si une plateforme s'y trouve ou non.

```{image} ../media/platformer_grid.png
```

Pour cela, nous allons définir une variable constante `WORLD_MAP` qui contient une liste de listes (donc un tableau 2D). Un `1` signifie que l'on y place un bloc tandis qu'un `0` signifie que l'on n'y met rien. Je vous propose de reprendre le tableau ci-dessous.

```python
WORLD_MAP = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,1,1,0,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
]
```

Nous devons aussi connaître combien de lignes et de colonnes contient notre tableau. La fonction `len()` en Python retourne la longueur d'une liste. On peut l'utiliser pour calculer les constantes `ROWS` et `COLS` qui stockeront respectivement le nombre de lignes et de colonnes.  
Enfin, définissons également la taille que prendra chacun de nos blocs avec la constante `TILE_SIZE`. Cela nous permettra d'ajuster la taille de notre fenêtre de jeu en multipliant `TILE_SIZE` avec `ROWS` et `COLS`.

```python
WORLD_MAP = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,1,1,0,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
]

TILE_SIZE = 70 # Taille d'un bloc en pixels
ROWS = len(WORLD_MAP) # Nombre de lignes
COLS = len(WORLD_MAP[0]) # Nombre de colonnes

WIDTH = COLS*TILE_SIZE # Largeur de la fenêtre de jeu
HEIGHT = ROWS*TILE_SIZE # Hauteur
```

Bien, il ne reste plus qu'à faire apparaître nos blocs selon les positions données par `WORLD_MAP`. Comme nous aurons plein de plateformes, nous allons les stocker dans une liste `platforms`. Nous allons ensuite parcourir notre tableau, calculer les positions, et faire apparaître un bloc au bon endroit si on trouve un `1` en l'ajoutant à notre liste.

```python
player = Actor('alien_walk1')
player.x = WIDTH/2
player.y = HEIGHT/2 - 100
player.speed = 3
player.vy = 0

platforms = [] # On définit notre liste vide de plateformes
for row in range(ROWS): # On parcourt les lignes du tableau
    for col in range(COLS): # On parcourt les colonnes du tableau
        # Calcul de la position (x, y) du bloc en fonction de la ligne et de la colonne
        pos = (col*TILE_SIZE+TILE_SIZE/2, row*TILE_SIZE+TILE_SIZE/2)
        if WORLD_MAP[row][col] == 1:
            platform = Platform('grass_tile', pos, width=TILE_SIZE)
            platforms.append(platform)
```

Notez que l'on utilise l'argument `width` de l'acteur `Platform` pour lui donner la taille que l'on a définie avec notre constante `TILE_SIZE`.

Comme notre code commence à grandir, nous allons déplacer la logique du joueur dans une fonction `update_player()`. Cela garde la fonction principale `update()` bien plus lisible sans avoir besoin de créer une classe personnalisée.

```python
def update_player():
    player.vy += GRAVITY

    if keyboard.a:
        player.x -= player.speed
        player.flip_x = True
    elif keyboard.d:
        player.x += player.speed
        player.flip_x = False

    for platform in platforms: # On teste les collisions avec toutes nos plateformes
        platform.check_collision_with_actor(player)

    if keyboard.space and player.vy == 0:
        player.vy = -10

    player.y += player.vy

def draw():
    screen.fill('sky blue')
    for platform in platforms: # On dessine toutes nos plateformes
        platform.draw()
    player.draw()

def update():
    update_player()
```

Vous devriez pouvoir à présent librement déplacer votre personnage dans le niveau et sauter sur les blocs.

````{dropdown} Voir le code à ce point
```python
import pgzero
import pgzrun
from pgzhelper import *

TITLE = 'Platformer'

WORLD_MAP = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,1,1,0,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
]

TILE_SIZE = 70
ROWS = len(WORLD_MAP)
COLS = len(WORLD_MAP[0])

WIDTH = COLS*TILE_SIZE
HEIGHT = ROWS*TILE_SIZE

GRAVITY = 0.3

player = Actor('alien_walk1')
player.x = WIDTH/2
player.y = HEIGHT/2 - 100
player.speed = 3
player.vy = 0

platforms = []
for row in range(ROWS):
    for col in range(COLS):
        pos = (col*TILE_SIZE+TILE_SIZE/2, row*TILE_SIZE+TILE_SIZE/2)
        if WORLD_MAP[row][col] == 1:
            platform = Platform('grass_tile', pos, width=TILE_SIZE)
            platforms.append(platform)

def update_player():
    player.vy += GRAVITY

    if keyboard.a:
        player.x -= player.speed
        player.flip_x = True
    elif keyboard.d:
        player.x += player.speed
        player.flip_x = False

    for platform in platforms:
        platform.check_collision_with_actor(player)

    if keyboard.space and player.vy == 0:
        player.vy = -10

    player.y += player.vy

def draw():
    screen.fill('sky blue')
    for platform in platforms:
        platform.draw()
    player.draw()

def update():
    update_player()

pgzrun.go()
```
````

## 8. Différents types de blocs

Pour l'instant, nous avons uniquement des blocs qui servent de plateformes mais que l'on peut traverser librement (par exemple pour sauter dessus depuis dessous). Il peut être utile d'ajouter 2 autres types de blocs:

* Des blocs solides que l'on ne peut pas traverser.
* Des blocs solides que l'on ne peut pas traverser mais auxquels le personnage peut s'accrocher, pour escalader par exemple.

Pour cela, l'acteur `Platform` qui représente un bloc prend 2 arguments logiques supplémentaires: `solid` et `sticky`.  
Un bloc avec `solid = True` ne pourra pas être traversé.  
Un bloc avec `sticky = True` pourra être escaladé.

L'unique différence entre ces blocs se fait au niveau de la méthode `check_collision_with_actor(actor)` et vous n'avez pas à vous préoccuper de comment c'est fait (sauf si vous êtes curieux !).

Voici comment définir un bloc solide:

```python
platform = Platform('grass_tile', pos, solid=True, width=TILE_SIZE)
```

Et un bloc solide que l'on peut escalader:

```python
platform = Platform('grass_tile', pos, solid=True, sticky=True, width=TILE_SIZE)
```

Jouez avec ces 2 nouveaux types de blocs en remplaçant vos blocs d'origine.

````{dropdown} Voir le code à ce point
```python
import pgzero
import pgzrun
from pgzhelper import *

TITLE = 'Platformer'

WORLD_MAP = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,1,1,0,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
]

TILE_SIZE = 70
ROWS = len(WORLD_MAP)
COLS = len(WORLD_MAP[0])

WIDTH = COLS*TILE_SIZE
HEIGHT = ROWS*TILE_SIZE

GRAVITY = 0.3

player = Actor('alien_walk1')
player.x = WIDTH/2
player.y = HEIGHT/2 - 100
player.speed = 3
player.vy = 0

platforms = []
for row in range(ROWS):
    for col in range(COLS):
        pos = (col*TILE_SIZE+TILE_SIZE/2, row*TILE_SIZE+TILE_SIZE/2)
        if WORLD_MAP[row][col] == 1:
            platform = Platform('grass_tile', pos, solid=True, width=TILE_SIZE)
            platforms.append(platform)

def update_player():
    player.vy += GRAVITY

    if keyboard.a:
        player.x -= player.speed
        player.flip_x = True
    elif keyboard.d:
        player.x += player.speed
        player.flip_x = False

    for platform in platforms:
        platform.check_collision_with_actor(player)

    if keyboard.space and player.vy == 0:
        player.vy = -10

    player.y += player.vy

def draw():
    screen.fill('sky blue')
    for platform in platforms:
        platform.draw()
    player.draw()

def update():
    update_player()

pgzrun.go()
```
````

## 9. Remplir le niveau avec différents types de blocs

Voyons à présent une méthode permettant de disposer comme on le souhaite ces différents types de bloc dans notre niveau. Le plus simple est de modifier notre constante `WORLD_MAP`. Nous allons simplement ajouter des `2` pour signifier des blocs solides et des `3` pour signifier des blocs que l'on peut escalader.

```python
WORLD_MAP = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,3,0,0,0,1,1,1,0,0,2,2,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
]
```

Comment prendre en compte ces changements ? Lorsque nous parcourons ce tableau pour créer nos objets `Platform`, nous ajoutons 2 tests de condition pour savoir si l'élément parcouru est `1`, `2` ou `3` et créons le bon bloc en conséquence.

```python
platforms = []
for row in range(ROWS):
    for col in range(COLS):
        pos = (col*TILE_SIZE+TILE_SIZE/2, row*TILE_SIZE+TILE_SIZE/2)
        if WORLD_MAP[row][col] == 1: # Bloc classique traversable
            platform = Platform('grass_tile', pos, width=TILE_SIZE)
            platforms.append(platform)
        elif WORLD_MAP[row][col] == 2: # Bloc solide mais que l'on ne peut pas escalader
            platform = Platform('grass_tile', pos, solid=True, width=TILE_SIZE)
            platforms.append(platform)
        elif WORLD_MAP[row][col] == 3: # Bloc solide que l'on peut escalader
            platform = Platform('grass_tile', pos, solid=True, sticky=True, width=TILE_SIZE)
            platforms.append(platform)
```

Lancez le jeu pour tester que les bons types de blocs se trouvent bien au bon endroit.

````{dropdown} Voir le code à ce point
```python
import pgzero
import pgzrun
from pgzhelper import *

TITLE = 'Platformer'

WORLD_MAP = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,3,0,0,0,1,1,1,0,0,2,2,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
]

TILE_SIZE = 70
ROWS = len(WORLD_MAP)
COLS = len(WORLD_MAP[0])

WIDTH = COLS*TILE_SIZE
HEIGHT = ROWS*TILE_SIZE

GRAVITY = 0.3

player = Actor('alien_walk1')
player.x = WIDTH/2
player.y = HEIGHT/2 - 100
player.speed = 3
player.vy = 0

platforms = []
for row in range(ROWS):
    for col in range(COLS):
        pos = (col*TILE_SIZE+TILE_SIZE/2, row*TILE_SIZE+TILE_SIZE/2)
        if WORLD_MAP[row][col] == 1:
            platform = Platform('grass_tile', pos, width=TILE_SIZE)
            platforms.append(platform)
        elif WORLD_MAP[row][col] == 2:
            platform = Platform('grass_tile', pos, solid=True, width=TILE_SIZE)
            platforms.append(platform)
        elif WORLD_MAP[row][col] == 3:
            platform = Platform('grass_tile', pos, solid=True, sticky=True, width=TILE_SIZE)
            platforms.append(platform)

def update_player():
    player.vy += GRAVITY

    if keyboard.a:
        player.x -= player.speed
        player.flip_x = True
    elif keyboard.d:
        player.x += player.speed
        player.flip_x = False

    for platform in platforms:
        platform.check_collision_with_actor(player)

    if keyboard.space and player.vy == 0:
        player.vy = -10

    player.y += player.vy

def draw():
    screen.fill('sky blue')
    for platform in platforms:
        platform.draw()
    player.draw()

def update():
    update_player()

pgzrun.go()
```
````

## 10. Ajouter un ennemi qui se balade

Notre personnage se sent un peu seul dans son niveau. Pourquoi ne pas ajouter un slime qui se balade de gauche à droite sur les blocs ?

```{image} ../media/platformer_slime.png
```

Comme pour le joueur, nous allons utiliser directement `Actor`. Il suffit de créer l'acteur puis de lui ajouter les attributs dont on a besoin.

```python
slime = Actor('slime_green1', pos)
slime.images = ['slime_green1', 'slime_green2']
slime.vy = 0
slime.speed = 2
```

Pour son emplacement, je vous propose de l'ajouter à notre constante `WORLD_MAP` avec le numéro `4`.

```python
WORLD_MAP = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,4,0,0,0,0,0],
    [0,0,0,3,0,0,0,1,1,1,0,0,2,2,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
]
```

Nous devons donc créer une liste `slimes = []` et la remplir comme pour les plateformes.  
N'oublions finalement pas de mettre à jour les fonctions principales `draw` et `update`.

```python
platforms = []
slimes = [] # Création de la liste vide
for row in range(ROWS):
    for col in range(COLS):
        pos = (col*TILE_SIZE+TILE_SIZE/2, row*TILE_SIZE+TILE_SIZE/2)
        if WORLD_MAP[row][col] == 1:
            platform = Platform('grass_tile', pos, width=TILE_SIZE)
            platforms.append(platform)
        elif WORLD_MAP[row][col] == 2:
            platform = Platform('grass_tile', pos, solid=True, width=TILE_SIZE)
            platforms.append(platform)
        elif WORLD_MAP[row][col] == 3:
            platform = Platform('grass_tile', pos, solid=True, sticky=True, width=TILE_SIZE)
            platforms.append(platform)
        elif WORLD_MAP[row][col] == 4:
            slime = Actor('slime_green1', pos)
            slime.images = ['slime_green1', 'slime_green2']
            slime.vy = 0
            slime.speed = 2
            slimes.append(slime)

def draw():
    screen.fill('sky blue')
    player.draw()
    for slime in slimes:
        slime.draw()
    for platform in platforms:
        platform.draw()

def update():
    update_player()
    for slime in slimes:
        pass # Nous allons ajouter la logique juste après
```

Occupons-nous à présent d'une fonction `update_slime(slime)` afin qu'il puisse se déplacer. Nous allons simplement le faire se déplacer vers la droite selon sa vitesse (`speed`). Nous allons également lui appliquer la gravité et contrôler sa collision avec les blocs de la même manière qu'on l'a fait pour notre joueur.

```python
def update_slime(slime):
    slime.vy += GRAVITY # On augmente sa vitesse verticale avec la gravité

    for platform in platforms: # On teste sa collision avec chaque bloc
        platform.check_collision_with_actor(slime)

    slime.x += slime.speed # On met à jour sa position en x
    slime.y += slime.vy # On met à jour sa position en y
```

Testez votre jeu ! Le slime devrait à présent tomber de sa position initiale puis se déplacer vers la droite à l'infini.  
Il serait intéressant de faire en sorte que notre slime reste dans une zone choisie et qu'il se retourne lorsqu'il dépasse cette zone.

Pour cela, nous allons simplement ajouter deux attributs à notre acteur: `max_distance_x` pour la distance maximale autorisée, et `distance_x` pour la distance déjà parcourue.

```python
slime = Actor('slime_green1', pos)
slime.images = ['slime_green1', 'slime_green2']
slime.vy = 0
slime.speed = 2
slime.max_distance_x = 300
slime.distance_x = 0
```

Enfin, il ne reste plus qu'à mettre à jour la fonction `update_slime` pour augmenter `distance_x` à chaque déplacement et contrôler si `0 <= distance_x <= max_distance_x` pour savoir si notre ami est toujours dans sa zone. Si ce n'est pas le cas, on inverse sa vitesse `speed` pour qu'il reparte dans l'autre sens et on change l'orientation de son sprite (`flip_x`).

```python
def update_slime(slime):
    slime.vy += GRAVITY

    for platform in platforms:
        platform.check_collision_with_actor(slime)

    slime.x += slime.speed
    slime.y += slime.vy
    slime.distance_x += slime.speed # On met à jour sa distance parcourue

    if not (0 <= slime.distance_x <= slime.max_distance_x): # S'il sort de sa zone
        slime.flip_x = not slime.flip_x # On inverse l'orientation de son sprite
        slime.speed = -slime.speed # On inverse sa vitesse horizontale
```

Et voilà ! Votre ami le slime devrait à présent se cantonner à sa zone. Nous ne nous préoccupons pas de sa collision avec le joueur dans ce tutoriel, revoyez le tutoriel précédent pour voir comment ajouter ce comportement.

````{dropdown} Voir le code à ce point
```python
import pgzero
import pgzrun
from pgzhelper import *

TITLE = 'Platformer'

WORLD_MAP = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,4,0,0,0,0,0],
    [0,0,0,3,0,0,0,1,1,1,0,0,2,2,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
]

TILE_SIZE = 70
ROWS = len(WORLD_MAP)
COLS = len(WORLD_MAP[0])

WIDTH = COLS*TILE_SIZE
HEIGHT = ROWS*TILE_SIZE

GRAVITY = 0.3

player = Actor('alien_walk1')
player.x = WIDTH/2
player.y = HEIGHT/2 - 100
player.speed = 3
player.vy = 0

platforms = []
slimes = []
for row in range(ROWS):
    for col in range(COLS):
        pos = (col*TILE_SIZE+TILE_SIZE/2, row*TILE_SIZE+TILE_SIZE/2)
        if WORLD_MAP[row][col] == 1:
            platform = Platform('grass_tile', pos, width=TILE_SIZE)
            platforms.append(platform)
        elif WORLD_MAP[row][col] == 2:
            platform = Platform('grass_tile', pos, solid=True, width=TILE_SIZE)
            platforms.append(platform)
        elif WORLD_MAP[row][col] == 3:
            platform = Platform('grass_tile', pos, solid=True, sticky=True, width=TILE_SIZE)
            platforms.append(platform)
        elif WORLD_MAP[row][col] == 4:
            slime = Actor('slime_green1', pos)
            slime.images = ['slime_green1', 'slime_green2']
            slime.vy = 0
            slime.speed = 2
            slime.max_distance_x = 300
            slime.distance_x = 0
            slimes.append(slime)

def update_player():
    player.vy += GRAVITY

    if keyboard.a:
        player.x -= player.speed
        player.flip_x = True
    elif keyboard.d:
        player.x += player.speed
        player.flip_x = False

    for platform in platforms:
        platform.check_collision_with_actor(player)

    if keyboard.space and player.vy == 0:
        player.vy = -10

    player.y += player.vy

def update_slime(slime):
    slime.vy += GRAVITY

    for platform in platforms:
        platform.check_collision_with_actor(slime)

    slime.x += slime.speed
    slime.y += slime.vy
    slime.distance_x += slime.speed

    if not (0 <= slime.distance_x <= slime.max_distance_x):
        slime.flip_x = not slime.flip_x
        slime.speed = -slime.speed

def draw():
    screen.fill('sky blue')
    player.draw()
    for slime in slimes:
        slime.draw()
    for platform in platforms:
        platform.draw()

def update():
    update_player()
    for slime in slimes:
        update_slime(slime)

pgzrun.go()
```
````

## 11. Ajouter des objets à ramasser

Nous n'avons aucun objectif dans le jeu ! Il serait bien d'ajouter des objets à ramasser pour le joueur. Pourquoi pas des pièces ? C'est très classique mais ça fonctionne toujours.

```{image} ../media/platformer_coin.png
```

Ici encore, pas besoin de créer une classe. Une pièce peut être représentée par un simple `Actor`.

```python
coin = Actor('coin', pos)
```

Pour choisir l'emplacement de nos pièces, le plus simple est de passer par notre constante `WORLD_MAP`. Nous pouvons utiliser la valeur `5` pour représenter une pièce.

```python
WORLD_MAP = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,5,0,0,0,0,0,4,0,0,0,5,0],
    [0,0,0,3,0,0,0,1,1,1,0,0,2,2,0],
    [0,0,0,0,0,0,0,0,0,0,5,5,0,0,0],
    [1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
]
```

Modifions à présent notre parcours du tableau pour créer les acteurs `coin` au bon endroit. Nous devons aussi créer une liste `coins` pour nos pièces, comme nous l'avons fait pour nos plateformes. Finalement, n'oublions pas d'adapter les fonctions principales `draw` et `update` pour afficher les pièces de notre liste.

```python
platforms = []
slimes = []
coins = [] # Création de la liste vide
for row in range(ROWS):
    for col in range(COLS):
        pos = (col*TILE_SIZE+TILE_SIZE/2, row*TILE_SIZE+TILE_SIZE/2)
        if WORLD_MAP[row][col] == 1:
            platform = Platform('grass_tile', pos, width=TILE_SIZE)
            platforms.append(platform)
        elif WORLD_MAP[row][col] == 2:
            platform = Platform('grass_tile', pos, solid=True, width=TILE_SIZE)
            platforms.append(platform)
        elif WORLD_MAP[row][col] == 3:
            platform = Platform('grass_tile', pos, solid=True, sticky=True, width=TILE_SIZE)
            platforms.append(platform)
        elif WORLD_MAP[row][col] == 4:
            slime = Actor('slime_green1', pos)
            slime.images = ['slime_green1', 'slime_green2']
            slime.vy = 0
            slime.speed = 2
            slime.max_distance_x = 300
            slime.distance_x = 0
            slimes.append(slime)
        elif WORLD_MAP[row][col] == 5: # Création d'une pièce
            coin = Actor('coin', pos)
            coins.append(coin)

def draw():
    screen.fill('sky blue')
    player.draw()
    for slime in slimes:
        slime.draw()
    for platform in platforms:
        platform.draw()
    for coin in coins:
        coin.draw()

def update():
    update_player()
    for slime in slimes:
        update_slime(slime)
    for coin in coins:
        pass # Nous allons ajouter la logique juste après
```

Reste à savoir de quelle manière gérer les collisions avec le joueur. Il y a 2 possibilités:

* Ajouter le test de collision avec une pièce dans `update_player()`.
* Ajouter le test de collision avec le joueur dans une fonction `update_coin(coin)`.

Je vous propose la 2ème solution, qui a pour avantage de ne pas alourdir `update_player()`.  
Il suffit alors de tester s'il y a collision avec le `player` et, le cas échéant, marquer le `coin` pour qu'il soit supprimé.

```python
def update_coin(coin):
    if player.collides_with(coin): # Test de collision avec le joueur
        coins.remove(coin) # On supprime la pièce de la liste pour qu'elle disparaisse du jeu

def update():
    update_player()
    for slime in slimes:
        update_slime(slime)
    for coin in coins:
        update_coin(coin) # Chaque pièce teste si elle est en collision avec le player
```

Testez le jeu et ramassez les pièces pour voir si tout fonctionne. Pour le moment, ramasser des pièces n'apporte rien au joueur, vous serez libre d'ajouter cette fonctionnalité par vous-même.

````{dropdown} Voir le code à ce point
```python
import pgzero
import pgzrun
from pgzhelper import *

TITLE = 'Platformer'

WORLD_MAP = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,5,0,0,0,0,0,4,0,0,0,5,0],
    [0,0,0,3,0,0,0,1,1,1,0,0,2,2,0],
    [0,0,0,0,0,0,0,0,0,0,5,5,0,0,0],
    [1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
]

TILE_SIZE = 70
ROWS = len(WORLD_MAP)
COLS = len(WORLD_MAP[0])

WIDTH = COLS*TILE_SIZE
HEIGHT = ROWS*TILE_SIZE

GRAVITY = 0.3

player = Actor('alien_walk1')
player.x = WIDTH/2
player.y = HEIGHT/2 - 100
player.speed = 3
player.vy = 0

platforms = []
slimes = []
coins = []
for row in range(ROWS):
    for col in range(COLS):
        pos = (col*TILE_SIZE+TILE_SIZE/2, row*TILE_SIZE+TILE_SIZE/2)
        if WORLD_MAP[row][col] == 1:
            platform = Platform('grass_tile', pos, width=TILE_SIZE)
            platforms.append(platform)
        elif WORLD_MAP[row][col] == 2:
            platform = Platform('grass_tile', pos, solid=True, width=TILE_SIZE)
            platforms.append(platform)
        elif WORLD_MAP[row][col] == 3:
            platform = Platform('grass_tile', pos, solid=True, sticky=True, width=TILE_SIZE)
            platforms.append(platform)
        elif WORLD_MAP[row][col] == 4:
            slime = Actor('slime_green1', pos)
            slime.images = ['slime_green1', 'slime_green2']
            slime.vy = 0
            slime.speed = 2
            slime.max_distance_x = 300
            slime.distance_x = 0
            slimes.append(slime)
        elif WORLD_MAP[row][col] == 5:
            coin = Actor('coin', pos)
            coins.append(coin)

def update_player():
    player.vy += GRAVITY

    if keyboard.a:
        player.x -= player.speed
        player.flip_x = True
    elif keyboard.d:
        player.x += player.speed
        player.flip_x = False

    for platform in platforms:
        platform.check_collision_with_actor(player)

    if keyboard.space and player.vy == 0:
        player.vy = -10

    player.y += player.vy

def update_slime(slime):
    slime.vy += GRAVITY

    for platform in platforms:
        platform.check_collision_with_actor(slime)

    slime.x += slime.speed
    slime.y += slime.vy
    slime.distance_x += slime.speed

    if not (0 <= slime.distance_x <= slime.max_distance_x):
        slime.flip_x = not slime.flip_x
        slime.speed = -slime.speed

def update_coin(coin):
    if player.collides_with(coin):
        coins.remove(coin)

def draw():
    screen.fill('sky blue')
    player.draw()
    for slime in slimes:
        slime.draw()
    for platform in platforms:
        platform.draw()
    for coin in coins:
        coin.draw()

def update():
    update_player()
    for slime in slimes:
        update_slime(slime)
    for coin in coins[:]:
        update_coin(coin)

pgzrun.go()
```
````

## 12. Changer de niveau

Notre jeu ne comporte qu'un seul niveau, il est temps que cela change ! Nous allons ajouter un portail permettant de passer à un second niveau.

Comme pour les pièces, un portail peut être représenté par un simple `Actor`. Je propose d'utiliser le numéro `6` dans `WORLD_MAP` pour le représenter. Afin de garder la même structure que pour les blocs et les pièces, nous allons stocker nos portails dans une liste `portals`.

```python
WORLD_MAP = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,5,0,0,0,0,6,4,0,0,0,5,0],
    [0,0,0,3,0,0,0,1,1,1,0,0,2,2,0],
    [0,0,0,0,0,0,0,0,0,0,5,5,0,0,0],
    [1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
]
```

```python
platforms = []
slimes = []
coins = []
portals = [] # On crée la liste vide pour les portails
for row in range(ROWS):
    for col in range(COLS):
        pos = (col*TILE_SIZE+TILE_SIZE/2, row*TILE_SIZE+TILE_SIZE/2)
        if WORLD_MAP[row][col] == 1:
            platform = Platform('grass_tile', pos, width=TILE_SIZE)
            platforms.append(platform)
        elif WORLD_MAP[row][col] == 2:
            platform = Platform('grass_tile', pos, solid=True, width=TILE_SIZE)
            platforms.append(platform)
        elif WORLD_MAP[row][col] == 3:
            platform = Platform('grass_tile', pos, solid=True, sticky=True, width=TILE_SIZE)
            platforms.append(platform)
        elif WORLD_MAP[row][col] == 4:
            slime = Actor('slime_green1', pos)
            slime.images = ['slime_green1', 'slime_green2']
            slime.vy = 0
            slime.speed = 2
            slime.max_distance_x = 300
            slime.distance_x = 0
            slimes.append(slime)
        elif WORLD_MAP[row][col] == 5:
            coin = Actor('coin', pos)
            coins.append(coin)
        elif WORLD_MAP[row][col] == 6: # On crée un portail et on l'ajoute à la liste
            portal = Actor('portal', pos)
            portals.append(portal)

def draw():
    screen.fill('sky blue')
    player.draw()
    for slime in slimes:
        slime.draw()
    for platform in platforms:
        platform.draw()
    for coin in coins:
        coin.draw()
    for portal in portals:
        portal.draw()

def update():
    update_player()
    for slime in slimes:
        update_slime(slime)
    for coin in coins:
        update_coin(coin)
    for portal in portals:
        pass # Nous allons ajouter la logique juste après

    remove_actors(coins)
```

Vous devriez voir le portail apparaître à l'endroit indiqué. Voyons à présent comment modifier le niveau lorsque le joueur est en contact avec le portail et qu'il appuie sur la touche `e`. On va commencer par écrire une fonction `update_portal(portal)` pour qu'il puisse détecter cet événement. Pour le moment, affichons simplement l'activation du niveau 2 sous forme de texte dans la console avec `print`.

```python
def update_portal(portal):
    if player.collides_with(portal) and keyboard.e:
        print('Niveau 2 !')
```

Une manière de changer de niveau est de simplement créer une autre constante `WORLD_MAP_2` et recréer toutes les plateformes en conséquence.

```python
WORLD_MAP = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,5,0,0,0,0,6,4,0,0,0,5,0],
    [0,0,0,3,0,0,0,1,1,1,0,0,2,2,0],
    [0,0,0,0,0,0,0,0,0,0,5,5,0,0,0],
    [1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
]

WORLD_MAP_2 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,5,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
    [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,4,0,0,0,1,1,5,1,0,0,0,0,0,0],
    [5,5,5,0,0,0,0,0,0,4,0,0,0,5,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
```

Définissons ensuite une fonction `load_level(world_map)` qui va s'occuper de créer tous les objets du jeu en fonction de la `world_map` qu'on lui passe et qui les **retourne** au programme principal. Donc l'idée est simplement de déplacer tout notre code qui remplit les listes d'objets dans une fonction. On part du principe que tous les niveaux vont contenir autant de lignes et de colonnes.

```python
def create_slime(pos):
    slime = Actor('slime_green1', pos)
    slime.images = ['slime_green1', 'slime_green2']
    slime.vy = 0
    slime.speed = 2
    slime.max_distance_x = 300
    slime.distance_x = 0
    return slime

def load_level(world_map):
    platforms = []
    slimes = []
    coins = []
    portals = []
    for row in range(ROWS):
        for col in range(COLS):
            pos = (col*TILE_SIZE+TILE_SIZE/2, row*TILE_SIZE+TILE_SIZE/2)
            if world_map[row][col] == 1:
                platform = Platform('grass_tile', pos, width=TILE_SIZE)
                platforms.append(platform)
            elif world_map[row][col] == 2:
                platform = Platform('grass_tile', pos, solid=True, width=TILE_SIZE)
                platforms.append(platform)
            elif world_map[row][col] == 3:
                platform = Platform('grass_tile', pos, solid=True, sticky=True, width=TILE_SIZE)
                platforms.append(platform)
            elif world_map[row][col] == 4:
                slimes.append(create_slime(pos))
            elif world_map[row][col] == 5:
                coin = Actor('coin', pos)
                coins.append(coin)
            elif world_map[row][col] == 6:
                portal = Actor('portal', pos)
                portals.append(portal)

    return platforms, slimes, coins, portals

player = Actor('alien_walk1')
player.x = 100
player.y = 100
player.speed = 3
player.vy = 0

# Appel de notre fonction pour remplir toutes les listes
platforms, slimes, coins, portals = load_level(WORLD_MAP)
```

Si tout a fonctionné, vous ne devriez voir aucun changement par rapport à tout à l'heure, on a simplement déplacé du code, mais il fait la même chose.  
Il ne reste plus à présent qu'à appeler la fonction `load_level` lorsque l'on passe le portail mais en lui passant `WORLD_MAP_2` ! Cependant, comme nous souhaitons ici **modifier** les listes des objets (`platforms`, `coins`, etc) depuis une fonction, nous devons déclarer ces variables `global` avant de pouvoir les toucher.

```python
def update_portal(portal):
    if player.collides_with(portal) and keyboard.e:
        print('Niveau 2 !')
        global platforms # On déclare les variables externes que l'on veut modifier comme globales
        global slimes
        global coins
        global portals
        platforms, slimes, coins, portals = load_level(WORLD_MAP_2) # On met à jour les listes grâce à notre fonction
```

Et voilà ! Testez si tout fonctionne comme souhaité !  
Vous avez remarqué ? Notre portail ressemble plutôt à une serrure... Et si vous faisiez en sorte qu'il faille d'abord ramasser une clé cachée dans le niveau afin de pouvoir traverser le portail ?

````{dropdown} Voir le code à ce point
```python
import pgzero
import pgzrun
from pgzhelper import *

TITLE = 'Mon premier platformer'

WORLD_MAP = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,5,0,0,0,0,6,4,0,0,0,5,0],
    [0,0,0,3,0,0,0,1,1,1,0,0,2,2,0],
    [0,0,0,0,0,0,0,0,0,0,5,5,0,0,0],
    [1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
]

WORLD_MAP_2 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,5,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
    [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,4,0,0,0,1,1,5,1,0,0,0,0,0,0],
    [5,5,5,0,0,0,0,0,0,4,0,0,0,5,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

TILE_SIZE = 70
ROWS = len(WORLD_MAP)
COLS = len(WORLD_MAP[0])

WIDTH = COLS*TILE_SIZE
HEIGHT = ROWS*TILE_SIZE

GRAVITY = 0.3

def create_slime(pos):
    slime = Actor('slime_green1', pos)
    slime.images = ['slime_green1', 'slime_green2']
    slime.vy = 0
    slime.speed = 2
    slime.max_distance_x = 300
    slime.distance_x = 0
    return slime

def load_level(world_map):
    platforms = []
    slimes = []
    coins = []
    portals = []
    for row in range(ROWS):
        for col in range(COLS):
            pos = (col*TILE_SIZE+TILE_SIZE/2, row*TILE_SIZE+TILE_SIZE/2)
            if world_map[row][col] == 1:
                platform = Platform('grass_tile', pos, width=TILE_SIZE)
                platforms.append(platform)
            elif world_map[row][col] == 2:
                platform = Platform('grass_tile', pos, solid=True, width=TILE_SIZE)
                platforms.append(platform)
            elif world_map[row][col] == 3:
                platform = Platform('grass_tile', pos, solid=True, sticky=True, width=TILE_SIZE)
                platforms.append(platform)
            elif world_map[row][col] == 4:
                slimes.append(create_slime(pos))
            elif world_map[row][col] == 5:
                coin = Actor('coin', pos)
                coins.append(coin)
            elif world_map[row][col] == 6:
                portal = Actor('portal', pos)
                portals.append(portal)

    return platforms, slimes, coins, portals

player = Actor('alien_walk1')
player.x = 100
player.y = 100
player.speed = 3
player.vy = 0

platforms, slimes, coins, portals = load_level(WORLD_MAP)

def update_player():
    player.vy += GRAVITY

    if keyboard.a:
        player.x -= player.speed
        player.flip_x = True
    elif keyboard.d:
        player.x += player.speed
        player.flip_x = False

    for platform in platforms:
        platform.check_collision_with_actor(player)

    if keyboard.space and player.vy == 0:
        player.vy = -10

    player.y += player.vy

def update_slime(slime):
    slime.vy += GRAVITY

    for platform in platforms:
        platform.check_collision_with_actor(slime)

    slime.x += slime.speed
    slime.y += slime.vy
    slime.distance_x += slime.speed

    if not (0 <= slime.distance_x <= slime.max_distance_x):
        slime.flip_x = not slime.flip_x
        slime.speed = -slime.speed

def update_coin(coin):
    if player.collides_with(coin):
        coins.remove(coin)

def update_portal(portal):
    if player.collides_with(portal) and keyboard.e:
        print('Niveau 2 !')
        global platforms
        global slimes
        global coins
        global portals
        platforms, slimes, coins, portals = load_level(WORLD_MAP_2)

def draw():
    screen.fill('sky blue')
    player.draw()
    for slime in slimes:
        slime.draw()
    for platform in platforms:
        platform.draw()
    for coin in coins:
        coin.draw()
    for portal in portals:
        portal.draw()

def update():
    update_player()
    for slime in slimes:
        update_slime(slime)
    for coin in coins:
        update_coin(coin)
    for portal in portals:
        update_portal(portal)

pgzrun.go()
```
````

## 13. Idées d'améliorations

Voici plusieurs idées d'amélioration du jeu.  
Vous pouvez bien sûr me proposer d'autres idées et je vous dirai leur difficulté.

**Totalement dans vos cordes (facile):**

* Ajouter une animation au joueur quand il se déplace.
* Ajouter une musique de fond.
* Ajouter des bruitages (par exemple pour le saut ou les pièces).
* Empêcher le joueur de sortir de l'écran à gauche et droite.
* Faire en sorte que le joueur perde de la vie à chaque contact avec un ennemi.
* Créer un game over sous les conditions de votre choix (par exemple au contact d'un ennemi ou après un certain temps). Cela affiche par exemple un écran noir avec écrit "Game Over" en grand.
* Ajouter un compteur de pièces pour le score.
* Ajouter un 3ème niveau.
* Permettre de mettre le jeu en pause avec la touche espace.

**Un peu plus complexe (moyen):**

* Ajouter une clé dans le niveau nécessaire au déblocage du portail vers le prochain niveau.
* Permettre au joueur de tirer des projectiles soumis à la gravité pour détruire les slimes (ex: flèches).
* Permettre au joueur de sauter sur les ennemis pour les détruire.
* Permettre au joueur de faire des doubles sauts.
* Ajouter un nouveau type d'ennemi (ex: qui peut sauter).
* Faire en sorte que les ennemis suivent le joueur s'il est suffisamment proche au lieu de se balader aléatoirement.
* Faire en sorte qu'en cas de contact avec un ennemi, le joueur perd de la vie et l'ennemi meurt. La vie du joueur est affichée sous le score.
* Créer un nouveau type de bloc qui peut tuer le joueur au contact (ex: lave).

**Challenging (difficile):**

* Permettre au joueur de poser des bombes pour détruire certains blocs.
* Ajouter un système d'interrupteur à activer pour détruire des blocs et donc ouvrir des passages.
* Ajouter un second joueur pour pouvoir faire une course aux pièces (celui qui en ramasse le plus gagne).
* Ajouter un item qui permet au joueur de voler pendant un temps limité.
* Permettre la création de niveaux bien plus grands que la fenêtre de jeu principale qui défileront ensuite avec le déplacement du joueur. Indice: déplacez tous les acteurs du jeu dans la direction inverse au déplacement du joueur.
* Créer un menu avant le début du jeu qui permet de choisir la difficulté ou d'autres options.
