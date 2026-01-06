(prog_jeu.hit_the_fly)=

# 4. Hit the fly (shooter)

Le jeu consiste en un personnage pouvant se déplacer librement au clavier et pouvant tirer des projectiles sur des ennemis se déplaçant aléatoirement avec des clics de souris.

{download}`Téléchargement des ressources du jeu<../data/prog_2d/hit_the_fly.zip>`.

```{image} ../media/hit_the_fly.gif
```

## 1. Faire apparaître une fenêtre

La première étape est de définir le nom de notre jeu dans la variable `TITLE`, ainsi que la largeur `WIDTH` et la hauteur `HEIGHT` de notre fenêtre. Nous allons également importer des fonctions de `pgzhelper` afin de nous faciliter la vie. Pygame Zero s'occupe du reste !

```python
import pgzero
import pgzrun
from pgzhelper import *

TITLE = 'Hit the fly'

WIDTH = 800
HEIGHT = 600

pgzrun.go() # Lance le jeu
```

```{image} ../media/pygame_fenetre.png
```

Pygame Zero fonctionne avec 2 fonctions principales: `draw` et `update`. Tandis que `draw` est appelée pour afficher des choses à l'écran, `update` est appelée pour faire évoluer le jeu. Elles sont toutes 2 appelées en boucle automatiquement.

```python
import pgzrun
from pgzhelper import *

TITLE = 'Hit the fly'
WIDTH = 800
HEIGHT = 600

def draw():
    pass # Ajouter ici tout ce qui concerne l'affichage
    # pass est une instruction qui ne fait rien, à remplacer par du code par la suite

def update():
    pass # Ajouter ici tout ce qui concerne l'évolution du jeu

pgzrun.go()
```

## 2. S'occuper du fond d'écran

`screen` est un objet accessible grâce à Pygame qui représente la fenêtre de notre jeu.  
On va y attacher cette image de fond.

```{image} ../media/grass.png
```

Voici comment faire:

```python
def draw():
    screen.blit('grass', (0, 0)) # Dessine l'image 'grass' aux coordonnées (0, 0)
```

La méthode `blit(image, (x, y))` de `screen` permet de dessiner une image sur la fenêtre aux coordonnées (x, y) correspondant au coin supérieur gauche de l'image. Comme l'image est plus grande que la fenêtre, elle la recouvre entièrement.

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Hit the fly'
WIDTH = 800
HEIGHT = 600

def draw():
    screen.blit('grass', (0, 0))

def update():
    pass

pgzrun.go()
```
````

## 3. Ajouter le joueur

Il est temps d'ajouter notre joueur.

```{image} ../media/alien_walk1.png
```

Comme dans le jeu précédent, nous créons une classe `Player` qui nécessitera au minimum une image et des coordonnées de position (`x` et `y`).

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        # Ce code sera généralement identique pour tous les acteurs
```

Nous pouvons à présent créer notre objet `player` grâce à notre classe. Nous lui passons le nom de l'image qui va le représenter ainsi que ses coordonnées afin qu'il soit placé au centre de la fenêtre.

```python
player = Player('alien_walk1', (WIDTH/2, HEIGHT/2)) # Positionnement au centre de la fenêtre
```

Afin de dessiner notre joueur, il faut en dernier lieu appeler la méthode `player.draw()` dans la fonction principale `draw` de Pygame.

```python
def draw():
    screen.blit('grass', (0, 0))
    player.draw() # On dessine le joueur ici !
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Hit the fly'
WIDTH = 800
HEIGHT = 600

class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)

player = Player('alien_walk1', (WIDTH/2, HEIGHT/2))

def draw():
    screen.blit('grass', (0, 0))
    player.draw()

def update():
    pass

pgzrun.go()
```
````

## 4. Déplacer le joueur

Nous allons déplacer le joueur grâce aux touches `w, a, s, d`. Une manière propre de le faire est de définir une méthode `update` pour notre classe `Player` qui va définir comment notre joueur doit se comporter.

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
    
    def update(self):
        # Que doit faire notre joueur...
