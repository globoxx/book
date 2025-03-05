(prog_jeu.hit_the_fly)=

# 2. Hit the fly (shooter)

Le jeu consiste en un personnage pouvant se déplacer librement au clavier et pouvant tirer des projectiles sur des ennemis se déplaçant aléatoirement avec des clics de souris.

{download}`Téléchargement des ressources du jeu<../data/prog_2d/hit_the_fly.zip>`.

```{image} ../media/hit_the_fly.gif
```

## 1. Faire apparaître une fenêtre

La première étape est de définir le nom de notre jeu dans la variable `TITLE`, ainsi que la largeur `WIDTH` et la hauteur `HEIGHT` de notre fenêtre. Nous allons également importer des fonctions de `pgzhelper` afin de nous faciliter la vie. Pygame Zero s'occupe du reste !

```python
import pgzrun
from pgzhelper import *

TITLE = 'Hit the fly'

WIDTH = 800
HEIGHT = 600

pgzrun.go() # Lance le jeu
```

```{image} ../media/pygame_fenetre.png
```

Pygame Zero fonctionne avec 2 fonctions principales: `draw` et `update`. Tandis que `draw` est appelée pour afficher des choses à l'écran, `update` est appelée pour faire évoluer le jeu. Elles sont toutes 2 appelées en boucle automatiquement tant qu'on ne quitte pas le jeu.

```python
import pgzrun
from pgzhelper import *

TITLE = 'Hit the fly'
WIDTH = 800
HEIGHT = 600

def draw():
    pass # Ajouter ici tout ce qui concerne l'affichage

def update():
    pass # Ajouter ici tout ce qui concerne l'évolution du jeu

pgzrun.go()
```

## 2. S'occuper du fond d'écran

Tous les dessins de notre jeu se feront via la fonction `draw` de Pygame. Il nous faut donc lui ajouter l'instruction permettant de colorier le fond.

```python
def draw():
    screen.fill('red') # Colorie le fond en rouge
```

`screen` est un objet accessible grâce à Pygame qui représente la fenêtre de notre jeu.  
Bon c'est joli mais ça serait sympa d'avoir une image de fond plutôt qu'une simple couleur. Prenons simplement de l'herbe.

```{image} ../media/grass.png
```

Voici comment faire:

```python
def draw():
    screen.blit('grass', (0, 0)) # Dessine l'image 'grass' aux coordonnées (0, 0)
```

La méthode `blit(image, (x, y))` de `screen` permet de dessiner une image sur la fenêtre aux coordonnées (x, y) correspondant au coin supérieur gauche de l'image. Comme l'image est au moins aussi grande que la fenêtre, elle la recouvre entièrement.

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

Il est temps d'ajouter notre joueur. Il sera représenté par un `objet`. Voyez un objet comme une sorte de super variable qui peut contenir d'autres variables. Chaque objet sera également représenté par une image que nous appelerons un sprite. Chaque sprite doit être sauvegardé dans le dossier `images`.

```{image} ../media/alien_walk1.png
```

La plateforme <a href="https://kenney.nl/assets" target="_blank">Kenny</a> contient énormément de sprites gratuits à utiliser pour vos jeux. Le sprite du petit alien ci-dessus vient du <a href="https://kenney.nl/assets/platformer-art-deluxe">Platformer art deluxe</a>.

Pour chaque nouvel objet que l'on veut ajouter à notre jeu, nous allons créer une `classe` associée. Voyez une classe comme un moule qui nous permettra de créer des objets, comme notre joueur. En <a href="https://courspython.com/classes-et-objets.html" target="_blank">programmation orientée objet</a>, une classe possède des `attributs` (des variables décrivant l'objet) et des `méthodes` (des fonctions pouvant être appelées par l'objet).

```{image} ../media/classe_voiture.svg
```

Nous créons donc une classe `Player` qui hérite des attributs et méthodes d'une autre classe nommée `Actor` offerte par Pygame. En fait, tous les objets que nous allons ajouter à notre jeu sont des `acteurs`.

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs): # Init est le constructeur de la classe
        super().__init__(image, pos, **kwargs) # Cette ligne appelle le constructeur de la classe mère Actor
        # Ne vous en préoccupez pas trop pour le moment
