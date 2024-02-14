# 1. Création d'un jeu de plateformes

Dans ce tutoriel, nous allons développer un jeu de plateforme où le personnage peut se déplacer sur des blocs pour attraper des objets et combattre des ennemis. Nous allons également devoir un système de gravité pour permettre au joueur de sauter et de tomber des blocs.

```{image} ../media/hit_the_fly.gif
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
    pass # Notre acteur platform n'a pas de fonction update à appeler, il doit juste s'afficher
```

```{image} ../media/platformer_bloc.png
```

## 2. Faire apparaître notre joueur

Faisons à présent apparaître notre personnage au-dessus de ce bloc. Comme pour le jeu précédent, nous allons implémenter une classe `Player` qui va représenter notre joueur.

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)

    def update(self):
        pass # Ne fait rien pour le moment
```

Nous allons ensuite pouvoir le créer dans le programme principal et appeler sa méthode `draw` et `update` dans les fonctions principales du même nom. On place notre joueur de telle sorte à ce qu'il se trouve juste un peu au dessus de notre bloc.

```python
player = Player('alien_walk1', (WIDTH/2, HEIGHT/2-100))

def draw():
    screen.fill('sky blue')
    platform.draw()
    player.draw()

def update():
    player.update() # Ne fait rien pour le moment
```

```{image} ../media/platformer_bloc_joueur.png
```

## 3. Déplacer le joueur horiontalement

Commençons de manière simple par implémenter les déplacements horizontaux de notre personnage avec les touches `a` et `d`.  
Comme pour le jeu précédent, nous allons définir une vitesse pour notre personnage (ex: `speed = 3`).

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.speed = 3

    def update(self):
        pass # Ne fait rien pour le moment
```

La logique du déplacement doit être codée dans la méthode `update`. Il suffit de vérifier si la touche `a` ou `d` est enfoncée et si c'est le cas, mettre à jour la position `x` du joueur en tenant compte de sa vitesse. On en profite également pour retourner l'image si le déplacement se fait vers la gauche.

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.speed = 3

    def update(self):
        if keyboard.a:
            self.x -= self.speed
            self.flip_x = True
        elif keyboard.d:
            self.x += self.speed
            self.flip_x = False
```

Et voilà ! Vous devriez voir votre personnage flotter de gauche à droite de l'écran au-dessus du bloc.

## 4. Ajouter la gravité

L'heure est grave, notre personnage flotte sans jamais tomber ! Repensons à notre ami Newton... la gravité est une accélération vers le bas. La vitesse verticale de notre personnage doit donc augmenter avec le temps.

La première chose à faire est de fixer notre constante de gravité à l'aide d'une variable. Elle vaut 9.81 m/s^2 sur Terre mais cela serait trop pour notre petit jeu. Fixons-la à 0.3 pour le moment. Il nous faut aussi déclarer une vitesse verticale `vy` pour notre personnage, qui est nulle par défaut.

```python
GRAVITY = 0.3 # Une constante s'écrit en majuscule par convention

class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.vy = 0 # vitesse verticale du personnage
        self.speed = 3
```

Bien, à présent il nous faut ajouter cette accélération à la vitesse verticale `vy` de notre personnage à chaque `tick` du jeu et faire évoluer sa position verticale `y`. Tout ceci se passe dans la méthode `update` de la classe `Player`.

```python
def update(self):
    self.vy += GRAVITY # Augmente la vitesse verticale du joueur

    if keyboard.a:
        self.x -= self.speed
        self.flip_x = True
    elif keyboard.d:
        self.x += self.speed
        self.flip_x = False

    self.y += self.vy # Met à jour la position verticale du joueur
```

Vous devriez à présent pouvoir voir votre personnage chuter dès le début du jeu (et tomber à travers notre platforme).

## 5. Se poser sur une plateforme

Il faut maintenant s'occuper de faire tenir notre personnage sur le bloc afin de l'empêcher de passer au travers. En temps normal, c'est une implémentation difficile car il y a beaucoup de petits détails à prendre en compte mais je vous ai un peu facilité le travail. Notre acteur `Plateform` contient une méthode qui permet de gérer les collisions avec les autres acteurs: `check_collision_with(actor)`.  
Il nous suffit de l'appeler dans la méthode `update` de notre joueur pour l'empêcher de passer au travers.

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.vy = 0
        self.speed = 3

    def update(self):
        self.vy += GRAVITY
        
        if keyboard.a:
            self.x -= self.speed
            self.flip_x = True
        elif keyboard.d:
            self.x += self.speed
            self.flip_x = False
            
        platform.check_collision_with_actor(self) # S'occupe automatiquement de gérer la collision
            
        self.y += self.vy
```

Je vous invite à aller jeter un oeil à l'implémentation de cette méthode dans le fichier `pgzhelper.py`.

## 6. Permettre au personnage de sauter

Un jeu de plateforme n'en est pas un si notre personnage ne peut pas sauter ! Nous allons le faire avec la touche espace (`space`) du clavier.  
Quand on y pense, faire sauter notre personnage revient à modifier sa vitesse verticale. En la rendant négative, le personnage se déplace vers le haut jusqu'à ce que la gravité vienne compenser l'action du saut et le fasse tomber à nouveau.

Il suffit donc d'ajouter 2 lignes de code à la méthode `update` où l'on vérifie si la touche `space` est enfoncée. Si c'est le cas, on modifie la vitesse verticale `vy` de notre personnage (ex: `vy = -10`).

