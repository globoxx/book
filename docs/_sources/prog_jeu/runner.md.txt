(prog_jeu.runner)=

# 3. Running Ninja (runner)

Dans cette introduction, nous allons développer un premier jeu simple étape par étape. Le jeu consiste en un ninja devant sauter par dessus des obstacles. Le jeu est terminé si le ninja touche un obstacle.

{download}`Téléchargement des ressources du jeu<../data/prog_2d/runner.zip>`.

```{image} ../media/runner.gif
```

## 1. Faire apparaître une fenêtre

La première étape est de définir le nom de notre jeu dans la variable `TITLE`, ainsi que la largeur `WIDTH` et la hauteur `HEIGHT` de notre fenêtre. Nous allons également importer `pgzrun` et des fonctions de `pgzhelper` afin de nous faciliter la vie. Pygame Zero s'occupe du reste !

```python
import pgzrun
from pgzhelper import *

TITLE = 'Runner'

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

TITLE = 'Runner'
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

Tous les dessins de notre jeu se feront via la fonction `draw` de Pygame. Il nous faut donc lui ajouter l'instruction permettant de colorier le fond et faire un carré d'herbe.

`screen` est un objet accessible grâce à Pygame qui représente la fenêtre de notre jeu.  
Nous allons faire un ciel bleu ainsi que de l'herbe verte.

```python
def draw():
    screen.fill((163, 232, 254)) # Colorie le fond en bleu ciel (valeurs RGB)
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152)) # Dessine un rectangle vert
    # Rect(x, y, largeur, hauteur)
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Runner'
WIDTH = 800
HEIGHT = 600

def draw():
    screen.fill((163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))

def update():
    pass

pgzrun.go()
```
````

## 3. Ajouter le joueur

Il est temps d'ajouter notre joueur. Il sera représenté par un `objet`. Chaque objet sera également représenté par une image (que nous appelerons un sprite) et une position. Chaque sprite doit être sauvegardé dans le dossier `images`.

```{image} ../media/run__003.png
```

La plateforme <a href="https://kenney.nl/assets" target="_blank">Kenny</a> contient énormément de sprites gratuits à utiliser pour vos jeux.

Pour chaque nouvel objet que l'on veut ajouter à notre jeu, nous allons créer une `classe` associée. Voyez une classe comme un moule qui nous permettra de créer des objets, comme notre joueur. En <a href="https://courspython.com/classes-et-objets.html" target="_blank">programmation orientée objet</a>, une classe possède des `attributs` (des variables décrivant l'objet) et des `méthodes` (des fonctions pouvant être appelées par l'objet).

Nous créons donc une classe `Player` qui hérite des attributs et méthodes d'une autre classe nommée `Actor` offerte par Pygame. En fait, tous les objets que nous allons ajouter à notre jeu sont des `Actor`.

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs): # Init est le constructeur de la classe
        super().__init__(image, pos, **kwargs) # Cette ligne appelle le constructeur de la classe mère Actor
        # Ne vous en préoccupez pas trop pour le moment mais pour faire simple, elle s'occupe d'initialiser l'objet avec la bonne image et la bonne position
        # **kwargs permet de donner d'autres paramètres optionnels comme la taille par exemple
```

Ce code crée une classe `Player` héritant de la classe `Actor`. La méthode `init` est ce que l'on appelle un **constructeur** qui est appelé lors de la création d'un objet. Ce construction prend obligatoirement une image en entrée, ainsi que des coordonnées `pos` (`x`, `y`) pour savoir où placer l'objet créé.

Nous pouvons à présent créer notre objet `player` grâce à notre classe. Nous lui passons le nom de l'image qui va le représenter ainsi que ses coordonnées (`x`, `y`) afin qu'il soit placé à `100` pixels du bord gauche et `400` pixels du bord haut.

```python
player = Player('run__000', (100, 400)) # Création du joueur
```

Afin de dessiner notre joueur, il faut en dernier lieu appeler la méthode `player.draw()` dans la fonction principale `draw` de Pygame.