```

Ce code crée une classe `Player` héritant de la classe `Actor`. La méthode `init` est ce que l'on appelle un **constructeur** qui est appelé lors de la création d'un objet. Ce construction prend obligatoirement une image en entrée, ainsi que des coordonnées `pos` pour savoir où placer l'objet créé.

Nous pouvons à présent créer notre objet `player` grâce à notre classe. Nous lui passons le nom de l'image qui va le représenter ainsi que ses coordonnées (x, y) afin qu'il soit placé au centre de la fenêtre.

```python
player = Player('alien_walk1', (WIDTH/2, HEIGHT/2)) # Appel du constructeur init
```

Afin de dessiner notre joueur, il faut en dernier lieu appeler la méthode `player.draw()` dans la fonction principale `draw` de Pygame.

```python
def draw():
    screen.blit('grass', (0, 0))
    player.draw() # On dessine le joueur ici !
```

`draw` est une méthode possèdée par tous les objets de type `Actor`. Etant donné que notre objet de type `Player` est aussi un `Actor`, il hérite de cette méthode ainsi que de plein d'attributs dont nous aurons besoin plus tard comme les coordonnées `x` et `y` de notre objet.

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

Remarquez que, tout comme `init`, `update` prend un argument spécial: `self`. Cet argument `self` représente l'objet en lui-même (c'est à dire le joueur dans notre cas). C'est grâce à lui que nous pourrons modifier par exemple la position de notre joueur via `self.x` qui correspond à sa position horizontale.

`keyboard` est (tout comme `screen`) un objet donné par Pygame qui nous permet de récupérer les touches enfoncées par l'utilisateur. C'est très simple d'utilisation: si la touche `x` est enfoncée, alors `keyboard.x` vaudra `True`, sinon il vaudra `False`.

```python
if keyboard.a: # Si la touche a est appuyée
    # Déplace le joueur à gauche
```

Il nous suffit donc de contrôler quelles touches sont enfoncées et de modifier les coordonnées de notre joueur en conséquence:

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
    
    def update(self):
        if keyboard.a:
            self.x -= 3 # Equivalent à self.x = self.x - 3
        elif keyboard.d:
            self.x += 3 # Equivalent à self.x = self.x + 3

        if keyboard.w:
            self.y -= 3
        elif keyboard.s:
            self.y += 3
```

Vous remarquez que nous bougeons de `3` pixels par `tick` (un `tick` représente un tour dans la boucle principale du jeu). Afin de rendre le code plus propre et pouvoir facilement modifier la vitesse de notre personnage par la suite, il serait plus judicieux de lui définir une vitesse.

Nous pouvons ajouter un attribut `speed` à notre classe `Player` et lui donner la valeur `3`. Ainsi, nous n'aurons ensuite plus qu'à modifier cette valeur pour accélérer ou ralentir notre personnage à notre guise. Cet ajout se fait dans le **constructeur** de notre classe, c'est à dire dans la méthode `init`.

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.speed = 3 # Ajout de l'attribut ici !
    
    def update(self):
        if keyboard.a:
            self.x -= self.speed
        elif keyboard.d:
            self.x += self.speed

        if keyboard.w:
            self.y -= self.speed
        elif keyboard.s:
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
        elif keyboard.d:
            self.x += self.speed
            self.flip_x = False #On regarde à droite, on ne flipe pas

        if keyboard.w:
            self.y -= self.speed
        elif keyboard.s:
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
        elif keyboard.d:
            self.x += self.speed
            self.flip_x = False

        if keyboard.w:
            self.y -= self.speed
        elif keyboard.s:
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

## 5. Empêcher un acteur de sortir de l'écran

La détection des bords de la fenêtre de jeu est un élément récurrent de tout jeu vidéo. Il existe plétore de manières de résoudre ce problème mais je vous propose la solution suivante: **si un acteur sort de l'écran, il réapparaît du coté opposé**.

Comme cela ne concernera pas que notre joueur mais probablement d'autres acteurs de notre jeu, il semble être une bonne idée de créer une fonction qui pourra s'appliquer à n'importe quel acteur. Notre fonction `detect_border` prendra donc un acteur en argument.

```python
def detect_border(actor):
    # Ajouter ici la détection des bords
    # et la modification des coordonnées de l'acteur si nécessaire
```