```{admonition}
:class: warning
Attention, il faut également que le personnage se trouve sur une plateforme pour pouvoir sauter ! Cela se vérifie si la vitesse verticale de notre personange est nulle au moment du saut ! (`vy == 0`)
```

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.vy = 0
        self.speed = 3

    def update(self):
        self.vy += GRAVITY
        
        if keyboard.a:
            self.x -= self.speed
            self.flip_x = True
        elif keyboard.d:
            self.x += self.speed
            self.flip_x = False

        platform.check_collision_with_actor(self)
            
        # Il est important que ce test se fasse après le contrôle de collision avec la platforme
        if keyboard.space and self.vy == 0:
            self.vy = -10 # On met une vitesse verticale négative pour sauter
            
        self.y += self.vy
```

## 7. Créer un niveau rempli de plateformes

Bon notre jeu est un peu triste avec une unique plateforme. Il est temps de créer un niveau entier.  
Il existe évidemment plein de manières de s'y prendre. Une solution courante et répendue est de représenter le niveau sous la forme d'un tableau en 2 dimensions où chaque élément du tableau spécifie si une plateforme s'y trouve ou non.

Pour cela, nous allons définir une variable constante `WORLD_MAP` qui contient une liste de listes (donc un tableau 2D). Un `1` signifie que l'on y place un bloc tandis qu'un `0` signifie que l'on y met rien. Je vous propose de reprendre le tableau ci-dessous.

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

Nous devons aussi connaître combien de lignes et de colonnes contient notre tableau. La fonction `len()` en python retourne la longueur d'une liste. On peut l'utiliser pour calculer les constantes `ROWS` et `COLS` qui stockeront respectivement le nombre de lignes et de colonnes.  
Enfin, définissons également la taille que prendra chacun de nos blocs avec la constante `TILE_SIZE`. Cela nous permettra d'ajuter la taille de notre fenêtre de jeu en multipliant `TILE_SIZE` avec `ROWS` et `COLS`.

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

Bien, il ne reste plus qu'à faire apparaître nos blocs selon les positions données par `WORLD_MAP`. Comme nous aurons plein de plateformes, nous allons les stocker dans une liste `plateformes`. Nous allons ensuite parcourir notre tableau, calculer les positions, et faire apparaître un bloc au bon endroit si on trouve un `1` en l'ajoutant à notre liste.

```python
player = Player('alien_walk1', (WIDTH/2, HEIGHT/2-100))

platforms = [] #On définit notre liste vide de plateformes
for row in range(ROWS): # On parcourt les lignes du tableau
    for col in range(COLS): # On parcourt les colonnes du tableau
        pos = (col*TILE_SIZE, row*TILE_SIZE) # On calcule la position en fonction de la ligne et de la colonne du tableau
        if WORLD_MAP[row][col] == 1:
            platform = Platform('grass_tile', pos, width=TILE_SIZE)
            platforms.append(platform)
```

Notez que l'on utilise l'argument `width` de l'acteur `Platform` pour lui donner la taille que l'on a définit avec notre constante `TILE_SIZE`.

Il ne reste à présent plus qu'à modifier notre code pour afficher toutes les plateformes de notre liste ainsi que faire le contrôle de collision de notre joueur avec toutes les plateformes également.

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.vy = 0
        self.speed = 3

    def update(self):
        self.vy += GRAVITY
        
        if keyboard.a:
            self.x -= self.speed
            self.flip_x = True
        elif keyboard.d:
            self.x += self.speed
            self.flip_x = False
            
        for platform in platforms: # On teste les collisions avec toutes nos plateformes
            platform.check_collision_with_actor(self)
            
        if keyboard.space and self.vy == 0:
            self.vy = -10
            
        self.y += self.vy

# ...

def draw():
    screen.fill('sky blue')
    for platform in platforms: # On dessine toutes nos plateformes
        platform.draw()
    player.draw()
```

Vous devriez pouvoir à présent librement déplacer votre personnage dans le niveau et sauter sur les blocs.

## 8. Différents types de blocs



## 14. Idées d'améliorations

Voici plusieurs idées d'amélioration du jeu. **Il vous est demandé d'en choisir au minimum 2 dans la liste et de les implémenter par vous-même.**

Totalement dans vos cordes:

- Ajouter une animation au joueur quand il se déplace.
- Faire en sorte que le jeu arrête de créer des ennemis s'il y en a déjà 5 ou plus en jeu.
- Faire en sorte que plus le score augmente, plus les ennemis se déplacent rapidement.
- Détruire les missiles lorsqu'ils sortent de l'écran et limiter le joueur à 3 missiles à la fois.
- Créer un game over sous les conditions de votre choix (par exemple au contact d'un ennemi ou après un certain temps). Cela affiche par exemple un écran noir avec écrit "Game Over" en grand.
- Une autre idée à me proposer !

Un peu plus complexe:

- Faire en sorte que les ennemis suivent le joueur au lieu de se balader aléatoirement.
- Faire en sorte qu'en cas de contact avec un ennemi, le joueur perd de la vie et l'ennemi meurt. La vie du joueur est affichée sous le score.
- Permettre au joueur de ramasser des objets pour augmenter son score, par exemple des pièces.

Challenging:

- Ajouter un nouveau type d'ennemi qui se comporte différemment.
- Ajouter des armes au personnage. Par exemple une attaque au corps à corps ou la possibilité de larguer des bombes qui explosent après quelques secondes.
- Faire en sorte que le monde bouge autour du personnage afin qu'il puisse se balader librement dans toutes les directions sans jamais toucher un bord. Indice: le joueur ne se déplace plus, mais déplacez tous les acteurs du jeu dans la direction inverse au déplacement du joueur.