```

On va utiliser l'objet `keyboard` pour récupérer les touches enfoncées par l'utilisateur et modifier les coordonnées `x` et `y` du joueur.

```python
def update(self):
    if keyboard.a: # Si la touche a est enfoncée
        self.x -= 3 # Déplace le joueur à gauche
```

Il nous suffit donc de contrôler quelles touches sont enfoncées et de modifier les coordonnées de notre joueur en conséquence:

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
    
    def update(self):
        if keyboard.a:
            self.x -= 3 # Déplacement à gauche
        if keyboard.d:
            self.x += 3 # Déplacement à droite

        if keyboard.w:
            self.y -= 3 # Déplacement en haut
        if keyboard.s:
            self.y += 3 # Déplacement en bas
```

Vous remarquez que nous bougeons de `3` pixels par "tour de jeu". Afin de pouvoir facilement modifier la vitesse de notre personnage par la suite, il serait plus judicieux de lui définir une vitesse.

Nous pouvons ajouter un attribut `speed` à notre classe `Player` et lui donner la valeur `3`. Ainsi, nous n'aurons ensuite plus qu'à modifier cette valeur pour accélérer ou ralentir notre personnage à notre guise.

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.speed = 3 # Ajout de l'attribut ici !
    
    def update(self):
        if keyboard.a:
            self.x -= self.speed
        if keyboard.d:
            self.x += self.speed

        if keyboard.w:
            self.y -= self.speed
        if keyboard.s:
            self.y += self.speed
```

Afin que le jeu comprenne à présent qu'il doit effectuer l'`update` de notre joueur, il nous faut encore appeler la méthode `player.update()` dans la fonction `update` principale du jeu:

```python
def update():
    player.update()
```

Dernière étape: faire en sorte que le sprite représentant le joueur s'adapte à sa direction. Par défaut il regarde à droite, mais on voudrait qu'il regarde à gauche s'il se déplace à gauche.

Ceci est faisable grâce à l'attribut `flip_x` hérité de la classe `Actor`. Par défaut, `flip_x` vaut `False`. Il suffit de le faire passer à `True` au bon moment.

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.speed = 3
    
    def update(self):
        if keyboard.a:
            self.x -= self.speed
            self.flip_x = True # On regarde à gauche, on flipe
        if keyboard.d:
            self.x += self.speed
            self.flip_x = False # On regarde à droite, on ne flipe pas

        if keyboard.w:
            self.y -= self.speed
        if keyboard.s:
            self.y += self.speed
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Hit the fly'
WIDTH = 800
HEIGHT = 600

class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.speed = 3
    
    def update(self):
        if keyboard.a:
            self.x -= self.speed
            self.flip_x = True
        if keyboard.d:
            self.x += self.speed
            self.flip_x = False

        if keyboard.w:
            self.y -= self.speed
        if keyboard.s:
            self.y += self.speed

player = Player('alien_walk1', (WIDTH/2, HEIGHT/2))

def draw():
    screen.blit('grass', (0, 0))
    player.draw()

def update():
    player.update()

pgzrun.go()
```
````

## 5. Ajouter un ennemi

Il est temps d'ajouter un ennemi pour pimenter un peu notre jeu. Dans notre cas, ce sera une mouche virevoltant aléatoirement.

```{image} ../media/fly1.png
```

Comme pour `Player`, la première étape est de créer une nouvelle classe pour représenter notre ennemi.

```python
class Ennemy(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
    
    def update(self):
        pass # Ajouter ici les instructions codant le comportant de l'ennemi
```

Nous pouvons ensuite créer un ennemi et lui donner une image et des coordonnées de départ **aléatoires**. La foncton permettant de tirer un nombre entier aléatoire entre 2 bornes `a` et `b` se nomme `randint(a, b)`. Pour qu'elle fonctionne, nous devons également importer le module `random` qui contient cette fonction.

```python
from random import * # Importe tout un tas de fonctions pour faire de l'aléatoire

# reste du code...

player = Player('alien_walk1', (WIDTH/2, HEIGHT/2))
ennemy = Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT))) # Création de l'ennemi aux coordonnées aléatoires
```

N'oublions pas d'appeler la méthode `ennemy.draw()` dans la fonction `draw` du programme principal. Nous pouvons également déjà appeler la méthode `ennemy.update()` dans la fonction `update` même si elle ne fait rien pour l'instant.