Tout `Actor` possède des attributs `x` et `y` que nous pouvons lire pour savoir si l'acteur sort de la fenêtre de jeu. Par exemple, si `actor.x > WIDTH`, cela signifie que l'acteur sort du jeu par la droite. Dans ce cas, vous voulons faire réapparaître l'acteur à gauche, c'est à dire que `actor.x` doit valoir `0`.

Nous n'avons qu'à faire les 4 tests pour les 4 bords de la fenêtre:

```python
def detect_border(actor):
    if actor.x > WIDTH: # Dépassement à droite
        actor.x = 0
    elif actor.x < 0: # Dépassement à gauche
        actor.x = WIDTH

    if actor.y > HEIGHT: # Dépassement en bas
        actor.y = 0
    elif actor.y < 0:
        actor.y = HEIGHT # Dépassement en haut
```

Mais à quel moment appeler cette fonction ? Eh bien à la fin du déplacement de notre personnage ! C'est à dire à la fin de la méthode `player.update`.

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

        if keyboard.w:
            self.y -= self.speed
        elif keyboard.s:
            self.y += self.speed
            
        detect_border(self) # Appel de la fonction ici !
```

Notez ici que l'argument donné à `detect_border` est `self` car il représente justement le joueur !

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
        elif keyboard.d:
            self.x += self.speed
            self.flip_x = False

        if keyboard.w:
            self.y -= self.speed
        elif keyboard.s:
            self.y += self.speed
            
        detect_border(self)

def detect_border(actor):
    if actor.x > WIDTH:
        actor.x = 0
    elif actor.x < 0:
        actor.x = WIDTH

    if actor.y > HEIGHT:
        actor.y = 0
    elif actor.y < 0:
        actor.y = HEIGHT
    
player = Player('alien_walk1', (WIDTH/2, HEIGHT/2))

def draw():
    screen.blit('grass', (0, 0))
    player.draw()
    
def update():
    player.update()

pgzrun.go()
```
````

## 6. Ajouter un ennemi

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

Nous pouvons ensuite créer un ennemi en appelant son constructeur et en lui donnant un sprite et des coordonnées de départ **aléatoires**. La foncton permettant de tirer un nombre entier aléatoire entre 2 bornes `a` et `b` se nomme `randint(a, b)`. Pour qu'elle fonctionne, nous devons également importer le module `random` qui contient cette fonction.