```python
def draw():
    screen.fill((163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    player.draw() # On dessine le joueur ici !
```

`draw` est une méthode possèdée par tous les objets de type `Actor`. Etant donné que notre objet de type `Player` est aussi un `Actor`, il hérite de cette méthode ainsi que de plein d'attributs dont nous aurons besoin plus tard comme les coordonnées `x` et `y` de notre objet.

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Runner'
WIDTH = 800
HEIGHT = 600

class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)

player = Player('run__000', (100, 400))

def draw():
    screen.fill((163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    player.draw()

def update():
    pass

pgzrun.go()
```
````

## 4. Animer le joueur

Notre joueur est statique pour le moment. Nous allons donc ajouter une animation pour le faire courir. Dans un jeu, une animation est une suite d'images qui se succèdent rapidement pour donner l'illusion du mouvement.

```{image} ../media/run__000.png
```

```{image} ../media/run__003.png
```

```{image} ../media/run__009.png
```

Il nous faut commencer par définir la liste des images qui composent notre animation. Pour cela, nous ajoutons un attribut `images` à notre classe `Player` qui contiendra toutes les images de notre animation.

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = [f'run__00{i}' for i in range(10)] # Liste des images de l'animation (run__000 à run__009)
        # Raccourci pour ['run__000', 'run__001', ..., 'run__009']
```

Pour faire avancer l'animation à chaque tour, il nous faut encore appeler `player.animate()` dans la fonction `update` principale. Par défaut, l'animation se fait à 5 fps (images par seconde) mais on peut choisir une autre valeur.

```python
def update():
    player.animate(20) # On anime le joueur à 20 fps (images par seconde)
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Runner'
WIDTH = 800
HEIGHT = 600

class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = [f'run__00{i}' for i in range(10)]

player = Player('run__000', (100, 400))

def draw():
    screen.fill((163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    player.draw()

def update():
    player.animate(20)

pgzrun.go()
```
````

## 5. Ajouter des obstacles

Nous allons ajouter des obstacles qui vont défiler de droite à gauche. Pour cela, nous allons créer une nouvelle classe `Obstacle` qui hérite de `Actor`. Les obstacles seront représentés par des cactus.

```{image} ../media/cactus.png
```

```python
class Obstacle(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)

obstacle = Obstacle('cactus', (850, 430)) # Création d'un obstacle en dehors de l'écran à droite
```

Notre objet `obstacle` est créé en dehors de l'écran à droite (`x = 850`). Nous allons le faire défiler de droite à gauche en le déplaçant de `10` pixels à chaque tour du jeu.

Pour cela, nous allons ajouter une méthode `update` à notre classe `Obstacle`. C'est dans cette méthode que nous décrivons les actions que l'obstacle doit effectuer à chaque `tour` du jeu. Dans notre cas, il doit se déplacer de `10` pixels vers la gauche et réapparaître à droite une fois qu'il est sorti de l'écran.

```python
class Obstacle(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)

    def update(self):
        self.x -= 10 # Déplacement de l'obstacle de 10 pixels vers la gauche
        if self.x < -50: # Si l'obstacle sort de l'écran à gauche
            self.x = 850 # Il réapparaît à droite

obstacle = Obstacle('cactus', (850, 430))
```

A ce point, il ne reste plus qu'à appeler la méthode `obstacle.draw()` dans la fonction `draw` et `obstacle.update()` dans la fonction `update`.

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Runner'
WIDTH = 800
HEIGHT = 600

class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = [f'run__00{i}' for i in range(10)]

class Obstacle(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)

    def update(self):
        self.x -= 10
        if self.x < -50:
            self.x = 850

player = Player('run__000', (100, 400))
obstacle = Obstacle('cactus', (850, 430))

def draw():
    screen.fill((163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    player.draw()
    obstacle.draw()

def update():
    player.animate(20)
    obstacle.update()

pgzrun.go()
```
````

## 6. Permettre au joueur de sauter

Pour pouvoir sauter et retomber, notre personnage doit posséder une vitesse verticale. Nous allons donc ajouter un attribut `vy` à notre classe `Player` qui représente la vitesse verticale du joueur.

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = [f'run__00{i}' for i in range(10)]
        self.vy = 0 # Vitesse verticale
```

Sauter correspond à une action de notre joueur. Nous allons donc devoir ajouter une fonction `update` à notre classe `Player`. Cette fonction sera appelée à chaque `tour` du jeu et permettra de mettre à jour la position du joueur en fonction de sa vitesse verticale.

**N'oubliez pas d'appeler la méthode `player.update()` dans la fonction `update` du programme principal !**

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = [f'run__00{i}' for i in range(10)]
        self.vy = 0

    def update(self):
        self.y += self.vy # Mise à jour de la position verticale du joueur
        self.vy += 1 # Augmentation de la vitesse verticale (gravité)
```

Oups, notre personnage tombe du jeu et disparaît ! Pour éviter cela, nous allons devoir ajouter une condition (`if`) pour détecter le sol (coordonnée `y` à `400`) et remettre la vitesse verticale à `0`.

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = [f'run__00{i}' for i in range(10)]
        self.vy = 0

    def update(self):
        self.y += self.vy
        self.vy += 1
        if self.y > 400: # Si le joueur touche le sol (est trop bas sur l'axe y)
            self.y = 400 # Le joueur est remis sur le sol
            self.vy = 0 # La vitesse verticale est remise à 0
```

Bon et maintenant il faut pouvoir sauter ! Nous allons donc ajouter une condition pour détecter si la touche `space` (espace) est pressée. Si c'est le cas, nous allons donner une vitesse verticale (`vy`) négative au joueur pour le faire aller vers le haut. Pygame Zero nous offre un objet `keyboard` qui nous permet de détecter les touches pressées.

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = [f'run__00{i}' for i in range(10)]
        self.vy = 0

    def update(self):
        self.y += self.vy
        self.vy += 1
        if self.y > 400:
            self.y = 400
            self.vy = 0

        if keyboard.space: # Si la touche espace est pressée
            self.vy = -15 # Le joueur saute avec une vitesse négative (vers le haut)
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Runner'
WIDTH = 800
HEIGHT = 600

class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = [f'run__00{i}' for i in range(10)]
        self.vy = 0

    def update(self):
        self.y += self.vy
        self.vy += 1
        if self.y > 400:
            self.y = 400
            self.vy = 0

        if keyboard.space:
            self.vy = -15

class Obstacle(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)

    def update(self):
        self.x -= 10
        if self.x < -50:
            self.x = 850

player = Player('run__000', (100, 400))
obstacle = Obstacle('cactus', (850, 430))

def draw():
    screen.fill((163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    player.draw()
    obstacle.draw()

def update():
    player.animate(20)
    player.update()
    obstacle.update()

pgzrun.go()
```
````

## 7. Détecter un game over

Notre joueur est invicible ! Il est temps d'ajouter la détection de collision entre le joueur et les obstacles. Si le joueur touche un obstacle, c'est la fin du jeu.

Pour détecter une collision, nous allons utiliser la méthode `collides_with(actor)` héritée de `Actor`. Cette méthode retourne `True` si l'objet est en collision avec un autre `Actor`.

Nous allons donc ajouter une condition dans la fonction `update` du `Player` pour détecter une collision avec l'`obstacle`. Nous devons aussi créer une variable `game_over` pour savoir si le jeu est terminé. Par souci de simplicité, nous pouvons définir `game_over` comme un attribut de notre classe `Player`.

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = [f'run__00{i}' for i in range(10)]
        self.vy = 0
        self.game_over = False # Ajout de l'attribut game_over

    def update(self):
        self.y += self.vy
        self.vy += 1
        if self.y > 400:
            self.y = 400
            self.vy = 0

        if keyboard.space:
            self.vy = -15

        if self.collides_with(obstacle): # Si le joueur touche l'obstacle
            self.game_over = True # Le jeu est terminé
```

Bien, nous avons maintenant une variable `game_over` qui est `True` si le joueur touche un obstacle. Il ne reste plus qu'à ajouter une condition dans la fonction `update` du programme principal pour arrêter le jeu si `game_over` est `True`. Il suffit de faire les updates des objets uniquement si `game_over` est `False`.

```python
def update():
    if not player.game_over: # Si le jeu n'est pas terminé
        # On anime le joueur et on met à jour le joueur et l'obstacle
        player.animate(20)
        player.update()
        obstacle.update()
```

Nous pouvons également ajouter un message de game over à l'écran si `game_over` est `True`. C'est de l'affichage, cela se fait donc dans la fonction `draw`.

```python
def draw():
    screen.fill((163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    player.draw()
    obstacle.draw()
    if player.game_over: # Si le jeu est terminé
        screen.draw.text('Game Over', centerx=400, centery=270, color=(255,255,255), fontsize=60)
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Runner'
WIDTH = 800
HEIGHT = 600

class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = [f'run__00{i}' for i in range(10)]
        self.vy = 0
        self.game_over = False

    def update(self):
        self.y += self.vy
        self.vy += 1
        if self.y > 400:
            self.y = 400
            self.vy = 0

        if keyboard.space:
            self.vy = -15

        if self.collides_with(obstacle):
            self.game_over = True

class Obstacle(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)

    def update(self):
        self.x -= 10
        if self.x < -50:
            self.x = 850

player = Player('run__000', (100, 400))
obstacle = Obstacle('cactus', (850, 430))

def draw():
    screen.fill((163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    player.draw()
    obstacle.draw()
    if player.game_over:
        screen.draw.text('Game Over', centerx=400, centery=270, color=(255,255,255), fontsize=60)

def update():
    if not player.game_over:
        player.animate(20)
        player.update()
        obstacle.update()

pgzrun.go()
```
````

## 8. Tenir et afficher un score

Le score est important dans les jeux ! Pour en tenir un, on peut le définir dans les attributs de notre `player` et l'initialiser à `0`.

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = [f'run__00{i}' for i in range(10)]
        self.vy = 0
        self.game_over = False
        self.score = 0 # Initialisation du score à 0
```

Avant de nous occuper de l'augmentation du `score`, voyons déjà comment l'afficher. Afficher du texte à l'écran se fait via l'objet `screen` offert par Pygame. Nous l'utilisons dans la fonction `draw` du programme principal, juste après avoir défini l'image de fond.

```python
def draw():
    ...
    screen.draw.text(f'Score: {player.score}', (15,10), color=(0,0,0), fontsize=30) # Affichage du score
    ...
```

Le score va augmenter à chaque fois qu'un obstacle sort de l'écran. Il suffit donc de l'augmenter de `1` à chaque fois que cela se produit dans la méthode `update` de notre classe `Obstacle`.

```python
class Obstacle(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)

    def update(self):
        self.x -= 10
        if self.x < -50:
            self.x = 850
            player.score += 1 # Augmentation du score car l'obstacle est sorti de l'écran
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Runner'
WIDTH = 800
HEIGHT = 600

class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = [f'run__00{i}' for i in range(10)]
        self.vy = 0
        self.game_over = False
        self.score = 0

    def update(self):
        self.y += self.vy
        self.vy += 1
        if self.y > 400:
            self.y = 400
            self.vy = 0

        if keyboard.space:
            self.vy = -15

        if self.collides_with(obstacle):
            self.game_over = True

class Obstacle(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)

    def update(self):
        self.x -= 10
        if self.x < -50:
            self.x = 850
            player.score += 1

player = Player('run__000', (100, 400))
obstacle = Obstacle('cactus', (850, 430))

def draw():
    screen.fill((163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    player.draw()
    obstacle.draw()
    screen.draw.text(f'Score: {player.score}', (15,10), color=(0,0,0), fontsize=30)
    if player.game_over:
        screen.draw.text('Game Over', centerx=400, centery=270, color=(255,255,255), fontsize=60)

def update():
    if not player.game_over:
        player.animate(20)
        player.update()
        obstacle.update()

pgzrun.go()
```
````

## 9. Ajouter un son de saut

Ajouter un bruitage est très simple. La première étape consiste à ajouter le fichier `.wav` ou `.mp3` souhaité dans le dossier `sounds` (à créer). De nombreux bruitages et musiques gratuits peuvent être trouvés sur <a href="https://freesound.org/" target="_blank">FreeSound</a> ou <a href="https://opengameart.org/" target="_blank">OpenGameArt</a>. Priviliégiez les sons courts pour éviter des problèmes de performance.

Pygame nous offre l'objet `sounds` qui nous permet de facilement lancer un bruitage. Dans notre cas, nous souhaitons lancer un son lorsque le joueur saute. Nous allons donc ajouter une ligne `sounds.jump.play()` dans la méthode `update` de notre classe `Player`.

```python
class Player(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)
        self.images = [f'run__00{i}' for i in range(10)]
        self.vy = 0
        self.game_over = False
        self.score = 0

    def update(self):
        self.y += self.vy
        self.vy += 1
        if self.y > 400:
            self.y = 400
            self.vy = 0

        if keyboard.space:
            self.vy = -15
            sounds.jump.play() # Ajout du son de saut

        if self.collides_with(obstacle):
            self.game_over = True
```

`sounds.jump.play()` fait ici référence au nom du fichier son: `jump.wav`.

## 10. Ajouter une musique de fond

Ajouter une musique de fond est tout aussi simple ! Il suffit d'ajouter un fichier `.mp3` ou `.wav` dans le dossier `music` (à créer) et d'utiliser l'objet `music` offert par Pygame.

Pour lancer notre musique `ninja_music.mp3` au début du jeu, il reste qu'à appeler `music.play(ninja_music)` au début du programme principal.

```python
player = Player('run__000', (100, 400))
obstacle = Obstacle('cactus', (850, 430))

music.play('ninja_music') # Ajout de la musique ici !
```

## 11. Améliorations possibles

```{admonition} Travail à rendre
Votre travail consiste à ajouter au minimum les améliorations suivantes au jeu:

* 2 améliorations faciles
* 1 amélioration moyenne
```

Voici plusieurs idées d'amélioration du jeu.  
Vous pouvez bien sûr me proposer d'autres idées et je vous dirai leur difficulté.

**Totalement dans vos cordes (facile):**

* Corriger le bug des sauts infinis. Le joueur ne devrait pouvoir sauter que s'il est au sol.
* Changer/Stoper l'animation du joueur en cours de saut.
* Créer un vrai écran de game over dans lequel on ne voit plus le jeu derrière mais un écran noir par exemple.
* Permettre de mettre le jeu en pause en appuyant sur une touche.
* Faire en sorte que les obstacles accélèrent progressivement quand le score augmente.
* Faire en sorte que l'on puisse changer la taille de la fenêtre de jeu dans le code (`WIDTH` et `HEIGHT`) et que tout s'adapte automatiquement.

**Un peu plus complexe (moyen):**

* Permettre de relancer le jeu du début après un game over en appuyant sur une touche.
* Ajouter un nouveau type d'obstacle pour lequel il faut rester au sol pour l'éviter.
* Changer aléatoirement l'image de l'obstacle à chaque fois qu'il réapparaît. Piochez dans les images fournies ou trouvez-en d'autres.
* Plusieurs obstacles peuvent apparaître en même temps. Indice: créez une liste d'obstacles.
* Permettre au joueur de ramasser des objets pour augmenter son score, par exemple des pièces.

**Challenging (difficile):**

* Permettre au joueur de tirer sur les obstacles pour les détruire.
* Donner de la vie au joueur lui permettant de prendre un certain nombre de coups avant de mourir. La vie du joueur est affichée et à chaque coup, le joueur est invincible pendant un cours laps de temps.
* Créer un menu avant le début du jeu qui permet de choisir la difficulté ou d'autres options.
* Créer un système de sauvegarde du score.
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