```python
def draw():
    screen.blit('grass', (0, 0))
    player.draw()
    ennemy.draw() # On dessine l'ennemi !

def update():
    player.update()
    ennemy.update() # Ne fait rien pour le moment
```

Occupons nous à présent du déplacement de l'ennemi. Nous allons créer un attribut `direction` qui indique la direction dans laquelle notre ennemi va se déplacer. Il s'agit d'un angle entre `0` et `360` degrés où `0` correspond à un déplacement vers la droite.

Nous allons donc spécifier la valeur de cet attribut lors de la création de notre objet, dans la méthode `init`. Nous en profitons pour définir sa vitesse (`speed`) à 3.

```python
class Ennemy(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.direction = randint(0, 360) # Direction initiale aléatoire
        self.speed = 3 # Vitesse de déplacement

    def update(self):
        pass
```

Ecrivons à présent la méthode `update` qui va définir le comportement de notre ennemi. Nous souhaitons faire 2 choses:

1. Légèrement modifier la direction de manière aléatoire
2. Avancer dans la direction (la méthode `move_in_direction(speed)` héritée de la classe `Actor` permet de le faire)

```python
class Ennemy(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.direction = randint(0, 360) # Direction initiale aléatoire
        self.speed = 3 # Vitesse de déplacement

    def update(self):
        self.direction += randint(-10, 10) # Modification aléatoire de la direction
        self.move_in_direction(self.speed) # Avancer dans la direction à une certaine vitesse
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *
from random import *

TITLE = 'Hit the fly'
WIDTH = 800
HEIGHT = 600

class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.speed = 3
    
    def update(self):
        if keyboard.a:
            self.x -= self.speed
            self.flip_x = True
        if keyboard.d:
            self.x += self.speed
            self.flip_x = False

        if keyboard.w:
            self.y -= self.speed
        if keyboard.s:
            self.y += self.speed
            
class Ennemy(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.direction = randint(0, 360)
        self.speed = 3

    def update(self):
        self.direction += randint(-10, 10)
        self.move_in_direction(self.speed)


player = Player('alien_walk1', (WIDTH/2, HEIGHT/2))
ennemy = Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))

def draw():
    screen.blit('grass', (0, 0))
    player.draw()
    ennemy.draw()
    
def update():
    player.update()
    ennemy.update()

pgzrun.go()
```
````

## 6. Animer un acteur

Nous allons tenter d'ajouter un peu de vie à notre jeu en animant notre ennemi.  
Pour animer un objet, il faut au minimum 2 images.

```{image} ../media/fly1.png
```

```{image} ../media/fly2.png
```

Tous nos objets héritant de la classe `Actor` possèdent un attribut nommé `images` qui permet de stocker la **liste** des images de l'animation.  
La première étape consiste donc à définir la valeur de cet attribut `images` dans le constructeur de notre ennemi.

```python
class Ennemy(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = ['fly1', 'fly2'] # Nouvel attribut ici !
        self.direction = randint(0, 360)
        self.speed = 3
```

Par la suite, tout ce qu'il reste à faire est appeler la méthode `ennemy.animate()` dans la fonction `update` du programme principal. Cette méthode permet de faire avancer l'animation de notre objet.

```python
def update():
    player.update()
    ennemy.update()
    ennemy.animate() # Avance l'animation de l'ennemi à 5 fps par défaut
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *
from random import *

TITLE = 'Hit the fly'
WIDTH = 800
HEIGHT = 600

class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.speed = 3
    
    def update(self):
        if keyboard.a:
            self.x -= self.speed
            self.flip_x = True
        if keyboard.d:
            self.x += self.speed
            self.flip_x = False

        if keyboard.w:
            self.y -= self.speed
        if keyboard.s:
            self.y += self.speed
            
class Ennemy(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = ['fly1', 'fly2']
        self.direction = randint(0, 360)
        self.speed = 3

    def update(self):
        self.direction += randint(-10, 10)
        self.move_in_direction(self.speed)

    
player = Player('alien_walk1', (WIDTH/2, HEIGHT/2))
ennemy = Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))

def draw():
    screen.blit('grass', (0, 0))
    player.draw()
    ennemy.draw()
    
def update():
    player.update()
    ennemy.update()
    ennemy.animate()

pgzrun.go()
```
````