```python
from random import * # Importe tout un tas de fonctions pour faire de l'aléatoire

# reste du code...

player = Player('alien_walk1', (WIDTH/2, HEIGHT/2))
ennemy = Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT))) # Création de l'ennemi aux coordonnées aléatoires sur la fenêtre
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

Occupons nous à présent du déplacement de l'ennemi. Cela se code dans la méthode `update` de la classe `Ennemy`. Nous allons utiliser l'attribut `direction` qui indique la direction dans laquelle notre ennemi va se déplacer. Il s'agit d'un angle entre `0` et `360` degrés où `0` correspond à un déplacement vers la droite.

Nous allons donc spécifier la valeur de cet attribut lors de la création de notre objet, dans la méthode `init`. Nous en profitons pour également définir sa vitesse (`speed`) à 3.

```python
class Ennemy(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.direction = randint(0, 360) # Direction initiale aléatoire
        self.speed = 3 # Vitesse de déplacement

    def update(self):
        pass
```

Ecrivons à présent la méthode `update` qui va définir le comportement de notre ennemi à chaque `tick`. Nous souhaitons faire 3 choses:

1. Légèrement modifier la direction de manière aléatoire
2. Avancer dans la direction (la méthode `move_in_direction(speed)` héritée de la classe `Actor` permet de le faire)
3. Détecter les bords de la fenêtre

```python
class Ennemy(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.direction = randint(0, 360) # Direction initiale aléatoire
        self.speed = 3 # Vitesse de déplacement

    def update(self):
        self.direction += randint(-10, 10) # Modification aléatoire de la direction
        self.move_in_direction(self.speed) # Avancer dans la direction
        detect_border(self) # Détecter les bords comme pour le joueur
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
        elif keyboard.d:
            self.x += self.speed
            self.flip_x = False

        if keyboard.w:
            self.y -= self.speed
        elif keyboard.s:
            self.y += self.speed
            
        detect_border(self)

class Ennemy(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.direction = randint(0, 360)
        self.speed = 3

    def update(self):
        self.direction += randint(-10, 10)
        self.move_in_direction(self.speed)
        detect_border(self)

def detect_border(actor):
    if actor.x > WIDTH:
        actor.x = 0
    elif actor.x < 0:
        actor.x = WIDTH

    if actor.y > HEIGHT:
        actor.y = 0
    elif actor.y < 0:
        actor.y = HEIGHT
    
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

## 7. Animer un acteur

Nous allons tenter d'ajouter un peu de vie à notre jeu en animant notre ennemi.  
Pour animer un objet, il faut au minimum 2 sprites qui vont se succéder à une certaine vitesse (fps).

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
    #...
```

Par la suite, tout ce qu'il reste à faire est appeler la méthode `ennemy.animate()` dans la fonction `draw` du programme principal. Cette méthode héritée de `Actor` permet de faire avancer l'animation de notre objet.

```python
def draw():
    screen.blit('grass', (0, 0))
    player.draw()
    ennemy.draw()
    ennemy.animate() # On fait avancer l'animation ici !
```

Notez que par défaut, l'animation se déroule à `5` fps. Cela signifie que l'image change 5 fois par seconde. Pour changer cette valeur, il suffirait de modifier l'attribut `fps` dans le constructeur de la classe `Ennemy`.

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
        elif keyboard.d:
            self.x += self.speed
            self.flip_x = False

        if keyboard.w:
            self.y -= self.speed
        elif keyboard.s:
            self.y += self.speed
            
        detect_border(self)

class Ennemy(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = ['fly1', 'fly2']
        self.direction = randint(0, 360)
        self.speed = 3

    def update(self):
        self.direction += randint(-10, 10)
        self.move_in_direction(self.speed)
        detect_border(self)

def detect_border(actor):
    if actor.x > WIDTH:
        actor.x = 0
    elif actor.x < 0:
        actor.x = WIDTH

    if actor.y > HEIGHT:
        actor.y = 0
    elif actor.y < 0:
        actor.y = HEIGHT
    
player = Player('alien_walk1', (WIDTH/2, HEIGHT/2))
ennemy = Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))

def draw():
    screen.blit('grass', (0, 0))
    player.draw()
    ennemy.draw()
    ennemy.animate()
    
def update():
    player.update()
    ennemy.update()

pgzrun.go()
```
````

## 8. Ajouter des ennemis à intervalle régulier

Pour avoir plusieurs ennemis en même temps dans le jeu, nous allons remplir une **liste d'ennemis**. Nous allons donc remplacer notre unique objet `ennemy` par une liste (`[]`) qui contient initialement un seul ennemi.

```python
ennemies = [Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))]
```

Evidemment, il faut mettre à jour les fonctions principales `draw` et `update` car au lieu de desinner `ennemy`, nous voulons à présent parcourir la liste `ennemies` et dessiner chacun d'eux.

```python
def draw():
    screen.blit('grass', (0, 0))
    player.draw()
    for ennemy in ennemies: # Parcourt la liste des ennemis
        ennemy.draw() # Dessine chacun d'eux
        ennemy.animate() # Avance l'animation de chacun d'eux

def update():
    player.update()
    for ennemy in ennemies: # Parcourt la liste des ennemis
        ennemy.update() # Met à jour chacun d'eux
```

Nous avons à présent une liste d'ennemis qui contient 1 ennemi. Mais comment remplir cette liste au cours du jeu ? Commençons par définir une fonction qui va s'occuper d'ajouter un nouvel ennemi à la liste.

```python
def add_ennemy():
    ennemy = Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))
    ennemies.append(ennemy) # Ajoute ennemy à la liste ennemies
```

La question est: quand appeler cette fonction ? Quand voulons nous ajouter un ennemi ? Ici, disons que nous aimerions ajouter un ennemi toutes les 15 secondes.

Pygame nous offre pour ceci un objet très utile: `clock`. **Cet objet permet d'agender des appels de fonction dans le temps**.

```python
clock.schedule_interval(add_ennemy, 15.0)
```

La méthode `schedule_interval` permet d'appeler une fonction toutes les x secondes. Nous l'avons donc réglée pour appeler `add_ennemy` toutes les 15 secondes.

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
        elif keyboard.d:
            self.x += self.speed
            self.flip_x = False

        if keyboard.w:
            self.y -= self.speed
        elif keyboard.s:
            self.y += self.speed
            
        detect_border(self)

class Ennemy(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = ['fly1', 'fly2']
        self.direction = randint(0, 360)
        self.speed = 3

    def update(self):
        self.direction += randint(-10, 10)
        self.move_in_direction(self.speed)
        detect_border(self)

def detect_border(actor):
    if actor.x > WIDTH:
        actor.x = 0
    elif actor.x < 0:
        actor.x = WIDTH

    if actor.y > HEIGHT:
        actor.y = 0
    elif actor.y < 0:
        actor.y = HEIGHT

def add_ennemy():
    ennemy = Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))
    ennemies.append(ennemy)
    
player = Player('alien_walk1', (WIDTH/2, HEIGHT/2))
ennemies = [Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))]