## 7. Ajouter des ennemis à intervalle régulier

Pour avoir plusieurs ennemis en même temps dans le jeu, nous allons remplir une **liste d'ennemis**. Nous allons donc remplacer notre unique objet `ennemy` par une liste nommée `ennemies` qui contient initialement un seul ennemi.

```python
ennemies = [Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))]
# Ici on utilise des crochets [] pour créer une liste contenant un seul ennemi
```

Evidemment, il faut mettre à jour les fonctions principales `draw` et `update` car au lieu de desinner `ennemy`, nous voulons à présent parcourir la liste `ennemies` et dessiner chacun d'eux. Un parcours de liste se fait avec une boucle `for`.

```python
def draw():
    screen.blit('grass', (0, 0))
    player.draw()
    for ennemy in ennemies: # Parcourt la liste des ennemis
        ennemy.draw() # Dessine chacun d'eux

def update():
    player.update()
    for ennemy in ennemies: # Parcourt la liste des ennemis
        ennemy.update() # Met à jour chacun d'eux
        ennemy.animate() # Avance l'animation de chacun d'eux
```

Nous avons à présent une liste d'ennemis qui contient `1` ennemi. Mais comment remplir cette liste au cours du jeu ? Commençons par définir une fonction qui va s'occuper d'ajouter un nouvel ennemi à la liste.

```python
def add_ennemy():
    ennemy = Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))
    ennemies.append(ennemy) # Ajoute ennemy à la liste ennemies
```

La question est: quand appeler cette fonction ? Quand voulons nous ajouter un ennemi ? Ici, disons que nous aimerions ajouter un ennemi toutes les 5 secondes.

Pygame nous offre pour ceci un objet très utile: `clock`. **Cet objet permet d'agender des appels de fonction dans le temps**.

```python
clock.schedule_interval(add_ennemy, 5.0)
```

La méthode `schedule_interval` permet d'appeler une fonction toutes les `x` secondes. Nous l'avons donc réglée pour appeler `add_ennemy` toutes les 5 secondes, mais essayez de modifier cette valeur.

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *
from random import *

TITLE = 'Hit the fly'
WIDTH = 800
HEIGHT = 600

class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.speed = 3
    
    def update(self):
        if keyboard.a:
            self.x -= self.speed
            self.flip_x = True
        if keyboard.d:
            self.x += self.speed
            self.flip_x = False

        if keyboard.w:
            self.y -= self.speed
        if keyboard.s:
            self.y += self.speed
            
class Ennemy(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = ['fly1', 'fly2']
        self.direction = randint(0, 360)
        self.speed = 3

    def update(self):
        self.direction += randint(-10, 10)
        self.move_in_direction(self.speed)


def add_ennemy():
    ennemy = Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))
    ennemies.append(ennemy)
    
player = Player('alien_walk1', (WIDTH/2, HEIGHT/2))
ennemies = [Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))]

clock.schedule_interval(add_ennemy, 5.0)

def draw():
    screen.blit('grass', (0, 0))
    player.draw()
    for ennemy in ennemies:
        ennemy.draw()

def update():
    player.update()
    for ennemy in ennemies:
        ennemy.update()
        ennemy.animate()

pgzrun.go()
```
````

## 8. Tirer des projectiles

Il est temps de pouvoir frapper nos ennemis ! Nous allons créer un nouvel objet pour représenter un projectile qui sera tiré avec un clic de souris et qui partira depuis le joueur dans la direction du curseur de la souris.

```{image} ../media/missile.png
```

Commençons par créer la classe `Missile` associée.
Nous pouvons également déjà lui donner une vitesse (de 5 par exemple).

```python
class Missile(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.speed = 5

    def update(self):
        pass # On s'en occupe plus tard
```

Créons à présent une liste de missiles, tout comme pour les ennemis. Cette liste doit être vide au départ et se remplira à chaque clic de souris.

```python
player = Player('alien_walk1', (WIDTH/2, HEIGHT/2))
ennemies = [Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))]
missiles = [] # Création de la liste vide de missiles
```

Nous voulons ajouter un missile à chaque clic de souris. Pygame nous fournit la fonction `on_mouse_down(pos)` qui nous permet de réagir à un clic de souris. `pos` correspond à l'emplacement `(x, y)` du curseur au moment du clic.

Nous devons utiliser `pos` pour calculer la direction que devra prendre notre missile. Il est possible de calculer l'angle entre un acteur et une coordonnée grâce à la méthode `angle_to` héritée de `Actor`.

```python
def on_mouse_down(pos):
    missile = Missile('missile', (player.x, player.y)) # Création du missile à l'emplacement du joueur
    missile.direction = player.angle_to(pos) # La direction du missile est l'angle entre le joueur et la position du clic
    missiles.append(missile) # Ajout du missile à la liste