clock.schedule_interval(add_ennemy, 15.0)

def draw():
    screen.blit('grass', (0, 0))
    player.draw()
    for ennemy in ennemies:
        ennemy.draw()
        ennemy.animate()

def update():
    player.update()
    for ennemy in ennemies:
        ennemy.update()

pgzrun.go()
```
````

## 9. Tirer des projectiles

Il est temps de pouvoir frapper nos ennemis ! Nous allons créer un nouvel objet pour représenter un projectile qui sera tiré avec un clic de souris et qui partira depuis le joueur dans la direction du curseur de la souris.

```{image} ../media/missile.png
```

Commençons par créer la classe `Missile` associée.
Chaque missile créé aura une direction de départ différente, cela signifie que nous devons donner cette information dès sa création. Nous ajoutons donc un argument `direction` à son constructeur `init`.  
Nous pouvons également déjà lui donner une vitesse (de 5 par exemple).

```python
class Missile(Actor):
    def __init__(self, image, pos, direction, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.direction = direction # La direction initiale dépendra de la valeur donnée lors de la création du missile
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
    direction = player.angle_to(pos) # Calcul de l'angle entre le joueur et le curseur de la souris
    missile = Missile('missile', (player.x, player.y), direction) # Création du missile avec la direction calculée
    missiles.append(missile) # Ajout du missile à la liste
```

Dessinons à présent nos missiles en les ajoutant à la fonction `draw`. On peut déjà l'ajouter également à `update` même si on a pas encore défini les déplacements du missile.

```python
def draw():
    screen.blit('grass', (0, 0))
    player.draw()
    for ennemy in ennemies:
        ennemy.draw()
        ennemy.animate()
    for missile in missiles: # Parcourt les missiles
        missile.draw()

def update():
    player.update()
    for ennemy in ennemies:
        ennemy.update()
    for missile in missiles: # Parcourt les missiles
        missile.update()
```

Il ne nous reste plus qu'à définir le déplacement de nos missiles dans leur méthode `update`. C'est assez simple, nous voulons simplement qu'il avance dans sa direction avec sa vitesse.

```python
class Missile(Actor):
    def __init__(self, image, pos, direction, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.direction = direction
        self.speed = 5

    def update(self):
        self.move_in_direction(self.speed)
```

Vous remarquez un dernier détail visuel à régler... Les sprites des missiles devraient s'orienter dans la direction de leur déplacement. Chaque `Actor` possède un attribut `angle` qui règle l'angle du sprite associé. Par défaut, cet angle vaut `0`.

```{image} ../media/rotation.svg
```

Il suffit donc de donner à `angle` la même valeur que `direction` à la création du missile.

```python
class Missile(Actor):
    def __init__(self, image, pos, direction, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.direction = direction
        self.angle = direction # Ajout de l'attribut ici !
        self.speed = 5

    def update(self):
        self.move_in_direction(self.speed)
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
        elif keyboard.d:
            self.x += self.speed
            self.flip_x = False

        if keyboard.w:
            self.y -= self.speed
        elif keyboard.s:
            self.y += self.speed

        detect_border(self)

class Ennemy(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = ['fly1', 'fly2']
        self.direction = randint(0, 360)
        self.speed = 3

    def update(self):
        self.direction += randint(-10, 10)
        self.move_in_direction(self.speed)
        detect_border(self)
        
class Missile(Actor):
    def __init__(self, image, pos, direction, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.direction = direction
        self.angle = direction
        self.speed = 5

    def update(self):
        self.move_in_direction(self.speed)
        
def detect_border(actor):
    if actor.x > WIDTH:
        actor.x = 0
    elif actor.x < 0:
        actor.x = WIDTH

    if actor.y > HEIGHT:
        actor.y = 0
    elif actor.y < 0:
        actor.y = HEIGHT
        
def add_ennemy():
    ennemy = Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))
    ennemies.append(ennemy)
    
def on_mouse_down(pos):
    direction = player.angle_to(pos)
    missile = Missile('missile', (player.x, player.y), direction)
    missiles.append(missile)

player = Player('alien_walk1', (WIDTH/2, HEIGHT/2))
ennemies = [Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))]
missiles = []

clock.schedule_interval(add_ennemy, 15.0)

def draw():
    screen.blit('grass', (0, 0))
    player.draw()
    for ennemy in ennemies:
        ennemy.draw()
        ennemy.animate()
    for missile in missiles:
        missile.draw()

def update():
    player.update()
    for ennemy in ennemies:
        ennemy.update()
    for missile in missiles:
        missile.update()

pgzrun.go()
```
````

## 10. Gérer les collisions

Il est temps de donner du pouvoir à nos missiles pour détruire les ennemis ! Normalement, la gestion des collisions est un moment compliqué dans le développement d'un jeu car cela requiert des algorithmes assez complexes. Heureusement pour nous, Pygame nous mâche le travail grâce à la classe `Actor` qui est déjà capable de détecter des collisions grâce à sa méthode `collides_with(other_actor)`. Elle retourne `True` si l'acteur est en contact avec `other_actor`.

```{image} ../media/collision.png
```

Où ajouter le contrôle de collision ? Eh bien dans la méthode `update` du missile ! Après le déplacement, on parcourt la liste des ennemis et on contrôle si le missile est en contacte avec l'un d'eux.

```python
class Missile(Actor):
    def __init__(self, image, pos, direction, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.direction = direction
        self.angle = direction
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
    def __init__(self, image, pos, direction, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.direction = direction
        self.angle = direction
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
Par soucis de simplicité, j'ai écrit une fonction toute prête: `remove_actors(actors)` qui s'occupe de supprimer de la liste `actors` tous les acteurs dont l'attribut `to_remove` est à `True`.

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
        elif keyboard.d:
            self.x += self.speed
            self.flip_x = False

        if keyboard.w:
            self.y -= self.speed
        elif keyboard.s:
            self.y += self.speed

        detect_border(self)

class Ennemy(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = ['fly1', 'fly2']
        self.direction = randint(0, 360)
        self.speed = 3

    def update(self):
        self.direction += randint(-10, 10)
        self.move_in_direction(self.speed)
        detect_border(self)
        
class Missile(Actor):
    def __init__(self, image, pos, direction, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.direction = direction
        self.angle = direction
        self.speed = 5

    def update(self):
        self.move_in_direction(self.speed)
        
def detect_border(actor):
    if actor.x > WIDTH:
        actor.x = 0
    elif actor.x < 0:
        actor.x = WIDTH

    if actor.y > HEIGHT:
        actor.y = 0
    elif actor.y < 0:
        actor.y = HEIGHT
        
def add_ennemy():
    ennemy = Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))
    ennemies.append(ennemy)
    
def on_mouse_down(pos):
    direction = player.angle_to(pos)
    missile = Missile('missile', (player.x, player.y), direction)
    missiles.append(missile)

player = Player('alien_walk1', (WIDTH/2, HEIGHT/2))
ennemies = [Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))]
missiles = []

clock.schedule_interval(add_ennemy, 15.0)

def draw():
    screen.blit('grass', (0, 0))
    player.draw()
    for ennemy in ennemies:
        ennemy.draw()
        ennemy.animate()
    for missile in missiles:
        missile.draw()

def update():
    player.update()
    for ennemy in ennemies:
        ennemy.update()
    for missile in missiles:
        missile.update()

pgzrun.go()
```
````

## 11. Ajouter un son de collision

Ajouter un bruitage est très simple. La première étape consiste à ajouter le fichier `.wav` souhaité dans le dossier `sounds`. De nombreux bruitages et musiques gratuits peuvent être trouvés sur <a href="https://opengameart.org/" target="_blank">OpenGameArt</a> ou <a href="https://freesound.org/" target="_blank">FreeSound</a>. Priviliégiez les sons courts pour éviter des problèmes de performance.

Pygame nous offre l'objet `sounds` qui nous permet de facilement lancer un bruitage. Dans notre cas, nous souhaitons lancer un bruit d'explosion lorsque qu'un missile touche un ennemi.

```python
class Missile(Actor):
    def __init__(self, image, pos, direction, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.direction = direction
        self.angle = direction
        self.speed = 5

    def update(self):
        self.move_in_direction(self.speed)
        for ennemy in ennemies:
            if self.collides_with(ennemy):
                print('BOOOOM')
                sounds.explosion.play() # Ajout du bruitage ici !
                ennemy.to_remove = True
                self.to_remove = True
```

`sounds.explosion.play()` fait ici référence au nom du fichier son: `explosion.wav`.

## 12. Ajouter une musique de fond

Ajouter une musique de fond est tout aussi simple ! Il suffit d'ajouter un fichier `.mp3` dans le dossier `music` et d'utiliser l'objet `music` offert par Pygame.

Pour lancer notre musique `adventure.mp3` au début du jeu, il reste qu'à appeler `music.play(adventure)` au début du programme principal.

```python
music.play('adventure') # Ajout de la musique ici !

player = Player('alien_walk1', (WIDTH/2, HEIGHT/2))
ennemies = [Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))]
missiles = []