```

Dessinons à présent nos missiles en les ajoutant à la fonction `draw`. On peut déjà l'ajouter également à `update` même si on a pas encore défini les déplacements du missile.

```python
def draw():
    screen.blit('grass', (0, 0))
    player.draw()
    for ennemy in ennemies:
        ennemy.draw()
    for missile in missiles: # Parcourt les missiles
        missile.draw()

def update():
    player.update()
    for ennemy in ennemies:
        ennemy.update()
        ennemy.animate()
    for missile in missiles: # Parcourt les missiles
        missile.update()
```

Il ne nous reste plus qu'à définir le déplacement de nos missiles dans leur méthode `update`. C'est assez simple, nous voulons simplement qu'il avance dans sa direction avec sa vitesse.

```python
class Missile(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.speed = 5

    def update(self):
        self.move_in_direction(self.speed) # Se déplace dans sa direction à sa vitesse, comme les mouches
```

Vous remarquez un dernier détail visuel à régler... Les sprites des missiles devraient s'orienter dans la direction de leur déplacement. Chaque `Actor` possède un attribut `angle` qui règle l'angle de l'image. Par défaut, cet angle vaut `0`.

```{image} ../media/rotation.svg
```

Il suffit donc de donner à `angle` la même valeur que `direction` à la création du missile.

```python
def on_mouse_down(pos):
    missile = Missile('missile', (player.x, player.y))
    missile.direction = player.angle_to(pos)
    missile.angle = missile.direction # On oriente le missile dans la direction
    missiles.append(missile)
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *
from random import *

TITLE = 'Hit the fly'
WIDTH = 800
HEIGHT = 600

class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.speed = 3
        
    def update(self):
        if keyboard.a:
            self.x -= self.speed
            self.flip_x = True
        if keyboard.d:
            self.x += self.speed
            self.flip_x = False

        if keyboard.w:
            self.y -= self.speed
        if keyboard.s:
            self.y += self.speed

class Ennemy(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = ['fly1', 'fly2']
        self.direction = randint(0, 360)
        self.speed = 3

    def update(self):
        self.direction += randint(-10, 10)
        self.move_in_direction(self.speed)
        
class Missile(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.speed = 5

    def update(self):
        self.move_in_direction(self.speed)
        
        
def add_ennemy():
    ennemy = Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))
    ennemies.append(ennemy)
    
def on_mouse_down(pos):
    missile = Missile('missile', (player.x, player.y))
    missile.direction = player.angle_to(pos)
    missile.angle = missile.direction
    missiles.append(missile)

player = Player('alien_walk1', (WIDTH/2, HEIGHT/2))
ennemies = [Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))]
missiles = []

clock.schedule_interval(add_ennemy, 5.0)

def draw():
    screen.blit('grass', (0, 0))
    player.draw()
    for ennemy in ennemies:
        ennemy.draw()
    for missile in missiles:
        missile.draw()

def update():
    player.update()
    for ennemy in ennemies:
        ennemy.update()
        ennemy.animate()
    for missile in missiles:
        missile.update()