clock.schedule_interval(add_ennemy, 15.0)
```

## 13. Tenir et afficher un score

Le score est important dans les jeux ! Pour en tenir un, on peut le définir dans les attributs de notre `player` et l'initialiser à `0`.

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.speed = 3
        self.score = 0 # Création de l'attribut score ici !
```

Avant de nous occuper de l'augmentation du score, voyons déjà comment l'afficher. Afficher du texte à l'écran se fait via l'objet `screen` offert par Pygame. Nous l'utilisons dans la fonction `draw` du programme principal, juste après avoir défini l'image de fond.

```python
def draw():
    screen.blit('grass', (0, 0))
    screen.draw.text(f"Score: {player.score}", (0, 0)) # Ajout du score ici aux coordonnées (0, 0), tout en haut à gauche
    player.draw()
    for ennemy in ennemies:
        ennemy.draw()
        ennemy.animate()
    for missile in missiles:
        missile.draw()
```

Le score va augmenter à chaque fois que l'on détruit un ennemi. Il suffit donc de l'augmenter de 1 à chaque fois qu'un missile détruit un missile dans sa méthode `update`.

```python
class Missile(Actor):
    def __init__(self, image, pos, direction, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.direction = direction
        self.angle = direction
        self.speed = 5

    def update(self):
        self.move_in_direction(self.speed)
        for ennemy in ennemies:
            if self.collides_with(ennemy):
                print('BOOOOM')
                sounds.explosion.play()
                ennemy.to_remove = True
                self.to_remove = True
                player.score += 1 # Augmentation du score de 1
```

````{dropdown} Voir le code final
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
        self.score = 0
        
    def update(self):
        if keyboard.a:
            self.x -= self.speed
            self.flip_x = True
        elif keyboard.d:
            self.x += self.speed
            self.flip_x = False

        if keyboard.w:
            self.y -= self.speed
        elif keyboard.s:
            self.y += self.speed

        detect_border(self)

class Ennemy(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = ['fly1', 'fly2']
        self.direction = randint(0, 360)
        self.speed = 3

    def update(self):
        self.direction += randint(-10, 10)
        self.move_in_direction(self.speed)
        detect_border(self)
        
class Missile(Actor):
    def __init__(self, image, pos, direction, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.direction = direction
        self.angle = direction
        self.speed = 5

    def update(self):
        self.move_in_direction(self.speed)
        for ennemy in ennemies:
            if self.collides_with(ennemy):
                print('BOOOOM')
                sounds.explosion.play()
                ennemy.to_remove = True
                self.to_remove = True
                player.score += 1
        
def detect_border(actor):
    if actor.x > WIDTH:
        actor.x = 0
    elif actor.x < 0:
        actor.x = WIDTH

    if actor.y > HEIGHT:
        actor.y = 0
    elif actor.y < 0:
        actor.y = HEIGHT
        
def add_ennemy():
    ennemy = Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))
    ennemies.append(ennemy)
    