pgzrun.go()
```
````

## 9. Gérer les collisions

Il est temps de donner du pouvoir à nos missiles pour détruire les ennemis !

```{image} ../media/collision.png
```

Où ajouter le contrôle de collision ? Le plus simple est de le faire dans la classe `Missile`! Après le déplacement d'un missile, on parcourt la liste des ennemis et on contrôle si le missile est en contact avec l'un d'eux.

```python
class Missile(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.speed = 5

    def update(self):
        self.move_in_direction(self.speed)
        for ennemy in ennemies: # Parcourt chaque ennemi
            if self.collides_with(ennemy): # Si il y a collision
                print('BOOOOM') # On affiche boom dans la console
```

Bon, on affiche `BOOOOM` quand on touche en ennemi, mais on voudrait bien qu'il soit détruit, ainsi que notre missile ! Pour détruire un acteur du jeu, il suffit de le supprimer de la liste qui le contient. C'est à dire que nous voulons supprimer le missile de `missiles` et l'ennemi touché de `ennemies`.

Mais à quel moment ? En fait il existe plein de manières de faire... Une façon propre est d'utiliser l'attribut `to_remove` qui traque si un objet doit être retiré du jeu ou non (il vaut `False` par défaut). Il suffit donc de passer `to_remove` à `True` pour le missile en question et pour l'ennemi qu'il a touché.

```python
class Missile(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.speed = 5

    def update(self):
        self.move_in_direction(self.speed)
        for ennemy in ennemies:
            if self.collides_with(ennemy):
                print('BOOOOM')
                ennemy.to_remove = True # On marque l'ennemi touché
                self.to_remove = True # On marque le missile en question
```

A la fin de la fonction `update` du programme principal, on parcourt nos listes et on supprime tous les objets qui sont marqués pour être détruits. Cela permet de tous les détruire en même temps pour éviter les bugs et simplifier la logique du jeu.  
Par soucis de simplicité, j'ai écrit une fonction toute prête: `remove_actors` qui s'occupe de supprimer d'une liste tous les acteurs dont l'attribut `to_remove` est à `True`.

```python
def update():
    player.update()
    for ennemy in ennemies:
        ennemy.update()
    for missile in missiles:
        missile.update()
        
    remove_actors(ennemies) # On supprime les ennemis marqués
    remove_actors(missiles) # On supprime les missiles marqués
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *
from random import *

TITLE = 'Hit the fly'
WIDTH = 800
HEIGHT = 600

class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.speed = 3
        
    def update(self):
        if keyboard.a:
            self.x -= self.speed
            self.flip_x = True
        if keyboard.d:
            self.x += self.speed
            self.flip_x = False

        if keyboard.w:
            self.y -= self.speed
        if keyboard.s:
            self.y += self.speed

class Ennemy(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = ['fly1', 'fly2']
        self.direction = randint(0, 360)
        self.speed = 3

    def update(self):
        self.direction += randint(-10, 10)
        self.move_in_direction(self.speed)
        
class Missile(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.speed = 5

    def update(self):
        self.move_in_direction(self.speed)
        for ennemy in ennemies:
            if self.collides_with(ennemy):
                print('BOOOOM')
                ennemy.to_remove = True
                self.to_remove = True
        
        
def add_ennemy():
    ennemy = Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))
    ennemies.append(ennemy)
    
def on_mouse_down(pos):
    missile = Missile('missile', (player.x, player.y))
    missile.direction = player.angle_to(pos)
    missile.angle = missile.direction
    missiles.append(missile)

player = Player('alien_walk1', (WIDTH/2, HEIGHT/2))
ennemies = [Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))]
missiles = []

clock.schedule_interval(add_ennemy, 5.0)

def draw():
    screen.blit('grass', (0, 0))
    player.draw()
    for ennemy in ennemies:
        ennemy.draw()
    for missile in missiles:
        missile.draw()

def update():
    player.update()
    for ennemy in ennemies:
        ennemy.update()
        ennemy.animate()
    for missile in missiles:
        missile.update()

    remove_actors(ennemies)
    remove_actors(missiles)

pgzrun.go()
```
````

## 10. Idées d'améliorations

```{admonition} Travail à rendre
Votre travail consiste à ajouter au minimum les améliorations suivantes au jeu:

* 2 améliorations faciles
* 1 amélioration moyenne
```

Voici plusieurs idées d'amélioration du jeu.  
Vous pouvez bien sûr me proposer d'autres idées et je vous dirai leur difficulté.

**Totalement dans vos cordes (facile):**

* Ajouter une animation au joueur ainsi que des bruitages ou de la musique.
* Faire en sorte que le joueur (ou les ennemis) ne puisse pas sortir de l'écran (par exemple en réapparaissant de l'autre côté).
* Faire en sorte que le jeu arrête de créer des ennemis s'il y en a déjà 5 ou plus en jeu.
* Ajouter un système de score quand vous détruisez des ennemis.
* Détruire les missiles lorsqu'ils sortent de l'écran et limiter le joueur à 3 missiles à la fois.
* Créer un game over sous les conditions de votre choix (par exemple au contact d'un ennemi ou après un certain temps).
* Faire en sorte que le personnage ne se déplace pas plus rapidement en diagonal qu'à l'horizontal ou à la verticale.

**Un peu plus complexe (moyen):**

* Faire en sorte qu'en cas de contact avec un ennemi, le joueur perd de la vie et l'ennemi meurt. La vie du joueur est affichée à l'écran.
* Permettre au joueur de ramasser des objets pour augmenter son score, par exemple des pièces.
* Ajouter une image d'explosion qui apparaît lorsqu'un ennemi est détruit.
* Ajouter un second joueur qui pourra se déplacer et tirer avec d'autres touches.
* Ajouter un nouveau type d'ennemi qui se comporte différemment.
* Ajouter un item qui permet d'augmenter temporairement la vitesse du joueur si rammassé.
* Faire en sorte qu'en cas de contact avec un ennemi, le joueur perde un peu de vie et soit invincible pendant un court laps de temps ou soit repoussé (pour éviter des dégats à répétition).
* Ajouter un boss qui apparaît seulement après un certain temps et nécessite beaucoup de dégats pour être battu mais offre un score élevé.
* Faire en sorte que les ennemis suivent le joueur au lieu de se balader aléatoirement.

**Challenging (difficile):**

* Ajouter des armes au personnage. Par exemple une attaque au corps à corps ou la possibilité de larguer des bombes qui explosent après quelques secondes.
* Permettre au joueur de poser des pièges qui blesseront les ennemis qui passent dessus.
* Faire en sorte que le monde bouge autour du personnage afin qu'il puisse se balader librement dans toutes les directions sans jamais toucher un bord. Indice: le joueur ne se déplace plus, mais déplacez tous les acteurs du jeu dans la direction inverse au déplacement du joueur.
* Créer un second niveau atteignable en passant un certain score où les ennemis sont différents et plus coriaces.
* Donner aux ennemis la capacité d'essayer d'esquiver les projectiles (en se déplaçant perpendiculairement à leur trajectoire).
* Créer un menu avant le début du jeu qui permet de choisir la difficulté ou d'autres options.
* Autres idées..?

## Travailler en dehors du TP

`````{admonition} Comment travailler en dehors du TP
:class: danger
````{dropdown} Depuis la maison
1. Téléchargez et installez [Python](https://www.python.org/downloads/).
2. Téléchargez et installez [Pycharm Community](https://www.jetbrains.com/fr-fr/pycharm/download/). Faites attention à prendre la version **Community** (en bas de la page) qui est gratuite.
3. Ouvrez Pycharm et créez un nouveau projet.
4. Déplacez les fichiers et dossiers du jeu dans le dossier de votre projet (PycharmProject).
5. Installez le package `pgzero`. Pour cela, ajoutez la ligne `import pgzero` tout en haut de votre code et Pycharm vous proposera de l'installer **en passant le curseur de la souris dessus** (sur `pgzero`).
```{image} ../media/pgzero.png
```
Programmez !
````
````{dropdown} Depuis l'école
1. Ouvrez Pycharm et créez un nouveau projet.
2. Déplacez les fichiers et dossiers du jeu dans le dossier de votre projet (PycharmProject). **Attention**, si vous prenez votre dossier de travail depuis votre disque réseau (pxxxxx), il faudra le copier sur le bureau avant de le déplacer dans Pycharm.
3. Installez le package `pgzero`. Pour cela, ajoutez la ligne `import pgzero` tout en haut de votre code et Pycharm vous proposera de l'installer **en passant le curseur de la souris dessus** (sur `pgzero`).
```{image} ../media/pgzero.png
```
Programmez !
````
`````