def on_mouse_down(pos):
    direction = player.angle_to(pos)
    missile = Missile('missile', (player.x, player.y), direction)
    missiles.append(missile)

music.play('adventure')

player = Player('alien_walk1', (WIDTH/2, HEIGHT/2))
ennemies = [Ennemy('fly1', (randint(0, WIDTH), randint(0, HEIGHT)))]
missiles = []

clock.schedule_interval(add_ennemy, 15.0)

def draw():
    screen.blit('grass', (0, 0))
    screen.draw.text(f"Score: {player.score}", (0, 0))
    player.draw()
    for ennemy in ennemies:
        ennemy.draw()
        ennemy.animate()
    for missile in missiles:
        missile.draw()

def update():
    player.update()
    for ennemy in ennemies:
        ennemy.update()
    for missile in missiles:
        missile.update()
        
    remove_actors(ennemies)
    remove_actors(missiles)

pgzrun.go()
```
````

## 14. Idées d'améliorations

```{admonition} Travail à rendre
Votre travail consiste à ajouter au minimum les améliorations suivantes au jeu:

* 2 améliorations faciles
* 1 amélioration moyenne
```

Voici plusieurs idées d'amélioration du jeu.  
Vous pouvez bien sûr me proposer d'autres idées et je vous dirai leur difficulté.

**Totalement dans vos cordes (facile):**

* Ajouter une animation au joueur quand il se déplace.
* Faire en sorte que le jeu arrête de créer des ennemis s'il y en a déjà 5 ou plus en jeu.
* Faire en sorte que plus le score augmente, plus les ennemis se déplacent rapidement.
* Détruire les missiles lorsqu'ils sortent de l'écran et limiter le joueur à 3 missiles à la fois.
* Faire en sorte que le joueur perde de la vie à chaque contact avec un ennemi.
* Créer un game over sous les conditions de votre choix (par exemple au contact d'un ennemi ou après un certain temps).
* Faire en sorte que le personnage ne se déplace pas plus rapidement en diagonal qu'à l'horizontal ou à la verticale.

**Un peu plus complexe (moyen):**

* Faire en sorte qu'en cas de contact avec un ennemi, le joueur perd de la vie et l'ennemi meurt. La vie du joueur est affichée sous le score.
* Permettre au joueur de ramasser des objets pour augmenter son score, par exemple des pièces.
* Ajouter un second joueur qui pourra se déplacer et tirer avec d'autres touches.
* Ajouter un nouveau type d'ennemi qui se comporte différemment.
* Ajouter un item qui permet d'augmenter temporairement la vitesse du joueur si rammassé.
* Faire en sorte qu'en cas de contact avec un ennemi, le joueur perde un peu de vie et soit invincible pendant un court laps de temps (pour éviter des dégats à répétition).
* Ajouter un boss qui apparaît seulement après un certain temps et nécessite beaucoup de dégats pour être battu mais offre un score élevé.
* Faire en sorte que les ennemis suivent le joueur au lieu de se balader aléatoirement.

**Challenging (difficile):**

* Ajouter des armes au personnage. Par exemple une attaque au corps à corps ou la possibilité de larguer des bombes qui explosent après quelques secondes.
* Permettre au joueur de poser des pièges qui blesseront les ennemis qui passent dessus.
* Faire en sorte que le monde bouge autour du personnage afin qu'il puisse se balader librement dans toutes les directions sans jamais toucher un bord. Indice: le joueur ne se déplace plus, mais déplacez tous les acteurs du jeu dans la direction inverse au déplacement du joueur.
* Créer un second niveau atteignable en passant un certain score où les ennemis sont différents et plus coriaces.
* Donner aux ennemis la capacité d'essayer d'esquiver les projectiles (en se déplaçant perpendiculairement à leur trajectoire).
* Créer un menu avant le début du jeu qui permet de choisir la difficulté ou d'autres options.

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